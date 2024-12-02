#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

def return_data():
    return [('zz','123456'),('xz','123456'),('qs','123456')]

@pytest.mark.parametrize('username,pwd',return_data())
def test_01(username,pwd):
    print('\n' + username)
    print('\n' + pwd)

if __name__ == '__main__':
    pytest.main(['-s','test_func.py'])