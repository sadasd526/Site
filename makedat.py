# import json

# f = open('data.txt', 'r')
# data = f.read()
# f.close()

# data = json.loads(data)


# text = ""

# for i in data:
#     # if i['canBuy'] > 10:
#     text = text + f"{i['name']} (if less then / если меньше) {i['price']} ₽ \n "

# f = open('data.data.txt', 'w', encoding="utf-8")
# f.write(text)
# print(text)

authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NTA2NjU3OSwianRpIjoiNDMzYTU3NTEtMjU5Zi00MTU4LTkxZTktYjk2YjllZDEzM2M5IiwibmJmIjoxNjY1MDY2NTc5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjIyNzguMTE5OTk5OTk5ODMzLCJldXIiOjcuNzcxNTYxMTcyMzc2MDk2ZS0xNn0sImJhbGFuY2Vfb2Zmc2V0Ijp7InVzZCI6MC4wLCJydWIiOjAuMCwiZXVyIjowLjB9LCJyZWZfY29kZSI6IiIsImF2YXRhcl91cmwiOiIzIiwibWFpbl9sYW5ndWFnZSI6ImVuIiwibWFpbl9jdXJyZW5jeSI6InJ1YiIsIm1haW5fY291bnRyeSI6IlJVIn0sImV4cCI6MTY2NTE1Mjk3OX0.EO1JSiccHiZU7Q5aJ9UM2CLNd6_wsGuXfyFSxrSoIYE"
import requests, json

def get_info(lis):

    r = requests.post('https://trades.starpets.gg/api/goods/info', json = lis )
    return r.text

a = input("Pet: ")
print({"items":[a],"currency":"rub"})

print(get_info({"items":[str(a)],"currency":"rub"}))