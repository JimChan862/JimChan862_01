#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import allure
import pytest



# 前置操作
from class03.p05_testcae_step.case02.common_function2 import *


@pytest.fixture
def login_fix():
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
    # 浏览商品
    open_goods()
    add_cart()
    buy_goods()
    pay_goods()

if __name__ == '__main__':
    pytest.main(['--alluredir', './result'])
    os.system('allure generate ./result -o ./hutu_report --clean')