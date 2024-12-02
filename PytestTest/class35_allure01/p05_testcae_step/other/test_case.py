#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest


def test_case(fix1,fix2,fix3):
    print("测试用例一")

if __name__ == '__main__':
    pytest.main(['--alluredir', './result'])
    os.system('allure generate ./result -o ./hutu_report --clean')