"""
author: bugmaster
data: 2022/10/01
desc: 数据库操作
"""
import unittest
from seldom.db_operation import SQLiteDB, MySQLDB
from seldom.db_operation.mssql_db import MSSQLDB


class MySQLTest(unittest.TestCase):
    """测试操作MySQL数据库API"""

    def setUp(self) -> None:
        """"初始化DB连接"""
        self.db = MySQLDB(host="localhost", port=3306, user="root", password="198876", database="guest3")
        self.db.execute_sql("INSERT INTO api_user (name, age) VALUES ('test', 11) ")

    def tearDown(self) -> None:
        self.db.delete("api_user", {"name": "test"})

    def test_query_sql(self):
        """测试查询SQL"""
        result = self.db.query_sql("select * from api_user")
        self.assertIsInstance(result, list)

    def test_query_one(self):
        """测试查询SQL一条数据"""
        result = self.db.query_one("select * from api_user")
        self.assertIsInstance(result, dict)

    def test_execute_sql(self):
        """测试执行SQL"""
        db = self.db
        db.execute_sql("INSERT INTO api_user (name, age) VALUES ('tom', 22) ")
        db.execute_sql("UPDATE api_user SET age=23 WHERE name='tom'")
        db.execute_sql("DELETE FROM api_user WHERE name = 'tom' ")
        result = db.query_sql("select * from api_user WHERE name='tom'")
        self.assertEqual(len(result), 0)

    def test_select_sql(self):
        """测试查询SQL"""
        result1 = self.db.select(table="api_user", where={"name": "test"})
        self.assertEqual(result1[0]["name"], "test")
        result2 = self.db.select(table="api_user", one=True)
        self.assertIsInstance(result2, dict)

    def test_delete_sql(self):
        """测试删除SQL"""
        # delete sql
        self.db.delete(table="api_user", where={"name": "test"})
        result = self.db.query_sql("select * from api_user WHERE name='test'")
        self.assertEqual(len(result), 0)

    def test_update_sql(self):
        """测试更新SQL"""
        self.db.update(table="api_user", where={"name": "test", }, data={"age": "22"})
        result = self.db.query_sql("select * from api_user WHERE name='test'")
        self.assertEqual(result[0]["age"], 22)

    def test_insert_sql(self):
        """测试插入SQL"""
        data = {"name": "jean", "age": 11}
        self.db.insert(table="api_user", data=data)
        result = self.db.query_sql("select * from api_user WHERE name='jean'")
        self.assertTrue(len(result[0]) > 1)

    def test_init_table(self):
        """测试批量插入数据"""
        # more table data
        table_data = {
            "api_group": [
                {"name": "test"},
                {"name": "product"},
                {"name": "develop"},
            ],
            "api_user": [
                {"name": "jeannie", "age": 25},
                {"name": "joye", "age": 26},
                {"name": "blue", "age": 27},
            ],
        }
        self.db.init_table(table_data)


