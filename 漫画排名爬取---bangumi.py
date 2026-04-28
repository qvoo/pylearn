"""
http://bangumi.tv/book/browser/?sort=rank&page=1
爬 排行 标题 评分 评价人数

确定url
发情请求 获取响应
解析响应内容数据

一页有24条数据 然后循环每条数据取出字段 要知道每条字段的规则
去元素页面看层级

ctrl F 调用出查找
ul#browserItemList>li  写出每层规则
爬10页
"""

from bs4 import BeautifulSoup
import  requests
nums=1
for i in range(1,11):
    url1=f"http://bangumi.tv/book/browser/?sort=rank&page={i}"
    headers1={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}

    res=requests.get(url=url1,headers=headers1)
    # 发生乱码了  转换编码utf-8
    res.encoding='utf-8'

    # print(res.text)

    soup=BeautifulSoup(res.text,'html.parser')

    comic_list=soup.select('ul#browserItemList>li')

    for li in comic_list:
        # print("漫画名字：",li.select('div.inner>h3>a')[0].text) #.text 才会只拿文字
        # print("原名：",li.select('div.inner>h3>small')[0].text)
        # print("漫画排名：",li.select('div.inner>span')[0].text)
        # print("信息：",li.select('div.inner>p.info.tip')[0].text)


        title=li.select('div.inner>h3>a')
        title1=title[0].text
        print(title1)
        info=li.select('div.inner>p.info.tip')
        info1=info[0].text
        info1=info1.replace(' ','').replace('\n','')#把空格换成空 把换行换成空
        print(info1)
        print("评分：",li.select('div.inner>p.rateInfo>small')[0].text)
        print("评分人数：",li.select('div.inner>p.rateInfo>span.tip_j')[0].text,'\n')
        print(f"当前爬了{nums}个漫画数据")
        nums+=1
