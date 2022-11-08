import seldom
from seldom import testdata


class FileDataTest(seldom.TestCase):
    """
    Randomly generate test data
    """

    def test_testdata(self):
        """
        used testdata test
        """
        self.open("https://www.runoob.com/try/try.php?filename=tryhtml_input")
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=testdata.first_name())
        self.type(name="lastname", text=testdata.last_name())
        self.sleep(1)


if __name__ == '__main__':
    seldom.main(browser="gc", debug=True)
