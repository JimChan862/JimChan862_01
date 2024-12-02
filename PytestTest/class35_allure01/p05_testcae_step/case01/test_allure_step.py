#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import allure
import pytest
from class03.p05_testcae_step.case01.common_function import *


# 前置操作
@pytest.fixture
def login_fix():
    with allure.step("setup:登陆"):
        login("zz","123456")

@allure.feature("购物模块")
@allure.title("测试购物流程")
def test_shopping(login_fix):
    """
        用例步骤：
        1.登陆
        2.浏览商品
        3.添加购物车
        4.生成订单
        5.支付成功
    """
    with allure.step("浏览商品"):
        open_goods()
        with allure.step("嵌套步骤"):
            add_cart()

    with allure.step("添加购物车"):
        add_cart()
        assert 1 == 2

    with allure.step("购买商品"):
        buy_goods()

    with allure.step("支付"):
        pay_goods()

if __name__ == '__main__':
    pytest.main(['--alluredir', './result'])
    os.system('allure generate ./result -o ./hutu_report --clean')