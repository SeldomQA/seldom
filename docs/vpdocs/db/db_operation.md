# 数据库操作

seldom 支持sqlite3、MySQL、MongoDB数据库操作。

|  sqlite3   | MySQL  |
|  ----  | ----  |
| execute_sql()  | execute_sql() |
| query_sql()  | query_sql() |
| delete()  | delete() |
| insert()  | insert() |
| select()  | select() |
| update()  | update() |
| init_table()  | init_table() |
| close()  | close() |

### 连接数据库

__连接sqlit3数据库__

```py
from seldom.db_operation import SQLiteDB

db = SQLiteDB(r"D:\learnAPI\db.sqlite3")
```

__连接MySQL数据库（需要）__

1. 安装pymysql驱动

```shell
> pip install pymysql
```

2. 链接

```py
from seldom.db_operation import MySQLDB

db = MySQLDB(host="127.0.0.1", 
             port="3306", 
             user="root", 
             password="123", 
             database="db_name")
```

### 操作方法

* execute_sql

执行sql语句，无返回结果。

```python
db.execute_sql("INSERT INTO table_name (id, name) VALUES (1, 'tom') ")
db.execute_sql("UPDATE table_name SET name = 'jack' WHERE id=1")
db.execute_sql("DELETE FROM table_name WHERE id = 1")
```

* query_sql

执行查询sql语句，返回查询结果。

```python
ret = db.query_sql("select * from table_name")
print(ret)
```

* delete

删除表数据。

```py
db.delete(table="user", where={"id":1})
```

* insert

插入一条数据。

```py
data = {'id': 1, 'username': 'admin', 'password': "123"},
db.insert(table="user", data=data)
```

* select_data

查询表数据。

```py
result = db.select(table="user", where={"id":1, "name": "tom"})
print(result)
```

* update

更新表数据。

```py
db.update(table="user", data={"name":"new tom"}, where={"name": "tom"})
```


* init_table

批量插入数据，在插入之前先清空表数据。

```py

datas = {
    'api_event': [
        {'id': 1, 'name': '红米Pro发布会'},
        {'id': 2, 'name': '可参加人数为0'},
        {'id': 3, 'name': '当前状态为0关闭'},
        {'id': 4, 'name': '发布会已结束'},
        {'id': 5, 'name': '小米5发布会'},
    ],
    'api_guest': [
        {'id': 1, 'real_name': 'alen'},
        {'id': 2, 'real_name': 'has sign'},
        {'id': 3, 'real_name': 'tom'},
    ]
}

db.init_table(datas)
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
pip show pymongo
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


