import time
from typing import Callable, List, Dict, Any


class Benchmark:
    """
    Benchmark Class
    """

    def __init__(self):
        self.results = {}

    @staticmethod
    def measure(func: Callable, rounds: int, iterations: int, *args: Any, **kwargs: Any) -> List[float]:
        """
        Measures the time of 'func' execution and supports rounds and iterations.
        Call 'iterations' func each time and count the total time.
        :param func:
        :param rounds:
        :param iterations:
        :param args:
        :param kwargs:
        :return:
        """

        durations = []
        for _ in range(rounds):
            start_time = time.time()
            for _ in range(iterations):  # exe `iterations` times
                func(*args, **kwargs)
            end_time = time.time()
            durations.append(float((end_time - start_time) / iterations))
        return durations

    def add_result(self, test_name: str, durations: List[float], iterations: int) -> None:
        """
        Save test results, including test name, durations, and number of iterations.
        :param test_name:
        :param durations:
        :param iterations:
        :return:
        """
        if test_name not in self.results:
            self.results[test_name] = {'durations': [], 'iterations': 0}
        self.results[test_name]['durations'].extend(durations)
        self.results[test_name]['iterations'] = iterations  # 存储迭代次数

    def get_stats(self, test_name: str) -> Dict[str, Any]:
        """
        Get statistics for a test, including minimum, maximum, mean, standard difference, and so on.
        :param test_name:
        :return:
        """
        durations = self.results[test_name]['durations']
        iterations = self.results[test_name]['iterations']
        min_time = min(durations)
        max_time = max(durations)
        mean_time = self.mean(durations)
        stddev_time = self.stddev(durations, mean_time)
        median_time = self.median(durations)
        iqr = self.iqr(durations)
        ops = 1 / mean_time if mean_time > 0 else 0
        return {
            "min": min_time,
            "max": max_time,
            "mean": mean_time,
            "stddev": stddev_time,
            "median": median_time,
            "iqr": iqr,
            "ops": ops,
            "rounds": len(durations),
            "iterations": iterations
        }

    def report(self) -> None:
        """
        Output the benchmark test report.
        """
        print(
            f"=============================================== benchmark: {len(self.results)} tests ===========================================")
        print(
            f"Name (time in s)             Min     Max    Mean  StdDev  Median     IQR  Outliers     OPS  Rounds  Iterations")
        print(
            f"--------------------------------------------------------------------------------------------------------------")

        for test_name, durations in self.results.items():
            stats = self.get_stats(test_name)
            outliers = self.get_outliers(durations['durations'], stats['mean'], stats['stddev'], stats['iqr'])
            print(
                f"{test_name:<20} {stats['min']:7.4f} {stats['max']:7.4f} {stats['mean']:7.4f} {stats['stddev']:7.4f} "
                f"{stats['median']:7.4f} {stats['iqr']:7.4f} {outliers:<10} {stats['ops']:7.4f} {stats['rounds']:7} {stats['iterations']:10}")
        print(
            f"--------------------------------------------------------------------------------------------------------------")
        print("Legend: ")
        print(
            "  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.")
        print("  OPS: Operations Per Second, computed as 1 / Mean")

    def get_outliers(self, durations: List[float], mean: float, stddev: float, iqr: float) -> str:
        """
        Identifies outliers in the benchmark results based on the mean, standard deviation, and IQR.
        :param durations:
        :param mean:
        :param stddev:
        :param iqr:
        :return:
        """
        outliers = []
        if not durations or not isinstance(durations, list):
            return "0;0"  # 没有数据或数据格式不正确

        # 确保每个 duration 都是 float 类型
        for duration in durations:
            try:
                duration = float(duration)
            except (ValueError, TypeError):
                continue  # 如果无法转换为浮动数值，则跳过

            if abs(duration - mean) > stddev or \
                    duration < self.percentile(durations, 25) - 1.5 * iqr or \
                    duration > self.percentile(durations, 75) + 1.5 * iqr:
                outliers.append(duration)
        return f"{len(outliers)};{len(durations) - len(outliers)}"

    def mean(self, data: List[float]) -> float:
        """Calculates the mean (average) of a list of numbers."""
        return sum(data) / len(data) if data else 0

    def stddev(self, data: List[float], mean: float) -> float:
        """Calculates the standard deviation of a list of numbers."""
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return variance ** 0.5 if data else 0

    def median(self, data: List[float]) -> float:
        """Calculates the median of a list of numbers."""
        data_sorted = sorted(data)
        n = len(data_sorted)
        if n % 2 == 0:
            return (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
        else:
            return data_sorted[n // 2]

    def percentile(self, data: List[float], p: float) -> float:
        """Calculates the p-th percentile of a list of numbers."""
        data_sorted = sorted(data)
        k = (len(data_sorted) - 1) * p / 100
        f = int(k)
        c = k - f
        if f + 1 < len(data_sorted):
            return data_sorted[f] + c * (data_sorted[f + 1] - data_sorted[f])
        else:
            return data_sorted[f]

    def iqr(self, data: List[float]) -> float:
        """Calculates the interquartile range (IQR) of a list of numbers."""
        return self.percentile(data, 75) - self.percentile(data, 25)


benchmark = Benchmark()


def benchmark_test(rounds: int = 5, iterations: int = 1):
    """
    benchmark test decorator
    :param rounds:
    :param iterations:
    :return:
    """

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            durations = benchmark.measure(func, rounds, iterations, self, *args, **kwargs)
            benchmark.add_result(func.__name__, durations, iterations)

        return wrapper

    return decorator
