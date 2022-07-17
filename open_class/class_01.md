## SeldomQA 公开课

* seldom 相关项目介绍
* seldom 设计原理
* seldom 项目展望
* 如何参与seldom项目


## seldom 的定位

seldom vs selenium （webdriver） requests

手机 vs CPU

seldom vs pytest (手机架构)

seldom vs httpRunner 2.0/ 3.0


设计理念不一样！

```python
def totken():
   return """""
```

```json
{
    url: "/api/user",
    method: POST,
    sing: "${totken}"
}
```

requests/ falsk / yagmail 

seldom vs robot framework


robot framework ~= 单元框架
SeleniumLibrary     selenium
apppiumLibrary      appium
RequestsLibrary...  requests

关键驱动

## seldom QA

* seldom
* XTestRunner + unittest 写
* poium 用来page objects  + selenium + pytest



## seldom 设计原理

seldom unittest 不完全支持 pytest xdist

1. unittest简单够用，python默认的。
2. 很容易基于unittest做二次开发
3. 参数化


```json 
# data.json
[
    ["admin", "admin123", "222"],
    ["admin1", "admin1231", "22"]
]
```

```py
import pytest

@pytest.mark.parametrize(
    "username, password, age",  # --> 
    data("data.json")
)
def test_login(username, password, age):
    print("账号:{},密码:{}".format(username,password]))
```

## seldom 缺点 

1. 多线程
2. 单个用例的执行

web UI selenium

playwright

httpx

unittest

pytest 


Dubbo 


## 如何参与seldom项目

1. 纯使用者 --> 参与者
2. 面试 - 可以吹牛~！
3. 分担我的工作


## 背景

随着seldom的用户增多，官方QQ群或Github的 issues 时长能收到一些需求，有些人认为“不支持啊~！拜拜吧”，每个框架都是在不断的使用过程中发展的，我个人精力有限，很希望能把它推向社区，而且牛人群里的有些人是有能力贡献代码的，于是，就组织了这次线上的公开课，对seldomQA框架做了比较全面的介绍。包括优点和不足。

## 参与开源项目

参与开源项目，还是好处多多的。

* 更快的修复问题，实现功能：比如发现项目不支持的功能，可以自己动手实现。
* 阅读优秀的代码：seldom 谈不上多么高大上，经过我几年的维护，有一些设计上的思考值得阅读，为你自己设计测试框架提供思路。
* 可以吹牛：参与开源项目，本来就是一件可以吹牛的事情。


## 其他

1. 关于视频中介绍的无法执行单个用例，已经在 `version 2.8.0 ` 版本实现。

2. @nickliya 用vuepress 实现了新的官网文档，阅读体验暴增：https://seldomqa.github.io/

3. 当然是期待你的参与，官方QQ群：948994709 （没有吹水，没有斗图，纯技术交流学习）！

