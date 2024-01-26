from gevent.pywsgi import WSGIServer
from flask import Flask, request
from os import getenv, getcwd, listdir
from os.path import join

# 初始化 (固定格式)
app = Flask(__name__)
app.config["timeout"] = 3600

@app.route('/', methods = ['GET', 'POST'])
def hello():

    if request.method == "GET":
        # get通过request.args.get("param_name","")形式获取参数值

        dir = getcwd()
        files = [join(dir, file) for file in listdir(dir)]

        return {'code':200, 'message':'success', 'data':{"curdir":getcwd(),"files:":str(files)}}
    elif request.method == "POST":
        name = request.form["name"]
        value = request.form["value"]
        # post通过request.form["param_name"]形式获取参数值
        return {'code':200, 'message':'success', 'data':{}}

if __name__ == '__main__':

    print('hello flask')
    server = WSGIServer(('0.0.0.0', getenv("PORT", default=5000)), app)
    server.serve_forever()
