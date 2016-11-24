"""
队列用于存储按顺序排列的数据，先进先出，这点和栈不一样，在栈中，
最后入栈的元素反而被优先处理。可以将队列想象成在银行前排队的人群，排在最前面的人第一个办理业务，新来的人只能在后面排队，直到轮到他们为止。
python中有Queue模块，其中同步队列的常用方法：
put()将一个值放入队列
get()讲一个取出来（从对头取出并删除）
qsize()队列的长度
empty()队列是否为空
full()队列是否满了
"""
