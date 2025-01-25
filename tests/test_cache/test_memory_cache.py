import seldom
import time
from seldom.logging import log
from seldom.utils import memory_cache


@memory_cache()
def add(x, y):
    log.info(f"calculating: {x} + {y}")
    time.sleep(2)
    return x + y


class MyTest(seldom.TestCase):

    def test_case(self):
        """test cache 1"""
        r = add(1, 2)
        self.assertEqual(r, 3)

    def test_case2(self):
        """test cache 2"""
        r = add(2, 3)
        self.assertEqual(r, 5)

    def test_case3(self):
        """test cache 3"""
        r = add(1, 2)
        self.assertEqual(r, 3)

    def test_case4(self):
        """test cache 4"""
        r = add(2, 3)
        self.assertEqual(r, 5)


if __name__ == '__main__':
    seldom.main(debug=False)

