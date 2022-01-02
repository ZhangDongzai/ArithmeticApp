import tkinter as tk
import random as ra
import time as ti
from tkinter import messagebox

class My_GUI():

    def __init__(self):
        
        self.version = 1.0
        self.true = 0
        self.false = 0

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
        
        
    
        self.progress = tk.Label(self.root,text = '进度：' + str(self.i) + '/' + str(5))
        self.title = tk.Label(self.root,text = str(self.a) + ' * ' + str(self.b) + ' =')
        self.answer = tk.Entry(self.root)
        self.button = tk.Button(self.root,text = '确定',command = self.ok)

        self.progress.pack()
        self.title.pack()
        self.answer.pack()
        self.button.pack()

            

    def ok(self):
        self.user_answer = int(self.answer.get())
        self.root_answer = self.a *self.b

        if self.user_answer == self.root_answer:
            tk.messagebox.showinfo('提示','正确')
            self.true += 1

            
        else:
            tk.messagebox.showinfo('提示','错误')
            self.false += 1

        
        if self.i <= 4:
            #定义乘数
            self.a = ra.randint(0,50)
            self.b = ra.randint(0,50)
            self.i += 1

            self.progress.destroy()
            self.title.destroy()
            self.answer.destroy()
            self.button.destroy()
        
            self.frame()
        else:
            tk.messagebox.showinfo('提示','结束\n正确' + str(self.true) + '题，错误' + str(self.false) + '题')
            self.root.quit()
            

        
        
    def mainloop(self):
        self.root.mainloop()

gui = My_GUI()

    