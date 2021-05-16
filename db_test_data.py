import time
from seldom.db_operation import SQLiteDB, MySQLDB


# 定义过去时间
past_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 100000))
past_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 100000 + 7200))

# 发布会开始&结束时间
start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 432000))
end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 432000 + 7200))

# 创建更新
now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


datas = {
    'api_event': [
        {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': start_time,
         "end_time": end_time, "create_time": now_time, "update_time": now_time},
        {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京会展中心', 'start_time': start_time,
         "end_time": end_time, "create_time": now_time, "update_time": now_time},
        {'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0, 'address': '北京会展中心', 'start_time': start_time,
         "end_time": end_time, "create_time": now_time, "update_time": now_time},
        {'id': 4, 'name': '发布会已结束', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': past_start_time,
         "end_time": past_end_time, "create_time": now_time, "update_time": now_time},
        {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心', 'start_time': start_time,
         "end_time": end_time, "create_time": now_time, "update_time": now_time},
    ],
    'api_guest': [
        {'id': 1, 'real_name': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1,
         "create_time": now_time, },
        {'id': 2, 'real_name': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com', 'sign': 1, 'event_id': 1,
         "create_time": now_time, },
        {'id': 3, 'real_name': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com', 'sign': 0, 'event_id': 5,
         "create_time": now_time, },
    ]
}

if __name__ == '__main__':
    # test sqlite3
    db = SQLiteDB(r"D:\learnAPI\db.sqlite3")
    db.init_table(datas)
    # test mysql
    db = MySQLDB(host="127.0.0.1", port="3306", user="root", password="123", database="db_name")
    db.init_table(datas)
