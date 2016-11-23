import xlrd

workbook = xlrd.open_workbook('D:\pythonCode/text.xlsx')#读取xlsx文件

print workbook.sheet_names() #获取表的全部名称
sheet1name=workbook.sheet_names()[0]  #获取具体的表
sheet2name=workbook.sheet_names()[1]  
print sheet1name
print sheet2name
sheet1=workbook.sheet_by_index(0) #根据标号获取这个表的内容
sheet2=workbook.sheet_by_name(sheet2name)#根据表的名称获取这个表的内容
print sheet1
print sheet2
print sheet1.name,sheet1.nrows,sheet1.ncols #表1的行数与列数还有名称   

rowscontext=unicode(sheet1.row_values(0))
print rowscontext

print sheet1.cell(1,0).value.encode('utf-8')
print sheet1.cell_value(4,0).encode('utf-8')
print sheet1.row(1)[0].value.encode('utf-8')
print sheet1.row_values(0)
