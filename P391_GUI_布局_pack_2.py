import tkinter as tk

class Layout(tk.Frame):
    def __init__(self):
        """sets up the window and widget.s"""
        tk.Frame.__init__(self)
        self.master.title("button win")
        self.pack()
        tk.Label(self, text="alpha").pack(side=tk.LEFT)
        tk.Label(self, text="beta").pack(side=tk.LEFT)
        tk.Entry(self).pack(side=tk.LEFT)
        
Layout().mainloop()