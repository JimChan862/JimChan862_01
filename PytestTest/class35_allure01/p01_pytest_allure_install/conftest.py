#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(autouse=True)
def fix():
    print("用例准备工作")