"""
author: bugmaster
data: 2022/10/01
desc: 数据库操作
Please install the library. https://github.com/psycopg/psycopg2
"""
import unittest

from seldom.db_operation.postgres_db import PostgresDB


class PostgresDBTest(unittest.TestCase):
    def setUp(self) -> None:
        """"初始化DB连接"""
        self.db = PostgresDB(host="localhost", port=3306, user="dev", password="808801", database="db_user")
        sql = """INSERT INTO 
        public.cusm_account (id, name, cn_name, mobile_phone_region, mobile_phone, email, password, status) 
        VALUES (DEFAULT, 'test', 'ces', '+86', '13122221111', null, '123456Aq!', 1) """
        self.db.execute_sql(sql)

    def tearDown(self) -> None:
        self.db.delete("public.cusm_account", {"name": "test"})

    def test_query_sql(self):
        """测试查询SQL"""
        result = self.db.query_sql("select * from public.cusm_account")
        self.assertIsInstance(result, list)

    def test_query_one(self):
        """测试查询SQL一条数据"""
        result = self.db.query_one("select * from public.cusm_account")
        self.assertIsInstance(result, dict)

    def test_execute_sql(self):
        """测试执行SQL"""
        db = self.db
        db.execute_sql("INSERT INTO public.cusm_account (name, cn_name) VALUES ('tom', 22) ")
        db.execute_sql("UPDATE public.cusm_account SET cn_name=23 WHERE name='tom'")
        db.execute_sql("DELETE FROM public.cusm_account WHERE name = 'tom' ")
        result = db.query_sql("select * from public.cusm_account WHERE name='tom'")
        self.assertEqual(len(result), 0)

    def test_select_sql(self):
        """测试查询SQL"""
        result1 = self.db.select(table="public.cusm_account", where={"name": "test"})
        self.assertEqual(result1[0]["name"], "test")
        result2 = self.db.select(table="public.cusm_account", one=True)
        self.assertIsInstance(result2, list)

    def test_delete_sql(self):
        """测试删除SQL"""
        # delete sql
        self.db.delete(table="public.cusm_account", where={"name": "test"})
        result = self.db.query_sql("select * from public.cusm_account WHERE name='test'")
        self.assertEqual(len(result), 0)

    def test_update_sql(self):
        """测试更新SQL"""
        self.db.update(table="public.cusm_account", where={"name": "test", }, data={"cn_name": "22"})
        result = self.db.query_sql("select * from public.cusm_account WHERE name='test'")
        self.assertEqual(result[0]["cn_name"], 22)

    def test_insert_sql(self):
        """测试插入SQL"""
        data = {"name": "jean", "cn_name": 11}
        self.db.insert(table="public.cusm_account", data=data)
        result = self.db.query_sql("select * from public.cusm_account WHERE name='jean'")
        self.assertTrue(len(result[0]) > 1)


if __name__ == "__main__":
    unittest.main()
