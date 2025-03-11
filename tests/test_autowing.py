"""
> pip install autowing
"""
import seldom
from seldom import Seldom
from autowing.selenium.fixture import create_fixture
from dotenv import load_dotenv


class TestBingSearch(seldom.TestCase):

    @classmethod
    def start_class(cls):
        # load .env file
        load_dotenv()
        # Create AI fixture
        ai_fixture = create_fixture()
        cls.ai = ai_fixture(Seldom.driver)

    def test_bing_search(self):
        """
        Test Bing search functionality using AI-driven automation.
        """
        self.open("https://cn.bing.com")

        self.ai.ai_action('搜索输入框输入"playwright"关键字，并回车')
        self.sleep(3)

        items = self.ai.ai_query('string[], 搜索结果列表中包含"playwright"相关的标题')

        self.assertGreater(len(items), 1)

        self.assertTrue(
            self.ai.ai_assert('检查搜索结果列表第一条标题是否包含"playwright"字符串')
        )


if __name__ == '__main__':
    seldom.main(browser="edge", debug=True)
