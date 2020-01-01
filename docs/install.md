## seldom 安装

seldom的安装非常简单。

### 快速安装

目前已经上传 pypi.org ,可以使用pip命令安装。

```shell
> pip install seldom
```

### 体验最新代码

如果你想随时体验最新的代码，可以使用下面的命令。

```shell
> pip install -U git+https://github.com/defnngj/seldom.git@master
```

### 安装依赖

随着seldom 加入更多的功能，seldom不得不依赖其他的开源库。你可以在 requirements.txt 文件里面看到这些依赖。

```shell
colorama==0.4.3
selenium==3.141.0
parameterized==0.7.0
poium==0.5.2
```

先通过 `pip` 命令安装这些依赖库，可以加快seldom的这安装。

```shell
> pip install -r requirements.txt
```

### 检查安装

最后，我们可以通过`pip show seldom`命令检查安装。

```shell
> pip show seldom

Name: seldom
Version: 1.0.0b0
Summary: WebUI automation testing framework based on Selenium and unittest.
Home-page: https://github.com/seldomQA/seldom/
Author: bugmaster
Author-email: fnngj@126.com
License: BSD
Location: c:\python37\lib\site-packages\seldom-1.0.0b0-py3.7.egg
Requires: selenium, parameterized, colorama
Required-by:
```
