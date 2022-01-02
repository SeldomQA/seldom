import re
import unittest
import functools


class DebugTestRunner(unittest.TextTestRunner):

    def __init__(self, *args, **kwargs):
        """
        Append blacklist & whitelist attributes to TestRunner instance
        """
        self.whitelist = set(kwargs.pop('whitelist', []))
        self.blacklist = set(kwargs.pop('blacklist', []))

        super(DebugTestRunner, self).__init__(*args, **kwargs)

    @classmethod
    def test_iter(cls, suite):
        """
        Iterate through test suites, and yield individual tests
        """
        for test in suite:
            if isinstance(test, unittest.TestSuite):
                for t in cls.test_iter(test):
                    yield t
            else:
                yield test

    def run(self, testlist):
        """
        Run the given test case or test suite.
        """
        # Change given testlist into a TestSuite
        suite = unittest.TestSuite()

        # Add each test in testlist, apply skip mechanism if necessary
        for test in self.test_iter(testlist):
            # Determine if test should be skipped
            skip = bool(self.whitelist)
            test_method = getattr(test, test._testMethodName)
            test_labels = getattr(test, '_labels', set()) | getattr(test_method, '_labels', set())
            if test_labels & self.whitelist:
                skip = False
            if test_labels & self.blacklist:
                skip = True

            if skip:
                # Test should be skipped.
                # replace original method with function "skip"
                # Create a "skip test" wrapper for the actual test method
                @functools.wraps(test_method)
                def skip_wrapper(*args, **kwargs):
                    raise unittest.SkipTest('label exclusion')
                skip_wrapper.__unittest_skip__ = True
                if len(self.whitelist) >= 1:
                    skip_wrapper.__unittest_skip_why__ = f'label whitelist {self.whitelist}'
                if len(self.blacklist) >= 1:
                    skip_wrapper.__unittest_skip_why__ = f'label blacklist {self.blacklist}'
                setattr(test, test._testMethodName, skip_wrapper)

            suite.addTest(test)

        # Resume normal TextTestRunner function with the new test suite
        super(DebugTestRunner, self).run(suite)


if __name__ == '__main__':
    import argparse

    # ---- create commandline parser
    parser = argparse.ArgumentParser(description='Find and run cqparts tests.')

    def label_list(value):
        return re.split(r'\W+', value)

    parser.add_argument('-w', '--whitelist', dest='whitelist',
                        type=label_list, default=[],
                        help="list of labels to test (skip all others)")
    parser.add_argument('-b', '--blacklist', dest='blacklist',
                        type=label_list, default=[],
                        help="list of labels to skip")

    args = parser.parse_args()

    # ---- Discover and run tests

    # Discover Tests
    loader = unittest.TestLoader()
    tests = loader.discover('.', pattern='test_*.py')

    # Run tests
    testRunner = DebugTestRunner(
        blacklist=args.blacklist,
        whitelist=args.whitelist,
        verbosity=2,
    )
    testRunner.run(tests)
