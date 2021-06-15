## 数据库操作

seldom 支持sqlite3、MySQL数据库操作。

|  sqlite3   | MySQL  |
|  ----  | ----  |
| delete_data()  | delete_data() |
| insert_data()  | insert_data() |
| select_data()  | select_data() |
| update_data()  | update_data() |
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

* delete_data

删除表数据。

```py
db.delete_data(table="user", where={"id":1})
```

* insert_data

插入一条数据。

```py
data = {'id': 1, 'username': 'admin', 'password': "123"},
db.insert_data(table="user", data=data)
```

* select_data

查询表数据。

```py
result = db.select_data(table="user", where={"id":1, "name": "tom"})
print(result)
```

* update_data

更新表数据。

```py
db.update_data(table="user", data={"name":"new tom"}, where={"name": "tom"})
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