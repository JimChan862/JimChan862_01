#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def fix():
    a = 'zz'
    b = '123456'
    print("传出a,b")
    return (a,b)

def test_case(fix):
    username = fix[0]
    passwd = fix[1]
    print('通过fixture的元祖取出用户名和密码')
    print(username)
    print(passwd)

if __name__ == '__main__':
    pytest.main(['-s','test_multi_fixture01.py'])