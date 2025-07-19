import unittest
from pathlib import Path
from seldom.utils import file


class TestFilePathUtils(unittest.TestCase):

    def test_path_is_string_and_correct(self):
        """测试 path 属性是否是字符串且路径正确"""
        self.assertIsInstance(file.path, str)
        expected_path = str(Path(__file__).resolve())
        self.assertEqual(file.path, expected_path)

    def test_dir_is_string_and_correct(self):
        """测试 dir 属性是否是字符串且路径正确"""
        self.assertIsInstance(file.dir, str)
        expected_dir = str(Path(__file__).resolve().parent)
        self.assertEqual(file.dir, expected_dir)

    def test_dir_dir_is_string_and_correct(self):
        """测试 dir_dir 属性是否是字符串且路径正确"""
        self.assertIsInstance(file.dir_dir, str)
        expected_dir_dir = str(Path(__file__).resolve().parent.parent)
        self.assertEqual(file.dir_dir, expected_dir_dir)

    def test_dir_dir_dir_is_string_and_correct(self):
        """测试 dir_dir_dir 属性是否是字符串且路径正确"""
        self.assertIsInstance(file.dir_dir_dir, str)
        expected_dir_dir_dir = str(Path(__file__).resolve().parent.parent.parent)
        self.assertEqual(file.dir_dir_dir, expected_dir_dir_dir)

    def test_parent_dir_is_string_and_correct(self):
        """测试 parent_dir 方法是否是字符串且路径正确（level=4）"""
        self.assertIsInstance(file.parent_dir(4), str)
        expected_parent_4 = str(Path(__file__).resolve().parents[3])
        self.assertEqual(file.parent_dir(4), expected_parent_4)


if __name__ == '__main__':
    unittest.main()
