import functools
import threading
from time import time

import global_val

lock = threading.Lock()


def runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        lock.acquire()
        try:
            global_val.set_runtime(format(end - start, '.8f'))
        finally:
            lock.release()

        return result

    return wrapper
