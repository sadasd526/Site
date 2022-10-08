

from asyncore import read
from importlib.resources import path
import os
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

import json
from flask import Flask, render_template, redirect, url_for, request, jsonify, send_file, send_from_directory
# from PIL import Image
from flask_cors import CORS, cross_origin
# from flask_cors import CORS
import base64, time
import openpyxl
import sys
from io import BytesIO
import threading
import requests
from bs4 import BeautifulSoup
from testsite import get_all_tradeable

# a = Thread(target=run)
# a.start()

f = open("index.html", "r", encoding='utf-8')
index = f.read()
f.close()


template_dir = os.path.abspath('')
app = Flask(__name__, template_folder=template_dir)
CORS(app, support_credentials=True)

data = json.loads(open('Python\data.json').read())

@app.route('/')
def main():
    return render_template('index.html')  #redirect('http://127.0.0.1:5500/')

@app.route('/ru')
def main1():
    return render_template('index.html')  #redirect('http://127.0.0.1:5500/')

@app.route('/trade')
def trade11():
    return render_template('trade.html')

@app.route('/css/<path:path>')
def css(path):
    return send_file("css/"+path)

@app.route('/js/<path:path>')
def js(path):
    f = open("js/"+path, "r", encoding='utf-8')
    js1 = f.read()
    f.close()
    return js1

@app.route('/fonts/<path:path>')
def fonts(path):
    return send_from_directory('fonts', path)
def js(path):
    f = open("js/"+path, "r", encoding='utf-8')
    js1 = f.read()
    f.close()
    return js1

@app.route('/api/inventory')
def my():
    return json.loads(open('Python\my.json').read())

@app.route('/api/profile')
def profile():
    return json.loads(open('Python\data.json').read())

@app.route('/inventory')
def profile1():
    return render_template('inventory.html')
@app.route('/img/<imgn>')
def img(imgn):
    return redirect('https://starpets.gg/img/' + imgn)

@app.route('/goods/<path:mm>')
def goods(mm):
    print(mm)
    a = request.args.get('id')
    print(a)
    return redirect('https://goods.starpets.gg/api/assets/fetch?id=' + a)

@app.route('/api/user/get-country')
def gc():
    print()
    j = requests.get("https://geolocation-db.com/json/' + request.remote_addr + '&position=true").json()

    return '{"country": "'+j['country_code']+'", "city": "' + j['city'] + '"}'

    #https://127.0.0.1:8000/api/goods


#/api/best/products

@app.route('/api/best/products')
def best():
    return BeautifulSoup(open('items.json').read(), "html5lib")
str2 = json.dumps({'count' : 13297, 'items' : get_all_tradeable()})


@app.route('/api/goods', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def goods1():
    data = json.loads(request.data.decode('UTF-8'))
    print(data)
    if not 'page' in data.keys():
        return json.dumps({'count' : 13297, 'items' : get_all_tradeable()})
    return ''



def f():
    while True:
        str2 = json.dumps({'count' : 13297, 'items' : get_all_tradeable()})
        time.sleep(5)




if __name__ == '__main__':
    try:
        y = threading.Thread(target = f)
        y.daemon = True
        y.start()
        app.run(port=5502, host='0.0.0.0')
    except KeyboardInterrupt:
        sys.exit(1)

    

# while True:
#     json.dumps({'count' : 13297, 'items' : get_all_tradeable()})
#     time.sleep(5)