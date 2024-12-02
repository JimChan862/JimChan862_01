#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure


@allure.step("登陆")
def login(username,passwd):
    """登陆"""
    print("前置操作:先登录")

@allure.step("浏览商品")
def open_goods():
    """浏览商品"""
    with allure.step("步骤1：选择颜色"):
        pass
    with allure.step("步骤2：选择大小"):
        pass
    print("浏览商品")

@allure.step("添加商品到购物车")
def add_cart(goods_id="10086"):
    """添加购物车"""
    print("添加购物车")

@allure.step("生成订单")
def buy_goods():
    """生成订单"""
    print("buy")

@allure.step("支付")
def pay_goods():
    """支付"""
    print("支付")