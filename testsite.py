# https://goods.starpets.gg/api/goods/fetch_by_id_list

authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NTE1NTY1NSwianRpIjoiMmI0YjA4YjQtNWI1OS00MTFjLWFkMzMtMjhmNzE5ZDgwMzA3IiwibmJmIjoxNjY1MTU1NjU1LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjIzNjQuNjE5OTk5OTk5ODYwMywiZXVyIjo3Ljc3MTU2MTE3MjM3NjA5NmUtMTZ9LCJiYWxhbmNlX29mZnNldCI6eyJ1c2QiOjAuMCwicnViIjowLjAsImV1ciI6MC4wfSwicmVmX2NvZGUiOiIiLCJhdmF0YXJfdXJsIjoiMyIsIm1haW5fbGFuZ3VhZ2UiOiJlbiIsIm1haW5fY3VycmVuY3kiOiJydWIiLCJtYWluX2NvdW50cnkiOiJSVSJ9LCJleHAiOjE2NjUyNDIwNTV9.uy7nHE7Zec_f0nVFI9VyuzYisrFnuBwhX74tgkP-ZpM"

last = []
items = []

import requests
import json
import time
# from webapp import keep_alive

f = open('data.txt', 'w')

def get_goods(page=None):
    lis = {"currency":"rub","filter":{"types":[{"type":"egg"},{"type":"pet"},{"type":"potion"},{"type":"transport"}]},"sort":{"popularity":"desc"},"page":page}
    r = requests.post('https://sales.starpets.gg/api/goods', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": authorization,
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, data = json.dumps(lis) )
    
    return r.json()

def get_all_goods():
    items = {'items' : []}
    for i in range(0, 20):
        for j in get_goods(i)['items']:
            # if j['rare'] == 'legendary' or j['rare'] == 'ultra_rare' or j['rare'] == 'rare':
            items['items'].append(j)
    global last
    last = items['items']
    return items

def get_products(itemid):
    payload = {"currency": "rub", "id": itemid}
    r = requests.post("https://sales.starpets.gg/api/best/products", json={"currency": "rub", "id": itemid},  cookies={'access-token':"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU2MzU1MywianRpIjoiYmQ3OGVlN2UtZjE4My00ZGE4LWFmZTgtOGE5MjgzNTE5NjRkIiwibmJmIjoxNjY0NTYzNTUzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjEyLjg2OTk5OTk5OTk5OTk0NCwiZXVyIjo3Ljc3MTU2MTE3MjM3NjA5NmUtMTZ9LCJiYWxhbmNlX29mZnNldCI6eyJ1c2QiOjAuMCwicnViIjowLjAsImV1ciI6MC4wfSwicmVmX2NvZGUiOiIiLCJhdmF0YXJfdXJsIjoiMyIsIm1haW5fbGFuZ3VhZ2UiOiJydSIsIm1haW5fY3VycmVuY3kiOiJydWIiLCJtYWluX2NvdW50cnkiOiJSVSJ9LCJleHAiOjE2NjQ2NDk5NTN9.Ns41dfx5uFoZIG-MD73CS-wSrkQ8fMDPFnS_sLeBV_4"})
    return r.json()

def get_inventory():
    r = requests.get('https://items.starpets.gg/api/items/?userId=6135f4014109475dac0b5ba2', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": authorization,
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  })
    
    inv = r.json()
    return inv



def get_info(lis):

    r = requests.post('https://trades.starpets.gg/api/goods/info', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": authorization,
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, data = json.dumps(lis) )
    return r.json()

def get_all_tradeable():
    lis = {"items":[],"currency":"rub"}
    goods2 = get_all_goods()['items']
    for i in goods2:
        lis['items'].append(i['goodId'])

    tab = []
    for i in get_info(lis):
        t = i
        # print(t)
        if 0 != t['category'] and t['available'] and t['locked'] != True and t['canBuy'] > 0 and float(t['purchasePrice']) > 2 and float(t['purchasePrice']) :
            
            
            for v in goods2:
                if v['goodId'] == i['goodId']:
                    for vv in v:
                        i[vv] = v[vv]
            tab.append(i)


    li = []
    for i in tab:
        if (float(i['price']) - float(i['purchasePrice'])) < 0 and 0 != t['category'] and t['available'] and t['locked'] != True and t['canBuy'] > 0 and float(t['purchasePrice']) > 2 and float(t['purchasePrice']):
            li.append(i)
    return li

def get_all_tradeable_inv():
    lis = {"items":[],"currency":"rub"}
    for i in get_inventory()['items']:
        lis['items'].append(i['goodId'])

    tab = []
    for i in get_info(lis):
        if i['canBuy'] > 0 and float(i['purchasePrice']) > 2:
            tab.append(i)

    return tab

def get_data():
    tab = get_all_tradeable()
    for i in tab:
        for v in last:
            if v['goodId'] == i['goodId']:
                i['price'] = v['price']
                i['name'] = v['name']

    return tab



def get_profit():
    tab = get_data()
    lis = []
    # wlist = []
    for i in tab:
        # if i['canBuy'] > 300 and float(i['purchasePrice']) > 2:
        #     wlist.append({'purchasePrice': i['purchasePrice'], 'price': i['price'], 'name': i['name']})
        if float(i['price']) < float(i['purchasePrice']) and float(i['purchasePrice']) > 2 and i['canBuy'] > 300:
            
            print(i['canBuy'], i['goodId'])
            lis.append({'goodId': i['goodId'], 'purchasePrice': i['purchasePrice'], 'name' : i['name'], 'canBuy' : i['canBuy'], 'price' : i['price'], 'id' : i['id']})
    # f = open('data.txt', 'w')
    # f.write(json.dumps(wlist))
    # f.close()
    return lis

def buy_product(ids):
    payload = {"items":ids}
    print(payload)
    r = requests.post("https://sales.starpets.gg/api/buy", headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": authorization,
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  },
  data= json.dumps(payload))
    print(r.json())
    return r.json()

def buy_products():
    profit = get_profit()

    for i in profit:
        for v in get_products(i['id'])['items']:
            print(v)
            if v['price'] < float(i['purchasePrice']) and i['canBuy'] > 0:
                i['canBuy'] -= 1
                buy_product([{'id' : v['id'], 'price' : v['price']}])

def trade():
    tab = {'user': [], 'site': [], 'currency': 'rub'}
    tradeables = get_all_tradeable_inv()

    for i in tradeables:
        temp = {'goodId': i['goodId'], 'price' : get_info({"items":[i['goodId']],"currency":"rub"})[0]['purchasePrice'] ,'uniqueIds': []}
        for v in get_inventory()['items']:
            if i['goodId'] == v['goodId']:
                temp['uniqueIds'].append(v['uniqueId'])
        tab['user'].append(temp)

    print(tab)
    r = requests.post('https://trades.starpets.gg/api/items/trade', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": authorization,
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, data = json.dumps(tab) )

    # print(r.json())
                

tries = 2303

# print(get_info({"items":["6308d9840aee69c340b58442"],"currency":"rub"}))
# f.write(json.dumps({'count' : 13297, 'items' : get_all_tradeable()}))
print(json.dumps({'count' : 13297, 'items' : get_all_tradeable()}))
# while True:
#     print(buy_products())
#     time.sleep(3)
# keep_alive()
# while True:
#     tries += 1
#     # print('Try: '+str(tries))
#     f.write(json.dumps(get_all_tradeable()))
#     time.sleep(5)