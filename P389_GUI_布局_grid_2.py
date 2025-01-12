import tkinter as tk

class Layout(tk.Frame):
    def __init__(self):
        """sets up the window and widget.s"""
        tk.Frame.__init__(self)
        self.master.title("button win")
        self.grid()
        tk.Label(self, text="name:").grid(row=0,sticky=tk.W)        #tk.W: 方向为西   sticky:拉伸后对齐方向
        tk.Label(self, text="password:").grid(row=1, sticky=tk.W)
        tk.Entry(self).grid(row=0, column=1)
        tk.Entry(self).grid(row=1, column=1)

Layout().mainloop()