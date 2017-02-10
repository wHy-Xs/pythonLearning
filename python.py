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
8.python中的.find() .replace .strip() .split() .join()
1).find():find(str, pos_start, pos_end)  返回值：如果查到：返回查找的第一个出现的位置。否则，返回-1。
2).repalce():str.replace(old, new[, max])把旧的换成新的
3）.strip():strip() 方法用于移除字符串头尾指定的字符（默认为空格）
4).split():split()通过指定分隔符对字符串进行切片,返回分割后的 字符串列表(注意！！！)。
5）__all__作用：此时被导入模块若定义了__all__属性，则只有all内指定的属性、方法、类可被导入。若没定义，则模块内的所有都将被导入。
6）if __name__=='__main__':main()
7).join():方法用于将序列中的元素以指定的字符连接生成一个新的字符串     
        str = "-";
        seq = ("a", "b", "c"); # 字符串序列
        print str.join( seq );
####################################################################################################################
9.python中函数下划线命名：
变量:
1.  前带_的变量:  标明是一个私有变量, 只用于标明, 外部类还是可以访问到这个变量
2.  前带两个_ ,后带两个_ 的变量:  标明是内置变量,
3.  大写加下划线的变量:  标明是 不会发生改变的全局变量
函数:
1. 前带_的变量: 标明是一个私有函数, 只用于标明,
2.  前带两个_ ,后带两个_ 的函数:  标明是特殊函数
###################################################################################################################
10.计算机中的编码Unicode utf-8 ascii
1)Unicode（统一码、万国码、单一码）是计算机科学领域里的一项业界标准,包括字符集、编码方案等
2)搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：
  在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
  用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
  
什么是字符集？
        在介绍字符集之前，我们先了解下为什么要有字符集。我们在计算机屏幕上看到的是实体化的文字，而在计算机存储介质中存放的实际是二进制的比特流。
        那么在这两者之间的转换规则就需要一个统一的标准，否则把我们的U盘插到老板的电脑上，文档就乱码了；小伙伴QQ上传过来的文件，在我们本地打开又乱码了。
        于是为了实现转换标准，各种字符集标准就出现了。简单的说字符集就规定了某个文字对应的二进制数字存放方式（编码）和某串二进制数值代表了哪个文字（解码
        ）的转换关系。那么为什么会有那么多字符集标准呢？这个问题实际非常容易回答。问问自己为什么我们的插头拿到英国就不能用了呢？
        为什么显示器同时有DVI，VGA，HDMI，DP这么多接口呢？很多规范和标准在最初制定时并不会意识到这将会是以后全球普适的准则，
        或者处于组织本身利益就想从本质上区别于现有标准。于是，就产生了那么多具有相同效果但又不相互兼容的标准了。
什么是字符编码？
        对于一个字符集来说要正确编码转码一个字符需要三个关键元素：字库表（character repertoire）、编码字符集（coded character set）、
        字符编码（character encoding form）。其中字库表是一个相当于所有可读或者可显示字符的数据库，字库表决定了整个字符集能够展现表示
        的所有字符的范围。编码字符集，即用一个编码值code point来表示一个字符在字库中的位置。字符编码，将编码字符集和实际存储数值之间的转换关系。
#########################################################################################
11.相对路径与绝对路径
绝对路径：是从盘符开始的路径，形如
C:\windows\system32\cmd.exe
相对路径：是从当前路径开始的路径，假如当前路径为C:\windows
要描述上述路径，只需输入
system32\cmd.exe
在网络中，以http开头的链接都是绝对路径，绝对路径就是你的主页上的文件或目录在硬盘上真正的路径，
绝对路径一般在CGI程序的路径配置中经常用到，而在制作网页中实际很少用到。
##########################################################################################
#######################os模块常用函数######################################################
1.os.path.dirname(__file__):文件所在的目录
2.os.path.abspath(__file__):文件的绝对路径
3.os.getcwd():显示python当前工作的路径一直到运行的哪个文件
4.os.remove("filename"):删除指定的一个文件
5.os.makedirs("1/2/3"):可生成多层递归目录
6.os.rmdir("dirname"):删除单级目录
7.os.chdir(path): 方法用于改变当前工作目录到指定的路径。
8.os.path.exists(path) :如果路径存在则返回true，否则返回false
##########################################################################################
######################sys模块常用的函数###################################################
1.sys.argv[]:获取命令行的参数
2.sys.path.append("dfdf"):对于模块和自己写的程序不在同一个目录下，可以把模块的路径通过sys.path.append(路径)添加到程序中。
#########################################################################################
1.列表
不用声明可以直接使用，并且一个数组中可以存储多种不同的数据类型（包括另外的列表，元组，字典）
a=['1','2','3']
  list.remove(value)  删除指定的值
  list.pop()  删除末尾的值
  list.insert(index,value) 在指定位置插入值 
  list.reverse() 翻转数组
  list.append(value)  在数组末尾追加一个值
  list.extend(list1)  在数组末尾追加另一个数组
判断数据类型：
  a = 111
  isinstance(a, int)
  True
2.遗留为题：发布方法
3.try/except/finally方法运用
###########################################################################################
sort():原地排序，排序完成后会覆盖掉之前的数据
sorted()：复制排序,会生成一个新的排序列表，原来的列表顺序不变
###########################################################################################
12.列表推倒
常规：
a=[1,2,3,4,5]
c=[]
for i in a:
    c=i*3
print c
列表推倒:c=[i*3 for i in a]
