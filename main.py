import requests

url="https://uapis.cn/api/v1/game/epic-free"

res=requests.get(url)

data=(res.json())

# with open("weather.txt","w") as f:
#     f.write(data)

print(data)