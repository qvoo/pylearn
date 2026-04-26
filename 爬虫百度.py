import  requests

headers1={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}

url1=""

res=requests.get(url=url1,headers=headers1)

print(res.text)
with open("baidu.html","w",encoding='utf-8') as f:
    f.write(res.text)