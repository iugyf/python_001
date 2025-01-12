# 第三个文件：GUI模块    代码中的注释全是“通义千问”注释的

#------------------------------------------------------------------------------------
# 此处的头文件应该在 "P406_GUI_实例_电话簿_04_GUI_UI图形界面.py" 文件中装载。   
# 之所以这里重复装载，是因为独立调用本文件时可执行。
import tkinter as tk
import tkinter.messagebox as mb
#------------------------------------------------------------------------------------

# 创建新窗口，实现程序的子功能。 （实际上就创建了两个窗口：添加新联系人， 查找）
class InputWin(tk.Frame):
    """可用于作为独立的顶层窗口或者作为其它窗口中的部件的数据输入窗口。
    创建对象时（调用初始化方法）的参数说明：
        title:        作为窗口标题。
        button_label: 指定输入按钮上的文字。
        entries:      是一个字符串的表，字符串为窗口中各输入项的标签。
        callback:     指定接收输入的回调函数。"""
    
    def __init__(self, title='数据录入', button_label='输入', entries=tuple("None"), callback=lambda: None):
        """define a framed window. 定义一个带输入框的窗口，并设置其布局和行为。"""               # 文档串

        # ------------------------------------------------------------------------
        tk.Frame.__init__(self, tk.Toplevel())      # 初始化 Frame 实例     
                                                    # 通过传递 tk.Toplevel()，你可以确保每次创建 InputWin 实例时，都会弹出一个新的独立窗口，
                                                        # 而不是将 Frame 放置在主应用程序窗口中。
                                                    # self：这是隐式传递的，表示当前 InputWin 类的实例。
                                                        # tk.Frame 的构造函数会将 self 作为 Frame 的实例进行初始化。
       
        # # 这两行代码是等价的：
        # tk.Frame.__init__(self, tk.Toplevel())  # 显式调用父类构造函数
        # super().__init__(tk.Toplevel())          # 使用 super() 调用父类构造函数
        # ------------------------------------------------------------------------

        self.master.title(title)                    # 设置窗口标题
        self.grid()                                 # 安置本 Frame
        self._callback = callback                   


        # 创建一个 Frame 用于放置输入项（标签 + 输入框）
        frm = tk.Frame(self)        # 该输入框的父物件(父窗口)是本类实例
        frm.grid()

        # 实际接收输入的变量表  
        self._varlist = []                          

        # 设置窗口上部的输入框及其标签
        i = 0
        for title in entries:
            v = self._build(frm, i, title)
            self._varlist.append(v)     #将 StringVar 对象添加到 _varlist 中
            i += 1
        
        # 设置窗口下部的按钮
        frm = tk.Frame(self, relief=tk.SUNKEN)
        frm.grid(sticky=tk.EW)
        but1 = tk.Button(frm, text=button_label, width=8, command=self._input_data)
        but1.grid(column=0, row=0, padx=16, pady=1)
        but2 = tk.Button(frm, text='结束', width=8, command=self.master.destroy)
        but2.grid(column=1, row=0, padx=16, pady=1)



    def _build(self, frm, i, lname):
        """创建一个输入项，包括标签和输入框，并返回与输入框关联的 StringVar 对象。
        参数:
            frm:  包含输入项的 Frame。
            i:    输入项的行号。
            lname: 输入项的标签文本。
        """
        # 创建标签，显示输入项的名称，并将其放置在网格布局的第 i 行，第 0 列
        label = tk.Label(frm, text=lname, anchor=tk.W)
        label.grid(row=i, column=0, sticky=tk.EW+tk.W)
        v = tk.StringVar()      # 创建 StringVar 对象，用于绑定输入框的值
        # 创建输入框，将其与 StringVar 对象绑定，并放置在网格布局的第 i 行，第 1 列
        entry = tk.Entry(frm, textvariable=v, justify=tk.RIGHT)
        entry.grid(row=i, column=1)
        return v
    


    def _input_data(self):
        """处理用户输入，调用回调函数并根据返回值决定是否清空输入框或显示错误消息。"""
        message = self._callback([v.get() for v in self._varlist])          # _callback，即：回调函数， 它指向源函数的文件中的函数
        if not message:
            for v in self._varlist: v.set("")       # 清空所有输入框，准备接受新的输入
        else:
            mb.showerror("输入错误", message)



# # 如果独立调用本文件，执行以下代码， 这不是整个程序的入口，仅仅是本模块调试运行的启动接口
# InputWin().mainloop()