import requests
import unittest
import json
import jsonpath

class Case01(unittest.TestCase):
    def test_case01(self):
        # 分页获取店铺商品列表接口，post请求
        response = requests.post(
            url='https://tmallapi.bluemoon.com.cn/ec-oms/ebp-live/admin/lrm/product/productInfoList?testPsw=Er78s1hcT4Tyoaj2',
            json={
                "shopCodeList": ["10020"],
                "productKeyWord": "3319227971696460648",
                "pageNum": 1,
                "pageSize": 50
                },
            # 如果需要用data的话，字典改成的字符串  json.dumps(data)
            # data=json.dumps({
            #     "shopCodeList": ["10020"],"productKeyWord": "3319227971696460648",
            #     "pageNum": 1,"pageSize": 50
            #     }),
            headers={
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4MTAwMzQzNSIsImNsaWVudFR5cGUiOiJwYyIsImFwcFR5cGUiOiJwb3J0YWwiLCJleHAiOjE3MzIyNzc5OTMsImlhdCI6MTczMTYyOTM1OH0.s8GjOtVuXi1ZosAPccK96UOrg_iiXqfC2PRn3OFLUwI',
                'Content-Type': 'application/json'
            })
        self.assertEqual(response.status_code,200,'返回状态错误，不为200')
        print(response.text)
        Case01.PlatProductCode= jsonpath.jsonpath(response.json(),'$..platProductCode')[0]
        print( Case01.PlatProductCode)


if __name__ == '__main__':
    unittest.main()