from openpyxl import Workbook

#创建一个新的Excel工作簿
wb = Workbook()

#获取默认的活动工作表
ws = wb.active
#设置工作表标题
ws.title = "单表操作"

#写入一些是数据到工作表中
ws.append(["姓名", "年龄", "性别"])
ws.append(["张三", 25, "男"])
ws.append(["李四", 30, "女"])


#保存工作簿到文件中
wb.save("my_excel_file.xlsx")