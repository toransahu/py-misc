#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-25 13:40

"""
func+class_based_class_decorator_with_pre.py
"""

__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'


def time_it(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            orig_attribute = getattr(self.wrapped, name)
            if callable(orig_attribute):
                def method_wrapper(*args, **kwargs):
                    print(f"Before calling the {name} of class {self.wrapped}")
                    result = orig_attribute(*args, **kwargs)
                    print(f"After calling the {name} of class {self.wrapped}")
                    return result
                return method_wrapper
            return orig_attribute
    return Wrapper


@time_it
class Example:

    abc = "I'm a class/static variable"

    def __init__(self, name):
        self.name = name
        print(f"{name} instantiated Example class")

    def foo(self, a, b):
        print("Foo", a, b)

    def bar(self, c, d):
        print("bar", c, d)

    def foo_static(e,f):
        print("foo_static", e, f, Example.abc)

    def bar_class(cls, g, h):
        print("bar_class", g, h, cls.abc)


e = Example("Toran")

e.foo(1, 2)
e.bar(3, 4)
print(Example.abc)
