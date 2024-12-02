#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_case(fix1):
    print("测试用例一")

if __name__ == '__main__':
    pytest.main(['-s'])