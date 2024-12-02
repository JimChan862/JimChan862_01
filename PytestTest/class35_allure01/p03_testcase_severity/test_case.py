#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    allure对用例的等级划分成五个等级：
    blocker　 阻塞缺陷（功能未实现，无法下一步）
    critical　　严重缺陷（功能点缺失）
    normal　　 一般缺陷（边界情况，格式错误） 默认等级
    minor　 次要缺陷（界面错误与ui需求不符）
    trivial　　 轻微缺陷（必须项无提示，或者提示不规范）
"""
import os

import allure
import pytest


@allure.severity('normal')
def test_case01():
    print("测试用例一")

@allure.severity('critical')
def test_case02():
    print("测试用例二")

@allure.severity('blocker')
def test_case03():
    print("测试用例3")

def test_case04():
    print("测试用例4")

def test_case05():
    print("测试用例5")

def test_case06():
    print("测试用例6")

if __name__ == '__main__':
    # pytest.main(['--alluredir','./result'])
    # 如果有很多用例，现在想快速的回顾，只执行用例等级为blocker和critical的用例
    pytest.main(['--alluredir', './result','--allure-severities','blocker,critical','--clean-alluredir'])
    os.system('allure serve result')