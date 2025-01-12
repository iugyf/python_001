import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

class SimpleEditor(tk.Frame):
    def __init__(self):
        """A simple editor."""
        self.about = 'this ieditpr\nis developed by\nqzy'
        tk.Frame.__init__(self)
        self.master.title("simple editor")
        self.grid()

        # 文本框
        self.text = tk.Text(self, height=6, width=40)
        self.text.pack()

        top = self.winfo_toplevel()     # 获取顶层窗口
        self.menubar = tk.Menu(top)     # 建立窗口菜单条。   Menu是菜单条物件，它的第一个参数说明该物件的父物件是顶层窗口
        
        top['menu'] = self.menubar      # 将刚才建立的“菜单条”物件，加入“顶层窗口的菜单属性”中
        
        filemenu = tk.Menu(top)         # 建立file子菜单，它的物件是顶层窗口(top)
        filemenu.add_command(label='save', command=lambda: self.save(self.text))        # 在子菜单中加入菜单项
        filemenu.add_command(label='quit', command=lambda: top.destroy())
        self.menubar.add_cascade(label='file', menu=filemenu)           # 在 “菜单条” 设置下拉方式，并将刚才设置的 “子菜单” 加入 “菜单条”
        
        helpmenu = tk.Menu(self.menubar)    # 建立help子菜单
        helpmenu.add_command(label='about', command=lambda: mb.showinfo('about',self.about))
        self.menubar.add_cascade(label='help',menu=helpmenu)

    def save(self,text):
        data = text.get('0.0', tk.END)      # "0.0"， tk.END  ：从头到尾。     这里是将 "text" 文本框物件里所有的文字全部选中并获取
        filename = fd.asksaveasfilename(filetypes=[('text', '*.txt')], title='save as ...')
        if filename:
            writer = open(filename, 'w')
            writer.write(data)
            writer.close()
        else:
            mb.showwarning('warning','no filename is given')
    
SimpleEditor().mainloop()