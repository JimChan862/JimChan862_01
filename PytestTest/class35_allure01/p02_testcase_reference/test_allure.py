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


@allure.feature("编辑分类文章")
#测试类和测试用例
class TestEditPage():
    # 测试用例
    @allure.story("文章编辑")
    @allure.title("编辑文章分类，重复保存，保存失败")
    @allure.issue("http://127.0.0.1:8080/zentao/buge-login.html") # 禅道系统的地址
    @allure.testcase("http://127.0.0.1:8080/zentao/testcase-login.html") # 禅道用例的链接地址
    def test_1(self):
        """
            编辑文章分类，重复保存，保存失败
            前置条件：1.登录
            步骤：
                1.编辑文章分类，输入文章类别，如计算机
                2.点击保存按钮
                3.重新打开编辑页面，输入：计算机
                4.再次点击保存按钮
            预期结果：
                1.输入成功
                2.保存成功
                3.输入成功
                4.保存失败，提示：已存在
        """
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