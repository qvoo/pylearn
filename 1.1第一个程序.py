from urllib.request import urlopen, Request

url = "https://www.bilibili.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
req = Request(url, headers=headers)
response = urlopen(req)
print(response.read().decode('utf-8'))