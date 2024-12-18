# 专门封装getpost请求方式
import requests


class HttpClient:
    # 只要用post,get请求方式 就创建会话
    def __init__(self):
        self.session=requests.Session()

    # 发送请求  请求方式，接口地址 ，接口参数类型，接口数据，头部信息,q其他的信息
    # 判断 你要发送的是请求方式 如果get post
    # post请求参数类型 json data
    def send_request(self,method,url,param_type=None,data=None,headers=None,**kwargs):
        # 请求方式转成大写
        method=method.upper()
        # print(method)
        param_type=param_type.upper()
        if method=='GET':
            response=self.session.request(method=method,url=url,params=data,**kwargs)
        elif method=='POST':
            if param_type=='FORM':
                response=self.session.request(method=method,url=url,data=data,**kwargs)
            else:
                response=self.session.request(method=method,url=url,json=data,**kwargs)
        elif method=='DELETE':
            if param_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif method=='PUT':
            if param_type == 'FORM':
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            raise ValueError
        return response

    # 魔法方法  send_request 实例化类.方法
    # 实例化类 HttpClient().send_request()
    # a=HttpClient()
    def __call__(self, method,url,param_type,data=None,headers=None,**kwargs):
        return self.send_request(method,url,param_type,data,headers=None,**kwargs)

    def close_session(self):
        self.session.close()
