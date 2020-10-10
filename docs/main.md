## main() 方法

`main()`方法是seldom运行测试的入口, 很多重要的配置都是通过这个方法完成。

```python
import seldom

# ...

if __name__ == '__main__':

    seldom.main(path="./",
              browser="chrome",
              report=None,
              title="百度测试用例",
              description="测试环境：chrome",
              debug=False,
              rerun=0,
              save_last_run=False,
              timeout=None,
              xmlrunner=False
    )
```

#### 说明：

* path ： 指定测试目录或文件。
* browser : 指定测试浏览器，默认`Chrome`。
* report : 自定义测试报告的名称，默认格式为`2020_04_04_11_55_20_result.html`
* title ： 指定测试报告标题。
* description ： 指定测试报告描述。
* debug ： debug模式，设置为True不生成测试HTML测试，默认为`False`。
* rerun : 设置失败重新运行次数，默认为 `0`。
* save_last_run : 设置只保存最后一次的结果，默认为`False`。
* timeout : 设置超时时间，默认10秒
* xmlrunner: 设置为 True ，生成XML格式的报告。不支持同时生成HTML和 XML 两种格式的报告。