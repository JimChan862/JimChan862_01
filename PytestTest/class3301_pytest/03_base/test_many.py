#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_case01():
    assert 1==1

# def test_case02():
#     assert 1==2
#
# def test_case03():
#     assert 1==3
#
# def test_case04():
#     assert 1==4
#
# def test_case05():
#     assert 1==5
#
# def test_case06():
#     assert 1==6
#
# def test_case07():
#     assert 1==7

if __name__ == '__main__':
    # pytest.main(['test_many.py'])
    # 将测试执行发送到多个cpu
    # pytest.main(['-n','2','test_many.py'])
    # 使用与计算机具有cpu内核一样多的进程
    pytest.main(['-n', 'auto', 'test_many.py'])