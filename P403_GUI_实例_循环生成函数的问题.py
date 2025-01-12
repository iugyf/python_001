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
            digit = tk.Button(self, text=str(i), command=lambda:var.set(var.get()+str(i)))      # 这个command设置是共享的，经过初次循环后指向同一个函数，也就是说那9个不同按钮会得到同一个结果：最后一位是9
            digit.grid(row=1, column=i)
    
DigiWin().mainloop()