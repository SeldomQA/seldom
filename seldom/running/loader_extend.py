"""seldom Loading unittests."""

import functools
from fnmatch import fnmatchcase
from unittest.loader import TestLoader


class SeldomTestLoader(TestLoader):
    """
    This class is responsible for loading tests according to various criteria
    and returning them wrapped in a TestSuite
    """
    testNamePatterns = None
    collectCaseInfo = False  # Switch of collecting use case information
    collectCaseList = []     # List of use case information

    def getTestCaseNames(self, testCaseClass):
        """Return a sorted sequence of method names found within testCaseClass
        """

        def shouldIncludeMethod(attrname):
            """
            should Include Method
            :param attrname:
            :return:
            """
            if not attrname.startswith(self.testMethodPrefix):
                return False
            testFunc = getattr(testCaseClass, attrname)
            if not callable(testFunc):
                return False

            fullName = f"""{testCaseClass.__module__}.{testCaseClass.__qualname__}.{attrname}"""

            if self.collectCaseInfo is True:
                case_info = {
                    "file": testCaseClass.__module__,
                    "class": {
                        "name": testCaseClass.__name__,
                        "doc": testCaseClass.__doc__
                    },
                    "method": {
                        "name": attrname,
                        "doc": testFunc.__doc__
                    }
                }
                self.collectCaseList.append(case_info)

            return self.testNamePatterns is None or \
                   any(fnmatchcase(fullName, pattern) for pattern in self.testNamePatterns)

        testFnNames = list(filter(shouldIncludeMethod, dir(testCaseClass)))
        if self.sortTestMethodsUsing:
            testFnNames.sort(key=functools.cmp_to_key(self.sortTestMethodsUsing))
        return testFnNames


seldomTestLoader = SeldomTestLoader()
