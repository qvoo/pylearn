

import requests
import json

headers = {
    'Origin': 'http://fiddle.jshell.net',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'https://www.bkchina.cn/product/hamburg.html',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

url="https://www.bkchina.cn/product/productList"
data = {
    "type": "ham"
}

response = requests.post(url=url, headers=headers, data=data)
jsonscrect=json.loads(response.text)
# print(jsonscrect)

for key   in jsonscrect.keys():
    data=jsonscrect[key]
    for i in data:
        # print(i["FName"]i['FNameEng'])
        # namelist=i["FName"]
        # ENnamelist=i["FNameEng"]
        # for chname,enname in ENnamelist:
        print(i["FName"],i["FNameEng"])


