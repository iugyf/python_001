import tkinter as tk
import tkinter.filedialog as fd

class Openfile(tk.Frame):
    _frame = ''

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("file")
        self.grid()
        self._open = tk.Button(self, text='open a file', width=20, command=self.get_fname)      # command后面的函数不能加括号，否则就不是关联，而是执行该函数了。
        self._open.grid()
        
        self._quit = tk.Button(self, text='quit', fg='red', command=self.master.destroy)
        self._quit.grid()

    def get_fname(self):
        self._fname = fd.askopenfilename()
        print("file name>>", self._fname)

Openfile().mainloop()