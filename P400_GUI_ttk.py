from tkinter import ttk

class TwoButtonWin(ttk.Frame):
    def __init__(self):
        """set up the window and widgets."""
        ttk.Frame.__init__(self)
        self.master.title("button win")
        self.grid()

        self._label = ttk.Label(self, text='begin')
        self._label.grid(sticky='ew')
        
        self._button1 = ttk.Button(self, text='comming', command=self._switch, width=20)
        self._button1.grid(sticky='ew')

        self._button2 = ttk.Button(self, text='leaving', command=self._switch)
        self._button2.state(['disabled'])
        self._button2.grid(sticky='ew')

    def _switch(self):
        '''event handler for the button.'''
        if self._label['text'] == 'hello':
            self._label['text'] = 'goodbye'
            self._button1.state(['!disabled'])
            self._button2.state(['disabled'])
        else:
            self._label['text'] = 'hello'
            self._button1.state(['disabled'])
            self._button2.state(['!disabled'])

TwoButtonWin().mainloop()