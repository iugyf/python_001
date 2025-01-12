import tkinter as tk

class ShareVar(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("button win")
        self.grid()

        var = tk.StringVar()    # 得到一个能存放字符序列的控制变量
        self._label = tk.Label(self, textvariable = var, width=20)  # textvariable属性：用于关联控制变量物件。  此处通过 “var” 控制变量与 "_entry"物件关联了起来，实现共享功能。
        self._label.grid()  # 安置物件到窗口上
        self._entry = tk.Entry(self, textvariable=var, width=20)    # 当前“输入框”的 textvariable 关联到上面“文本框”的textvariable
        self._entry.grid()
        self.mainloop()

ShareVar()