
def assertJSON(src_data, dst_data):
    if isinstance(src_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key {}".format(key))
        for key in src_data:
            if key in dst_data:
                """递归"""
                assertJSON(src_data[key], dst_data[key])
            else:
                print("dst不存在这个: {}".format(key))
    elif isinstance(src_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data):
            print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            """递归"""
            assertJSON(src_list, dst_list)
    else:
        if str(src_data) != str(dst_data):
            print("value: {}".format(src_data))


if __name__ == '__main__':
    dict1 = {"id": "100", "name": ["苹果", "小米"], "info": {"uid": "2021", "phoneName": ["一代", "苹果12"]}}
    dict2 = {"name": ["苹果", "华为"], "info": {"uid": "2020", "phoneName": ["一代", "苹果12"]}}
    assertJSON(dict1, dict2)

