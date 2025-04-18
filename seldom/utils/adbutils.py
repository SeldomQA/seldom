import os
import re
import subprocess
import time
from typing import List, Tuple, Optional
from contextlib import contextmanager

from seldom.logging import log


class ADBUtils:
    """
    Enhanced ADB utility class with proper resource management
    Features: Device management, app control, and information retrieval
    """

    def __init__(self, default_device: str = None):
        """
        Initialize ADB controller with resource-safe implementation
        :param default_device: Default device serial number (optional)
        """
        self.default_device = default_device
        self._devices_cache = []
        self._last_refresh_time = 0
        self.CACHE_EXPIRE = 60

    @contextmanager
    def _safe_popen(self, command: str):
        """Context manager for safe subprocess handling"""
        process = None
        try:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            yield process
        finally:
            if process is not None:
                process.terminate()
                try:
                    process.wait(timeout=1)
                except subprocess.TimeoutExpired:
                    process.kill()

    def refresh_devices(self, force: bool = False) -> List[Tuple[str, str]]:
        """
        Safely refresh device list with proper resource cleanup
        :param force: Whether to force refresh
        :return: List of (serial, device_name) tuples
        """
        current_time = time.time()
        if not force and current_time - self._last_refresh_time < self.CACHE_EXPIRE:
            return self._devices_cache

        self._devices_cache = []
        try:
            with self._safe_popen("adb devices") as process:
                stdout, _ = process.communicate(timeout=5)
                raw_devices = stdout.splitlines()[1:]

                for line in raw_devices:
                    parts = line.split()
                    if len(parts) > 1 and parts[1] == "device":
                        serial = parts[0]
                        device_name = self._get_device_name(serial)
                        if device_name:
                            self._devices_cache.append((serial, device_name))

            self._last_refresh_time = current_time
        except Exception as e:
            log.error(f"Device  refresh failed: {str(e)}")

        return self._devices_cache

    def _get_device_name(self, device_serial: str) -> str:
        """
        Safely get device name with proper subprocess handling
        :param device_serial: Device serial number
        :return: Device model name or empty string on failure
        """
        try:
            with self._safe_popen(f"adb -s {device_serial} shell getprop ro.product.model") as process:
                stdout, _ = process.communicate(timeout=3)
                return stdout.strip().replace('  ', '')
        except Exception as e:
            log.error(f"Failed  to get device info: {str(e)}")
            return ""

    def set_default_device(self, device_serial: str) -> bool:
        """
        Set default device
        :param device_serial: Device serial number
        :return: Whether the operation succeeded
        """
        devices = [d[0] for d in self.refresh_devices()]
        if device_serial in devices:
            self.default_device = device_serial
            return True
        log.info(f"Device {device_serial} does not exist or is not connected")
        return False

    def launch_app(self, package_name: str, device_id: Optional[str] = None) -> bool:
        """
        Launch app (with error handling and result return)
        :param package_name: App package name
        :param device_id: Device serial number (optional)
        :return: Whether the operation succeeded
        """
        device = device_id or self.default_device
        try:
            cmd = f"adb{' -s ' + device if device else ''} shell monkey -p {package_name} -c android.intent.category.LAUNCHER   1"
            exit_code = os.system(cmd)
            return exit_code == 0
        except Exception as e:
            log.error(f"Failed to launch app {package_name}: {e}")
            return False

    def close_app(self, package_name: str, device_id: Optional[str] = None) -> bool:
        """
        Close app (optimized implementation)
        :param package_name: App package name
        :param device_id: Device serial number (optional)
        :return: Whether the operation succeeded
        """
        device = device_id or self.default_device
        try:
            cmd = f"adb{' -s ' + device if device else ''} shell am force-stop {package_name}"
            exit_code = os.system(cmd)
            return exit_code == 0
        except Exception as e:
            log.error(f"Failed to close app {package_name}: {e}")
            return False

    def get_foreground_app_info(self, device_id: Optional[str] = None) -> dict:
        """
        Enhanced foreground app detection with precise window dump parsing
        Returns: {
            'package': str,
            'activity': str,
            'window_state': str,
            'orientation': int,
            'stack_id': int,
            'bounds': Tuple[int,int,int,int]  # (x1,y1,x2,y2)
        }

        Example Output for Bing:
        {
            'package': 'com.microsoft.bing',
            'activity': 'com.microsoft.sapphire.app.main.MainSapphireActivity',
            'window_state': 'mCurrentFocus',
            'orientation': 0,  # portrait
            'stack_id': 18153,
            'bounds': (0, 0, 1200, 2640)
        }
        """
        device = device_id or self.default_device
        try:
            # Execute adb command to get window info
            cmd = f"adb{' -s ' + device if device else ''} shell dumpsys window windows"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)

            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, cmd)

            return self._parse_window_dump(result.stdout)

        except subprocess.TimeoutExpired:
            print("Window dump timed out after 5 seconds")
        except Exception as e:
            print(f"Foreground detection failed: {type(e).__name__}: {str(e)}")
        return None

    def _parse_window_dump(self, dump_content: str) -> List[dict]:
        """
        Enhanced window dump parser with precise pattern matching
        Returns filtered list of valid application windows only
        """
        window_info_list = []

        # Primary pattern for focused application windows
        app_window_pattern = re.compile(
            r"Window\{[\w]+\s[\w]+\s(?P<package>[^\s/]+)/(?P<activity>[^\s\}]+).*?"
            r"mDisplayId=(?P<display_id>\d+).*?"
            r"(rootTaskId|mTaskId)=(?P<stack_id>\d+).*?"
            r"mBounds=Rect\((?P<bounds>\d+,\s*\d+\s*-\s*\d+,\s*\d+)\)",
            re.DOTALL
        )

        # Secondary pattern for ActivityRecord entries
        activity_record_pattern = re.compile(
            r"ActivityRecord\{[\w]+\s[\w]+\s(?P<package>[^\s/]+)/(?P<activity>[^\s\}]+).*?"
            r"t(?P<stack_id>\d+)",
            re.DOTALL
        )

        # System/overlay window filter (exclude navigation bars, popups etc.)
        system_window_indicators = {
            'pip-dismiss-overlay',
            'GestureSildeOut',
            'GestureNavRight',
            'NavigationBar',
            'NotificationShade',
            'ShellDropTarget',
            'PopupWindow'
        }

        # Extract orientation
        orientation = 0
        orient_match = re.search(r"mRotation=ROTATION_(\d+)", dump_content)
        if orient_match:
            orientation = int(orient_match.group(1)) * 90

            # Process window matches
        for match in app_window_pattern.finditer(dump_content):
            info = match.groupdict()
            package = info['package']
            activity = info['activity']

            # Skip system/overlay windows
            if any(indicator in package for indicator in system_window_indicators):
                continue

                # Process bounds
            bounds = (0, 0, 0, 0)
            if info['bounds']:
                bounds = tuple(map(int, re.split(r"\s*,\s* |\s*-\s*", info['bounds'])))

            window_info = {
                'package': package,
                'activity': activity,
                'window_state': 'focused',
                'orientation': orientation,
                'stack_id': int(info.get('stack_id', 0)),
                'bounds': bounds,
                'window_id': match.group(0)[7:15],  # Extract window ID
                'source': 'window_dump'
            }
            window_info_list.append(window_info)

            # Process ActivityRecord matches
        for match in activity_record_pattern.finditer(dump_content):
            info = match.groupdict()
            if not any(w['package'] == info['package'] and
                       w['activity'] == info['activity']
                       for w in window_info_list):
                window_info_list.append({
                    'package': info['package'],
                    'activity': info['activity'],
                    'window_state': 'activity_record',
                    'stack_id': int(info.get('stack_id', 0)),
                    'source': 'activity_record'
                })

        # Filter and prioritize valid application windows
        return [
            info for info in window_info_list
            if not info['package'].startswith(('u0 ', 'pip-'))
               and '.' in info['activity']
        ]
