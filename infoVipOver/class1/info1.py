# 接口地址：https://openapiv5.ketangpai.com//UserApi/login
# 接口参数：{
#   "email": "2804555260@qq.com",
#   "password": "lan1314520",
#   "remember": "0",
#   "code": "",
#   "mobile": "",
#   "type": "login",
#   "reqtimestamp": 1654608178509
# }
# 请求方式：POST

import requests

url='https://openapiv5.ketangpai.com//UserApi/login'
data={
  "email": "2804555260@qq.com",
  "password": "lan1314520",
  "remember": "0",
  "code": "",
  "mobile": "",
  "type": "login",
  "reqtimestamp": 1654608178509
}
# def post(url, data=None, json=None, **kwargs):  到底选择data还是json  数据类型
# header头部 请求头 接口文档 登录完 token后面的接口 请求头 token
# 数据类型 要改变 在header改一下
# headers={'token':'gheighekhg'}
# headera={'content-type':'application/json'}
# data,json什么时候用  什么要改
res=requests.post(url,json=data)
print(res.json())