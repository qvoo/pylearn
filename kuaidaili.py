import requests
import re

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

url1 = "https://www.kuaidaili.com/free/"
res = requests.get(url=url1, headers=headers1)
res.encoding = "utf-8"  # 防止乱码

# 修正1：用 .*? 匹配<td>和IP之间的所有内容，无视class属性
# 匹配IP
ip_list = re.findall(r'<td.*?>(\d+\.\d+\.\d+\.\d+)</td>', res.text)
# 匹配端口
port_list = re.findall(r'<td.*?>(\d{2,5})</td>', res.text)

# 打印结果
print("IP列表:", ip_list)
print("端口列表:", port_list)

print("\n===== IP:端口 一一对应 =====")
for ip, port in zip(ip_list, port_list):
    print(f"{ip}:{port}")