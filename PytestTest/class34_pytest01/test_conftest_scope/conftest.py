#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(scope='session',autouse=True)
def fix1():
    print('\n开始执行session')

@pytest.fixture(scope='package',autouse=True)
def fix2():
    print('\n开始执行package')

@pytest.fixture(scope='module',autouse=True)
def fix3():
    print('\n开始执行module')

@pytest.fixture(scope='class',autouse=True)
def fix4():
    print('\n开始执行class')

@pytest.fixture(scope='function',autouse=True)
def fix5():
    print('\n开始执行function')