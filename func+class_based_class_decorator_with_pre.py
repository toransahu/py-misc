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
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print(f"Getting the {name} of class {self.wrapped}")
            #
            # or do something else here like call self.pre()
            #
            return getattr(self.wrapped, name)

        #
        # def pre(self, *args):
        #    # do something meaningful
        #

    return Wrapper


@time_it
class Example:
    def __init__(self, name):
        self.name = name
        print("Example instantiated")

    def foo(self, a, b):
        print("Foo", a, b)

    def bar(self, c, d=5):
        print("bar", c, d)


e = Example("Toran")

e.foo(1,2)

e.bar(3,4)