"""
appium API
"""
from typing import Any, Dict
from seldom.running.config import Seldom


class AppDriver:
    """
    appium base API
    """

    def background_app(self, seconds: int):
        """
        Puts the application in the background on the device for a certain duration.

        Args:
            seconds: the duration for the application to remain in the background
        """
        Seldom.driver.background_app(seconds=seconds)
        return self

    @staticmethod
    def is_app_installed(bundle_id: str) -> bool:
        """Checks whether the application specified by `bundle_id` is installed on the device.

        Args:
            bundle_id: the id of the application to query

        Returns:
            `True` if app is installed
        """
        return Seldom.driver.is_app_installed(bundle_id=bundle_id)

    def install_app(self, app_path: str, **options: Any):
        """Install the application found at `app_path` on the device.

        Args:
            app_path: the local or remote path to the application to install

        Keyword Args:
            replace (bool): [Android only] whether to reinstall/upgrade the package if it is
                already present on the device under test. True by default
            timeout (int): [Android only] how much time to wait for the installation to complete.
                60000ms by default.
            allowTestPackages (bool): [Android only] whether to allow installation of packages marked
                as test in the manifest. False by default
            useSdcard (bool): [Android only] whether to use the SD card to install the app. False by default
            grantPermissions (bool): [Android only] whether to automatically grant application permissions
                on Android 6+ after the installation completes. False by default

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.install_app(app_path=app_path, **options)
        return self

    def remove_app(self, app_id: str, **options: Any):
        """Remove the specified application from the device.

        Args:
            app_id: the application id to be removed

        Keyword Args:
            keepData (bool): [Android only] whether to keep application data and caches after it is uninstalled.
                False by default
            timeout (int): [Android only] how much time to wait for the uninstall to complete.
                20000ms by default.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.remove_app(app_id=app_id, **options)
        return self

    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.launch_app()
        return self

    def close_app(self):
        """Stop the running application, specified in the desired capabilities, on
        the device.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.close_app()
        return self

    @staticmethod
    def terminate_app(app_id: str, **options: Any) -> bool:
        """Terminates the application if it is running.

        Args:
            app_id: the application id to be terminates

        Keyword Args:
            `timeout` (int): [Android only] how much time to wait for the uninstall to complete.
                500ms by default.

        Returns:
            True if the app has been successfully terminated
        """

        return Seldom.driver.terminate_app(app_id=app_id, **options)

    def activate_app(self, app_id: str):
        """Activates the application if it is not running
        or is running in the background.

        Args:
            app_id: the application id to be activated

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.activate_app(app_id=app_id)
        return self

    @staticmethod
    def query_app_state(app_id: str) -> int:
        """Queries the state of the application.

        Args:
            app_id: the application id to be queried

        Returns:
            One of possible application state constants. See ApplicationState
            class for more details.
        """

        return Seldom.driver.query_app_state(app_id=app_id)

    @staticmethod
    def app_strings(language: str = None, string_file: str = None) -> Dict[str, str]:
        """Returns the application strings from the device for the specified
        language.

        Args:
            language: strings language code
            string_file: the name of the string file to query

        Returns:
            The key is string id and the value is the content.
        """

        return Seldom.driver.app_strings(language=language, string_file=string_file)

    def reset(self):
        """Resets the current application on the device.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.reset()
        return self
