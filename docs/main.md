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
              driver_path=None,
              grid_url=None,
              timeout=None
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
* driver_path : 设置浏览器驱动的`绝对`路径。要和 `browser` 设置保持一致。
* grid_url : 设置远程节点，[selenium Grid doc](https://www.selenium.dev/documentation/en/grid/)。
* timeout : 设置超时时间，默认10秒
