try:
    import pymysql.cursors
except ModuleNotFoundError:
    raise ModuleNotFoundError("Please install the library. https://pypi.org/project/PyMySQL/")
from seldom.db_operation.base_db import SQLBase


class MySQLDB(SQLBase):

    def __init__(self, host, port, user, password, database):
        """
        Connect to the MySQL database
        """
        self.connection = pymysql.connect(host=host,
                                          port=int(port),
                                          user=user,
                                          password=password,
                                          database=database,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def delete_table(self, table):
        """
        delete table data
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("delete from  {};".format(table))
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
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        self.connection.commit()

    def select_data(self, table, where=None):
        """
        select sql statement
        """
        data_list = []
        sql = """select * from {} """.format(table)
        if where is not None:
            sql += 'where {};'.format(self.dict_to_str_and(where))
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
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
