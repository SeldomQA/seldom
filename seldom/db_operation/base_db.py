
class SQLBase:

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
