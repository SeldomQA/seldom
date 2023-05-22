"""
MS SQL Server DB API
"""
from typing import Any
try:
    import pymssql
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("Please install the library. https://github.com/pymssql/pymssql")
from seldom.db_operation.base_db import SQLBase


class MSSQLDB(SQLBase):
    """SQL Server DB table API"""

    def __init__(self, server: str, user: str, password: str, database: str, charset="utf8mb4"):
        """
        Connect to the SQL Server database
        :param server:
        :param user:
        :param password:
        :param database:
        """
        self.connection = pymssql.connect(server=server,
                                          user=user,
                                          password=password,
                                          database=database,
                                          charset=charset)

        # self.cursor = self.connection.cursor(as_dict=True)

    def close(self) -> None:
        """
        Close the database connection
        """
        self.connection.close()

    def execute_sql(self, sql: str) -> None:
        """
        Execute SQL
        """
        print("running sql ", sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        self.connection.commit()

    def query_sql(self, sql: str) -> list:
        """
        Query SQL
        return: query data
        """
        data_list = []
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                data_list.append(row)
            self.connection.commit()
            return data_list

    def query_one(self, sql: str) -> Any:
        """
        Query one data SQL
        :return:
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
            self.connection.commit()
            return row

    def insert_get_last_id(self, sql: str) -> int:
        """
        insert sql and get last row id
        :param sql:
        :return:
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            last_id = cursor.lastrowid
            self.connection.commit()
            return last_id

    def insert_data(self, table: str, data: dict) -> None:
        """
        insert sql statement
        """
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        sql = f"""insert into {table} ({key}) values ({value})"""
        self.execute_sql(sql)

    def select_data(self, table: str, where: dict = None, one: bool = False) -> Any:
        """
        select sql statement
        """
        sql = f"""select * from {table} """
        if where is not None:
            sql += f""" where {self.dict_to_str_and(where)}"""
        if one is True:
            return self.query_one(sql)

        return self.query_sql(sql)

    def update_data(self, table: str, data: dict, where: dict) -> None:
        """
        update sql statement
        """
        sql = f"""update {table} set """
        sql += self.dict_to_str(data)
        if where:
            sql += f""" where {self.dict_to_str_and(where)};"""
        self.execute_sql(sql)

    def delete_data(self, table: str, where: dict = None) -> None:
        """
        delete table data
        """
        sql = f"""delete from {table}"""
        if where is not None:
            sql += f""" where {self.dict_to_str_and(where)};"""
        self.execute_sql(sql)

    def init_table(self, table_data: dict, clear: bool = True) -> None:
        """
        init table data
        """
        for table, data_list in table_data.items():
            if clear:
                self.delete_data(table)
            for data in data_list:
                self.insert_data(table, data)
