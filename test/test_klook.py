from unittest import TestCase

from seldom.utils.klook import MockEnv


class TestMockEnv(TestCase):

    def test_update_case_01(self):
        with open(file='./data/hello.txt', mode='rb') as f:
            file = f.read()
        args = {
            'headers': {
                'Cookie': 'sessionid=qbjk1cjjk98j79jvlkfryqb59dbutljf'
            },
            'files': {
                'file': file
            }
        }
        m = MockEnv(url='https://httpbin.org/post', data={'hello': 'world'}, **args)
        m.update()

    def test_update_case_02(self):
        m = MockEnv(url='https://httpbin.org/post', json={'hello': 'world'})
        m.update()

