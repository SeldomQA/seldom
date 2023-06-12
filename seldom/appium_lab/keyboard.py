"""
App keyboard operation
"""
from seldom.logging import log


keycodes = {
    '0': 7,
    '1': 8,
    '2': 9,
    '3': 10,
    '4': 11,
    '5': 12,
    '6': 13,
    '7': 14,
    '8': 15,
    '9': 16,
    'A': 29,
    'B': 30,
    'C': 31,
    'D': 32,
    'E': 33,
    'F': 34,
    'G': 35,
    'H': 36,
    'I': 37,
    'J': 38,
    'K': 39,
    'L': 40,
    'M': 41,
    'N': 42,
    'O': 43,
    'P': 44,
    'Q': 45,
    'R': 46,
    'S': 47,
    'T': 48,
    'U': 49,
    'V': 50,
    'W': 51,
    'X': 52,
    'Y': 53,
    'Z': 54,
    ',': 55,
    '.': 56,
    ' ': 62,
    '*': 17,
    '#': 18,
    '`': 68,
    '-': 69,
    '[': 71,
    ']': 72,
    '\\': 73,
    ';': 74,
    '/': 76,
    '@': 77,
    '=': 161,
    '+': 157,
    'NUM_LOCK': 143,
    'CAPS_LOCK': 115,
    'HOME': 4,
    'BACK': 3,
}


class KeyEvent:
    """
    KeyEvent:
    https://developer.android.com/reference/android/view/KeyEvent
    """

    def __init__(self, driver):
        self.driver = driver

    def key_text(self, text: str = ""):
        """
        keyword input text.
        :param text: input text

        Usage:
            key_text("Hello")
        """
        if text == "":
            return

        log.info(f'input "{text}"')
        for string in text:
            keycode = keycodes.get(string.upper(), 0)
            if keycode == 0:
                raise KeyError(f"The '{string}' character is not supported")
            if string.isupper():
                self.driver.press_keycode(keycode, 64, 59)
            else:
                self.driver.keyevent(keycode)

    def press_key(self, key: str):
        """
        keyboard
        :param key: keyword name
        press_key("HOME")
        """
        log.info(f'press key "{key}"')
        keycode = keycodes.get(key)
        self.driver.press_keycode(keycode)

    def back(self):
        """go back"""
        log.info("go back")
        self.driver.back()

    def home(self):
        """press home"""
        log.info("press home")
        self.driver.home()

    def hide_keyboard(self, key_name=None, key=None, strategy=None):
        """
        Hides the software keyboard on the device.

        In iOS, use `key_name` to press
        a particular key, or `strategy`. In Android, no parameters are used.

        Args:
            key_name: key to press
            key:
            strategy: strategy for closing the keyboard (e.g., `tapOutside`)

        """
        log.info("hide keyboard")
        self.driver.hide_keyboard(key_name=key_name, key=key, strategy=strategy)

    def is_keyboard_shown(self) -> bool:
        """Attempts to detect whether a software keyboard is present

        Returns:
            `True` if keyboard is shown
        """
        ret = self.driver.is_keyboard_shown()
        log.info(f"is keyboard shown: {ret}")
        return ret
