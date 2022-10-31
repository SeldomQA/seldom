# 平台化支持

为了更好的支持测试用例平台化，Seldom 提供了API用于获取用例列表，以及根据传入的用例信息运行测试用例。

目录结构如下：

```shell
mypro/
├── test_dir/
│   ├── module_api/
│   │   ├── test_http_demo.py
│   ├── module_web/
│   │   ├── test_first_demo.py
│   │   ├── test_ddt_demo.py
└── run.py
```


### 获取用例信息

```py
# run.py
from seldom import SeldomTestLoader
from seldom import TestMainExtend

if __name__ == '__main__':
    SeldomTestLoader.collectCaseInfo = True
    main_extend = TestMainExtend(path="./test_dir/")
    case_info = main_extend.collect_cases(json=True)
    print(case_info)
```

__说明__

返回的用例信息列表：

* `collectCaseInfo` ：`collectCaseInfo`设置为`True` 说明需要收集用例信息。
* `TestMainExtend(path="./test_dir/")` ： `TestMainExtend`类是`TestMain`类的扩展，`path`设置收集用例的目录，不能为空。
* `collect_cases(json=False, level="data", warning=False)`：返回收集的用例信息。
    * `json=False`：默认为`list`格式；设置为`True`返回`json`格式。
    * `level="data"` ：默认为`data`，数据驱动的每条数据被解析为一条用例。如果设置为 `method` 数据驱动的方法被解析为一条用例。
    * `warning=False`: 默认为`False`, 在收集用例的过程中，因为缺少依赖库，或导包错误会导致部分用例收集报错，是否要将这些错误保存下来。开启（True）后，默认保存在`reports/collect_warning.log` 文件中。

```json
[
    {
        "file": "module_api.test_http_demo",
        "class": {
            "name": "TestRequest",
            "doc": "\n    http api test demo\n    doc: https://requests.readthedocs.io/en/master/\n    "
        },
        "method": {
            "name": "test_get_method",
            "doc": "\n        test get request\n        "
        }
    },
    {
        "file": "module_api.test_http_demo",
        "class": {
            "name": "TestRequest",
            "doc": "\n    http api test demo\n    doc: https://requests.readthedocs.io/en/master/\n    "
        },
        "method": {
            "name": "test_post_method",
            "doc": "\n        test post request\n        "
        }
    },
    {
        "file": "module_web.test_ddt_demo",
        "class": {
            "name": "BaiduTest",
            "doc": "Baidu search test case"
        },
        "method": {
            "name": "test_baidu_0",
            "doc": "used parameterized test [with name=1, search_key='seldom']\n        :param name: case name\n        :param search_key: search keyword\n        "
        }
    },
    {
        "file": "module_web.test_ddt_demo",
        "class": {
            "name": "BaiduTest",
            "doc": "Baidu search test case"
        },
        "method": {
            "name": "test_baidu_1",
            "doc": "used parameterized test [with name=2, search_key='selenium']\n        :param name: case name\n        :param search_key: search keyword\n        "
        }
    },
    {
        "file": "module_web.test_ddt_demo",
        "class": {
            "name": "BaiduTest",
            "doc": "Baidu search test case"
        },
        "method": {
            "name": "test_baidu_2",
            "doc": "used parameterized test [with name=3, search_key='unittest']\n        :param name: case name\n        :param search_key: search keyword\n        "
        }
    },
    {
        "file": "module_web.test_first_demo",
        "class": {
            "name": "BaiduTest",
            "doc": "Baidu search test case"
        },
        "method": {
            "name": "test_case",
            "doc": "a simple test case "
        }
    }
]
```

数据结构说明：

* file: 获取类的文件名，包含目录名。
* class: 测试类的名字`name` 和 描述`doc`。
* method: 测试方法的名字`name` 和 描述`doc`。


### 执行用例信息

当获取用例信息之后，可以进行自定义，例如 挑选出需要执行的用例，重新传给Seldom 执行。

```python
# run.py
from seldom import TestMainExtend

if __name__ == '__main__':
    # 自定义要执行的用例
    cases = [
        {
            "file": "module_web.test_first_demo",
            "class": {
                "name": "BaiduTest",
                "doc": "Baidu search test case"
            },
            "method": {
                "name": "test_case",
                "doc": "a simple test case "
            }
        }
    ]
    main_extend = TestMainExtend(path="./test_dir")
    main_extend.run_cases(cases)
```

说明：

* `cases` 定义要执行的用例信息， `doc` 非必填字段。
* `TestMainExtend(path="./test_dir")` : 其中`path`指定从哪个目录查找用例集合。
* `run_cases(cases)`: 运行用例。


### 相关项目

seldom-platform: https://github.com/SeldomQA/seldom-platform
