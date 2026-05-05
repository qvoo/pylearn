from cv2 import moments
import requests
from lxml import etree
from openpyxl import Workbook
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

url = "https://datachart.500.com/ssq/history/newinc/history.php?start=24100&end=26050"

res = requests.get(url=url, headers=headers)
# print(res.text)  # 测试网页连接

wb=Workbook()
wb.remove(wb.active)
ws=wb.create_sheet("彩票大全")
ws.append(["期号","红球号码","蓝球号码","奖池奖金(元)","一等奖注数","一等奖奖金(元)","二等奖注数","二等奖奖金(元)","总投注额(元)","开奖日期"])


tree=etree.HTML(res.text)
tr_list=tree.xpath('//tr[@class="t_tr1"]')

for tr in tr_list:
    phases=tr.xpath('./td[1]/text()')#期号
    reballs=tr.xpath('./td[@class="t_cfont2"]/text()')#红球
    blueball=tr.xpath('./td[@class="t_cfont4"][1]/text()')#篮球
    sumoney=tr.xpath('./td[10]/text()')#奖池奖金
    firstmedol=tr.xpath('./td[11]/text() ')#一等奖zu
    firstmedolmoney=tr.xpath('./td[11]/text() | ./td[12]/text()')#一等奖
    secondmedol=tr.xpath('./td[13]/text()')#二等奖zu
    secondmedolmoney=tr.xpath('./td[13]/text() | ./td[14]/text()')#二等奖
    sumbuy=tr.xpath('./td[15]/text()')#总投注额(元
    datatime=tr.xpath('./td[16]/text()')#开奖日期
    
    reballs='/'.join(reballs)#用/拼接
    # money='/'.join(reballs)#用/拼接
    ws.append([phases[0],reballs[0],blueball[0],sumoney[0],firstmedol[0],firstmedolmoney[0],secondmedol[0],secondmedolmoney[0],sumbuy[0],datatime[0]])
    wb.save("彩票大全.xlsx")
    # print(phases[0],reballs,blueball[0],sumoney[0],firstmedol[0],secondmedol[0],sumbuy[0],datatime[0])


