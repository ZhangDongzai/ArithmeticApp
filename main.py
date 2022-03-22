from tkinter import ttk
from ttkbootstrap import Style
import tkinter as tk
import random as ra
import time as ti
import tkinter.messagebox as messagebox
import base64

class My_GUI():

    def __init__(self): 

        self.title_True = 0
        self.title_False = 0
        self.version = 1.0              #版本号
        self.child_window = child_GUI()
        style = Style(theme = self.child_window.topic)

        #生成窗口
        self.root = style.master
        self.root.title('算数生成器')
        self.root.geometry("250x200")

        #定义乘数
        self.a = ra.randint(0,50)
        self.b = ra.randint(0,50)
        self.i = 1

        self.frame()
        self.root.mainloop()

    def frame(self):

        self.run_number = self.child_window.run_number
        
        #创建菜单栏
        self.menu = tk.Menu(self.root)
        self.menu.add_command(label = "设置",command = self.child_window.entry_window)
        if self.child_window.quit == "True":
            self.menu.add_command(label = "退出",command = self.root.quit)
        self.menubutton = ttk.Menubutton(self.root,text = '程序',menu = self.menu)

        #创建部件并设置部件属性
        self.progress = ttk.Label(self.root,text = '进度：' + str(self.i) + '/' + str(self.run_number))
        self.title = ttk.Label(self.root,text = str(self.a) + ' * ' + str(self.b) + ' =')
        self.answer = ttk.Entry(self.root)
        self.button = ttk.Button(self.root,text = '确定',command = self.ok)

        #部件放置
        self.root.config(menu = self.menubutton)
        self.root.config(menu = self.menu)
        self.progress.pack()
        self.title.pack()
        self.answer.pack()
        self.button.pack()

    def ok(self):

        self.run_number = self.child_window.run_number
        
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
    
class child_GUI():

    def __init__(self):
        with open(file = "setup.bin",mode = "rb") as self.file:
            text = base64.b64decode(self.file.read()).decode("utf-8")
            for self.i in text.split("\n"):
                if self.i.split("=")[0] == "run_number":
                    self.run_number = int(self.i.split("=")[1])
                elif self.i.split("=")[0] == "topic":
                    self.topic = self.i.split("=")[1]
                elif self.i.split("=")[0] == "quit":
                    self.quit = self.i.split("=")[1]
                elif self.i.split("=")[0] == "password":
                    self.password = self.i.split("=")[1]

    def setup(self):
        self.child_label.destroy()
        self.child_entry.destroy()
        self.child_button.destroy()
        
        self.child.title("设置")

        #创建菜单栏
        self.setup_menu = tk.Menu(self.child)
        self.setup_menu.add_command(label = '应用',command = self.setup_app_command)
        self.setup_menu.add_command(label = '退出',command = self.child.destroy)
        
        #创建部件
        self.topic_label = tk.Label(self.child,text = "界面主题")
        self.topic_combobox = ttk.Combobox(self.child,value = ("cosmo","flatly","journal","literal","lumen","minty","pulse","sandstone","united","yeti","cyborg","darkly","solar","superhero"))
        
        self.run_number_label = tk.Label(self.child,text = "题目数量")
        self.run_number_entry = tk.Entry(self.child)

        self.password_label = tk.Label(self.child,text = "密码")
        self.password_entry = tk.Entry(self.child,show = "*")

        self.quit_label = tk.Label(self.child,text = "答题时可以退出")
        self.quit_button = tk.Button(self.child,text = "是"if self.quit == "True" else "否",command = self.setup_app_quit_button_command)
        
        #插入
        self.run_number_entry.insert(0,self.run_number)
        self.topic_combobox.insert(0,self.topic)
        self.password_entry.insert(0,self.password)

        #部件放置
        self.child.config(menu = self.setup_menu)
        
        self.topic_label.grid(row = 0,column = 0)
        self.topic_combobox.grid(row = 0,column = 1)
        
        self.run_number_label.grid(row = 1,column = 0)
        self.run_number_entry.grid(row = 1,column = 1)

        self.password_label.grid(row = 2,column = 0)
        self.password_entry.grid(row = 2,column = 1)

        self.quit_label.grid(row = 3,column = 0)
        self.quit_button.grid(row = 3,column = 1)

    def setup_app_command(self):
        
        try:
            self.run_number = int(self.run_number_entry.get())
            self.topic = self.topic_combobox.get()
            self.password = self.password_entry.get()
            
            self.setup_app_ok()

            #提示
            messagebox.showinfo(title = "提示",message = "修改成功！")
        except:
            #提示
            messagebox.showinfo(title = "提示",message = "修改失败，请重新输入！")

            #插入
            self.setup_entry.insert(0,self.run_number)

    def setup_app_ok(self):
        with open(file = "setup.bin",mode = "wb") as file:
            text = "run_number=%d\ntopic=%s\npassword=%s\nquit=%s"%(self.run_number,self.topic,self.password,self.quit)
            text_encode_base64 = base64.b64encode(text.encode("utf-8"))
            file.write(text_encode_base64)

    def entry_window(self):
        self.child = tk.Toplevel()
        self.child.title("密码输入窗口")
        
        #创建部件
        self.child_label = tk.Label(self.child,text = "请输入密码：")
        self.child_entry = tk.Entry(self.child,show = "*")
        self.child_button = tk.Button(self.child,text = "确定",command = self.entry_window_app_command)
        
        #部件放置
        self.child_label.pack()
        self.child_entry.pack()
        self.child_button.pack()

        self.child.mainloop()

    def entry_window_app_command(self):
        self.entry_text = self.child_entry.get()
        if self.entry_text == self.password:
            self.setup()
        else:
            #提示
            messagebox.showinfo(title = "提示",message = "密码错误!")

    def setup_app_quit_button_command(self):
        self.quit = "True" if self.quit == "False" else "False"
        self.quit_button["text"] = "是" if self.quit == "True" else "否"
                    
gui = My_GUI()                                      #运行实例
