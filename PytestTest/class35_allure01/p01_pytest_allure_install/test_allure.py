#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import allure
import pytest

#这不是用例函数，只是普通函数
@allure.step("步骤1：登陆")
def step_1():
    print("点击登陆")

@allure.step("步骤2：输入用户名密码")
def step_2():
    print("输入用户名密码")


#测试类和测试用例
class TestEditPage():
    # 测试用例
    def test_1(self):
        step_1()
        step_2()
        print("执行登陆")

    def test_2(self):
        print("查询商品")

if __name__ == '__main__':
    # pytest.main(['-vs'])
    pytest.main(['--alluredir','./result'])
    # 执行命令行的命令
    # os.system('allure generate ./life -o ./report')
    # 这个clean没有清理任何内容，只是允许你重复使用同一个目录生成报告，数据都会保留
    os.system('allure generate ./result -o ./hutu_report --clean')