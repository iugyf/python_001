import tkinter as tk

class EntryWin(tk.Frame):
    def __init__(self):
        """sets up the window and widget.s"""
        tk.Frame.__init__(self)
        self.master.title("button win")
        self.grid()
        self._label = tk.Label(self, text="", width=200)
        self._label.grid()

        self._entry = tk.Entry(self,width=20)   # 输入框
        self._entry.grid()

        self._button = tk.Button(self, 
                                 text="copy&clear", 
                                 command = self._action)
        self._button.grid()

    def _action(self):
        """event handler for the button."""
        st = self._entry.get()
        self._label["text"] = st
        self._entry.delete(0, len(st))

EntryWin().mainloop()