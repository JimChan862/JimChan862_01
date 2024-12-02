#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def fix1():
    print('\nconftest里的fix1')