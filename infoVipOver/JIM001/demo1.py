# 这节课：重点
# 1.requests做接口测试
# 2.jsonpath的使用
# 3.接口关联

# 1.安装
import json

import jsonpath
import requests

# get请求
# 接口
# 接口步骤：
# 接口地址
# 接口参数
# 请求方式
# 响应内容

# # 百度
url='http://www.baidu.com'
res=requests.get(url)
# 打印响应回来的内容  二进制文本内容
print(res.content)
# 文本内容
print(res.text)
# 接口地址
print(res.url)
# cookie
print(res.cookies)
# 打印头部内容
print(res.headers)
# 打印json
# print(res.json())