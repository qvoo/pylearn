import  requests

from lxml import etree

import lxml .html as etre
headers1={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}

url1="https://spiderbuf.cn/challenge/scraping-images-from-web"

html=requests.get(url=url1,headers=headers1).text
print(html)
f=open('05.tml','w',encoding='utf-8')f
f.write(html)
f.close()

root=etree.HTML(html)
