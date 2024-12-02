#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_case01():
    assert 1==1

def test_case02():
    assert 1==2

def test_case03():
    assert 1==3

def test_case04():
    assert 1==4

def test_case05():
    assert 1==5

def test_case06():
    assert 1==6

def test_case07():
    assert 1==7

if __name__ == '__main__':
    # 重新运行所有测试失败用例
    # pytest.main(['--reruns', '3', 'test_rerun.py'])
    # 在每次重跑之间，增加一次延迟时间
    pytest.main(['--reruns', '3','--reruns-delay','2','test_rerun.py'])