#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def first_fix():
    return "a"

@pytest.fixture
def order(first_fix):
    return [first_fix]

# 测试用例
def test_string(order):
    order.append("b")
    print(order)

if __name__ == '__main__':
    pytest.main(['-s','test_append.py'])