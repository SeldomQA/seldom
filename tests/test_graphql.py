import seldom
from seldom import TestCase
from seldom.utils.resource_loader import resource_file


class TestGraphQL(TestCase):

    def test_graphql_query(self):
        """
        查询中国（code: "CN"）的名称、首都、货币和官方语言
        """

        params = {
            "query": resource_file("country.graphql"),
            "variables": {
                "code": "CN"  # 可以改成 "US", "FR", "JP" 等
            }
        }
        self.post("/", json=params)
        self.assertStatusOk()
        self.assertPath("data.country.name", "China")


if __name__ == '__main__':
    seldom.main(base_url="https://countries.trevorblades.com", debug=True)
