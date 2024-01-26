from gevent.pywsgi import WSGIServer
from flask import Flask, request, send_from_directory
from util.path import curDir
from werkzeug.datastructures import ImmutableMultiDict

# 初始化 (固定格式)
app = Flask(__name__)
app.config["timeout"] = 3600

@app.route('/hello', methods = ['GET', 'POST'])
def hello():

    rAddr = request.remote_addr

    if request.method == "GET":
        # get通过request.args.get("param_name","")形式获取参数值
        return {'code':200, 'message':'success', 'data':{}}
    elif request.method == "POST":
        name = request.form["name"]
        value = request.form["value"]
        # post通过request.form["param_name"]形式获取参数值
        return {'code':200, 'message':'success', 'data':{}}

@app.route('/mobile/<path:upath>/')
def mobile(upath):
    return 'path:%s' % upath

@app.route('/files/home/<path:fileName>', methods = ['GET', 'POST'])
def file(fileName):

    return fileName
    # return send_from_directory(curDir(),fileName)

@app.route('/files', methods = ['GET', 'POST'])
def files():

    pth = request.args.get("path","")
    return pth

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host=127.0.0.1, port=5000, debug=false
    # app.run(host='127.0.0.1', port=4000)
    # app.run(host='0.0.0.0', port=4000) # 0.0.0.0 获取的本机地址

    print('hello flask')
    server = WSGIServer(('0.0.0.0', 3701), app)
    server.serve_forever()