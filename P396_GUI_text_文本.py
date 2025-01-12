import tkinter as tk
import tkinter.messagebox as ms

# 类TextWin, 继承Frame
class TextWin(tk.Frame):
    def __init__(self):     # 初始化
        tk.Frame.__init__(self) # 初始化父类
        self.master.title("x-window");      # 加不加分号都一样     master.title: 父类的抬头
        self.grid()     # 放置本物件

        # 文本框
        text_1 = tk.Text(self, height=2, width=16)
        text_1.grid()

        # 按钮
        button = tk.Button(self, text='add a x', command=lambda: self.addX(text_1))
        button.grid()

    def addX(self, text_2):
        text_2.insert(tk.INSERT,'X')

TextWin().mainloop()