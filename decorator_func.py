import time
"""
Let's create a custom decorator fucntion to understand the decorators.
Def: Decorators are nothing but a wrapper, which wraps a method. Like

1. do something before a function
2. run a function
3. do something after a function
"""

def my_decorator(some_func):
    def wrapper():
        print("Do something before some function")
        some_func();
        print("Do something after some function")
    return wrapper

"""
Lets define a function and pass it to my_decorator

please uncomment it to run the example


def some_func1():
    print("I'm some function 1.")


res = my_decorator(some_func1)
print(res)
print(res())
"""

"""
Real world examples on decorator
"""

# track execution time of a function

def exec_time(some_func):
    def wrapper():
        print("function started at ", time.time())
        some_func()
        print("function ended at ", time.time())
    return wrapper
