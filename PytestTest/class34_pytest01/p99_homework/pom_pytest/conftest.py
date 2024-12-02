#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    # 返回基础页面操作
    driver = webdriver.Chrome()
    yield driver
    # 后置，关闭所有页面
    driver.quit()