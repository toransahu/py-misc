#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-25 13:01

"""
class_based_func_decorator.py
"""

__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'


##
# function decorator (class based)
##

class TimeIt:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print("Enter")
        self.func(*args)
        print("Exit")


@TimeIt
def me():
    print("me")


me()