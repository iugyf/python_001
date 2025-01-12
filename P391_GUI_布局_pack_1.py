import tkinter as tk

class Layout(tk.Frame):
    def __init__(self):
        """sets up the window and widget.s"""
        tk.Frame.__init__(self)
        self.master.title("button win")
        self.pack()
        tk.Label(self, text="alpha").pack()
        tk.Label(self, text="beta").pack()
        tk.Entry(self).pack()
        
Layout().mainloop()