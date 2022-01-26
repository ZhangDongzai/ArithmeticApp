import tkinter as tk
import tkinter.messagebox as messagebox

class GUI():

    def __init__(self):
        with open(file = "setup.ini",mode = "r") as file:
            self.run_number = int(file.readlines()[0])


    def setup(self):
        self.child = tk.Toplevel()
        self.child.title("设置")
        self.child.geometry('256x100+250+200')
        self.child.resizable(0,0)


        #创建菜单栏
        self.setup_menu = tk.Menu(self.child)
        self.setup_menu.add_command(label = '应用',command = self.setup_app_command)
        self.setup_menu.add_command(label = '退出',command = self.child.destroy)
        
        #创建部件
        self.setup_label_1 = tk.Label(self.child,text = "题目数量")
        self.setup_entry_1 = tk.Entry(self.child)
        
        #插入
        self.setup_entry_1.insert(0,self.run_number)

        #部件放置
        self.child.config(menu = self.setup_menu)
        self.setup_label_1.grid(row = 0,column = 0)
        self.setup_entry_1.grid(row = 0,column = 1)
        
        #窗口循环
        self.child.mainloop()

    def setup_app_command(self):
        try:
            self.run_number_test = int(self.setup_entry_1.get())
            self.run_number = self.run_number_test

            self.setup_app_ok()

            #提示
            messagebox.showinfo(title = "提示",message = "修改成功！")
        except:
            #提示
            messagebox.showinfo(title = "提示",message = "修改失败，请重新输入！")

            #插入
            self.setup_entry_1.insert(0,self.run_number)

    def setup_app_ok(self):
        with open(file = "setup.ini",mode = "w") as file:
            file.write("%d"%(self.run_number))

    def about():
        pass