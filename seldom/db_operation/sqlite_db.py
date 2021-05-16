import sqlite3


class SQLiteDB:

    def __init__(self, db_path):
        """
        Connect to the sqlite database
        """
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def delete_table(self, table):
        """
        delete table data
        """
        self.cursor.execute("delete from {};".format(table))
        self.connection.commit()

    def close(self):
        """
        Close the database connection
        """
        self.connection.close()

    def insert_data(self, table, data):
        """
        insert sql statement
        """
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        sql = """INSERT INTO {t} ({k}) VALUES ({v})""".format(t=table, k=key, v=value)
        self.cursor.execute(sql)
        self.connection.commit()

    def select_table(self, table):
        """
        select sql statement
        """
        data_list = []
        sql = """select * from {} ;""".format(table)
        rows = self.cursor.execute(sql)
        for row in rows:
            data_list.append(row)
        return data_list

    def init_table(self, table_data):
        """
        init table data
        """
        for table, data in table_data.items():
            self.delete_table(table)
            for d in data:
                self.insert_data(table, d)
        self.close()
