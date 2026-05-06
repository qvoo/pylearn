import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "Cookie":" "
}

url = "https://my.4399.com/forums/mtags"

res = requests.get(url=url, headers=headers)
res.encoding='utf-8'
print(res.text)  # 测试网页连接


with open('4399.html','w',encoding='utf-8') as f:
    f.write(res.text)