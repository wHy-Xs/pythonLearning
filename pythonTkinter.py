from Tkinter import *
import datetime
import time
root = Tk()#创建主窗体
root.title(unicode('QQ','eucgb2312_cn'))#窗口名称
#按钮的触发函数
def sendMessage():
    msgcontent=unicode('我','eucgb2312_cn')+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n'
    text_left_top.insert(END,msgcontent,'green')
    text_left_top.insert(END,text_left_middle.get('0.0',END))
    text_left_middle.delete('0.0',END)
    
#布置格局
frame_left_top = Frame(width=380,height=270,bg='white')
frame_left_middle = Frame(width=380,height=100,bg='red')
frame_left_bottom = Frame(width=380,height=20)
frame_right=Frame(width=100,height=400,bg='white')

#转换成相应的控件
text_left_top=Text(frame_left_top)
text_left_middle=Text(frame_left_middle)
button_left_bottom=Button(frame_left_bottom,text=unicode('发送','eucgb2312_cn'),command=sendMessage)

text_left_top.tag_config('green', foreground='#008B00')
#页面布局具体位置的摆放
frame_left_top.grid(row=0,column=0,padx=2,pady=5)
frame_left_middle.grid(row=1,column=0,padx=2,pady=5) 
frame_left_bottom .grid(row=2,column=0)
frame_right.grid(row=0,column=1,rowspan=3,padx=4,pady=5)
#设定大小
frame_left_top.grid_propagate(0)
frame_left_middle.grid_propagate(0)
frame_left_bottom.grid_propagate(0)
#展现
text_left_top.grid()
text_left_middle.grid()
button_left_bottom.grid(sticky=E)

root.mainloop()
