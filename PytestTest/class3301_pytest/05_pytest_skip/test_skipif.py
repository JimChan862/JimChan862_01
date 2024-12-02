#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

def test_02():
    print("用例2执行")
    return True

# 条件成立就跳过，条件不成立就执行
@pytest.mark.skipif(condition= True ,reason="不想跑了")
def test_01():
    print("用例1执行")

@pytest.mark.skipif(condition= 1==2 ,reason="不想跑了")
def test_03():
    print("用例3执行")



if __name__ == '__main__':
    pytest.main(['-s','test_skipif.py'])

