import time


def exec_time(some_func):
    """ Track execution time of a function"""
    def wrapper(*args, **kwargs):
        ts = time.time()
        print("Function started at ", ts)
        some_func(*args, **kwargs)
        te = time.time()
        print("Function ended at ", te)
        print("Execution time:",'%r  %2.2f ms' % 
            (some_func.__name__, (te - ts) * 1000))
    return wrapper
