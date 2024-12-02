#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(scope='class',autouse=True)
def fix4():
    print('\n开始执行class')

@pytest.fixture(scope='function',autouse=True)
def fix5():
    print('\n开始执行function')

@pytest.fixture(scope='session',autouse=True)
def fix1():
    print('\n开始执行session')

@pytest.fixture(scope='package',autouse=True)
def fix2():
    print('\n开始执行package')

@pytest.fixture(scope='module',autouse=True)
def fix3():
    print('\n开始执行module')



def test_a():
    print("用例a执行")

def test_b():
    print("用例b执行")

class TestCase:
    def test_c(self):
        print("类里的用例c执行")

    def test_d(self):
        print("类里的用例d执行")

if __name__ == '__main__':
    pytest.main(['-s','test_auto_scope.py'])