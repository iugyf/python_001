import tkinter as tk
import tkinter.messagebox as mb     # 即使前面tkinter已经导入的情况下，messagebox包依然需要单独导入

class MessageShow(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("popup message box")
        self.grid()
        errmsg = 'sorry, no spam allowed!'
        wrmmsg = 'escape not yet implemented'
        bt1 = tk.Button(self, text='quit', command=self.callback, width=16)
        bt1.grid()
        bt2 = tk.Button(self, text='escape', width=16, command=lambda : mb.showerror("escape", wrmmsg))
        bt2.grid()
        bt3 = tk.Button(self, text='span', width=16, command=lambda : mb.showerror("spam", errmsg))
        bt3.grid()
    
    def callback(self):
        if mb.askyesno("verift", 'do you really want to quit?'):
            self.master.destroy()
        else:
            mb.showinfo('no', 'quit has been cancelled')
        
MessageShow().mainloop()
