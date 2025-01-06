import time
import seldom
from seldom.testdata import get_int
from seldom.utils.benchmark import benchmark_test


class MyTests(seldom.TestCase):

    @benchmark_test()
    def test_something_performance_1(self):
        """
        something code performance
        """
        num = get_int(1, 2000) / 1000
        time.sleep(num)

    @benchmark_test(rounds=10, iterations=2)
    def test_something_performance_2(self):
        """
        something code performance
        """
        num = get_int(1, 2000) / 1000
        time.sleep(num)

    @benchmark_test(rounds=10)
    def test_http_performance(self):
        """
        test http benchmark
        """
        self.get("https://httpbin.org/get")
        self.assertStatusOk()


if __name__ == "__main__":
    seldom.main(debug=True)
