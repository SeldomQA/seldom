import time
from seldom.db_operation import SQLiteDB, MySQLDB


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

if __name__ == "__main__":
    # connect SQLite3
    db = SQLiteDB(r"you\path\db.sqlite3")
    # connect MySQL
    # db = MySQLDB(host="127.0.0.1", port="3306", user="root", password="123456", database="dev_db")

    # query sql
    ret = db.query_sql("select * from user")
    print(ret)

    # execute sql
    db.execute_sql("INSERT INTO user (id, name) VALUES (1, 'tom') ")
    db.execute_sql("UPDATE user SET name = 'jack' WHERE id=1")
    db.execute_sql("DELETE FROM user WHERE id = 1")

    # select sql
    result = db.select(table="user", where={"id": 1, "name": "tom"})
    print(result)

    # delete sql
    db.delete(table="user", where={"id": 5})

    # update sql
    db.update(table="user", where={"name": "tom", }, data={"name": "jack"})

    # insert sql
    data = {"id": 10, "name": "jean"}
    db.insert(table="user", data=data)

    # Batch insert data
    db.init_table(table_data)
