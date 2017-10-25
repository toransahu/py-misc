# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:10:01 2017

@author: toran.sahu
"""

import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()