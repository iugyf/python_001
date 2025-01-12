import tkinter as tk


# ImageWin 类，继承 Frame 类。     Frame: 框架类
class ImageWin(tk.Frame):  
    def __init__(self, fname, caption):
        """sets up the window and widgets."""   # __doc__ 文档串
        tk.Frame.__init__(self)                 # 初始化 Frame 实例
        self.master.title("image window")       # 设置窗口标题
        self.grid()                             # 安置本 Frame
        self._image = tk.PhotoImage(file = fname)
        self._imagelabel = tk.Label(self, image = self._image)
        self._imagelabel.grid()
        self._textlable = tk.Label(self, text = caption)
        self._textlable.grid()

ImageWin("P383_背景图片.gif", "背景图片").mainloop()         # 启动窗口循环，接受消息并响应