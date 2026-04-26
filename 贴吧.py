import  requests

headers1={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}

url1="https://tieba.baidu.com/c/f/frs/page_pc"

res=requests.get(url=url1,headers=headers1)

data=res.text
print(data)