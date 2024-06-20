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

    @property
    def path(self) -> Path:
        """
        Returns the absolute path to the directory where the current file resides
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/test_dir/test_sample.py"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        file_path = Path(ins.filename).resolve()
        return file_path

    @property
    def dir(self) -> Path:
        """
        Returns the absolute path to the directory where the current file resides
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/test_dir/"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        file_path = Path(ins.filename).resolve()
        return file_path.parent

    @property
    def dir_dir(self) -> Path:
        """
        Returns the absolute directory path of the current file directory.
        For example:
            "/User/tech/you/test_dir/test_sample.py"
            return "/User/tech/you/"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        file_path = Path(ins.filename).resolve()
        return file_path.parent.parent

    @property
    def dir_dir_dir(self) -> Path:
        """
        Returns the absolute directory path of the current file directory
        For example:
            /User/tech/you/test_dir/test_sample.py
            return "/User/you/"
        """
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        file_path = Path(ins.filename).resolve()
        return file_path.parent.parent.parent

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
