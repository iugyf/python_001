import tkinter as tk

class MixColor(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)     # 初始化框架
        self.master.title("mixcolor")   # 上层物件，也就是"窗口"抬头写为mixcolor
        self.grid()     # 安置本物件，即安置框架，放入窗口中

        label = tk.Label(self, text='', width = 30)     # 标签
        label.grid(row=0, column=0, columnspan=3)   # columnspan：跨列

        red = tk.IntVar()
        green = tk.IntVar()
        blue = tk.IntVar()
        ilist = ((0, "red", red),(1,"green", green),(2,"blue", blue))
        for i, name, var in ilist:
            color = tk.Checkbutton(self, text=name, variable=var)   # Checkbutton: 复选框
            color.grid(row=1, column=i) 
        
        # “更新”按钮
        button = tk.Button(self, text="update",
                        command = lambda : self.update(label, red, green, blue))
        button.grid(row=2, column=0, columnspan=3)
        self.update(label, red, green, blue)




    # 如果选择了红色和绿色复选框，标签的背景颜色将变为黄色（#FFFF00）。
    # 如果选择了红色和蓝色复选框，标签的背景颜色将变为洋红色（#FF00FF）。
    # 如果选择了所有三个复选框，标签的背景颜色将变为白色（#FFFFFF）。
    # 如果没有选择任何复选框，标签的背景颜色将保持为黑色（#000000）。
    def update(self, widget, r, g, b):
        color = '#'
        for var in (r,g,b):
            color += "FF" if var.get() else "00"
        widget['bg'] = color





MixColor().mainloop()