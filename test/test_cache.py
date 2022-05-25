"""
author: bugmaster
data: 2022/5/22
desc: 缓存用法
"""
from seldom.utils import cache

# 清除指定缓存
cache.clear("token")

# 清除所有缓存
cache.clear()

# 获取指定缓存
token = cache.get("token")
print(f"token: {token}")
if token is None:
    # 写入缓存
    cache.set({"token": "123"})

# 获取指定缓存
token = cache.get("token")
print(f"token: {token}")

# 获取所有缓存
all_token = cache.get()
print(f"all: {all_token}")


