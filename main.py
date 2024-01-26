from gevent.pywsgi import WSGIServer
from flask import Flask, request
from os import getenv, getcwd, listdir
from os.path import join
from subprocess import Popen
from psutil import process_iter

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


@app.route('/alive')
def alive():

    if not running():
        Popen('./hub-twtr')
        ret += ' started'
    else:
        ret += ' launched'

    print(ret)
    return ret


@app.route('/testdel')
def testdel():
    delete()
    return 'TEST DELETE'


def running(pname='hub-twtr'):
    return any(proc.name() == pname for proc in process_iter())


# test delete
def delete():

    from os import path as ospath
    from os import stat, listdir

    COUNT = 99  # 保留个数

    print('begin')
    dir = './data/whyyoutozhele'
    lts = [ospath.join(dir, file) for file in listdir(dir)]

    if lts and len(lts) > COUNT:

        try:
            # 获取每个文件的修改时间并组合成元组
            items = [(item, stat(item).st_mtime) for item in lts]
            print('-' * 20)
            print(items)

            # 根据修改时间排序
            sortedItems = sorted(items, key=lambda x: x[1], reverse=True)
            print('-' * 20)
            print(sortedItems)

            while len(sortedItems) > COUNT:
                item = sortedItems.pop()
                if item and len(item) > 0:
                    print('delete old item', item)

        except Exception as exc:
            print(exc)
    else:
        print('count:' + str(len(lts)))

if __name__ == '__main__':

    print('hello flask')
    # server = WSGIServer(('0.0.0.0', getenv("PORT", default=5000)), app)
    # server.serve_forever()
