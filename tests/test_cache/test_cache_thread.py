"""
author: bugmaster
data: 2024/8/27
desc: 多线程缓存用法
"""
from seldom.utils import cache
from seldom.extend_lib import threads

if __name__ == "__main__":

    @threads(3)
    def operating_token(tk: str):
        """
        根据传入的token操作
        """
        cache.clear("token")

        # 获取指定缓存
        token = cache.get("token")
        # 判断为空写入缓存
        if token is None:
            cache.set({"token": tk})


    # 将两条用例拆分，分别用不同的浏览器执行
    token = ["t123", "t456", "t789"]

    for t in token:
        operating_token(t)
