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

    def delete_data(self, table, where=None):
        """
        delete table data
        """
        sql = """delete from {}""".format(table)
        if where is not None:
            sql += ' where {};'.format(self.dict_to_str_and(where))
        with self.connection.cursor() as cursor:
            self.connection.ping(reconnect=True)
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(sql)
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
            self.connection.ping(reconnect=True)
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
            self.connection.ping(reconnect=True)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                data_list.append(row)
            return data_list

    def update_data(self, table, data, where):
        """
        update sql statement
        """
        sql = """update {} set """.format(table)
        sql += self.dict_to_str(data)
        if where:
            sql += ' where {};'.format(self.dict_to_str_and(where))
        with self.connection.cursor() as cursor:
            self.connection.ping(reconnect=True)
            cursor.execute(sql)
        self.connection.commit()

    def init_table(self, table_data):
        """
        init table data
        """
        for table, data_list in table_data.items():
            self.delete_data(table)
            for data in data_list:
                self.insert_data(table, data)
        self.close()
