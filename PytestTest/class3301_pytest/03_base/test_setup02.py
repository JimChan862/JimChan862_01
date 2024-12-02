#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 功能函数
import pytest


def multiply(a,b):
    return a*b

class TestCase:
    """
        第一批次：setup_class/teardown_class：在当前的测试类的开始和结束时执行
        第二批次：setup_method/teardown_method:在每个测试方法开始与结束时执行
        第三批次：setup/teardown:在每个测试方法开始与结束时执行
        ps：执行的顺序按优先级来的，改变方法位置结果也一样
    """
    @classmethod
    def setup_class(cls):
        print("setup_class========================")

    @classmethod
    def teardown_class(cls):
        print("teardown_class======================")

    def setup_method(self,method):
        print("setup_method===================")

    def teardown_method(self,method):
        print("teardown_method================")


    def setup(self):
        print("setup================")

    def teardown(self):
        print("teardown================")

    #============测试用例============
    def test01(self):
        print("类里的第一条用例")
        # print(multiply(2,2))

    def test02(self):
        print("类里的第二条用例")
        # print(multiply(4,4))

if __name__ == '__main__':
    pytest.main(['-s','test_setup02.py'])