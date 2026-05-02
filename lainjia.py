import  requests
from lxml import etree

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}

url="https://cs.lianjia.com/zufang"

res=requests.get(url=url,headers=headers)

print(res.text)
tree=etree.HTML(res.text)
div_list=tree.xpath('//div[@class="content__list--item"]')

for div in div_list:
    title=div.xpath('.//div[@class="content__list--item--main"]/p/a/text()')
    title=''.join(title).strip()
    print(title)
