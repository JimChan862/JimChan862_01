#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

# 用例预置数据
@pytest.fixture
def first_fix():
    return ['a']

# 测试用例
def test_case01(first_fix):
    # 用例步骤
    first_fix.append("b")
    print(first_fix)

if __name__ == '__main__':
    pytest.main(['-s','test_quick_exam.py'])