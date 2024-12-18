# 3.把token放在session中
# session:英文  开会 会议
# 编程：一次会话
# 登录--下单--支付 session
# 登录开始 会话开始建立  系统任何操作  session存放了会话过程中任何对象
# 浏览器关闭 session会话就结束了

# 登录进去了  token放在session里面  记录到我了  我在里面做的操作 都会知道是谁做的
# 你在session去访问  访问  登录 session    关闭
import allure
import jsonpath
import pytest
import requests

# 1.创建session对象
# 2.设置session的headers属性  token放进去
from infoVipOver.class3.httpclient import HttpClient

@allure.feature('接口自动化测试')
class TestCase:
    httpclient=HttpClient()
    openid=None
    proid=None
    userid=None
    cartid=None
    # 响应 token号会变 1.响应回来的token号提取出来 保存在变量。
    # 2.放在一个地方 都可以拿到token  类变量  其他方式 2.session  3.返回值
    # 作业：获得token   后面两条用例自己补充完
    @allure.story('登录流程')
    @allure.title('登录')
    def test_login(self):
        url='http://39.98.138.157:5000/api/login'
        # 张三 token 2h
        data={"password": "123456","username": "admin"}
        # res=requests.post(url,json=data)
        res=TestCase.httpclient(method='post',url=url,param_type='json',data=data)
        print(res.json())
        # 提取token  保存在变量中了  接口关联  要用的数据 提取出来 保存在变量中  类变量中 下个接口要用
        token=jsonpath.jsonpath(res.json(), '$..token')[0]
        # 把这个token放在session的headers里面  给头部里面设置属性 用update
        TestCase.httpclient.session.headers.update({'token':token})
        sjmsg=jsonpath.jsonpath(res.json(),'$..msg')[0]
        assert 'success'==sjmsg

    # 获得个人信息  获得谁的个人信息  拿到token
    # # # 注意 添加购物车 下单的时候需要用到这里面的userid和openid 这个怎么弄
    @allure.story('获得个人信息流程')
    @allure.title('个人信息')
    def test_getUserinfo(self):
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        # session头部里面已经有了token
        # res=requests.get(url,headers=header)
        # res=TestCase.session.get(url)
        res=TestCase.httpclient(url=url,method='get',param_type='json')
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
    # #
    # # # 选择商品 data=str  写法str  表单和json
    @allure.story('选择商品流程')
    @allure.title('商品')
    def test_shopping(self):
        url ='http://39.98.138.157:5000/api/getproductinfo?productid=8888'
        res=TestCase.httpclient(url=url,method='get',param_type='json')
        print(res.json())
        TestCase.proid=jsonpath.jsonpath(res.json(),'$..productid')[0]
        sjproductid=jsonpath.jsonpath(res.json(),'$..productid')[0]
        assert 8888==sjproductid
    # #
    # # # 添加购物车  为什么会失败  写法看着没有问题  注意  有问题  运行起来  没问题  没有运行起来
    # # # 信息传入不正确 值 有问题  请求头  没有问题  没有测试 参数有没有问题  传的值对不对
    # # # 确定一下 这个值是不是你想要 影响到你的判断 没有关联的代码注释掉
    # # # 更好的解决代码  理解这一块步骤  你写的代码是什么意思
    @allure.story('添加购物车流程')
    @allure.title('购物车')
    def test_cart(self):
        url='http://39.98.138.157:5000/api/addcart'
        # 参数 不能直接写死 userid  openid 取userid的值  取openid值 拿 哪里响应的哪个地方拿
        # userid和openid拿到值了  还是报错
        data={"openid": TestCase.openid,"productid": TestCase.proid,"userid": TestCase.userid}
        # res=requests.post(url,json=data,headers=header)
        res=TestCase.httpclient(url=url,method='post',param_type='json',data=data)
        print(res.json())
        TestCase.cartid = jsonpath.jsonpath(res.json(), '$..cartid')[0]
        # 断言  debug用在跳页面的时候  习惯
        exmsg=45233
        sjmsg=jsonpath.jsonpath(res.json(),'$..cartid')[0]
        # print(sjmsg)
        assert exmsg==sjmsg

    @allure.story('下单流程')
    @allure.title('下单')
    def test_order(self):
        url='http://39.98.138.157:5000/api/createorder'
        data={ "cartid": TestCase.cartid, "openid": TestCase.openid, "productid": TestCase.proid, "userid": TestCase.userid}
        # res = requests.post(url, json=data, headers=header)
        res=TestCase.httpclient(url=url,method='post', data=data,param_type='json')
        print(res.json())

if __name__ == '__main__':
    pytest.main(['-sv','test_py4.py'])

# 流程 改变的地方
# get  post  一种方式 又能接受get又能接受post请求   封装 请求方式

# allure测试报告  漂亮的测试报告
# 出现问题 自己解决 打断点  大概的分析问题

# 作业：自己封装了request在给个测试报告

