"""
SQL API
"""


class SQLBase:
    """SQL base API"""

    @staticmethod
    def dict_to_str(data: dict) -> str:
        """
        dict to set str
        """
        tmp_list = []
        for key, value in data.items():
            if value is None:
                tmp = f"{key}=null"
            elif isinstance(value, int):
                tmp = f"{key}={value}"
            else:
                tmp = f"{key}='{value}'"
            tmp_list.append(tmp)
        return ','.join(tmp_list)

    @staticmethod
    def dict_to_str_and(conditions: dict) -> str:
        """
        dict to where and str
        """
        tmp_list = []
        for key, value in conditions.items():
            if value is None:
                tmp = f"{key}=null"
            elif isinstance(value, int):
                tmp = f"{key}={value}"
            else:
                tmp = f"{key}='{value}'"
            tmp_list.append(tmp)
        return ' and '.join(tmp_list)

    def delete(self, table: str, where: dict = None) -> None:
        """
        delete table data
        """
        return self.delete_data(table, where)

    def insert(self, table: str, data: dict) -> None:
        """
        insert sql statement
        """
        return self.insert_data(table, data)

    def select(self, table: str, where: dict = None, one: bool = False) -> list:
        """
        select sql statement
        """
        return self.select_data(table, where, one)

    def update(self, table: str, data: dict, where: dict) -> None:
        """
        update sql statement
        """
        return self.update_data(table, data, where)
