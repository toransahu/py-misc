import time


def exec_time(some_func):
    """ Track execution time of a function"""
    def wrapper(*args, **kwargs):
        ts = time.time()
        print("\t======================================")
        print("\tFunction started at", ts)
        result = some_func(*args, **kwargs)
        te = time.time()
        print("\tFunction ended at", te)
        print("\tExecution time of %r is %2.2f ms" % 
            (some_func.__name__, (te - ts) * 1000))
        print("\t======================================")
        return result
    return wrapper
