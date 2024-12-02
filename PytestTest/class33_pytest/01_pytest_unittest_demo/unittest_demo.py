#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class UnitDemo(unittest.TestCase):
    def test_login(self):
        print("login")
        self.assertEqual("123","1231",msg="断言失败")

if __name__ == '__main__':
    unittest.main()