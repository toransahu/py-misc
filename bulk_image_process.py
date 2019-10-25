#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2019-10-25 12:33

"""Bulk Image Process."""

from PIL import Image

__author__ = 'Toran Sahu <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the MIT license'


for i in range(10):
    img = Image.open(f'{i}.png')
    print(img.size)
    box = (0, 120, 1255, 999)  # left, upper, right, lower
    cropped = img.crop(box)
    cropped.save(f'{i}_cropped.png')