#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_case_03():
    print("test_case_03")

def ff01():
    print("ff01用例")

class A01:
    def test_aaa(self):
        print("A类里的用例")
    def ff02(self):
        print("A类里的用例ff02")

class B01:
    def test_bbb(self):
        print("B类里的用例")
    def ff03(self):
        print("B类里的用例ff03")

class Test01:
    def test_ccc(self):
        print("Test01类里的用例")
    def ff04(self):
        print("Test01类里的用例ff04")