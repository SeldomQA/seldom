from seldom.db_operation import SQLiteDB

db = SQLiteDB(r"D:\github\quick\backend\dev.sqlite3")

db.select("projects")
