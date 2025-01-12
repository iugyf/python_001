import tkinter as tk
import tkinter.messagebox as mb  # 不导入这个库，tk.messagebox.showerror会抛出错误
import math

class DiskAreaCalculate(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('disk area calculator')
        self.grid()

        # label1 and field for inputing radius
        self._radiusLable1 = tk.Label(self, text='radius:')
        self._radiusLable1.grid(row=0, column=0)
        self._radiusVar = tk.DoubleVar()
        self._radiusEntry = tk.Entry(self, justify=tk.RIGHT, textvariable=self._radiusVar)
        self._radiusEntry.grid(row=0, column=1, sticky=tk.E)

        # label and fielld for showing the area
        self._areaLable1 = tk.Label(self, text='area:')
        self._areaLable1.grid(row=1, column=0)
        self._areaVar = tk.DoubleVar()
        self._areaEntry = tk.Entry(self, justify=tk.RIGHT, textvariable=self._areaVar)
        self._areaEntry.grid(row=1, column=1, sticky=tk.E)

        # command button
        self._button = tk.Button(self, text='compute', command=self._area)
        self._button.grid(row=2, column=0, columnspan=2)

    def _area(self):
        """event handler for the button."""
        try:
            radius = self._radiusVar.get()
            area = radius**2 * math.pi
            self._areaVar.set(area)
        except tk.TclError as ex:
            tk.messagebox.showerror(title='disk area: error', parent=self,message=str(ex))

DiskAreaCalculate().mainloop()