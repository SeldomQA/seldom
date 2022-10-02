"""
case more threading
"""
from threading import Thread
from seldom.logging import log


class ThreadWait:
    """
    Function thread decorator
    get_result()
    ThreadWait.get_all_result()
    """
    result_dict = {}
    thread_dict = {}

    class SeldomThread(Thread):
        """seldom thread"""

        def __init__(self, func, name='', *args, **kwargs):
            Thread.__init__(self)
            self.func = func
            self.name = name
            self.args = args
            self.kwargs = kwargs
            self.result = None

        def run(self):
            log.info(f"{self} Start with SeldomThread...")
            if isinstance(self.args, tuple) and len(self.args) > 1:
                name_key = self.args[0]
            else:
                name_key = self.ident
            self.result = self.func(*self.args, **self.kwargs)
            ThreadWait.result_dict[name_key] = self.result

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
