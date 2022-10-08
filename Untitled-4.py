import requests
import json
import time, asyncio
from threading import Thread
itemid = 13134
purchasePrice = 2.23

def get_info(lis):

    r = requests.post('https://trades.starpets.gg/api/goods/info', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY1NzAwNywianRpIjoiNzUzODc3YzktYzk1Ni00YWIwLTlmMTgtYjdlMzg0ZTAxOTIwIiwibmJmIjoxNjY0NjU3MDA3LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjE1MC44Njk5OTk5OTk5OTUyLCJldXIiOjcuNzcxNTYxMTcyMzc2MDk2ZS0xNn0sImJhbGFuY2Vfb2Zmc2V0Ijp7InVzZCI6MC4wLCJydWIiOjAuMCwiZXVyIjowLjB9LCJyZWZfY29kZSI6IiIsImF2YXRhcl91cmwiOiIzIiwibWFpbl9sYW5ndWFnZSI6InJ1IiwibWFpbl9jdXJyZW5jeSI6InJ1YiIsIm1haW5fY291bnRyeSI6IlJVIn0sImV4cCI6MTY2NDc0MzQwN30.Tt1czmCIqyayI_3Vq4iwAJGjzL34UV6AOurIJQ04gQA",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, data = json.dumps(lis) )
    return r.json()

def get_inventory():
    r = requests.get('https://items.starpets.gg/api/items/?userId=6135f4014109475dac0b5ba2', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY1NzAwNywianRpIjoiNzUzODc3YzktYzk1Ni00YWIwLTlmMTgtYjdlMzg0ZTAxOTIwIiwibmJmIjoxNjY0NjU3MDA3LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjE1MC44Njk5OTk5OTk5OTUyLCJldXIiOjcuNzcxNTYxMTcyMzc2MDk2ZS0xNn0sImJhbGFuY2Vfb2Zmc2V0Ijp7InVzZCI6MC4wLCJydWIiOjAuMCwiZXVyIjowLjB9LCJyZWZfY29kZSI6IiIsImF2YXRhcl91cmwiOiIzIiwibWFpbl9sYW5ndWFnZSI6InJ1IiwibWFpbl9jdXJyZW5jeSI6InJ1YiIsIm1haW5fY291bnRyeSI6IlJVIn0sImV4cCI6MTY2NDc0MzQwN30.Tt1czmCIqyayI_3Vq4iwAJGjzL34UV6AOurIJQ04gQA",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  })
    
    inv = r.json()

    lis = {}
    lis['items'] = []
    lis['currency'] = 'rub'

    for i in inv['items']:
        lis['items'].append(i['goodId'])
    

    r = requests.post('https://trades.starpets.gg/api/goods/info', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY1NzAwNywianRpIjoiNzUzODc3YzktYzk1Ni00YWIwLTlmMTgtYjdlMzg0ZTAxOTIwIiwibmJmIjoxNjY0NjU3MDA3LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjE1MC44Njk5OTk5OTk5OTUyLCJldXIiOjcuNzcxNTYxMTcyMzc2MDk2ZS0xNn0sImJhbGFuY2Vfb2Zmc2V0Ijp7InVzZCI6MC4wLCJydWIiOjAuMCwiZXVyIjowLjB9LCJyZWZfY29kZSI6IiIsImF2YXRhcl91cmwiOiIzIiwibWFpbl9sYW5ndWFnZSI6InJ1IiwibWFpbl9jdXJyZW5jeSI6InJ1YiIsIm1haW5fY291bnRyeSI6IlJVIn0sImV4cCI6MTY2NDc0MzQwN30.Tt1czmCIqyayI_3Vq4iwAJGjzL34UV6AOurIJQ04gQA",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, data = json.dumps(lis) )

    inv2 = r.json()

    for v in inv['items']:
        for i in inv2:
            if i['goodId'] == v['goodId']:
                v['id'] = i['id']
                if i['id'] == itemid:
                    global purchasePrice
                    purchasePrice = float(i['purchasePrice'])
    return inv

def trade():
    inv = get_inventory()
    id1 = ""
    trad = []
    uniq = []
    goodId = ""
    for i in inv['items']:
        uniq.append(i['goodId'])
        # if get_info(i['goodId']) == itemid:
        #     uniq.append(i['uniqueId'])
        #     trad.append(i)
        #     goodId = i['goodId']

    # {"goodId": goodId ,"price":  purchasePrice,"uniqueIds":uniq}
    uniq = list(dict.fromkeys(uniq))
    # print(uniq)

    # print(get_info({"items":uniq,"currency":"rub"}))

    tab = get_info({"items":uniq,"currency":"rub"})
    tab2 = []
    
    for i in tab:
        if i['canBuy'] > 0:
            tab2.append(i)
    print(tab2)


    items = []

    for v in tab2:
        temp = {'goodId': v['goodId'], 'price': v['purchasePrice'], 'uniqueIds': []}
        for i in inv['items']: 
            if v['goodId'] == i['goodId']:
                temp['uniqueIds'].append(i['uniqueId'])

        items.append(temp)
          
    print(items)
    lis = {'user': items, 'site': [], 'currency': 'rub'}

    r = requests.post('https://trades.starpets.gg/api/items/trade', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY1NzAwNywianRpIjoiNzUzODc3YzktYzk1Ni00YWIwLTlmMTgtYjdlMzg0ZTAxOTIwIiwibmJmIjoxNjY0NjU3MDA3LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjE1MC44Njk5OTk5OTk5OTUyLCJldXIiOjcuNzcxNTYxMTcyMzc2MDk2ZS0xNn0sImJhbGFuY2Vfb2Zmc2V0Ijp7InVzZCI6MC4wLCJydWIiOjAuMCwiZXVyIjowLjB9LCJyZWZfY29kZSI6IiIsImF2YXRhcl91cmwiOiIzIiwibWFpbl9sYW5ndWFnZSI6InJ1IiwibWFpbl9jdXJyZW5jeSI6InJ1YiIsIm1haW5fY291bnRyeSI6IlJVIn0sImV4cCI6MTY2NDc0MzQwN30.Tt1czmCIqyayI_3Vq4iwAJGjzL34UV6AOurIJQ04gQA",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, json = lis )

    print(r.json())



#     inventory = ''
#     # ignore this "{\"items\":{\"user\":[{\"goodId\":\"62ae1a5a277940d7b71389b1\",\"price\":1.7,\"uniqueIds\":[\"633534b747fd6ff683632e4b\"]}],\"site\":[]},\"currency\":\"rub\"}"

#     # get inventory

# while True:
trade()
    # time.sleep(1)
    # {'items': 
    # {'user': [
    #     {'goodId': '625dc50864e09e5993c307ba', 'price': 2.77, 'uniqueIds': ['6314d9eb20c1b6a4825d90a6']}, 
    #     {'goodId': '6328dc1be7ab753508206c9e', 'price': 2.63, 'uniqueIds': ['632eacc3470f6b0758b5d659']}
    #     ], 'site': []}, 'currency': 'rub'}