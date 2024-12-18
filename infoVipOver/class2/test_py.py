# 接口关联   实现登录 下单 流程
# 代码 流程实现出来  框架中 实现这个流程  哪个知识点 实现好一点？
# unittest/pytest会要好点  普通写个用例 函数  管理用例
import jsonpath
import pytest
import requests

class TestCase:
    token=None
    # 响应 token号会变 1.响应回来的token号提取出来 保存在变量。
    # 2.放在一个地方 都可以拿到token  类变量  其他方式 2.session  3.返回值
    def test_login(self):
        url='http://39.98.138.157:5000/api/login'
        # 张三 token 2h
        data={"password": "123456","username": "admin"}
        res=requests.post(url,json=data)
        print(res.json())
        # 提取token  保存在变量中了
        TestCase.token=jsonpath.jsonpath(res.json(), '$..token')[0]
        sjmsg=jsonpath.jsonpath(res.json(),'$..msg')[0]
        assert 'success'==sjmsg

    # 注意 添加购物车 下单的时候需要用到这里面的userid和openid 这个怎么弄
    def test_getUserinfo(self):
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        # 这个token不能写死  获得登录时的token
        header={"token":TestCase.token}
        res=requests.get(url,headers=header)
        print(res.json())
        sjname=jsonpath.jsonpath(res.json(),'$..nikename')[0]
        assert '风清扬'==sjname

    # 选择商品
    def test_shopping(self):
        url ='http://39.98.138.157:5000/api/getproductinfo?productid=8888'
        res=requests.get(url)
        print(res.json())
        sjproductid=jsonpath.jsonpath(res.json(),'$..productid')[0]
        assert 8888==sjproductid

    def test_cart(self):
        pass

    def test_order(self):
        pass


if __name__ == '__main__':
    pytest.main(['-sv','test_py.py'])

# 添加购物车 下单 作业 去做 关联
# 作业：怎么把toekn  2.session  3.返回值  一个案例就行
# http://39.98.138.157:5000/apidocs/#/%E6%B5%8B%E7%A0%81%E5%AD%A6%E9%99%A2VIP%E8%AF%BE%E7%A8%8B%E6%8E%A5%E5%8F%A3swagger%E6%96%87%E6%A1%A3/post_api_addcart

# 添加购物车 下单  补充完
# session 登录  获得个人信息
# 返回值  登录  获得个人信息

