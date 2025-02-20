import os
import time


def get_device_info(device: str) -> dict:
    """
    Get device name and serial number.
    :param device:
    :return:
    """
    try:
        name = os.popen(f"adb -s {device} shell getprop ro.product.model").read().strip().replace(' ', '')
        return {device: name}
    except Exception as e:
        print(f"Error retrieving device info for {device}: {e}")
        return {}


def get_devices() -> dict:
    """
    Get a list of dictionaries, each containing a single device's name and serial number.
    :return:
    """
    devices = {}
    raw_devices = os.popen("adb devices").read().splitlines()[1:]  # Skip the first line which is a header
    for line in raw_devices:
        parts = line.split()
        if len(parts) > 1 and parts[1] == "device":
            serial = parts[0]
            device_info = get_device_info(serial)
            if device_info:
                # Create a dictionary from the tuple and add it to the list
                devices = {**devices, **device_info}
    return devices


def launch_app(package_name: str = None) -> None:
    """
    launch App by adb command.
    :param package_name:
    :return:
    """
    try:
        os.popen(f"adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1")
    except Exception as e:
        print(f"launch app {package_name} error: {e}")


def close_app(package_name: str = None) -> None:
    """
    close App by adb command.
    :param package_name:
    :return:
    """
    try:
        os.popen(f"adb shell am force-stop {package_name}")
    except Exception as e:
        print(f"close app {package_name} error: {e}")


if __name__ == '__main__':
    a = get_devices()
    print(a)
    launch_app("com.microsoft.bing")
    time.sleep(3)
    close_app("com.microsoft.bing")
