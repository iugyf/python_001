# 改进版，解决共享局部变量的问题

import tkinter as tk

class DigiWin(tk.Frame):
    def __init__(self):
        """sets up the window and widgets."""
        tk.Frame.__init__(self)
        self.master.title("digits")
        self.grid()

        var = tk.StringVar()
        self.label = tk.Label(self, textvariable=var, anchor=tk.E)
        self.label.grid(row=0, columnspan=10, stick=tk.E+tk.W)

        for i in range(10):
            #------------------------------------------------------------------------------
            # 原问题： 这个command设置是共享的，经过初次循环后指向同一个函数，也就是说那9个不同按钮会得到同一个结果：最后一位是9
            # digit = tk.Button(self, text=str(i), command=lambda:var.set(var.get()+str(i)))    
            #------------------------------------------------------------------------------

            # 解决：这里创建 "s" 是带默认值的参数，只要不传入新参数，就只会记录当时 "i" 的值。
            digit = tk.Button(self, text=str(i), command=lambda s=str(i) :var.set(var.get()+s))   
            digit.grid(row=1, column=i)
    
DigiWin().mainloop()