# 使用闭包技术修正“共享局部变量问题”

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
            def outer_function(x):
                def inner_function():                   
                    var.set(var.get() + str(x))       # 此处 x 在 “定义” outer_function 时，被固定了。 
                                                      # 返回的是内部函数，所以外部函数的参数就是初次定义外部函数时所设置的值。
                return inner_function
                
            fun = outer_function(i)     # 实际赋给 “fun” 的是内部函数 “inner_function”

            digit = tk.Button(self, text=str(i), command=fun)
            digit.grid(row=1, column=i)
    


DigiWin().mainloop()