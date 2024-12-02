#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 功能函数,相乘
import pytest


def multiply(a,b):
    return a*b
#
# if __name__ == '__main__':
#     print(multiply(2,2))

"""
    不含有类的用例预置和后置函数
    第一批次：setup_module/teardown_module: 在当前文件中，在所有测试用例执行之前与之后执行
    第二批次：setup_function/teardown_function:在每个测试函数之前与之后执行
    第三批次：setup/teardown:在每个测试函数之前与之后执行，在类中也可以使用
    ps：执行的顺序按优先级来的，改变方法位置结果也一样
"""
# 用例前置后置
def setup_function(function):
    print("setup_function===================")

def teardown_function(function):
    print("teardown_function================")

def setup():
    print("setup===================")

def teardown():
    print("teardown===================")

def setup_module(module):
    print("setup_module===================")

def teardown_module(module):
    print("teardown_module================")

#
# ========测试用例=========
def test01():
    print("第一个用例")
    # print(multiply(3,4))


def test02():
    print("第二个用例")
    # print(multiply(4,4))

if __name__ == '__main__':
    pytest.main(['-s','test_setup01.py'])