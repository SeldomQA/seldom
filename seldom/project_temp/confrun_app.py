"""
seldom confrun.py hooks function  - app auto test project
Run:
> seldom -p test_dir
"""
from seldom.appium_lab.android import UiAutomator2Options


def app_info():
    """
    app UI test
    appium app config
    """
    capabilities = {
        'deviceName': 'ELS-AN00',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'appPackage': 'com.microsoft.bing',
        'appActivity': 'com.microsoft.sapphire.app.main.MainSapphireActivity',
        'noReset': True,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    return options


def app_server():
    """
    app UI test
    appium server address
    """
    return "http://127.0.0.1:4723"


def debug():
    """
    debug mod
    """
    return False


def rerun():
    """
    error/failure rerun times
    """
    return 0


def report():
    """
    setting report path
    Used:
    return "d://mypro/result.html"
    return "d://mypro/result.xml"
    """
    return None


def timeout():
    """
    setting timeout
    """
    return 10


def title():
    """
    setting report title
    """
    return "seldom test report"


def tester():
    """
    setting report tester
    """
    return "bugmaster"


def description():
    """
    setting report description
    """
    return ["windows", "jenkins"]


def language():
    """
    setting report language
    return "en"
    return "zh-CN"
    """
    return "en"


def whitelist():
    """test label white list"""
    return []


def blacklist():
    """test label black list"""
    return []
