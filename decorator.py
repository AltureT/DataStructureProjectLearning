import functools
import os
import sys
import threading
from time import time

import psutil

import global_val_dev

lock = threading.Lock()


def runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        # global_val_dev.set_runtime(format(end - start, '.8f'))
        lock.acquire()
        try:

            global_val_dev.set_runtime(format(end - start, '.8f'))

        finally:
            lock.release()

        return result

    return wrapper


def trace_malloc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # tracemalloc.start()
        # snapshot1 = tracemalloc.take_snapshot()
        # result = func(*args, **kwargs)
        # snapshot2 = tracemalloc.take_snapshot()
        result = func(*args, **kwargs)
        print(str(sys.getsizeof(result) / 1024) + 'KB')
        return result

    return wrapper


def count_info(func):
    def float_info(*args, **kwargs):
        pid = os.getpid()
        p = psutil.Process(pid)
        info_start = p.memory_full_info().uss
        result = func(*args, **kwargs)
        info_end = p.memory_full_info().uss
        print("程序占用了内存" + str(info_end - info_start) + "B")

        return result

    return float_info
