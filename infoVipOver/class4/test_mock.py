import unittest
from unittest import TestCase,mock

from infoVipOver.class4 import demo1
from infoVipOver.class4 import demo2
import demo3


class TestCase01(unittest.TestCase):
    # 注册的功能 有值给我
    # 登录的功能  有值给我
    def testcase01(self):
        # 把 1给到  res1=test_demo1()
        # 把1 给到  res2=test_demo2()
        demo3.test_demo1=mock.Mock(return_value=1)
        demo3.test_demo2=mock.Mock(return_value=2)
        # asser 2,1  2  2 用例成功
        self.assertEqual(2,demo3.fun())

if __name__ == '__main__':
    unittest.main()


# mock 创建真实的数据  a开发  b开发的功能也没动  不能动他们代码
# 数据  用mock去创建数据 返回数据 真实的数据  看你写的代码 能不能去使用这些数据

# 开发  a 注册
# b 登录
# c 首页  登录 注册  没返回值
# unittest的mock  构造了返回值 给到 a注册  给到了b开发登录 的值
# 断言
#


