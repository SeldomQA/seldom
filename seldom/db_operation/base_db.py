
class SQLBase:

    @staticmethod
    def dict_to_str(data: dict) -> str:
        """
        dict to set str
        """
        tmp_list = []
        for key, value in data.items():
            tmp = "{k}='{v}'".format(k=key, v=value)
            tmp_list.append(tmp)
        return ','.join(tmp_list)

    @staticmethod
    def dict_to_str_and(conditions: dict) -> str:
        """
        dict to where and str
        """
        tmp_list = []
        for key, value in conditions.items():
            tmp = "{k}='{v}'".format(k=key, v=value)
            tmp_list.append(tmp)
        return ' and '.join(tmp_list)

    def delete(self, table, where=None):
        """
        delete table data
        """
        return self.delete_data(table, where)

    def insert(self, table, data):
        """
        insert sql statement
        """
        return self.insert_data(self, table, data)

    def select(self, table, where=None):
        """
        select sql statement
        """
        return self.select_data(table, where)

    def update(self, table, data, where):
        """
        update sql statement
        """
        return self.update_data(self, table, data, where)
