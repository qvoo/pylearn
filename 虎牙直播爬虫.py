import  requests
import re
# 确定目标爬直播标题
# 确定url 确定位置
# 发起请求
headers1={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}

url1="https://www.huya.com/g/lol"

res=requests.get(url=url1,headers=headers1)
# print(res.text)

title_list=re.findall('"sIntroduction":"(.*?)"',res.text)
nick_list = re.findall('"sNick":"(.*?)"', res.text)
print(title_list)
print(nick_list)

# zip对齐打包：
# ("主播1", "标题1")
# ("主播2", "标题2")
# ("主播3", "标题3")
for nick, title in zip(nick_list, title_list):
    print(f"主播：{nick}   标题：{title}")