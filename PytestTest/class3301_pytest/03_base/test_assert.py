#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    借助Python的运算符号 和 assert关键字 来实现的。
"""
import pytest


def test_kkk_01():
    print('kkk')
    # assert  "预期结果" == "实际结果"
    assert 1 == 2
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


# 装饰器@pytest.mark.XXX装饰的所有测试用例  先在pytest.ini文件中注册自定义标记
@pytest.mark.ma
def test_kkk_02():
    print('kkk')
    assert 1==2
#
def test_zzz_03():
    print('zzz')
    assert 1==1

if __name__ == '__main__':
    pytest.main(['-vs'])
    # pytest.main(['-s','-v'])
    # pytest.main(['-s','-v','-k','zzz'])     #运行名称中包含某字符串的测试用例 -k
    # pytest.main(['-s', '-v', '-k=zzz'])
    # pytest.main(['-q'])     #简化输出信息 -q
    # pytest.main(['-x'])      # 如果出现一条测试用例失败，则退出测试

    # 指定目录以及特定类或方法执行
    # pytest.main(['-s','./doc/test_112233.py::TestDemo::test_case_03'])
    # pytest.main(['-s', './doc'])

    # 生成junit xml文件测试报告
    # pytest.main(['-s', '--junit-xml=./report/junit_report01.xml'])

    # 在第N个很用例失败之后，结束测试执行
    # pytest.main(['--maxfail=2'])
    # 通过标记表达式执行
    pytest.main(['-m','ma'])
    # pytest.main()
