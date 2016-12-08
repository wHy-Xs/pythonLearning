################################################################################################################################
################################################python中json文件的处理总结########################################################
"""
1.json文件的解析及json数据的解析
概念：  encoding：把一个Python对象编码转换成Json字符串
        decoding：把Json格式字符串解码转换成Python对象
        json.dumps对简单数据类型进行encoding：即将数据转换成json字符串
        json.loads处理简单数据类型的decoding：即将json字符串转换成Python数据
        加s的方法主要用于处理json数据而不适用处理json文件，处理json文件使用load与dump
"""
#举例子1
def change(path=None):
            files=file(vpath) #打开json文件
            s=json.load(files)#将json文件转换成字典类型
            s['data']['vid']=123123#修改json文件中的指定    
            json.dump(s,open('msg_v.json','w'),indent=4)#然后将字典类型用json.dump成json并写入msg_v.json文件，用'w'每次文件都清空
 #举例子2
data = [{"a":"aaa","b":"bbb","c":[1,2,3,(4,5,6)]},33,'tantengvip',True] #python类型数据
data2 = json.dumps(data) #将其转化成json格式
print(data2)#打印数据
f = open('./tt.txt','a')#打开一个文件
json.dump(data2,f)#将转换成功的json数据写入数据
##################################################################################################################################
##################################################################################################################################
####################################################python中的一些知识点总结########################################################
'''
1.self:首先明确的是self只有在类的方法中才会有，独立的函数或方法是不必带有self的。self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗，不要搞另类，大家会不明白的。
eg:
class Person:
          def _init_(myname,name):
                   myname.name=name
          def sayhello(myname):
                   print 'My name is:',myname.name
p=Person('Bill')
print p

self指的是类实例对象本身(注意：不是类本身)。
class Person:
         def _init_(self,name):
                  self.name=name
         def sayhello(self):
                  print 'My name is:',self.name
p=Person('Bill')
print p

在上述例子中，self指向Person的实例p。 为什么不是指向类本身呢，如下例子：
class Person:
         def _init_(self,name):
                  self.name=name
         def sayhello(self):
                  print 'My name is:',self.name
p=Person('Bill')
p1 = Person('Apple')
print p
如果self指向类本身，那么当有多个实例对象时，self指向哪一个呢？
###########################################################################################################################
2.python中的判断：在python中判断一个变量是否为空或者是否存在可以直接用其名字来判断，不让用非得让其==或！=来判断。注意shell中传None时是字符串，
不是Python中None的含义，而且shell中可以使用''或者""来当占位传入参数
###########################################################################################################################
3.python中的sys模块就是传入命令行非常方便 执行python 1.py case1 case2 case3时，python中sys.argv[1]=case1，sys.argv[2]=case2以此类推
############################################################################################################################
4.ptyon中random模块：random.randint(0,99)随机生成0--99的整数random.choice([1,2,3,5])随机生成数组中的数
#############################################################################################################################
5.python中time模块time.strftime("%Y%m%d%H%M%S",time.localtime())时间
##############################################################################################################################
6.shell中的知识：
1.stty erase ^H
  read -p 'please input a number ' number 可以在前台输入一个变量。linux中变量不用加$，只有将变量输出时才$变量名字
2.case work in
        1 ）
         点点滴滴 ；；
  esac
3.shell中可以使用''或者“”当占位符
###############################################################################################################################
7.python中的正则匹配
Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先使用re.compile()函数，将正则表达式的字符串形式编译为Pattern实例，
然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。
eg：
import re
pattern = re.compile('[a-zA-Z]')
result = pattern.findall('as3SiOPdj#@23awe')
print result
# ['a', 's', 'S', 'i', 'O', 'P', 'd', 'j', 'a', 'w', 'e']
#################################################################################################################
8.python中的.find() .replace .strip() .split() 
1).find():find(str, pos_start, pos_end)  返回值：如果查到：返回查找的第一个出现的位置。否则，返回-1。
2).repalce():str.replace(old, new[, max])把旧的换成新的
3）.strip():strip() 方法用于移除字符串头尾指定的字符（默认为空格）
4).split():split()通过指定分隔符对字符串进行切片,返回分割后的 字符串列表(注意！！！)。
