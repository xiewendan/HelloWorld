# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2018/11/17 17:22:33

# desc: desc

import os, sys
print("333333333333", os.getcwd())
print("2222222222222", __file__)
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
sys.path.append(ABSPATH)
print("11111111111111111", sys.path, ABSPATH)

a = 10
print("xjc")
b = 10