#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_01():
    print("hello")
    assert 1 == 1

if __name__ == '__main__':
    pytest.main(['-s'])
    # pytest.main()