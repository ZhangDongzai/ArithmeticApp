import tkinter as tk
import random as ra
import time as ti
import tkinter.messagebox as messagebox
import child

class My_GUI():

    def __init__(self): 

        self.title_True = 0
        self.title_False = 0
        self.version = 1.0                                  #版本号
        

        #生成窗口
        self.root = tk.Tk()
        self.root.title('算数生成器')
        self.root.geometry('256x100+250+200')
        self.root.resizable(0,0)

        self.child = child.GUI()

        #定义乘数
        self.a = ra.randint(0,50)
        self.b = ra.randint(0,50)
        self.i = 1

        self.frame()
        self.root.mainloop()

    def frame(self):

        self.run_number = child.GUI().run_number
        
        #创建菜单栏
        self.menu = tk.Menu(self.root)
        self.menu.add_command(label = '设置',command = self.child.setup)
        self.menu.add_command(label = '退出',command = self.root.destroy)

        #创建部件并设置部件属性
        self.progress = tk.Label(self.root,text = '进度：' + str(self.i) + '/' + str(self.run_number))
        self.title = tk.Label(self.root,text = str(self.a) + ' * ' + str(self.b) + ' =')
        self.answer = tk.Entry(self.root)
        self.button = tk.Button(self.root,text = '确定',command = self.ok)

        #部件放置
        self.root.config(menu = self.menu)
        self.progress.pack()
        self.title.pack()
        self.answer.pack()
        self.button.pack()

    def ok(self):

        self.run_number = child.GUI().run_number
        
        #获取答案
        self.user_answer = self.answer.get()
        self.root_answer = str(self.a * self.b)

        #判断结果
        if self.user_answer == self.root_answer:
            self.message = "正确"
            self.title_True += 1                     #如果正确，则返回"正确"   
        else:
            self.message = "错误"                     #如果错误，则返回"错误"
            self.title_False += 1
        messagebox.showinfo("提示",self.message)   #输出结果
        self.i += 1

        #判断运行次数
        if self.i <= self.run_number:
            #定义乘数
            self.a = ra.randint(0,50)
            self.b = ra.randint(0,50)

            #删除所有部件
            self.progress.destroy()
            self.title.destroy()
            self.answer.destroy()
            self.button.destroy()
        
            #运行窗口构建
            self.frame()
        else:
            tk.messagebox.showinfo('提示','结束\n对了%d题，错了%d题'%(self.title_True,self.title_False))   #提示结束
            self.root.destroy()                       #关闭窗口
    

gui = My_GUI()                                      #运行实例

    
