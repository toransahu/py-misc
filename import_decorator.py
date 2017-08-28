from decorator_func import my_decorator, exec_time

@my_decorator
def just_some_func():
    print("I'm just some ordinary function.")

just_some_func()


@exec_time
def do_some_math():
    print(10000*100000/1000)

do_some_math()
