"""
soloX:
https://github.com/smart-test-ti/SoloX
tidevice:
https://github.com/alibaba/taobao-iphone-device
"""
import os
import cv2
import time
import gevent
import base64
import tidevice
import inspect
import threading
import statistics
import matplotlib
import numpy as np
from . import cache
from seldom.logging import log
from seldom.running.config import Seldom, AppConfig
from ..u2driver import u2
from ..wdadriver import wda_, make_screenrecord
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from dateutil import parser
from tidevice._perf import DataType
from functools import wraps
from datetime import datetime
from solox.public.apm import Memory, CPU, FPS


class MySoloX:
    """iOS and Android perf driver, but iOS used not so good"""

    def __init__(self, pkgName, deviceId=None, platform=None):
        if deviceId is None:
            deviceId = Seldom.app_info.get('deviceName')
        if platform is None:
            platform = Seldom.app_info.get('platformName')
        if platform == Seldom.app_info.get('platformName'):
            wait_times = 0
            while wait_times <= 20:
                if u2.wait_app_u2() != 0:
                    break
                wait_times += 1
                log.info(f'Unable to obtain pid,retry...{wait_times}')
                time.sleep(0.5)
        self.mem = Memory(pkgName=pkgName, deviceId=deviceId, platform=platform)
        self.cpu = CPU(pkgName=pkgName, deviceId=deviceId, platform=platform)
        self.fps = FPS(pkgName=pkgName, deviceId=deviceId, platform=platform)

    def get_mem(self):
        """get mem info"""
        mem_list = []
        time_list = []
        try:
            while Common.threadLock:
                mem_res = self.mem.getProcessMem(noLog=True)
                now_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                log.trace(f'{now_time} : MEM{mem_res}')
                mem_list.append(tuple(mem_res))
                time_list.append(now_time)
        except Exception as e:
            cache.set({'PERF_ERROR': f"Error in get_mem: {e}"})

        return time_list, mem_list

    def get_cpu(self):
        """get cpu info"""
        cpu_list = []
        time_list = []
        try:
            while Common.threadLock:
                cpu_res = self.cpu.getCpuRate(noLog=True)
                now_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                log.trace(f'{now_time} : CPU{cpu_res}')
                cpu_list.append(tuple(cpu_res))
                time_list.append(now_time)
        except Exception as e:
            cache.set({'PERF_ERROR': f"Error in get_cpu: {e}"})

        return time_list, cpu_list

    def get_fps(self):
        """get fps info"""
        fps_list = []
        time_list = []
        try:
            while Common.threadLock:
                fps_res = self.fps.getFPS(noLog=True)
                now_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                log.trace(f'{now_time} : FPS{fps_res}')
                fps_list.append(tuple(fps_res))
                time_list.append(now_time)
        except Exception as e:
            cache.set({'PERF_ERROR': f"Error in get_fps: {e}"})

        return time_list, fps_list


class TidevicePerf:
    """Only iOS perf driver"""

    def __init__(self):
        self.t = tidevice.Device()
        self.perf = tidevice.Performance(self.t, [DataType.CPU, DataType.MEMORY, DataType.FPS])
        self.mem_list = []
        self.mem_time_list = []
        self.cpu_list = []
        self.cpu_time_list = []
        self.fps_list = []
        self.fps_time_list = []

    def callback(self, _type, value: dict):
        if _type.value == 'cpu':
            log.trace(f'cpu:{value}')
            self.cpu_time_list.append(
                str(((datetime.fromtimestamp(value['timestamp'] / 1000)).strftime('%H:%M:%S.%f'))[:-3]))
            self.cpu_list.append((round(value['value'], 2), round(value['sys_value'], 2)))
        elif _type.value == 'memory':
            log.trace(f'mem:{value}')
            self.mem_time_list.append(
                str(((datetime.fromtimestamp(value['timestamp'] / 1000)).strftime('%H:%M:%S.%f'))[:-3]))
            self.mem_list.append((round(value['value'], 2), 0, 0))
        elif _type.value == 'fps':
            log.trace(f'fps:{value}')
            self.fps_time_list.append(
                str(((datetime.fromtimestamp(value['timestamp'] / 1000)).strftime('%H:%M:%S.%f'))[:-3]))
            self.fps_list.append((value['value'], 0))

    def start(self, pkgName=None):
        if pkgName is None:
            pkgName = Seldom.app_info.get('platformName')
        self.mem_list = []
        self.mem_time_list = []
        self.cpu_list = []
        self.cpu_time_list = []
        self.fps_list = []
        self.fps_time_list = []
        self.perf.start(bundle_id=pkgName, callback=self.callback)

    def stop(self):
        self.perf.stop()
        cache.set({'CPU_INFO': (self.cpu_time_list, self.cpu_list)})
        cache.set({'MEM_INFO': (self.mem_time_list, self.mem_list)})
        cache.set({'FPS_INFO': (self.fps_time_list, self.fps_list)})


