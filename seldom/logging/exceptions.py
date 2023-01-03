"""
Exceptions that may happen in all the seldom code.
"""


class SeldomException(Exception):
    """
    Base seldom exception.
    """

    def __init__(self, msg: str = None, screen: str = None, stacktrace: str = None):
        self.msg = msg
        self.screen = screen
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = f"Message: {self.msg}\n"
        if self.screen is not None:
            exception_msg += "Screenshot: available via screen\n"
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += f"Stacktrace:\n{stacktrace}"
        return exception_msg


class BrowserTypeError(SeldomException):
    """
    Browser type error
    """
    pass


class NotFindElementError(SeldomException):
    """
    No element errors were found
    """
    pass


class TestFixtureRunError(SeldomException):
    """
    Test fixture run error
    """
    pass


class FileTypeError(SeldomException):
    """
    Data file type error
    """
    pass
