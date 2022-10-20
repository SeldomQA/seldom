"""
author: bugmaster
data: 2022/9/17
desc: 生成随机数用法
"""
from seldom.testdata import *


# 随机一个名字
print("名字：", first_name())
print("名字(男)：", first_name(gender="male"))
print("名字(女)：", first_name(gender="female"))
print("名字(中文男)：", first_name(gender="male", language="zh"))
print("名字(中文女)：", first_name(gender="female", language="zh"))

# 随机一个姓
print("姓:", last_name())
print("姓(中文):", last_name(language="zh"))

# 随机一个姓名
print("姓名:", username())
print("姓名(中文):", username(language="zh"))

# 随机一个生日
print("生日:", get_birthday())
print("生日字符串:", get_birthday(as_str=True))
print("生日年龄范围:", get_birthday(start_age=20, stop_age=30))

# 日期
print("日期(当前):", get_date())
print("日期(昨天):", get_date(-1))
print("日期(明天):", get_date(1))

print("当月：", get_month())
print("上个月：", get_month(-1))
print("下个月：", get_month(1))

print("今年：", get_year())
print("去年：", get_year(-1))
print("明年：", get_year(1))

# 数字
print("数字(8位):", get_digits(8))

# 邮箱
print("邮箱:", get_email())

# 浮点数
print("浮点数:", get_float())
print("浮点数范围:", get_float(min_size=1.0, max_size=2.0))

# 随机时间
print("当前时间:", get_now_datetime())
print("当前时间(格式化字符串):", get_now_datetime(strftime=True))
print("未来时间:", get_future_datetime())
print("未来时间(格式化字符串):", get_future_datetime(strftime=True))
print("过去时间:", get_past_datetime())
print("过去时间(格式化字符串):", get_past_datetime(strftime=True))

# 随机数据
print("整型:", get_int())
print("整型32位:", get_int32())
print("整型64位:", get_int64())
print("MD5:", get_md5())
print("UUID:", get_uuid())

print("单词:", get_word())
print("单词组(3个):", get_words(3))

print("手机号:", get_phone())
print("手机号(移动):", get_phone(operator="mobile"))
print("手机号(联通):", get_phone(operator="unicom"))
print("手机号(电信):", get_phone(operator="telecom"))
