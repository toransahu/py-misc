#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-24 23:23

"""
func_based_func_decorator_with_args.py
"""

__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'


##
# function decorator (function based) with args
##

def time_it(time_format):
    def time_it_inner(func):
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
# problems arises here
#
print("\nPrinting details about wrapped me():")
print(me.__name__)
print(me.__doc__)
print(me.__module__)

#
# we can solve it manually by assigning __doc__, __name__, __module__ of me() to wrapper()
# but better to use `from functools import wraps`
#
