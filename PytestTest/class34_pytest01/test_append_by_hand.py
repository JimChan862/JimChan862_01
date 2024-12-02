#!/usr/bin/env python
# -*- coding: utf-8 -*-

def first_entry():
    return "a"

def order(first_entry):
    return [first_entry]

def test_string(order):
    order.append("b")
    assert order == ["a","b"]
    print(order)

entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)


