# 平台化支持

为了更好的支持测试用例平台化，Seldom 提供了API用于获取用例列表，以及根据传入的用例信息运行测试用例。

## 接入平台方式

seldom-platform项目: https://github.com/SeldomQA/seldom-platform

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
    * `warning=False`: 默认为`False`,
      在收集用例的过程中，因为缺少依赖库，或导包错误会导致部分用例收集报错，是否要将这些错误保存下来。开启（True）后，默认保存在`reports/collect_warning.log`
      文件中。

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
      "doc": "\n        test get request\n        ",
      "label": null
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
      "doc": "\n        test post request\n        ",
      "label": null
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
      "doc": "used parameterized test [with name=1, search_key='seldom']\n        :param name: case name\n        :param search_key: search keyword\n        ",
      "label": null
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
      "doc": "used parameterized test [with name=2, search_key='selenium']\n        :param name: case name\n        :param search_key: search keyword\n        ",
      "label": null
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
      "doc": "used parameterized test [with name=3, search_key='unittest']\n        :param name: case name\n        :param search_key: search keyword\n        ",
      "label": null
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
      "doc": "a simple test case ",
      "label": null
    }
  }
]
```

数据结构说明：

* file: 获取类的文件名，包含目录名。
* class: 测试类的名字`name` 和 描述`doc`。
* method: 测试方法的名字`name` 和 描述`doc`, `label`。

> 注明：seldom==3.11.0 版本测试方法增加`label`字段。

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
                "doc": "a simple test case ",
                "label": ""
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

## 接入平台必读

如果你只是使用seldom框架编写用例，那么代码只要框架能运行即可，如果要接入seldom-platform平台，那么需要注意一下几点。

#### 🚧 测试每个子目录必须包含`__init__.py`文件。

* 目录结构

```shell
├───reports
├───test_data
├───test_dir
│   ├───api_case
│   │   └───__init__.py
│   ├───app_case
│   │   └───__init__.py
│   ├───web_case
│   │   └───__init__.py
│   └───__init__.py
└───run.py
```

> 如果子目录不添加 __init__.py 文件会导致目录下面的用例无法解析。

#### 🚧 用例的前置动作

在用 seldom框架写用例的时候需要执行一些`前置/后置`动作。

```python
import seldom
from seldom.utils import cache

if __name__ == '__main__':
    # 前置动作
    cache.set({"token": "token123"})
    # 执行用例
    seldom.main("./test_dir")
    # 后置动作
    cache.clear("token")
```

但是，平台执行的时候，不会执行 `前置/后置`动作。 那么，为了使平台可以执行前置动作，需要使用`confrun.py`文件进行配置。

* 目录结构

```shell
├───reports
├───test_data
├───test_dir
│   ├───...
├───confrun.py
└───run.py
```

* confrun.py配置

```python
"""
seldom confrun.py  hooks function
"""
from seldom.utils import cache


def start_run():
    """前置动作"""
    cache.set({"token": "token123"})


def end_run():
    """后置动作"""
    cache.clear("token")
```

* run.py文件

```python
import seldom

if __name__ == '__main__':
    # 执行用例
    seldom.main("./test_dir")
```

通过上面的配置，`前置、后置`动作就可以在平台上运行，当然，这样设置本地也可正常运行。
