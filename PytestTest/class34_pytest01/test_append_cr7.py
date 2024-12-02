#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def first_fix():
    return {'username':'admin','password':'admin123'}

@pytest.fixture
def order(first_fix):
    first_fix['aaa'] = "1111"
    return first_fix

# 测试用例
def test_string(order):
    print(order)

if __name__ == '__main__':
    pytest.main(['-s','test_append_cr7.py'])