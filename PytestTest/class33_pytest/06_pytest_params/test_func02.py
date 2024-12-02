#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

def return_data():
    return [('zz','123456'),('xz','123456'),('qs','123456')]

@pytest.mark.parametrize('data',return_data())
def test_01(data):
    print('\n' + data[0])
    print('\n' + data[1])

if __name__ == '__main__':
    pytest.main(['-s','test_func02.py'])