# 数据库操作

seldom 支持sqlite3、MySQL、SQL Server、MongoDB数据库操作。

| sqlite3              | MySQL                | SQL Server           | 
|----------------------|----------------------|----------------------|
| execute_sql()        | execute_sql()        | execute_sql()        |
| query_sql()          | query_sql()          | query_sql()          |
| query_one()          | query_one()          | query_one()          |
| insert_get_last_id() | insert_get_last_id() | insert_get_last_id() |
| delete()             | delete()             | delete()             |
| insert()             | insert()             | insert()             |
| select()             | select()             | select()             |
| update()             | update()             | update()             |
| init_table()         | init_table()         | init_table()         |
| close()              | close()              | close()              |

### 连接数据库

__连接sqlit3数据库__

```py
from seldom.db_operation import SQLiteDB

db = SQLiteDB(r"D:\learnAPI\db.sqlite3")
```

__连接MySQL数据库__

1. 安装pymysql驱动

```shell
> pip install pymysql
```

2. 链接

```py
from seldom.db_operation import MySQLDB

db = MySQLDB(host="127.0.0.1",
             port=3306,
             user="root",
             password="123",
             database="db_name")
```

__连接SQL Server数据库（需要）__

1. 安装pymssql驱动

```shell
> pip install pymssql
```

2. 链接

```py
from seldom.db_operation.mssql_db import MSSQLDB

db = MSSQLDB(server="127.0.0.1",
             user="SA",
             password="tc@123",
             database="TestDB")
```

### 操作方法

* execute_sql

执行sql语句，无返回结果。

```python
db.execute_sql("INSERT INTO user (id, name) VALUES (1, 'tom') ")
db.execute_sql("UPDATE user SET name = 'jack' WHERE id=1")
db.execute_sql("DELETE FROM user WHERE id = 1")
```

* query_sql

执行查询sql语句，返回查询结果。

```python
ret = db.query_sql("select * from user")
print(ret)
```

* query_one

执行查询sql语句，返回一条结果。

```python
ret = db.query_one("select * from user")
print(ret)
```

* insert_get_last_id

插入数据并返回最新的ID。

```python
last_id = db.insert_get_last_id("INSERT INTO user (id, name) VALUES (1, 'tom') ")
print(last_id)
```

* delete

删除表数据。

```py
db.delete(table="user", where={"id": 1})
```

* insert

插入一条数据。

```py
data = {"id": 10, "name": "jean"}
db.insert(table="user", data=data)
```

* select

查询表数据。

```py
result = db.select(table="user", where={"id": 1, "name": "tom"})
print(result)
result = db.select(table="user", one=True)  # one=True 返回一条结果
print(result)
```

* update

更新表数据。

```py
db.update(table="user", where={"name": "tom", }, data={"name": "jack"})
```

* init_table

批量插入数据，在插入之前先清空表数据。

```py

# more table data
table_data = {
    "group": [
        {"id": 1, "name": "test"},
        {"id": 2, "name": "product"},
        {"id": 3, "name": "develop"},
    ],
    "user": [
        {"id": 1, "name": "jeannie"},
        {"id": 2, "name": "joye"},
        {"id": 3, "name": "blue"},
    ],

}

db.init_table(table_data)
```

* close

关闭数据库连接。

```py
db.close()
```

## MongoDB

MongoDB 是一个基于分布式文件存储的数据库，属于非关系型数据库，与关系型数据库得操作有着较大得差异，它本身支持字典传参，所以，seldom 只简单封装了数据库连接。

* 安装pymongo

https://github.com/mongodb/mongo-python-driver

```shell
> pip show pymongo
```

* 连接MongoDB

```python
from seldom.db_operation.mongo_db import MongoDB

db = MongoDB(host="localhost", port=27017, db="yapi")
```

__参数说明:__

* host: 连接地址。
* port: 端口号。
* db: 数据库名字。

__pymongo__

以下操作seldom没有做任何封装，请参考[pymongo](https://github.com/mongodb/mongo-python-driver)

* 获取集合信息

```python
col = db.list_collection_names()
print(col)
```

结果：

```shell
collection list:  ['project', 'log', ...]
```

* 获取表一条数据

```python
data = db.project.find_one()
print("table one data:", data)
```

结果：

```shell
table data: {'_id': 11, 'switch_notice': True, 'is_mock_open': False, 'strice': False, 'is_json5': False, 'name': '发布会签到系统'}
```

* [添加数据](https://www.runoob.com/python3/python-mongodb-insert-document.html)
* [查询数据](https://www.runoob.com/python3/python-mongodb-query-document.html)
* [修改数据](https://www.runoob.com/python3/python-mongodb-update-document.html)
* [删除数据](https://www.runoob.com/python3/python-mongodb-delete-document.html)


