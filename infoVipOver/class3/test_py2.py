import jsonpath
import pytest
import requests


# 上个接口的返回值 下个接口想要用  返回值
class TestCase:
    def test_login(self):
        url='http://39.98.138.157:5000/api/login'
        # 张三 token 2h
        data={"password": "123456","username": "admin"}
        res=requests.post(url,json=data)
        print(res.json())
        # 提取token  保存在变量中了  接口关联  要用的数据 提取出来 保存在变量中  类变量中 下个接口要用
        token=jsonpath.jsonpath(res.json(), '$..token')[0]
        sjmsg=jsonpath.jsonpath(res.json(),'$..msg')[0]
        assert 'success'==sjmsg
        return token

    # 注意 添加购物车 下单的时候需要用到这里面的userid和openid 这个怎么弄
    # 获取个人信息 用token  方法调用 调用方法  hukhgeujkjfjlfdd
    def test_getUserinfo(self):
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        # 这个token不能写死  获得登录时的token
        header = {'token':self.test_login()}
        res = requests.get(url, headers=header)
        # 获取所有的结果
        print(res.json())
        # userid和openid  jsonpath  字典取值 jsonpath(数据，表达式)
        TestCase.openid = jsonpath.jsonpath(res.json(), '$..openid')[0]
        TestCase.userid = jsonpath.jsonpath(res.json(), '$..userid')[0]
        # 出现问题  分析问题   没有取到值 直接报错  刚开始的代码都是调通 新加的代码 排查问题
        # print('useridfefefefefe',TestCase.userid)
        # print('openidfefeeffeef',TestCase.openid)
        sjname = jsonpath.jsonpath(res.json(), '$..nikename')[0]
        assert '风清扬' == sjname

if __name__ == '__main__':
    pytest.main(['-sv','test_py2.py'])