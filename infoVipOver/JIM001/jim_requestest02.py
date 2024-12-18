import requests
import unittest
import json
import jsonpath
import pytest


class TestCase01:
    token = None
    # 响应 token号会变 1.响应回来的token号提取出来 保存在变量。
    # 2.放在一个地方 都可以拿到token  类变量  其他方式 2.session  3.返回值
    def testToken(self):
        #获取token接口，获取token值
        response01 = requests.post(
            url='https://tmallapi.bluemoon.com.cn/ec-oms/ebp-live/admin/lrm/base/getInfoByToken?testPsw=Er78s1hcT4Tyoaj2',
            json={
                "token":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4MTAwMzQzNSIsImNsaWVudFR5cGUiOiJwYyIsImFwcFR5cGUiOiJwb3J0YWwiLCJleHAiOjE3MzIyNzc5OTMsImlhdCI6MTczMTYyOTM1OH0.s8GjOtVuXi1ZosAPccK96UOrg_iiXqfC2PRn3OFLUwI"
            },
            headers={
                'Content-Type': 'application/json'
            })
        # self.assertEqual(response01.status_code, 400, '返回状态错误，不为200')
        print(response01.json())
        TestCase01.token= jsonpath.jsonpath(response01.json(),'$..authToken')[0]   #获取token进行关联使用
        print( TestCase01.token,type(TestCase01.token))
        tokenmsg = jsonpath.jsonpath(response01.json(), '$..responseMsg')[0]          #断言
        assert '认证成功' == tokenmsg

    def testSearch(self):
        # 分页获取店铺商品列表接口，post 请求
        response = requests.post(
            url='https://tmallapi.bluemoon.com.cn/ec-oms/ebp-live/admin/lrm/product/productInfoList?testPsw=Er78s1hcT4Tyoaj2',
            json={
                "shopCodeList": ["10020"],
                "productKeyWord": "3319227971696460648",
                "pageNum": 1,
                "pageSize": 50
                },
            #数据关联
            headers={
                "Authorization": TestCase01.token
            }
        )
        # 断言
        # self.assertEqual(response.status_code,200,'返回状态错误，不为200')
        Searchmsg = jsonpath.jsonpath(response.json(), '$..responseMsg')[0]
        assert '请求成功' == Searchmsg
        print(response.json())

if __name__ == '__main__':
    pytest.main(['-sv','jim_requestest02.py'])
