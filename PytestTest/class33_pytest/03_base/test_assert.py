#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    借助Python的运算符号 和 assert关键字 来实现的。
"""
import pytest


def test_kkk_01():
    print('kkk')
    # assert  "预期结果" == "实际结果"
    assert 1==2
    """
        测试不相等 !=
        <=
        >=
        测试包含 in
        测试不包含 not in
        判断是否为true: is True
        判断是否不为true: is not True/is False
        and
        or
    """

@pytest.mark.ma
def test_kkk_02():
    print('kkk')
    assert 1==2

def test_zzz_03():
    print('zzz')
    assert 1==1

if __name__ == '__main__':
    # pytest.main(['-vs'])
    # pytest.main(['-s','-v'])
    # pytest.main(['-s','-v','-k','zzz'])
    # pytest.main(['-s', '-v', '-k=zzz'])
    # pytest.main(['-q'])
    # pytest.main(['-x'])'
    # pytest.main(['-s','./doc/test_112233.py::TestDemo::test_case_03'])
    # pytest.main(['-s', './doc'])
    # pytest.main(['-s', '--junit-xml=./report/junit_report01.xml'])
    # pytest.main(['--maxfail=2'])
    pytest.main(['-m','ma'])