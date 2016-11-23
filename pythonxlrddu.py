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
print sheet1.row(1)[0].ctype
print sheet1.row_values(0)
#ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
#col_values(0)获取整列数
#如果遇到中文可以现获取这个列的值，然后再unicode，如果想直接输出中文，则需要先判断类型然后再看是否需要encode('utf-8')
#################################################################################
#################################################################################
import xlrd

class readExcel():
    def __init__(self):
        workbook = xlrd.open_workbook(r'D:\pythonCode/text.xlsx')  #加载文件
        self.workbook= workbook
        sheetNames=workbook.sheet_names()   #查看这个文件中有多少表，并把它们名字拿出来
        print sheetNames  #打印表的名称

    #选择哪张表
    def selectSheet(self,n):
        if n == 0:
            sheet1=self.workbook.sheet_names()[0]
            onlysheet = sheet1
        else:
            sheet=self.workbook.sheet_names()[n]
            onlysheet = sheet
        return onlysheet

    def readContext(self,onlysheet,row,col):
        sheetContext=self.workbook.sheet_by_name(onlysheet)
        print '这是表'+str(onlysheet)+".本表有"+str(sheetContext.nrows)+"行"+","+str(sheetContext.ncols)+"列."
        print sheetContext

        title=sheetContext.row_values(0)#取得本表的标题
        for i in title:
            print unicode(i),   #输出本表的标题
        print ''

        if row>sheetContext.nrows or col>sheetContext.ncols:
            return False
        else:
            context=sheetContext.row(row)[col].value
            print context
        
    def printdd(selfmai):
        print 'dfdf'


def main():
    excel=readExcel()
    excel.printdd()
    print("请选择查看哪张表:")
    sheetindex=input()
    onlysheet=excel.selectSheet(sheetindex)
    print '请选择查看具体位置的信息:'
    local1=input()
    local2=input()
    excel.readContext(onlysheet,local1,local2)

if __name__ == "__main__":
     main()

    


