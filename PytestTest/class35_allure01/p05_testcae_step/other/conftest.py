#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

#@allure.step 放在@pytest.fixture上面是不行，放在下面可以
# @allure.step("登陆前置操作")
# @pytest.fixture
# def fix():
#     print("登陆")

@allure.step("登陆前置操作")
@pytest.fixture
def fix1():
    with allure.step("登陆前置操作"):
        print("登陆")

@pytest.fixture
@allure.step("登陆前置操作")
def fix2():
    print("登陆")

