import tkinter as tk


class CanvasWin(tk.Frame):
    def __init__(self):
        """sets up the window and widgets"""
        tk.Frame.__init__(self)
        self.master.title("cavas window")
        self.grid()

        can = self.can = tk.Canvas(self, width=380, height=180)
        self.can.grid()
        self._image = tk.PhotoImage(file='P399_图标.png')

        x1 = can.create_arc(10, 10, 50, 50)
        x2 = can.create_oval(60, 10, 150, 60)
        x3 = can.create_rectangle(160, 10, 240, 60)
        x4 = can.create_image(300, 50, image=self._image)

        # create_bitmap 创建位图
        x5 = can.create_line(10, 60, 20, 140,
                             80, 80, 70, 130)
        x6 = can.create_text(60, 165,
                             text='hello, beijing')
        x7 = self.can.create_polygon(110, 100, 120, 150,
                                     200, 140, 180, 80)
        frm = tk.Frame(can, borderwidth=5, relief=tk.RAISED)
        win = self.can.create_window(300, 150, window=frm)
        tk.Label(frm, text='i am here.').grid()
        bn = tk.Button(frm, text='move', command=self._move)
        bn.grid(sticky = tk.W + tk.E)
        self.objs = [x1, x2, x3, x4, x5, x6, x7]

    def _move(self):
        self.can.move(self.objs[0], 5, 1)
        self.can.move(self.objs[1], -1, 3)

CanvasWin().mainloop()