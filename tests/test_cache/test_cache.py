"""
author: bugmaster
data: 2022/5/22
desc: 缓存用法
"""
from seldom.utils import cache

# 清除指定缓存
cache.clear()

# 获取指定缓存
token = cache.get("token")
print(f"token: {token}")

# 判断为空写入缓存
if token is None:
    cache.set({"token": "123"})

# 设置存在的数据(相当于更新)
cache.set({"token": "456"})

# value复杂格式设置存在的数据
cache.set({"user": [{"name": "tom", "age": 11}]})


# 获取所有缓存
all_token = cache.get()
print(f"all: {all_token}")

# 清除指定缓存
cache.clear("token")


