# -*- coding: utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx') # 创建一个excel文件
worksheet = workbook.add_worksheet()    # 创建一个工作表对象

worksheet.set_column('A:A',20)      # 设定第一列(A)宽度为20像素
bold = workbook.add_format({'bold':True})   # 定义一个加粗的格式对象

worksheet.write('A1','Hello')       # A1单元格写入'Hello'
worksheet.write('A2','World',bold)  # A2单元格写入'World'，并引用加粗格式对象bold
worksheet.write('B2',u'中文内容',bold)

worksheet.write(0,0,32)     # 用行列表示法写入数据'32'与'35.5'
worksheet.write(3,0,35.5)   # 等价于'A3'位置
worksheet.write(4,0,'=SUM(A3:A4)')  # 求A3:A4的和

worksheet.insert_image('B5','img/python-logo.png')  # 在B5单元格插入图片
workbook.close()

# Workbood类

# add_worksheet方法
'''
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet1 = workbook.add_worksheet()   # Sheet1
worksheet1 = workbook.add_worksheet("Foglio2")  # Foglio2
worksheet1 = workbook.add_worksheet("Data")     # Data
worksheet1 = workbook.add_worksheet()   # Sheet1
'''

# add_format方法
'''
bold = workbook.add_format()
bold.set_bold()
'''

# add_chart 创建图表对象

# http://xlsxwriter.readthedocs.org/