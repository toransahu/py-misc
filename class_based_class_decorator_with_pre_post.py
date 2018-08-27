#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-25 13:40

"""
func+class_based_class_decorator_with_pre.py
"""

__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'


class TimeIt:
    def __init__(self, cls):
        self.wrapped_cls = cls

    def __call__(self, *args, **kwargs):
        self.wrapped_obj = self.wrapped_cls(*args, **kwargs)
        return self.wrapped_obj

    def __getattr__(self, name):
        self.orig_attribute = getattr(self.wrapped_obj, name)

        # handle only func/methods
        if callable(self.orig_attribute):

            def method_wrapper(*args, **kwargs):
                self.pre()
                result = self.orig_attribute(*args, **kwargs)
                self.post()
                return result
            return method_wrapper
        return self.orig_attribute

    def pre(self):
        print(f"Before calling the {self.orig_attribute} of class {self.wrapped_cls}")

    def post(self):
        print(f"After calling the {self.orig_attribute} of class {self.wrapped_cls}")


@TimeIt
class Example:

    abc = "I'm a class/static variable"

    def __init__(self, name):
        self.name = name
        print(f"{name} instantiated Example class")

    def foo(self, a, b):
        print("Foo", a, b)

    def bar(self, c, d):
        print("bar", c, d)

    @staticmethod
    def foo_static(e,f):
        print("foo_static", e, f, Example.abc)

    @classmethod
    def bar_class(cls, g, h):
        print("bar_class", g, h, cls.abc)


e = Example("Toran")

e.foo(1, 2)
e.bar(3, 4)
print(Example.abc)
Example.foo_static(5, 6)
Example.bar_class(7, 8)

#
# TODO: issues with this pattern: it doesn't work if the wrapped class has methods that return another instance of the wrapped class
#

# def foo_return_instance(self):
#     return self

# res = foo_return_instance()

# # should print before func call
# res.foo()
# # should print after func call    