"""
this is tomorrow3 library,Easier way to use thread pool executor
https://github.com/dflupu/tomorrow3
"""
from functools import wraps
from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor


def threads(n, queue_max=None):
    def decorator(f):
        pool = ThreadPoolExecutor(n)
        sem_max = queue_max

        if sem_max is None:
            sem_max = n

        sem = Semaphore(sem_max)
        thrown_exception = None

        def wait():
            # everything has already been added to the pool when .wait is called
            # if we can acquire the semaphore sem_max times, it means nothing is left in the pool
            for _ in range(sem_max):
                sem.acquire()

            # release in case the function will be called again after .wait
            for _ in range(sem_max):
                sem.release()

            if thrown_exception:
                raise thrown_exception

        f.wait = wait

        def on_done(f):
            nonlocal thrown_exception

            try:
                f.result()
            except Exception as ex:
                thrown_exception = ex
            finally:
                sem.release()

        @wraps(f)
        def wrapped(*args, **kwargs):
            if thrown_exception:
                raise thrown_exception

            sem.acquire(blocking=True)
            future = pool.submit(f, *args, **kwargs)
            future.add_done_callback(on_done)

            return future

        return wrapped

    return decorator
