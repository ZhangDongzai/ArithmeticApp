import tkinter as tk
import random as ra
import time as ti
from tkinter import messagebox

class My_GUI():

    def __init__(self):
        
        self.version = 1.0                                  #版本号

        #生成窗口
        self.root = tk.Tk()
        self.root.title('算数生成器 v' + str(self.version))
        self.root.geometry('256x100+250+200')
        self.root.resizable(0,0)

        #定义乘数
        self.a = ra.randint(0,50)
        self.b = ra.randint(0,50)
        self.i = 1

        self.frame()
        self.mainloop()

    def frame(self):
        #创建部件并设置部件属性
        self.progress = tk.Label(self.root,text = '进度：' + str(self.i) + '/' + str(5))
        self.title = tk.Label(self.root,text = str(self.a) + ' * ' + str(self.b) + ' =')
        self.answer = tk.Entry(self.root)
        self.button = tk.Button(self.root,text = '确定',command = self.ok)

        #部件放置
        self.progress.pack()
        self.title.pack()
        self.answer.pack()
        self.button.pack()

            

    def ok(self):
        #获取答案
        self.user_answer = self.answer.get()
        self.root_answer = str(self.a * self.b)

        #判断结果
        if self.user_answer == self.root_answer:
            self.message = "正确"                     #如果正确，则返回"正确"   
        else:
            self.message = "错误"                     #如果错误，则返回"错误"

        tk.messagebox.showinfo("提示",self.message)   #输出结果
        
        #判断运行次数
        if self.i <= 4:
            #定义乘数
            self.a = ra.randint(0,50)
            self.b = ra.randint(0,50)
            self.i += 1

            #删除所有部件
            self.progress.destroy()
            self.title.destroy()
            self.answer.destroy()
            self.button.destroy()
        
            #运行窗口构建
            self.frame()
        else:
            tk.messagebox.showinfo('提示','结束')   #提示结束
            self.root.quit()                        #关闭窗口
          
    def mainloop(self):
        self.root.mainloop()                        #循环窗口

gui = My_GUI()                                      #运行实例

    