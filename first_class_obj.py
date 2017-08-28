"""
In Python, functions are first-class objects.
This means that functions can be passed around, and used as arguments, 
just like any other value (e.g, string, int, float).
"""

def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))