class SQLite3Test(unittest.TestCase):
    """测试SQLite数据库API"""

    def setUp(self) -> None:
        """"初始化DB连接"""
        self.db = SQLiteDB(r"D:\github\seldom\backend\db.sqlite3")
        self.db.insert(table="api_user", data= {"name": "test", "age": 11})

    def tearDown(self) -> None:
        self.db.delete("api_user", {"name": "test"})

    def test_query_sql(self):
        """测试查询SQL"""
        result = self.db.query_sql("select * from api_user")
        self.assertIsInstance(result, list)

    def test_query_one(self):
        """测试查询SQL"""
        result = self.db.query_one("select * from api_user")
        self.assertIsInstance(result, tuple)

    def test_execute_sql(self):
        """测试执行SQL"""
        db = self.db
        db.execute_sql("INSERT INTO api_user (name, age) VALUES ('tom', 22) ")
        db.execute_sql("UPDATE api_user SET age=23 WHERE name='tom'")
        db.execute_sql("DELETE FROM api_user WHERE name = 'tom' ")
        result = db.query_sql("select * from api_user WHERE name='tom'")
        self.assertEqual(len(result), 0)

    def test_select_sql(self):
        """测试查询SQL"""
        result = self.db.select(table="api_user", where={"name": "test"})
        self.assertEqual(result[0][1], "test")
        result = self.db.select(table="api_user", one=True)
        self.assertIsInstance(result, tuple)

    def test_delete_sql(self):
        """测试删除SQL"""
        # delete sql
        self.db.delete(table="api_user", where={"name": "test"})
        result = self.db.query_sql("select * from api_user WHERE name='test'")
        self.assertEqual(len(result), 0)

    def test_update_sql(self):
        """测试更新SQL"""
        self.db.update(table="api_user", where={"name": "test", }, data={"age": "22"})
        result = self.db.query_sql("select * from api_user WHERE name='test'")
        self.assertEqual(result[0][2], 22)

    def test_insert_sql(self):
        """测试插入SQL"""
        data = {"name": "jean", "age": 11}
        self.db.insert(table="api_user", data=data)
        result = self.db.query_sql("select * from api_user WHERE name='jean'")
        self.assertTrue(len(result[0]) > 1)

    def test_init_table(self):
        """测试批量插入数据"""
        # more table data
        table_data = {
            "api_group": [
                {"name": "test"},
                {"name": "product"},
                {"name": "develop"},
            ],
            "api_user": [
                {"name": "jeannie", "age": 25},
                {"name": "joye", "age": 26},
                {"name": "blue", "age": 27},
            ],
        }
        self.db.init_table(table_data)


class MSSQLTest(unittest.TestCase):
    """测试操作MS SQL Server数据库API"""

    def setUp(self) -> None:
        """"初始化DB连接"""
        self.db = MSSQLDB(server="127.0.0.1", user="SA", password="tc@123", database="TestDB")
        self.db.execute_sql("INSERT INTO users (email, password) VALUES ('test@gmail.com', 'test123') ")

    def tearDown(self) -> None:
        self.db.delete("users", {"email": "test@gmail.com"})

    def test_query_sql(self):
        """测试查询SQL"""
        result = self.db.query_sql("select * from users")
        self.assertIsInstance(result, list)

    def test_query_one(self):
        """测试查询SQL一条数据"""
        result = self.db.query_one("select * from users")
        self.assertIsInstance(result, tuple)

    def test_execute_sql(self):
        """测试执行SQL"""
        db = self.db
        db.execute_sql("INSERT INTO users (email, password) VALUES ('tom@gmail.com', 'tom22') ")
        db.execute_sql("UPDATE users SET password='tom33' WHERE email='tom@gmail.com'")
        db.execute_sql("DELETE FROM users WHERE email = 'tom@gmail.com' ")
        result = db.query_sql("select * from users WHERE email='tom@gmail.com'")
        self.assertEqual(len(result), 0)

    def test_select_sql(self):
        """测试查询SQL"""
        result1 = self.db.select(table="users", where={"email": "test@gmail.com"})
        self.assertEqual(result1[0][1], "test@gmail.com")
        result2 = self.db.select(table="users", one=True)
        self.assertIsInstance(result2, tuple)

    def test_delete_sql(self):
        """测试删除SQL"""
        self.db.delete(table="users",  where={"email": "test@gmail.com"})
        result = self.db.query_sql("select * from users WHERE email='test@gmail.com'")
        self.assertEqual(len(result), 0)

    def test_update_sql(self):
        """测试更新SQL"""
        self.db.update(table="users", where={"email": "test@gmail.com", }, data={"password": "test22"})
        result = self.db.query_sql("select * from users WHERE email='test@gmail.com'")
        self.assertEqual(result[0][2], 'test22')

    def test_insert_sql(self):
        """测试插入SQL"""
        data = {"email": "jean@gmail.com", "password": "jean11"}
        self.db.insert(table="users", data=data)
        result = self.db.query_sql("select * from users WHERE email='jean@gmail.com'")
        self.assertTrue(len(result[0]) > 1)

    def test_init_table(self):
        """测试批量插入数据"""
        # more table data
        table_data = {
            "users": [
                {"email": "jeannie@gmail.com", "password": "jeannie25"},
                {"email": "joye@gmail.com", "password": "joye26"},
                {"email": "blue@gmail.com", "password": "blue27"},
            ],
        }
        self.db.init_table(table_data)


if __name__ == "__main__":
    unittest.main()
