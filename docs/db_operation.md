## 数据库操作

seldom 支持sqlite3、MySQL数据库操作。

|  sqlite3   | MySQL  |
|  ----  | ----  |
| delete_table()  | delete_table() |
| close()  | close() |
| insert_data()  | insert_data() |
| select_table()  | select_table() |
| init_table()  | init_table() |

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

* delete_table

清空表数据。

```py
table_name = "user"
db.delete_table(table_name)
```

* insert_data

插入一条数据。

```py
table_name = "user"
data = {'id': 1, 'username': 'admin', 'password': "123"},
db.insert_data(table_name, data)
```

* select_table

查询表所有数据。

```py
table_name = "user"
result = db.insert_data(select_table)
print(result)
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