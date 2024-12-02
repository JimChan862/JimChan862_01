#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def fix1():
    print("fix1返回的值")

@pytest.fixture
def fix2():
    print("fix2返回的值")

# @pytest.mark.usefixtures('fix1','fix2')
# def test_1():
#     print("测试用例一")

# # 1.注意：这种方法，在fixture+conftest.py的组合形式下，是无法被引用的
# # 2. 这种直接在类上统一的使用fix，类当中的用例就不用再重复使用了
@pytest.mark.usefixtures('fix2')
@pytest.mark.usefixtures('fix1')
class TestCase():
    def test_2(self):
        print("类里的用例test2")

    def test_3(self):
        print("类里的用例test3")


if __name__ == '__main__':
    pytest.main(['-s','test_usefixtures.py'])