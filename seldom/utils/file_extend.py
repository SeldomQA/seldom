"""
file extend
"""
import os
import sys
import inspect
from pathlib import Path


class FindFilePath:
    """find file path"""

    def __new__(cls, name: str = None) -> str:
        if name is None:
            raise NameError("Please specify filename")
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        file_path = Path(ins.filename).resolve()
        this_file_dir = file_path.parent.parent

        _file_path = None
        for root, _, files in os.walk(this_file_dir, topdown=False):
            for _file in files:
                if _file == name:
                    _file_path = os.path.join(root, _file)
                    break
            else:
                continue
            break
        return _file_path


find_file_path = FindFilePath


class File:
    """file class"""

    @staticmethod
    def _get_caller_path(min_stack_level: int = 2) -> str:
        """
        Automatically find and return the correct caller's file path as string.
        """
        # 遍历调用栈，找到最终调用者的文件路径
        for level in range(min_stack_level, len(inspect.stack())):
            frame = inspect.stack()[level].frame
            filename = inspect.getframeinfo(frame).filename
            if not filename.endswith("file_extend.py"):
                return str(Path(filename).resolve())
        raise RuntimeError("Unable to determine caller path.")

    @property
    def path(self) -> str:
        """
        Returns the absolute path to the current file.
        e.g., /User/tech/you/test_dir/test_sample.py
        """
        return str(self._get_caller_path())

    @property
    def dir(self) -> str:
        """
        Returns the absolute path to the directory where the current file resides
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/test_dir/"
        """
        return str(Path(self.path).parent)

    def parent_dir(self, level: int = 1) -> str:
        """
        Generic method to get N-th parent directory.

        :param level: How many levels up from current file.
        :return: Parent directory path.
        """
        return str(Path(self.path).parents[level - 1])

    @property
    def dir_dir(self) -> str:
        """
        Returns the absolute directory path of the current file directory.
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/"
        """
        return self.parent_dir(2)

    @property
    def dir_dir_dir(self) -> str:
        """
        Returns the absolute directory path of the current file directory
        For example:
            /User/tech/you/test_dir/test_sample.py
            return "/User/tech/"
        """
        return self.parent_dir(3)

    @staticmethod
    def add_to_path(path: str = None) -> None:
        """
        add path to environment variable path.
        """
        if path is None:
            raise FileNotFoundError("Please setting the File Path")

        sys.path.insert(1, path)

    @staticmethod
    def join(a, *paths):
        """
        Connect two or more path names
        """
        return os.path.join(a, *paths)

    @staticmethod
    def remove(path) -> None:
        """
        del file
        :param path:
        :return:
        """
        if Path(path).exists():
            os.remove(path)
        else:
            raise FileNotFoundError("file does not exist")


file = File()
