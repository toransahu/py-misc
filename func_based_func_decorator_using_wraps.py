#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-25 16:01

"""
func_based_func_decorator_using_wraps.py
"""

from functools import wraps


__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'


##
# function decorator (function based) with args using `wraps` to solve metadata issues
##


def time_it(time_format):
    def time_it_inner(func):
        @wraps(func)
        def wrapper():
            print(f"Time in {time_format} format before func()")
            func()
            print(f"Time in {time_format} format after func()")
        return wrapper
    return time_it_inner


@time_it("hh:mm:ss")
def me():
    """I'm me() function"""
    print("me")

me()

#
# problems has been solved here
#
print("\nPrinting details about wrapped me():")
print(me.__name__)
print(me.__doc__)
print(me.__module__)

