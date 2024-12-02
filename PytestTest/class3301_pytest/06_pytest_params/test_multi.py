#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.mark.parametrize('username,pwd',[('zz','123456'),('xz','123456'),('qs','123456')])
def test_01(username,pwd):
    print('\n' + username)
    print('\n' + pwd)

if __name__ == '__main__':
    pytest.main(['-s','test_multi.py'])