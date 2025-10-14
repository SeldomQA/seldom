import seldom
from seldom import file_data


class TestRequest(seldom.TestCase):

    def test_put_method(self):
        """test put case"""
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        """test post case"""
        self.post('/post', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        """test get case"""
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get('/get', params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        """test delete case"""
        self.delete('/delete')
        self.assertStatusCode(200)


class TestDDT(seldom.TestCase):

    @file_data(file="../data.json", key="api")
    def test_get_method(self, _, id_, name):
        """test ddt case"""
        payload = {'key1': id_, 'key2': name}
        self.get('/get', params=payload)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org")
