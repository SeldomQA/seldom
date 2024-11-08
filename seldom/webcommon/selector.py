from appium.webdriver.common.appiumby import AppiumBy as By

from seldom.webcommon.locators import SELECTOR_LIST


def selection_checker(selector: str) -> (str, str):
    """
    Check the location method and return the corresponding locator strategy and value.
    :param selector: Selector string, which includes a prefix indicating the type of locator.
    :return: Tuple (locator strategy, value)
    """
    if len(selector) == 0:
        raise ValueError(f"The selector cannot have length 0")

    # Check for prefix match in the locator dictionary
    for prefix, (locator, length) in SELECTOR_LIST.items():
        if selector.startswith(prefix) and len(selector) > length:
            return locator, selector[length:]

    # Handle xpath and css selectors
    if selector.startswith("/"):
        return By.XPATH, selector
    else:
        return By.CSS_SELECTOR, selector
