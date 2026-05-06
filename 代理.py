import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 1. 获取代理IP
proxy_url = "https://proxy.scdn.io/api/get_proxy.php?protocol=https&count=1"
proxy_res = requests.get(url=proxy_url, headers=headers, timeout=10)
print("代理API返回：", proxy_res.text)

# 2. 解析代理IP（关键修复）
proxy_data = proxy_res.json()
proxy_list = proxy_data["data"]["proxies"]
# 取列表里的第一个代理IP
proxy = proxy_list[0]
print("获取到的代理IP：", proxy)

# 3. 构造代理字典（修复格式）
proxies = {
    "http": f"http://{proxy}",
    "https": f"https://{proxy}"
}

# 4. 访问目标地址（修复参数名porxies→proxies）
url ="https://kns.cnki.net/kns8s/defaultresult/index?crossids=YSTT4HG0%2CLSTPFY1C%2CJUP3MUPD%2CMPMFIG1A%2CWQ0UVIAA%2CBLZOG7CK%2CPWFIRAGL%2CEMRPGLPA%2CNLBO1Z6R%2CNN3FJMUV&korder=SU&kw=%E8%AE%A1%E7%AE%97%E6%9C%BA"
res = requests.get(url=url, headers=headers, proxies=proxies, timeout=15)
print("请求状态码：", res.status_code)
print("响应内容（前300字）：", res.text[:300])