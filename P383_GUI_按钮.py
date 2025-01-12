import tkinter as tk


class ButtonWin(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Main")
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # Hi按钮
        self._hi = tk.Button(self)
        self._hi["text"] = "hello world (click me)"
        self._hi["command"] = self._say_hi
        self._hi.grid()
        # 退出按钮
        self._quit = tk.Button(
            self, text = "QUIT", fg = "red",
            command = self.master.destroy)
        self._quit.grid() 
    # 按钮调用                            
    def _say_hi(self):
        print(("Hi there, everyone!"))

ButtonWin().mainloop()