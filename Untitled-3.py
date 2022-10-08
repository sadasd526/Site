authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDgyNDk2MCwianRpIjoiYjc1NjIwODUtYjQ2Ni00M2QwLWI3MTAtZTM2NDg4MDM4NzMxIiwibmJmIjoxNjY0ODI0OTYwLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjcwOS42OTk5OTk5OTk4ODU2LCJldXIiOjcuNzcxNTYxMTcyMzc2MDk2ZS0xNn0sImJhbGFuY2Vfb2Zmc2V0Ijp7InVzZCI6MC4wLCJydWIiOjAuMCwiZXVyIjowLjB9LCJyZWZfY29kZSI6IiIsImF2YXRhcl91cmwiOiIzIiwibWFpbl9sYW5ndWFnZSI6ImVuIiwibWFpbl9jdXJyZW5jeSI6InJ1YiIsIm1haW5fY291bnRyeSI6IlJVIn0sImV4cCI6MTY2NDkxMTM2MH0.C6Ph9PJmcoBNAyVAOCnSjs6KkJPxVELQvfTITnePkZs"

last = []
items = []

import requests
import json
import time

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

def withdraw(lis):
    r = requests.post('https://sales.starpets.gg/api/withdraw_from_sale', headers = {
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


def get_all_tradeable_inv():
    lis = {"items":[],"currency":"rub"}
    for i in get_inventory()['items']:
        lis['items'].append(i['goodId'])

    tab = []
    for i in get_info(lis):
        if i['canBuy'] > 0:
            tab.append(i)

    return tab

def trade():
    inv = get_all_tradeable_inv()


    for i in inv:
        uniq = []
        for v in get_inventory()['items']:
            if v['goodId'] == i['goodId']:
                uniq.append(v['uniqueId'])
        goodId = i['goodId']
        purchasePrice = get_info({"items":[i['goodId']],"currency":"rub"})[0]['purchasePrice']
        lis = {"items":{"user":[{"goodId": goodId ,"price":  float(purchasePrice),"uniqueIds":uniq}],"site":[]},"currency":"rub"}
        

        time.sleep(0.1)

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
    }, data = json.dumps(lis) )

        # №https://auth.starpets.gg/api/user/profile

    r = requests.get('https://auth.starpets.gg/api/user/profile', headers = {
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
    try:
        print(r.json()['balance']['rub']+"₽")
    except:
        pass

lis = []
for i in get_inventory()['items']:
    # print(i)
    # if i['onSale'] == True:
    #     lis.append(i['saleId'])

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
  }, data = json.dumps({ 'product' : get_info({"items": [i['goodId']],"currency":"rub"})[0]['id'] }) )

    print(r.json())
    print(json.dumps({ 'product' : get_info({"items": [i['goodId']],"currency":"rub"})[0]['id'] }))


withdraw(lis)

# while True:
#     trade()
#     time.sleep(1)