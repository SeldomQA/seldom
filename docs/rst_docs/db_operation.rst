Database Operation
--------------------

``seldom`` supports simple operations of SQLite3 and MySQL database.

+-------------------+-------------------+
| sqlite3           | MySQL             |
+===================+===================+
| delete\_data()    | delete\_data()    |
+-------------------+-------------------+
| insert\_data()    | insert\_data()    |
+-------------------+-------------------+
| select\_data()    | select\_data()    |
+-------------------+-------------------+
| update\_data()    | update\_data()    |
+-------------------+-------------------+
| init\_table()     | init\_table()     |
+-------------------+-------------------+
| close()           | close()           |
+-------------------+-------------------+


Connecting DB
~~~~~~~~~~~~~~~~~~

**Connect to SQLit3 database**

.. code:: py

    from seldom.db_operation import SQLiteDB

    db = SQLiteDB(r"D:\learnAPI\db.sqlite3")


**Connect to MySQL database**

1. Install the PyMySQL driver

.. code:: shell

    > pip install pymysql


2. connect to databases

.. code:: py

    from seldom.db\_operation import MySQLDB

    db = MySQLDB(host="127.0.0.1", port="3306", user="root", password="123",
    database="db_name")


Operation Method
~~~~~~~~~~~~~~~~~~

-  delete\_data

Delete table data.

.. code:: py

    db.delete_data(table="user", where={"id":1})


-  insert\_data

Insert a data.

.. code:: py

    data = {'id': 1, 'username': 'admin', 'password': "123"},
    db.insert_data(table="user", data=data)


-  select\_data

Query data in the table.

.. code:: py

    result = db.select_data(table="user", where={"id":1, "name": "tom"})
    print(result)


-  update\_data

Update table data.

.. code:: py

    db.update_data(table="user", data={"name":"new tom"}, where={"name": "tom"})


-  init\_table

Bulk inserts, clearing table data before inserting.

.. code:: py


    datas = {
        'api_event': [
            {'id': 1, 'name': 'Redmi PRO launch1'},
            {'id': 2, 'name': 'Redmi2 PRO launch'},
            {'id': 3, 'name': 'Redmi3 PRO launch'},
            {'id': 4, 'name': 'Redmi4 PRO launch'},
            {'id': 5, 'name': 'Redmi5 PRO launch'},
        ],
        'api_guest': [
            {'id': 1, 'real_name': 'alen'},
            {'id': 2, 'real_name': 'jack'},
            {'id': 3, 'real_name': 'tom'},
        ]
    }

    db.init_table(datas)

-  close

Close the database connection.

.. code:: py

    db.close()
