# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:08:07 2017

@author: toran.sahu
"""

# import pytest

def add(x, y):
    return x + y

def test_add_positive():
    assert add(3,4) == 7
    
def test_add_negative():
    assert add(3,3) == 7    