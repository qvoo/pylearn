import  requests
import  re

headers = {
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}
url1="https://www.kuaidaili.com/free/"

res=requests.get(url=url1,headers=headers)


ip_list=re.findall('"ip": "(.*?)"',res.text)
port_list=re.findall('"port": "(.*?)"',res.text)

print(ip_list)
print(port_list)

for ip, port in zip(ip_list, port_list):
    print(f"{ip}|{port}")

