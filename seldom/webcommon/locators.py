"""
appium & selenium locator
"""
from appium.webdriver.common.appiumby import AppiumBy as By

LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
    'ios_predicate': By.IOS_PREDICATE,
    'ios_class_chain': By.IOS_CLASS_CHAIN,
    'android_uiautomator': By.ANDROID_UIAUTOMATOR,
    'android_viewtag': By.ANDROID_VIEWTAG,
    'android_data_matcher': By.ANDROID_DATA_MATCHER,
    'android_view_matcher': By.ANDROID_VIEW_MATCHER,
    'accessibility_id': By.ACCESSIBILITY_ID,
    'image': By.IMAGE,
    'custom': By.CUSTOM,
}

SELECTOR_LIST = {
    "text=": (By.LINK_TEXT, 5),
    "text~=": (By.PARTIAL_LINK_TEXT, 6),
    "text*=": (By.PARTIAL_LINK_TEXT, 6),
    "id=": (By.ID, 3),
    "name=": (By.NAME, 5),
    "class=": (By.CLASS_NAME, 6),
    "tag=": (By.TAG_NAME, 4),
    "ios_predicate=": (By.IOS_PREDICATE, 14),
    "ios_class_chain=": (By.IOS_CLASS_CHAIN, 16),
    "android_uiautomator=": (By.ANDROID_UIAUTOMATOR, 20),
    "android_viewtag=": (By.ANDROID_VIEWTAG, 16),
    "android_datamatcher=": (By.ANDROID_DATA_MATCHER, 20),
    "android_viewmatcher=": (By.ANDROID_VIEW_MATCHER, 20),
    "accessibility_id=": (By.ACCESSIBILITY_ID, 17),
    "image=": (By.IMAGE, 6),
    "xpath=": (By.XPATH, 6),
    "css=": (By.CSS_SELECTOR, 4),
}
