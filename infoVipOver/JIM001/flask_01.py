# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/home')
def first_flask():
    return 'hello flask'

#运行
if __name__ == '__main__':
    # 启动服务   实时更新
    # app.run('127.0.0.1','5555')
    app.run(debug=True)