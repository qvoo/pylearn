import requests
import json
import  requests
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
         "Content-Type": "application/json" }



url="https://join.qq.com/api/v1/position/searchPosition"
payload = {
    "timestamp": "1777225570946"
}

response = requests.post(url=url, headers=headers, json=payload)#这里是json！！！，找了半天我日

json_data = response.json()

print("顶层键：", json_data.keys())
print("status状态：", json_data["status"])


position_list = json_data["data"]["positionList"]
print(position_list)

# 遍历输出所有岗位
print("\n==== 遍历所有岗位 ====")
for job in position_list:
    print("-" * 50)
    print("岗位名称：", job["positionTitle"])
    print("工作城市：", job["workCities"])
    print("事业群：", job["bgs"])

#
# import requests
# import json
#
# # 请求头
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
#     "Content-Type": "application/json"  # 必须加！
# }
#
# # 接口地址
# url = "https://join.qq.com/api/v1/position/searchPosition?timestamp=1777225570946"
#
# # 请求体（必须是JSON格式）
# payload = {
#     "timestamp": "1777225570946"
# }
#
# # 重点：必须用 POST + json=payload
# response = requests.post(url, headers=headers, json=payload)
#
# # 解析数据
# json_data = response.json()
#
# print("顶层键：", json_data.keys())
# print("status状态：", json_data["status"])
#
# # 取出岗位列表
# position_list = json_data["data"]["positionList"]
#
# # 遍历输出所有岗位
# print("\n==== 遍历所有岗位 ====")
# for job in position_list:
#     print("-" * 50)
#     print("岗位名称：", job["positionTitle"])
#     print("工作城市：", job["workCities"])
#     print("事业群：", job["bgs"])