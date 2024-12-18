# 第一个内容 作业
# 1.补充完后面登录-下单的流程
# 2.返回值返回token
# 3.把token放在session中

# 接口关联   实现登录 下单 流程
# 代码 流程实现出来  框架中 实现这个流程  哪个知识点 实现好一点？
# unittest/pytest会要好点  普通写个用例 函数  管理用例
import jsonpath
import pytest
import requests



class TestCase:
    token=None
    openid=None
    proid=None
    userid=None
    cartid=None
    # 响应 token号会变 1.响应回来的token号提取出来 保存在变量。
    # 2.放在一个地方 都可以拿到token  类变量  其他方式 2.session  3.返回值
    # 作业：获得token   后面两条用例自己补充完
    def test_login(self):
        url='http://39.98.138.157:5000/api/login'
        # 张三 token 2h
        data={"password": "123456","username": "admin"}
        res=requests.post(url,json=data)
        print(res.json())
        # 提取token  保存在变量中了  接口关联  要用的数据 提取出来 保存在变量中  类变量中 下个接口要用
        TestCase.token=jsonpath.jsonpath(res.json(), '$..token')[0]
        sjmsg=jsonpath.jsonpath(res.json(),'$..msg')[0]
        assert 'success'==sjmsg

    # 注意 添加购物车 下单的时候需要用到这里面的userid和openid 这个怎么弄
    def test_getUserinfo(self):
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        # 这个token不能写死  获得登录时的token
        header={"token":TestCase.token}
        res=requests.get(url,headers=header)
        # 获取所有的结果
        print(res.json())
        # userid和openid  jsonpath  字典取值 jsonpath(数据，表达式)
        TestCase.openid=jsonpath.jsonpath(res.json(),'$..openid')[0]
        TestCase.userid=jsonpath.jsonpath(res.json(),'$..userid')[0]
        # 出现问题  分析问题   没有取到值 直接报错  刚开始的代码都是调通 新加的代码 排查问题
        # print('useridfefefefefe',TestCase.userid)
        # print('openidfefeeffeef',TestCase.openid)
        sjname=jsonpath.jsonpath(res.json(),'$..nikename')[0]
        assert '风清扬'==sjname

    # 选择商品
    def test_shopping(self):
        url ='http://39.98.138.157:5000/api/getproductinfo?productid=8888'
        res=requests.get(url)
        print(res.json())
        TestCase.proid=jsonpath.jsonpath(res.json(),'$..productid')[0]
        sjproductid=jsonpath.jsonpath(res.json(),'$..productid')[0]
        assert 8888==sjproductid

    # 添加购物车  为什么会失败  写法看着没有问题  注意  有问题  运行起来  没问题  没有运行起来
    # 信息传入不正确 值 有问题  请求头  没有问题  没有测试 参数有没有问题  传的值对不对
    # 确定一下 这个值是不是你想要 影响到你的判断 没有关联的代码注释掉
    # 更好的解决代码  理解这一块步骤  你写的代码是什么意思
    def test_cart(self):
        url='http://39.98.138.157:5000/api/addcart'
        header={'token':TestCase.token}
        # 参数 不能直接写死 userid  openid 取userid的值  取openid值 拿 哪里响应的哪个地方拿
        # userid和openid拿到值了  还是报错
        data={"openid": TestCase.openid,"productid": TestCase.proid,"userid": TestCase.userid}
        res=requests.post(url,json=data,headers=header)
        print(res.json())
        TestCase.cartid = jsonpath.jsonpath(res.json(), '$..cartid')[0]
        # 断言  debug用在跳页面的时候  习惯
        exmsg=45233
        sjmsg=jsonpath.jsonpath(res.json(),'$..cartid')[0]
        # print(sjmsg)
        assert exmsg==sjmsg

    def test_order(self):
        url='http://39.98.138.157:5000/api/createorder'
        data={ "cartid": TestCase.cartid, "openid": TestCase.openid, "productid": TestCase.proid, "userid": TestCase.userid}
        header={'token':TestCase.token}
        res = requests.post(url, json=data, headers=header)
        print(res.json())

if __name__ == '__main__':
    pytest.main(['-sv','test_py.py'])

# 添加购物车 下单 作业 去做 关联
# 作业：怎么把toekn  2.session  3.返回值  一个案例就行
# http://39.98.138.157:5000/apidocs/#/%E6%B5%8B%E7%A0%81%E5%AD%A6%E9%99%A2VIP%E8%AF%BE%E7%A8%8B%E6%8E%A5%E5%8F%A3swagger%E6%96%87%E6%A1%A3/post_api_addcart

# 添加购物车 下单  补充完
# session 登录  获得个人信息
# 返回值  登录  获得个人信息

# 写代码 出现问题  自己解决 不会解决  那块系统地方问题