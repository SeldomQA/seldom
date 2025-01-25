import os
import pyautogui
import seldom
from seldom.testdata import get_int


class TestPyAutoGUINote(seldom.TestCase):

    def start(self):
        # 打开记事本（这里使用运行命令来打开，确保路径正确）
        os.system('notepad.exe')
        self.sleep()

    def end(self):
        # 模拟按下 Alt+F4 关闭记事本
        pyautogui.hotkey('alt', 'f4')

    def test_write_and_save(self):
        """
        打开一个新的标签页写入内容并保存
        """
        # 模拟按下 Ctrl+t 创建一个新的标签页
        pyautogui.hotkey('ctrl', 't')

        self.sleep()
        pyautogui.press('shift')  # 切换英文输入法

        # 写入字符串到记事本
        pyautogui.write('Hello, this is a test string written by pyautogui.', interval=0.1)  # interval 参数设置每个字符之间的延迟时间

        # 模拟按下 Ctrl+S 保存文件
        pyautogui.hotkey('ctrl', 's')
        self.sleep()

        # 切换英文输入法
        pyautogui.press('shift')
        self.sleep()

        # 输入文件名 + 回车确定
        pyautogui.write(f'test_file{get_int()}.txt')
        self.sleep()
        pyautogui.press('enter')
        self.sleep()


if __name__ == '__main__':
    seldom.main()
