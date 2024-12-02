#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

def read_list():
    return ['1','2','3']

@pytest.fixture(params=read_list())
def fix(request):
    #request是pytest的内置fixture，主要用于传递参数
    return request.param

def test_01(fix):
    print("测试用例：" + fix)
    print(fix)

if __name__ == '__main__':
    pytest.main(['-s','test_params.py'])