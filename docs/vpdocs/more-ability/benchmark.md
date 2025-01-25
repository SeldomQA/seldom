# 基准测试

基准测试属于性能测试的一种，用于评估和衡量软件的性能指标。我们可以在软件开发的某个阶段通过基准测试建立一个已知的性能水平，称为"
基准线"。当系统的软硬件环境发生变化之后再进行一次基准测试以确定那些变化对性能的影响。__这是基准测试最常见的用途。

Donald Knuth在1974年出版的《Structured Programming with go to Statements》提到：

> 毫无疑问，对效率的片面追求会导致各种滥用。程序员会浪费大量的时间在非关键程序的速度上，实际上这些尝试提升效率的行为反倒可能产生很大的负面影响，特别是当调试和维护的时候。我们不应该过度纠结于细节的优化，应该说约97%的场景：过早的优化是万恶之源。当然我们也不应该放弃对那关键3%的优化。一个好的程序员不会因为这个比例小就裹足不前，他们会明智地观察和识别哪些是关键的代码；但是仅当关键代码已经被确认的前提下才会进行优化。对于很多程序员来说，判断哪部分是关键的性能瓶颈，是很容易犯经验上的错误的，因此一般应该借助测量工具来证明。

虽然经常被解读为不需要关心性能，但是的少部分情况下（3%）应该观察和识别关键代码并进行优化。

## 进行基准测试

在某些情况下，需要进行，seldom 提供了基准测试的功能。

__示例__

```python
import time
import seldom
from seldom.testdata import get_int
from seldom.utils.benchmark import benchmark_test


class MyTests(seldom.TestCase):

    @benchmark_test()
    def test_something_performance_1(self):
        """
        something code performance
        """
        num = get_int(1, 2000) / 1000
        time.sleep(num)

    @benchmark_test(rounds=10, iterations=2)
    def test_something_performance_2(self):
        """
        something code performance
        """
        num = get_int(1, 2000) / 1000
        time.sleep(num)

    @benchmark_test(rounds=10)
    def test_http_performance(self):
        """
        test http benchmark
        """
        self.get("https://httpbin.org/get")
        self.assertStatusOk()


if __name__ == "__main__":
    seldom.main(benchmark=True)
```

运行结果：

```shell
> python test_benchmark.py

...

=============================================== benchmark: 3 tests ===========================================
Name (time in s)             Min     Max    Mean  StdDev  Median     IQR  Outliers     OPS  Rounds  Iterations
--------------------------------------------------------------------------------------------------------------
test_http_performance  0.9126  3.0273  1.3924  0.5931  1.2281  0.5033 1;9         0.7182      10          1
test_something_performance_1  0.1354  1.8026  0.7440  0.6109  0.5856  0.7842 1;4         1.3441       5          1
test_something_performance_2  0.6498  1.8315  1.1404  0.4289  1.0993  0.7592 5;5         0.8769      10          2
--------------------------------------------------------------------------------------------------------------
Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
```

__说明__

* `@benchmark_test()`: 基准测试装饰器：
    * `rounds`: 运行基准测试的轮数，默认参数为`5`。
    * `iterations`: 每轮调用函数的次数，默认参数为 `1`。

* `main()`运行方法中，`branch`参数必须设置为`True`，且不支持生成HTML报告。

* 基准测试结果说明
    * `Min`: 最小执行时间，单位为秒s。
    * `Max`: 最大执行时间，单位为秒s。
    * `Minean`: 该测试运行过程中的平均执行时间，单位为秒s。
    * `StdDev`: 标准差，表示测试执行时间的离散程度或波动性。较大的标准差意味着测试结果波动较大。。
    * `Median`: 中位数，表示排序后所有执行时间的中间值。它用于衡量数据的集中趋势，避免极端值（如最大或最小值）影响结果。
    * `IQR`: 四分位距，表示第 75 百分位数和第 25 百分位数之间的差距。它反映了数据的分布范围。
    * `Outliers`: 异常值的数量，以及非异常值的数量。异常值的定义通常是距离均值超过 1 个标准差，或者距离第一四分位数和第三四分位数超过
      1.5 倍 IQR。
    * `OPS`: 每秒操作数，计算公式是 1 / Mean。它衡量每秒能够执行的操作次数，越高代表性能越好。
    * `Rounds`: 运行基准测试的轮数，默认参数为`5`。
    * `Iterations`: 每轮调用函数的次数，默认参数为 `1`。
