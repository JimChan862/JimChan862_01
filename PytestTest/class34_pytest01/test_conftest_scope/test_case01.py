#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


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
    pytest.main(['-s'])