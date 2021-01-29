## seldom 运行

seldom的给运行新手造成了困扰，强烈不建议你在`pycharm`里面运行。因为许多新手根本搞不明白 pycharm 的运行配置，引起的运行错误也不知道怎么解决。

> Window建议使用cmder, mac/linux使用自带终端。

### 运行说明

参考目录结构如下：

```shell
mypro/
├── test_dir/
│   ├── test_sample.py
├── reports/
└── run.py
```

seldom要运行的测试是由`main()`方法决定的，创建 `run.py` 文件

```py
import seldom

seldom.main(path="./")
```

在cmder/终端下面运行 `run.py` 文件

```shell
> python run.py
```

或者：

```shell
> seldom -r run.py
```

__要运行的用例由 `path` 参数控制__

* `"./"` :  表示`run.py`文件所在目录下的所有以`test`开头的测试文件。

* `"./test_dir/"` : 指定`test_dir/`目录下所有以`test`开头的测试文件。

* `"./test_dir/test_sample.py"` : 指定`test_dir/`目录下的`test_samplepy`测试文件.

* `"test_sample.py"` : 指定当前目录下的`test_sample.py`测试文件。

### 运行单个测试类、方法

在调试阶段，需要运行单个测试类或方法。

```shell script
> cd test_dir/
> seldom -m test_sample.SampleTest.test_case
Runtime environment:
---------------------
Note: This mode is suitable for debugging single test classes and methods.
Python 3.7.9
seldom 1.10.0
Browser: Chrome(default)
---------------------
2021-01-29 18:59:53 [INFO] 👀 assertIn url: http://www.itest.info/.
.
----------------------------------------------------------------------
Ran 1 test in 18.497s

OK
``` 

* 运行粒度

```shell script
> seldom -m test_sample # 运行 test_sample.py 文件
> seldom -m test_sample.SampleTest # 运行 SampleTest 测试类
> seldom -m test_sample.SampleTest.test_case # 运行 test_case 测试方法
```

备注：如果测试方法 使用了`@data`、`@file_data` 装饰器，则不支持指定测试方法执行。
