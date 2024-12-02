#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def fix1():
    a = 'zz'
    print("\n传出a")
    return a

@pytest.fixture
def fix2():
    b = '123456'
    print('\n传出b')
    return b

def test_case(fix1,fix2):
    username = fix1
    passwd = fix2
    print("传入多个fix")
    print(username)
    print(passwd)

if __name__ == '__main__':
    pytest.main(['-s','test_multi_fixture02.py'])