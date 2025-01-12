import tkinter as tk

class LoginPopup(tk.Frame):
    def __init__(self):
        """sets up the window and widget.s"""
        tk.Frame.__init__(self)
        self.master.title("login pku intranet")
        self.grid()

        label1 = tk.Label(self, text="please login")
        label1.grid(row=0, columnspan=2)          # columnspan: 跨列数
        label2 = tk.Label(self, text="username:")
        label2.grid(row=1, sticky=tk.W)          #tk.W: 方向为西   sticky:拉伸后对齐方向
        label3 = tk.Label(self, text="password:")
        label3.grid(row=2, sticky=tk.W) 

        tk.Entry(self).grid(row=1, column=1)
        tk.Entry(self, show='*').grid(row=2, column=1)

        self._img = tk.PhotoImage(file="P389_登陆图标.gif")
        img_label = tk.Label(self, image=self._img)
        img_label.grid(row=0, column=2, rowspan=3,     # rowspan: 跨行数
                       sticky=tk.N + tk.S)              # tk.N + tk.S : 纵向扩展        sticky:拉伸后对齐方向

        button1 = tk.Button(self, text="login",
                            command = (lambda : None))
        button2 = tk.Button(self, text="cancel",
                            command = (lambda : None))
        button1.grid(row=3, column=0, columnspan=2)
        button2.grid(row=3, column=1, columnspan=2)        

LoginPopup().mainloop()