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