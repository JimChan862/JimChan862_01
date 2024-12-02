#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    1.程序开始执行以后，因为test函数终有yield关键字，
    所以test函数并不会真正的执行，而是先得到一个生成器g
    2.直到调用next方法，test函数正式开始执行，先执行test函数中的print方法，
    然后进入while循环
    3.程序遇到yield关键字，然后把yield相乘是return,return了一个8之后，程序停止，
    并没有执行赋值给a操作，此时next(g)语句执行完成，所以输出前面两行（第一行是while上面的
    print的结果，第二行是return出来的结果）
    4.程序执行print("**********************")
    5.又开始执行下面的print(next(g)),这个时候是从刚才next程序停止的地方开始执行，
    也就是要执行a的赋值操作，这个时候因为赋值操作的右边是没有值的，已经被return出去了
    这个时候a的值是none，所以接下来的输出是a:none
    6.程序会继续在whili里执行，又一次碰到yield，这个时候同样return出8，然后程序停止。
    print函数输出的8就是这次return出的8
"""


def test():
    print("begin....")
    while True:
        a = yield 8
        print("a:" ,a)

g = test()
print(next(g))
print("**********************")
print(next(g))
print("**********************")
print(next(g))