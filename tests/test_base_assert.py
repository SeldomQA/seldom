import seldom


class TestAssertions(seldom.TestCase):
    def test_assertEqual(self):
        self.assertEqual(10, 10)  # 正确
        with self.assertRaises(AssertionError):
            self.assertEqual(10, 20)  # 错误

        self.assertNotEqual(10, 20)  # 正确
        with self.assertRaises(AssertionError):
            self.assertNotEqual(10, 10)  # 错误

    def test_assertTrue(self):
        self.assertTrue(True)  # 正确
        with self.assertRaises(AssertionError):
            self.assertTrue(False)  # 错误

        self.assertFalse(False)  # 正确
        with self.assertRaises(AssertionError):
            self.assertFalse(True)  # 错误

    def test_assertIn(self):
        self.assertIn(1, [1, 2, 3])  # 正确
        with self.assertRaises(AssertionError):
            self.assertIn(4, [1, 2, 3])  # 错误

        self.assertNotIn(4, [1, 2, 3])  # 正确
        with self.assertRaises(AssertionError):
            self.assertNotIn(1, [1, 2, 3])  # 错误

    def test_assertIsInstance(self):
        self.assertIsInstance(10, int)  # 正确
        with self.assertRaises(AssertionError):
            self.assertIsInstance(10, str)  # 错误

        self.assertNotIsInstance(10, str)  # 正确
        with self.assertRaises(AssertionError):
            self.assertNotIsInstance(10, int)  # 错误

    def test_assertRegex(self):
        self.assertRegex("hello world", r"hello")  # 正确
        with self.assertRaises(AssertionError):
            self.assertRegex("hello world", r"goodbye")  # 错误

        self.assertNotRegex("hello world", r"goodbye")  # 正确
        with self.assertRaises(AssertionError):
            self.assertNotRegex("hello world", r"hello")  # 错误

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(1.0, 1.00001, places=4)  # 正确
        with self.assertRaises(AssertionError):
            self.assertAlmostEqual(1.0, 1.1, places=4)  # 错误

        self.assertNotAlmostEqual(1.0, 1.1, places=4)  # 正确
        with self.assertRaises(AssertionError):
            self.assertNotAlmostEqual(1.0, 1.00001, places=4)  # 错误

    def test_assertGreater(self):
        self.assertGreater(10, 5)  # 正确
        with self.assertRaises(AssertionError):
            self.assertGreater(5, 10)  # 错误

        self.assertGreaterEqual(10, 10)  # 正确
        with self.assertRaises(AssertionError):
            self.assertGreaterEqual(5, 10)  # 错误

    def test_assertLess(self):
        self.assertLess(5, 10)  # 正确
        with self.assertRaises(AssertionError):
            self.assertLess(10, 5)  # 错误

        self.assertLessEqual(10, 10)  # 正确
        with self.assertRaises(AssertionError):
            self.assertLessEqual(10, 5)  # 错误

    def test_assertCountEqual(self):
        self.assertCountEqual([1, 2, 3], [3, 2, 1])  # 正确
        with self.assertRaises(AssertionError):
            self.assertCountEqual([1, 2, 3], [1, 2])  # 错误


if __name__ == "__main__":
    seldom.main(debug=True)
