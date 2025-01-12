import tkinter as tk

class InputWin(tk.Frame):
    labels = ["姓名", "年龄", "电话"]     

    def __init__(self, parent=None, callback=lambda x:None):
        """build a framed window."""
        tk.Frame.__init__(self, parent)
        self._callback = callback
        self.master.title("数据录入")
        self.grid()


        frm = tk.Frame(self)                        # 第一个框架: 存放文本框与输入框
        frm.grid()

        self._varlist = []
        i = 0
        for title in InputWin.labels:
            v = self._build(frm, i, title)
            self._varlist.append(v)
            i += 1
        


        frm = tk.Frame(self)                        # 第二个框架：存入按钮
        frm.grid(sticky=tk.E + tk.W)
        but1 = tk.Button(frm, text="输入", command=self._input_data)
        but1.grid(column=0, row=0, padx=32,pady=2)

        but2 = tk.Button(frm, text="结束", command=self.master.destroy)
        but2.grid(column=1, row=0, padx=32, pady=2)



    def _build(self, frm, i ,lname):
        label = tk.Label(frm, text=lname, anchor=tk.W)
        label.grid(row=i, column=0, sticky=tk.E+tk.W)
        v = tk.StringVar()
        entry = tk.Entry(frm, textvariable=v, justify=tk.RIGHT)
        entry.grid(row=i, column=1)
        return v
    


    def _input_data(self):
        self._callback([v.get() for v in self._varlist])
        for v in self._varlist: v.set("")



InputWin(callback = print).mainloop()