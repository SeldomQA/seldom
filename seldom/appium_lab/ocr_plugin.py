"""
Appium OCR plugin
help: https://github.com/jlipps/appium-ocr-plugin
"""
from appium.webdriver.webdriver import ExtensionBase


class OCRCommand(ExtensionBase):
    def method_name(self):
        return 'ocr_command'

    def ocr_command(self, argument):
        return self.execute(argument)['value']

    def add_command(self):
        add = ('post', '/session/$sessionId/appium/ocr')
        return add
