#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.mark.parametrize('a',['aaa','bbb','cccc'])
def test_01(a):
    print('\n' + a)

if __name__ == '__main__':
    pytest.main(['-s','test_single.py'])