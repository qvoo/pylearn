import  requests
from lxml import etree


""""

//div[@class="zu-itemmod clearfix"] 获取每一条数据


"""

# headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "Referer": "https://cs.zu.anjuke.com/",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

url="https://cs.zu.anjuke.com/fangyuan/yuelu/"

res=requests.get(url=url,headers=headers)

res.encoding = 'utf-8'  # 或者用 res.apparent_encoding 自动识别
tree = etree.HTML(res.text)

div_list=tree.xpath('//div[@class="zu-itemmod clearfix"]')

# print(div_list)

#lxml局部遍历的坑 循环内 在每个解析元素前加一个. 固定写法
for div in div_list:
    # print(div)
    #/text() 获取文本内容
    title=div.xpath('.//div[@class="zu-info"]/h3/a/b/text()')#匹配div下的元素 既是第一个也是最后一个
    address=div.xpath('.//address[@class="details-item tag"]//text()')
    price=div.xpath('.//div[@class="zu-side"]//text()')

    #  //是获取该标签下全部的内容
    info=div.xpath('.//p[@class="details-item tag"]//text()')
    info=''.join(info).strip() #join方法把列表拼接成字符串 取出首尾特殊字符
    address=''.join(address).replace('\n','') .replace(' ','')
    price=''.join(price).replace('\n','') .replace(' ','')
    print(title)
    print(info)
    print(address)
    print(price,'\n')