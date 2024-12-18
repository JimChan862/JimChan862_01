# flask
# 1.导包  from flask import Flask
# 2.实例化 Flask
# 3.创建路由
"""
@app.route('/home')
def first_flask():
    return 'hello flask'
"""
# @app.route(页面路径，请求方式)
# 函数体
# 运行app.run()  实时更新代码 debug=True app.run(debug=True)
from pathlib import Path

import pytest
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

# @app.route('/home')
# def first_flask():
#     return 'hello flask'

# 没写请求方式 默认get
# @app.route('/api/login')
# def first_flask():
#     return 'hello flask'

# 改成post请求
# @app.route('/api/login',methods=['post'])
# def first_flask():
#     return 'hello flask'

# @app.route('/api/login',methods=['post','get'])
# def first_flask():
#     return 'hello flask'

# 里面 函数传参数进来  接受 requests
# @app.route('/api/login', methods=['post', 'get'])
# def login():
#     print(request.get_json())
#     print(request.get_data())
# 传参

# 题目：
# 传参数  登录  传过来的数据 是admin和123456 认为登录成功 否则认为登录失败
# 1.先要获得postman里面传了什么输数据  data
# 2.拿到对应的数据 去判断
# 3.判断传过来的值是admin和123456 登录成功  否则登录失败
#
# @app.route('/api/login', methods=['post', 'get'])
# def login():
#     data=request.get_json()
#     # print(data)
#     username=data['username']
#     password=data['password']
#     if username=='admin' and password=='123456':
#         return '登录成功'
#     else:
#         return '登录失败'

# 如果说 登录 需求 用户和密码的长度 不能小于2 大于18  我又应该怎么写  再来一个if
# 这个if在加到上一层  符合日常思维
# @app.route('/api/login', methods=['post', 'get'])
# def login():
#     data=request.get_json()
#     # print(data)
#     username=data['username']
#     password=data['password']
#     if (2<len(username)<18) and (2<len(password)<18):
#         if username=='admin' and password=='123456':
#             return '登录成功'
#         else:
#             return '登录失败'
#     else:
#         return '用户名或密码不符合要求'


# 返回数据的 返回的是登录成功 登录失败
# 返回真实点 数据
# @app.route('/api/login', methods=['post', 'get'])
# def login():
#     data=request.get_json()
#     # print(data)
#     username=data['username']
#     password=data['password']
#     if (2<len(username)<18) and (2<len(password)<18):
#         if username=='admin' and password=='123456':
#             return jsonify({"adress": { "city": "changsha" }, "httpstatus": 200, "info": { "age": 18, "name": "admin" }, "msg": "success", "token": "23657DGYUSGD126731638712GE18271H" })
#         else:
#             return jsonify({ "code": "001", "msg": "用户名或密码错误" })
#     else:
#         return '用户名或密码不符合要求'

# 百度 返回来的数据格式 返回来的是html页面
# @app.route('/api/login', methods=['post', 'get'])
# def home():
#     return '''
#     请输入用户名：<input type='text' name='username'>
#     请输入密码：<input type='password' name='password'>
#     '''

# 直接返回一个html页面  文件夹的名字不能错  而且要跟运行文件同层级 否则会报错
# @app.route('/api/login', methods=['post', 'get'])
# def home():
#     return render_template('index2.html')

# 页面中显示数据  html 页面中要拿到传过来的数据 html 循环数据  projects
# @app.route('/api/login', methods=['post', 'get'])
# def home():
#     projects=['projent1','project2']
#     return render_template('index3.html',projects=projects)

# 练习  扩展
# 通过在页面上面点击连接 能自动触发到我的项目 触发百度启动  文件夹的名称
# app.root_path 根目录 class4
# 这个函数我想要实现的事情是拿到workspace文件中的目录文件和文件名称
@app.route('/api/login', methods=['post', 'get'])
def home():
    workspace=Path(app.root_path)/'workspace'
    projects=[projects.name for projects in workspace.iterdir()]
    return render_template('index3.html',projects=projects)

# 拿到文件名称之后 点击文件 点击request就运行百度  点击selenium就运行京东
# 在页面上面 点击request 跳转到 build 这个路由里面就用pytest触发百度执行 京东执行
@app.route('/build')
def build():
    project_name=request.args.get('project')
    pytest.main([f'workspace/{project_name}'])
    return "构建成功"


# 运行
if __name__ == '__main__':
    # 启动服务   实时更新
    # app.run('127.0.0.1','5555')
    app.run(debug=True)

# 作业是：使用flask创建数据