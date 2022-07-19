from threading import Thread, currentThread
import time


class ThreadWait:
    """
    Function thread decorator
    get_result()
    ThreadWait.get_all_result()
    """
    result_dict = {}
    thread_dict = {}

    class SeldomThread(Thread):
        def __init__(self, func, name='', *args, **kwargs):
            Thread.__init__(self)
            self.func = func
            self.name = name
            self.args = args
            self.kwargs = kwargs
            self.result = None

        def run(self):
            print(f"{self} Start with SeldomThread...")
            self.result = self.func(*self.args, **self.kwargs)
            ThreadWait.result_dict[self.ident] = self.result

        def get_result(self):
            """Return run result"""
            self.join()
            return self.result

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        _my_thread = self.SeldomThread(self.func, self.func.__name__, *args, **kwargs)
        _my_thread.start()
        self.thread_dict[_my_thread.ident] = _my_thread
        return _my_thread

    @classmethod
    def get_all_result(cls):
        """Return all run result"""
        for k, thr in cls.thread_dict.items():
            thr.join()
        return cls.result_dict


def click(callback, *args, **kwargs):
    # print('in main func with <', callback.__name__, '>', *args, **kwargs)
    return callback(*args, **kwargs)


@ThreadWait
def event(name, s):
    print(f"{name}等待返回结果{s}")
    time.sleep(s)
    print(f'{currentThread()} < event > finished! {s}')
    return name, s


# g_a = 100
# event(4)
# a = event(5)
# print('a:', a.getResult())
# click(event, 3)
# click(event, 6)
# print('event all:', ThreadWait.getAllResult())
