#!/usr/bin/env python
# -*- coding: utf-8 -*-

def first_fix():
    return  ["a"]

def test_case(varA):
    varA.append("b")
    print(varA)

varA = first_fix()
test_case(varA)