Database Operation
--------------------

``seldom`` supports simple operations of SQLite3 and MySQL database.

+-------------------+-------------------+
| sqlite3           | MySQL             |
+===================+===================+
| execute_sql()     | execute_sql()     |
+-------------------+-------------------+
| query_sql()       | query_sql()       |
+-------------------+-------------------+
| delete()          | delete()          |
+-------------------+-------------------+
| insert()          | insert()          |
+-------------------+-------------------+
| select()          | select()          |
+-------------------+-------------------+
| update()          | update()          |
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

-  execute_sql

The SQL statement was executed, but no result was returned.

.. code:: py

    db.execute_sql("INSERT INTO table_name (id, name) VALUES (1, 'tom') ")
    db.execute_sql("UPDATE table_name SET name = 'jack' WHERE id=1")
    db.execute_sql("DELETE FROM table_name WHERE id = 1")


-  query_sql

The query SQL statement is executed and the query result is returned.

.. code:: py

    ret = db.query_sql("select * from table_name")
    print(ret)


-  delete

Delete table data.

.. code:: py

    db.delete(table="user", where={"id":1})


-  insert

Insert a data.

.. code:: py

    data = {'id': 1, 'username': 'admin', 'password': "123"},
    db.insert(table="user", data=data)


-  select

Query data in the table.

.. code:: py

    result = db.select(table="user", where={"id":1, "name": "tom"})
    print(result)


-  update

Update table data.

.. code:: py

    db.update(table="user", data={"name":"new tom"}, where={"name": "tom"})


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
