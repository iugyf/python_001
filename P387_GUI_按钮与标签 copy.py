import tkinter as tk

class TwoButtonWin(tk.Frame):
    def __init__(self):
        """sets up the window and widget.s"""
        tk.Frame.__init__(self)
        self.master.title("button win")
        self.grid()
        self._label = tk.Label(self, text="begin", width=20)
        self._label.grid()

        self._button1 = tk.Button(self, 
                                 text="coming", 
                                 command = self._switch)
        self._button1.grid()
        self._button2 = tk.Button(self,
                                  text="leaving",
                                  command = tk.DISABLED)
        self._button2.grid()

    def _switch(self):
        """event handler for the button."""
        if self._label["text"] == "hello":
            self._label["text"] = "goodbye"
            self._button1["state"] = tk.NORMAL
            self._button2["state"] = tk.DISABLED
        else:
            self._label["text"] = "hello"
            self._button2["state"] = tk.NORMAL
            self._button1["state"] = tk.DISABLED
            
TwoButtonWin().mainloop()