class RunType:
    NOTHING = 0
    DEBUG = 1
    DURATION = 2
    STRESS = 3


class Common:
    iOS_perf_obj = None
    threadLock = False
    log = False
    record = False
    CASE_ERROR = []
    PERF_ERROR = []
    LOGS_ERROR = []
    RECORD_ERROR = []

    @staticmethod
    def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            base64_data = base64.b64encode(image_bytes)
            base64_string = base64_data.decode("utf-8")
            return base64_string

    @staticmethod
    def extract_frames(video_file, output_dir, start_duration=AppConfig.FRAME_SECONDS,
                       end_duration=AppConfig.FRAME_SECONDS):
        """Screen recording framing"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 打开视频文件
        cap = cv2.VideoCapture(video_file)
        fps = cap.get(cv2.CAP_PROP_FPS)
        log.info("视频帧率为 {:.2f} 帧/秒".format(fps))

        # 计算帧数和总时长（以秒为单位）
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        total_duration = total_frames / fps

        # 计算前5s片段的开始帧数和结束帧数
        start_frame = 0
        end_frame = int(fps * start_duration)

        # 如果末尾5s片段时长大于总时长，则设置为总时长
        if end_duration > total_duration:
            end_duration = total_duration

        # 计算末尾5s片段的开始帧数和结束帧数
        end_start_frame = total_frames - int(fps * end_duration)
        end_end_frame = total_frames

        # 初始化计数器和当前帧数
        frame_count = 0
        current_frame = 0

        # 循环读取视频帧
        while True:
            # 读取一帧
            ret, frame = cap.read()

            # 如果未读取到帧，则结束循环
            if not ret:
                break

            # 如果当前帧数在前5s或末尾5s范围内，则进行保存
            if start_frame <= current_frame < end_frame or end_start_frame <= current_frame < end_end_frame:
                # 生成输出文件名
                output_file = os.path.join(output_dir, f"frame_{frame_count:06d}.jpg")

                # 保存帧为图像文件
                cv2.imwrite(output_file, frame)

            # 更新计数器
            frame_count += 1

            # 更新当前帧数
            current_frame += 1

        # 释放视频对象
        cap.release()

    @staticmethod
    def calculate_hash(image, hash_size=128):
        """Calculate the hash value of the input image"""
        # 将图像调整为指定大小，并转换为灰度图像
        image = cv2.resize(image, (hash_size, hash_size))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 计算均值
        mean = np.mean(gray)

        # 生成哈希值
        hash = []
        for i in range(hash_size):
            for j in range(hash_size):
                if gray[i, j] > mean:
                    hash.append(1)
                else:
                    hash.append(0)

        return hash

    @staticmethod
    def find_best_frame(reference_image_path, image_folder_path, is_start=True):
        """Find the image with the highest similarity to the reference image in the given image folder"""
        # 加载参考图像，并计算其哈希值
        reference_image = cv2.imread(reference_image_path)
        reference_hash = Common.calculate_hash(reference_image)

        # 遍历图像文件夹中的所有图像，并计算它们的哈希值
        frame_path_list = os.listdir(image_folder_path)
        best_match = None
        best_distance = float('inf')
        if len(frame_path_list) <= int(AppConfig.FRAME_SECONDS * AppConfig.FPS) * 2:
            start_frame_num = len(frame_path_list) / 2
        else:
            start_frame_num = AppConfig.FRAME_SECONDS * AppConfig.FPS
        for i, filename in enumerate(frame_path_list):
            if is_start and i < start_frame_num:
                if filename.endswith('.jpg'):
                    path = os.path.join(image_folder_path, filename)
                    image = cv2.imread(path)
                    hash = Common.calculate_hash(image)

                    # 计算当前图像和参考图像的哈希距离
                    distance = sum([a != b for a, b in zip(hash, reference_hash)])
                    # 更新最相似的图像
                    if distance <= best_distance:
                        best_match = path
                        best_distance = distance

            elif not is_start and i >= start_frame_num:
                if filename.endswith('.jpg'):
                    path = os.path.join(image_folder_path, filename)
                    image = cv2.imread(path)
                    hash = Common.calculate_hash(image)

                    # 计算当前图像和参考图像的哈希距离
                    distance = sum([a != b for a, b in zip(hash, reference_hash)])
                    # 更新最相似的图像
                    if distance < best_distance:
                        best_match = path
                        best_distance = distance

        # 输出最相似的图像路径
        return best_match

    @staticmethod
    def draw_chart(data_list, x_labels, line_labels, jpg_name='my_plt.jpg', label_title='Performance Chart',
                   x_name='Time', y_name='Value'):
        """Draw a chart of performance data"""
        matplotlib.use('TkAgg')  # 使用 Tkinter 后端
        # 将元组列表中的数据按列提取到列表中
        data_cols = list(zip(*data_list))
        # 将时间字符串转换为 datetime 对象
        x_labels = [parser.parse(x) for x in x_labels]
        # 动态调整X轴的日期间隔和显示格式
        x_len = len(x_labels)
        x_locator = mdates.AutoDateLocator(minticks=x_len, maxticks=x_len)
        x_formatter = mdates.DateFormatter('%H:%M:%S')
        # 设置绘图窗口大小
        width = max(x_len, 25)
        plt.figure(figsize=(width, 10))
        # 设置 x 轴的日期定位器和格式化器
        plt.gca().xaxis.set_major_locator(x_locator)
        plt.gca().xaxis.set_major_formatter(x_formatter)
        # 针对每列数据绘制一条折线
        for i, data in enumerate(data_cols):
            plt.plot(x_labels, data, label=line_labels[i])
            for x, y in zip(x_labels, data):
                label = f'{y:.1f}'
                plt.annotate(label, xy=(x, y), xytext=(0, 5), textcoords='offset points')
        plt.xticks(rotation=45, ha='right')
        # 添加标题、标签和图例
        plt.title(label_title)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.legend()
        # 保存为jpg格式图片
        plt.savefig(jpg_name, format='jpg')
        plt.close()  # 关闭图形窗口
        return Common.image_to_base64(jpg_name)


def start_recording():
    """Start screen recording identification"""
    Common.record = True
    time.sleep(2)


def run_testcase(func, *args, **kwargs):
    """Execute decorated test case"""
    try:
        func(*args, **kwargs)
    except Exception as e:
        Common.CASE_ERROR.append(f"{e}")
        log.error(f'Error in run_testcase: {e}')
        raise e
    if Common.record and (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'Android'):
        time.sleep(1)
        u2.stop_recording_u2()
    elif Common.record and (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'iOS'):
        Common.record = False
        if Common.iOS_perf_obj is not None:
            Common.iOS_perf_obj.stop()
    Common.threadLock = False
    AppConfig.log = False


def get_log(log_path, run_path):
    """Get logs for Android devices"""
    try:
        AppConfig.log = True
        while not os.path.exists(run_path):
            time.sleep(1)
        if (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'Android'):
            u2.write_log_u2(log_path)
    except Exception as e:
        Common.LOGS_ERROR.append(f"{e}")
        log.error(f'Error in get_log: {e}')


def get_perf():
    """Obtain mobile device performance data"""
    try:
        if (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'Android'):
            perf = MySoloX(pkgName=Seldom.app_info.get('appPackage'), platform=Seldom.app_info.get('platformName'))
            new_cpu = gevent.spawn(perf.get_cpu)
            new_mem = gevent.spawn(perf.get_mem)
            new_fps = gevent.spawn(perf.get_fps)
            gevent.joinall([new_cpu, new_mem, new_fps])
            cache.set({'CPU_INFO': new_cpu.value})
            cache.set({'MEM_INFO': new_mem.value})
            cache.set({'FPS_INFO': new_fps.value})
        elif (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'iOS'):
            Common.iOS_perf_obj = TidevicePerf()
            Common.iOS_perf_obj.start()
    except Exception as e:
        Common.PERF_ERROR.append(f"{e}")
        log.error(f"Error in get_perf: {e}")


def start_record(video_path, run_path):
    while not os.path.exists(run_path):
        time.sleep(1)
    while Common.threadLock and Seldom.driver:
        if Common.record:
            try:
                if (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'iOS'):
                    # while not WDAObj.c:
                    #     time.sleep(1)
                    with make_screenrecord(output_video_path=video_path):
                        while Common.record:
                            time.sleep(1)
                elif (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'Android'):
                    u2.start_recording_u2(video_path)
            except Exception as e:
                Common.RECORD_ERROR.append(f"{e}")
                log.error(f"Error in start_record: {e}")
            break
        time.sleep(1.5)


def AppPerf(MODE, duration_times=AppConfig.DURATION_TIMES, mem_threshold: int = 800,
            duration_threshold: int = 100, write_excel: bool = True, get_logs: bool = True):
    """Decorator for performance data"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # --------------------------initialization--------------------------
            testcase_name = func.__name__  # test case name
            testcase_desc = func.__doc__  # test case desc
            testcase_file_name = os.path.split(inspect.getsourcefile(func))[1]  # 获取被装饰函数所在的模块文件路径
            testcase_class_name = args[0].__class__.__name__  # 获取被装饰函数所在的类名
            testcase_folder_name = os.path.basename(os.path.dirname(os.path.abspath(func.__code__.co_filename)))
            cache.set({'TESTCASE_NAME': testcase_name})
            cache.set({'TESTCASE_CLASS_NAME': testcase_class_name})
            run_times = 1
            folder_time = datetime.now().strftime("%Y_%m_%d_%H_%M")  # 以当前时间来命名文件夹
            if AppConfig.PERF_OUTPUT_FOLDER is None:
                raise ValueError('Please do not run in debug mode or specify "AppConfig.PERF_OUTPUT_FOLDER" directory!')
            testcase_base_path = os.path.join(AppConfig.PERF_OUTPUT_FOLDER, testcase_folder_name, testcase_class_name,
                                              testcase_name)
            if not os.path.exists(testcase_base_path):
                os.makedirs(testcase_base_path)
            if MODE == RunType.NOTHING:
                log.info(f'Do nothing mode:{testcase_name}')
            elif MODE == RunType.DEBUG:
                log.info(f'Recording and framing mode:{testcase_name}')
            elif MODE == RunType.DURATION:
                log.info(f'Calculation time consumption mode:{testcase_name}')
                run_times = duration_times
                start_path = os.path.join(testcase_base_path, 'start.jpg')  # 开始帧的位置
                stop_path = os.path.join(testcase_base_path, 'stop.jpg')  # 结束帧的位置
                if not os.path.exists(start_path) or not os.path.exists(stop_path):
                    log.error(
                        f'如果是首次运行用例：{testcase_name}\n'
                        f'1.请先使用@AppPerf(MODE=RunType.DEBUG)模式执行一遍\n'
                        f'2.生成分帧后再挑出关键帧放置在该位置\n'
                        f'3.然后再执行@AppPerf(MODE=RunType.DURATION)模式！')
                    raise FileNotFoundError(f'{start_path}___or___{stop_path}')
            elif MODE == RunType.STRESS:
                log.info(f'Stress test mode:{testcase_name}')
            else:
                raise ValueError
            duration_list = []
            cpu_base64_list = []
            mem_base64_list = []
            fps_base64_list = []
            bat_base64_list = []
            flo_base64_list = []
            start_frame_list = []
            stop_frame_list = []
            testcase_assert = True
            for i in range(run_times):
                run_path = AppConfig.PERF_RUN_FOLDER = os.path.join(testcase_base_path, folder_time)
                video_path = os.path.join(run_path, f'{testcase_name}_{i}.mp4')  # 录屏文件路径
                log_path = os.path.join(run_path, f'{testcase_name}_{i}.txt')
                Common.CASE_ERROR = []
                Common.PERF_ERROR = []
                Common.LOGS_ERROR = []
                if MODE in [RunType.DEBUG, RunType.DURATION]:
                    frame_path = os.path.join(testcase_base_path, folder_time, f'{testcase_name}_frame_{i}')  # 分帧
                    if not os.path.exists(frame_path):
                        os.makedirs(frame_path)
                if MODE in [RunType.DURATION, RunType.STRESS]:
                    perf_path = os.path.join(testcase_base_path, folder_time, f'{testcase_name}_jpg_{i}')  # 性能图表
                    if not os.path.exists(perf_path):
                        os.makedirs(perf_path)
                else:
                    if not os.path.exists(run_path):
                        os.makedirs(run_path)
                Common.threadLock = True
                Common.record = False

                # --------------------------Run test case--------------------------
                if get_logs and (Seldom.app_info.get('platformName') == 'Android'):
                    log_thread = threading.Thread(target=get_log, args=(log_path, run_path))
                    log_thread.start()
                do_list = [gevent.spawn(run_testcase, func, *args, **kwargs),
                           gevent.spawn(start_record, video_path, run_path)]
                if MODE in [RunType.DURATION, RunType.STRESS]:  # 判断是否开启性能数据获取，开启的话就在协程队列中增加get_perf执行
                    do_list.append(gevent.spawn(get_perf))
                gevent.joinall(do_list)
                if Common.CASE_ERROR:
                    log.error(f'{Common.CASE_ERROR}')
                    assert False, f'{Common.CASE_ERROR}'
                # --------------------------Frame the recording screen--------------------------
                if MODE in [RunType.DEBUG, RunType.DURATION] and Common.RECORD_ERROR == []:
                    log.info("✅正在进行录屏分帧")
                    Common.extract_frames(video_path, frame_path)
                    log.info("✅录屏分帧结束")
                # --------------------------Find keyframes--------------------------
                if MODE == RunType.DURATION and Common.RECORD_ERROR == []:
                    log.info("🌝Start searching for the most similar start frame")
                    start_frame_path = Common.find_best_frame(start_path, frame_path)
                    start_frame = int(os.path.split(start_frame_path)[1].split('.')[0][-6:])
                    log.info(f"Start frame:[{start_frame}]")
                    log.info("🌚Start searching for the most similar end frame")
                    stop_frame_path = Common.find_best_frame(stop_path, frame_path, is_start=False)
                    stop_frame = int(os.path.split(stop_frame_path)[1].split('.')[0][-6:])
                    log.info(f"Stop frame:[{stop_frame}]")
                    # --------------------------Calculation time consumption--------------------------
                    duration = round((stop_frame - start_frame) / AppConfig.FPS, 2)
                    log.info(f"🌈[{testcase_name}]Func time consume[{duration}]s")
                    duration_list.append(duration)
                    start_frame_list.append(Common.image_to_base64(start_frame_path))
                    stop_frame_list.append(Common.image_to_base64(stop_frame_path))
                    if run_times != 1:
                        if (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'Android'):
                            u2.launch_app_u2(stop=True)
                        elif (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'iOS'):
                            wda_.launch_app_wda(stop=True)

                # --------------------------Performance image saved locally and converted to base64--------------------
                if MODE in [RunType.DURATION, RunType.STRESS] and Common.PERF_ERROR == []:
                    # CPU
                    cpu_info = cache.get('CPU_INFO')
                    cpu_image_path = os.path.join(perf_path, f'{testcase_name}_CPU_{i}.jpg')
                    cpu_base64_list.append(
                        Common.draw_chart(cpu_info[1], cpu_info[0], ['appCpuRate', 'sysCpuRate'],
                                          jpg_name=cpu_image_path,
                                          label_title='CPU'))
                    # MEM
                    mem_info = cache.get('MEM_INFO')
                    mem_image_path = os.path.join(perf_path, f'{testcase_name}_MEM_{i}.jpg')
                    mem_base64_list.append(
                        Common.draw_chart(mem_info[1], mem_info[0], ['totalPass', 'nativePass', 'dalvikPass'],
                                          jpg_name=mem_image_path, label_title='Memory'))
                    # 帧率
                    fps_info = cache.get('FPS_INFO')
                    fps_image_path = os.path.join(perf_path, f'{testcase_name}_FPS_{i}.jpg')
                    if fps_info is not None:
                        fps_base64_list.append(
                            Common.draw_chart(fps_info[1], fps_info[0], ['fps', 'jank'], jpg_name=fps_image_path,
                                              label_title='Fps'))
            # --------------------------Picture Write Back Report--------------------------
            if MODE in [RunType.DEBUG, RunType.DURATION, RunType.STRESS] and Common.PERF_ERROR == []:
                photo_list = cpu_base64_list + mem_base64_list + fps_base64_list + flo_base64_list \
                             + bat_base64_list + start_frame_list + stop_frame_list
                AppConfig.REPORT_IMAGE.extend(photo_list)
                # --------------------------Data Write Back Table--------------------------
                mode = 'DurationTest' if MODE == RunType.DURATION else 'StressTest'
                file_class_name = f"{testcase_file_name} --> {testcase_class_name}"
                in_excel_times = AppConfig.STRESS_TIMES if MODE == RunType.STRESS else duration_times
                test_case_data = {'Time': folder_time, 'TestCasePath': file_class_name, 'TestCaseName': testcase_name,
                                  'TestCaseDesc': testcase_desc, 'Device': Seldom.app_info.get('platformName'),
                                  'Times': in_excel_times, 'MODE': mode}
                # --------------------------Time consumption or memory threshold assertion--------------------------
                if MODE == RunType.DURATION:
                    max_duration_res = round(statistics.mean(duration_list), 2)
                    log.success("🌈Average time consumption of functions[{:.2f}]s".format(max_duration_res))
                    if max_duration_res > duration_threshold:
                        max_duration_res = f"Average time consumption{max_duration_res}," \
                                           f"Exceeding threshold{duration_threshold}"
                        testcase_assert = False
                        log.warning(max_duration_res)
                    test_case_data.update({'DurationList': str(duration_list), 'DurationAvg': max_duration_res})
                    if testcase_assert is False:
                        assert False, max_duration_res
                elif MODE == RunType.STRESS:
                    max_mem_res = max([tup[0] for tup in cache.get('MEM_INFO')[1]])
                    if max_mem_res > mem_threshold:
                        max_mem_res = f"Maximum Memory{max_mem_res},Exceeding threshold{mem_threshold}"
                        testcase_assert = False
                        log.warning(max_mem_res)
                    test_case_data.update({'MemMax': max_mem_res})
                    if testcase_assert is False:
                        assert False, max_mem_res
                if write_excel:
                    AppConfig.WRITE_EXCEL.append(test_case_data)

        return wrapper

    return my_decorator
