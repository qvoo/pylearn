import re
str1="""<a href="https://www.baidu.com">百度</a>
<a href="https://www.bilibili.com">B站</a>"""

text = "价格：99元，销量：1285，评分：4.9"

text1 = "abc@qq.com，test@163.com"

# res=re.findall('<a>.*?</a>',str1)

# res=re.findall(r'href="(.*?)"',str1) # 匹配所有a标签

# res=re.findall(r'\d+',text)

div = """<div class="title">Python爬虫</div>
<div class="title">正则表达式</div>"""
res = re.findall(r'<div class="title">(.*?)</div>', div)

img="""<img src="/upload/1.jpg" />
<img src="/upload/2.png" />"""
res = re.findall(r'src="(.*?)"', img)

apple="""<li>苹果 <span>5999</span></li>
<li>小米 <span>3299</span></li>"""
res=re.findall(r'<li>(.*?)<span>(\d+)</span</li>',text)

id="""user?id=1001&name=zhangsan&id=2002"""
res = re.findall(r'id=(\d+)', text)


# res=re.findall(r'\w+@\w+.\w+',text1)

print(res)
#？代表非贪婪

'''
1. 基础元字符
. 匹配任意字符（除换行）
* 匹配 0 次或多次
+ 匹配 1 次或多次
? 非贪婪匹配 / 0 或 1 次
^ 开头
$ 结尾
| 或
() 分组提取
2. 量词（爬虫最常用）
*? 非贪婪（爬虫必用！）
+? 非贪婪
{m,n} 最少 m，最多 n
3. 字符集
\d 数字 [0-9]
\D 非数字
\w 字母数字下划线 [a-zA-Z0-9_]
\W 非单词字符
\s 空白（空格、换行、制表）
\S 非空白
[a-z] 小写字母
[^0-9] 排除数字'''