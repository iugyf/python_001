# 第四个文件：图形界面UI    代码中的注释全是“通义千问”注释的


import tkinter as tk
import tkinter.messagebox as mb
from P406_GUI_实例_电话簿_03_GUI模块 import InputWin


# 图形界面的UI， 也就是主窗口
class UI(tk.Frame):
    """电话簿管理器的用户界面类。    
    该类继承自 `tk.Frame`，并使用 `InputWin` 类来处理用户输入(即建立子窗口)。它提供了添加联系人、查找联系人、保存电话簿和退出程序的功能。
    """    
    gnotes = ('欢迎使用电话簿\n\n请选择需要的操作')         # 静态变量，用于显示欢迎信息
    info_title = '电话簿信息'                             # 静态变量，用于消息框的标题

    def __init__(self, host):   
        """初始化电话簿管理器的用户界面。        
        参数:
            host: 电话簿的主机对象，负责处理电话簿的实际操作（如添加、查找、保存等）。
                  即：Phonebook类的实例对象，也是所有数据的基础，所有功能的实现
        """        
        # 构建并安置主窗口
        tk.Frame.__init__(self)                      
        self.master.title('电话簿管理器')            
        self.grid()                                
        
        self._host = host        # 保存传入的主机对象，即：Phonebook类的实例对象， 稍后用于调用电话簿的相关方法
        
        # 创建上半部分界面
        self._upper = tk.Frame(self)    
        self._upper.grid()  # 将上半部分界面放置在主窗口中        
        # 创建下半部分界面
        self._lower = tk.Frame(self)
        self._lower.grid()
        
        # 构建界面的上半部
        # 加载图标并创建一个标签显示图标
        self._image = tk.PhotoImage(file="P406_通讯录图标.png")
        title = tk.Label(self._upper, image=self._image)
        title.grid(row=0, column=0)  # 将图标放置在左上角
        # 创建一个标签显示欢迎信息
        note = tk.Label(self._upper, text=UI.gnotes, width=20, font=('Song', '16'))
        note.grid(row=0, column=1)  # 将欢迎信息放置在右上角
        
        # 构建界面的下半部
        # 定义一组按钮及其对应的命令
        ops = (                              # 二重元组数据类型
            ('添加联系人', self._add_entry),  # 添加联系人按钮
            ('查找', self._seach),            # 查找联系人按钮
            ('保存电话簿', self._save),       # 保存电话簿按钮
            ('结束使用', self.master.destroy) # 结束程序按钮，这个按钮的功能可直接实现，不用再建立子方法
        )        
        i = 0
        for name, op in ops:        # 遍历按钮定义，创建每个按钮并将其放置在下半部分界面中
            but = tk.Button(self._lower, text=name, command=op)
            but.grid(row=0, column=i, padx=10, pady=4, ipadx=4, ipady=2)  # 设置按钮的布局和间距
            i += 1


    
    # '添加联系人'按钮的接口
    def _add_entry(self):
        """打开一个输入窗口，允许用户添加新的联系人。        
        使用 `InputWin` 类创建一个新的窗口，用户可以在其中输入联系人的姓名和电话号码。输入完成后，调用 `_set_entry` 方法将数据添加到电话簿中。
        """        
        # 创建一个 `InputWin` 窗口，标题为“添加联系人”，包含两个输入项（姓名和电话号码），并指定回调函数为 `_set_entry`
        InputWin(           # InputWin是一个类，这里是创建这个类实例，该实例中会产生独立的子窗口供用户使用
            title='添加联系人',
            button_label='添加',
            entries=('姓名', '电话号码'),
            callback=self._set_entry        # 回调函数，这些函数的实现在本文件中，也就是说将本文件的函数传给 “InputWin” 类的实例，当该实例调用这些函数时，还会回到本文件中
        ).mainloop()  # 启动输入窗口的事件循环



    # '添加联系人'按钮的回调函数，它会被传给“InputWin”类，被那个类调用。 
    # 实现上本方法就是个中间商，它被“InputWin”类调用，之后它会去调用_host（也就是Phonebook类的实例）真正实现功能。
    # 即：它就是位于 “主窗口” 上，连接 “子窗口” 与 “底层功能模块” 的接口
    def _set_entry(self, entry):
        """处理用户输入的联系人信息，并将其添加到电话簿中。        
        参数:
            entry: 用户输入的联系人信息，格式为 [姓名, 电话号码]。        
        返回:
            如果输入格式错误或添加失败，返回错误信息；否则返回 None。
        """        
        # 检查输入是否包含两个元素（姓名和电话号码）
        if len(entry) != 2:
            return '输入格式错误'        
        # 调用主机对象的 `add` 方法，尝试将联系人添加到电话簿中
        res = self._host.add(*entry)        
        # 如果添加成功，弹出消息框提示用户
        if not res:
            mb.showinfo(UI.info_title, '联系人已加入')        
        # 返回主机对象的 `add` 方法的结果（如果有错误信息）
        return res
    

    # '查找'按钮的接口
    def _seach(self):
        """打开一个输入窗口，允许用户查找联系人。        
        使用 `InputWin` 类创建一个新的窗口，用户可以在其中输入联系人的姓名或电话号码。输入完成后，调用 `_lookup` 方法进行查找。
        """        
        # 创建一个 `InputWin` 窗口，标题为“检索名字号码”，包含两个输入项（姓名和电话号码），并指定回调函数为 `_lookup`
        InputWin(        # InputWin是一个类，这里是创建这个类实例，该实例中会产生独立的子窗口供用户使用
            title='检索名字号码',
            entries=('姓名', '电话号码'),
            button_label='检索',
            callback=self._lookup  # 回调函数，这些函数的实现在本文件中，也就是说将本文件的函数传给 “InputWin” 类的实例，当该实例调用这些函数时，还会回到本文件中
        ).mainloop()  # 启动输入窗口的事件循环


    # '查找'按钮的回调函数，调用原理与过程见上面其它的“回调函数”
    def _lookup(self, entry):
        """根据用户输入的姓名或电话号码查找联系人。        
        参数:
            entry: 用户输入的查找条件，格式为 [姓名, 电话号码]。        
        返回:
            如果查找成功，返回查找结果；如果查找失败，返回错误信息。
        """        
        # 检查用户是否提供了姓名或电话号码
        if entry[0] == '':
            if entry[1] == '':
                return '查询需提供名字或电话号码.'  # 如果两者都为空，返回错误信息            
            else:  # 给定电话号码检索联系人
                res = self._host.lookup_num(entry[1])  # 根据电话号码查找联系人
                if res:
                    mb.showinfo(UI.info_title, res)  # 如果找到，弹出消息框显示结果
                    return
                else:
                    return '没有这个电话号码.'  # 如果未找到，返回错误信息       
        else:
            if entry[1] == '':  # 给定人名检索电话号码
                res = self._host.lookup_name(entry[0])  # 根据姓名查找联系人
                if res:
                    mb.showinfo(UI.info_title, res)  # 如果找到，弹出消息框显示结果
                    return
                else:
                    return '没有这个联系人.'  # 如果未找到，返回错误信息
        
        # 用户提供了联系人与电话号码
        # res = self._host.lookup_num(entry[0])  # 根据姓名查找联系人。  原书这里有错，它将姓名的下标值，传入到查号码函数中
        res = self._host.lookup_name(entry[0])
        if not res:
            return '没有这个联系人.'  # 如果未找到，返回错误信息
        return '联系人号码是 ' + res[1]  # 如果找到，返回联系人的电话号码


    # “保存”按钮
    def _save(self):
        """保存当前电话簿到文件。        
        调用主机对象的 `save` 方法保存电话簿，并弹出消息框提示用户保存成功。
        """        
        self._host.save()  # 保存电话簿
        mb.showinfo(UI.info_title, '电话簿已保存')  # 弹出消息框提示用户



    # 这个start是从 “P406_GUI_实例_电话簿_02_Phonebook_启动程序” 调用的，也就是说这是“主窗口”的入口
    def start(self, load_ok):   
        """启动电话簿管理器的主事件循环。        
        参数:
            load_ok: 表示是否成功加载了电话簿文件。如果加载失败，弹出消息框提示用户。
        """        
        # 如果加载失败，弹出消息框提示用户
        if not load_ok:
            mb.showinfo(UI.info_title, '无法装入指定文件\n\n用空电话簿')        
        # 启动主事件循环，等待用户交互
        self.mainloop()


#######################################################################################
# 详细注释说明
# 1. 类定义与初始化
    # __init__ 方法：
    # tk.Frame.__init__(self)：调用父类 tk.Frame 的构造函数，初始化 Frame。
    # self.master.title('电话簿管理器')：设置主窗口的标题为“电话簿管理器”。
    # self.grid()：使用 grid 布局管理器将 Frame 放置在主窗口中。
    # self._host = host：保存传入的主机对象，稍后用于调用电话簿的相关方法（如添加、查找、保存等）。
    # self._upper 和 self._lower：分别创建上半部分和下半部分的界面，并使用 grid 布局管理器将它们放置在主窗口中。
    # self._image = tk.PhotoImage(file="P406_通讯录图标.png")：加载图标文件，并创建一个标签显示图标。
    # note = tk.Label(self._upper, text=UI.gnotes, ...)：创建一个标签显示欢迎信息，并将其放置在右上角。
    # ops：定义一组按钮及其对应的命令，包括“添加联系人”、“查找”、“保存电话簿”和“结束使用”。
    # for name, op in ops:：遍历按钮定义，创建每个按钮并将其放置在下半部分界面中，设置按钮的布局和间距。
# 2. _add_entry 方法
    # _add_entry 方法：
    # 打开一个 InputWin 窗口，允许用户输入联系人的姓名和电话号码。
    # 使用 InputWin 类创建一个新的窗口，标题为“添加联系人”，包含两个输入项（姓名和电话号码），并指定回调函数为 _set_entry。
    # 调用 mainloop() 启动输入窗口的事件循环，等待用户输入。
# 3. _set_entry 方法
    # _set_entry 方法：
    # 处理用户输入的联系人信息，并将其添加到电话簿中。
    # 检查输入是否包含两个元素（姓名和电话号码），如果格式错误，返回错误信息。
    # 调用主机对象的 add 方法，尝试将联系人添加到电话簿中。如果添加成功，弹出消息框提示用户；如果添加失败，返回错误信息。
# 4. _seach 方法
    # _seach 方法：
    # 打开一个 InputWin 窗口，允许用户输入联系人的姓名或电话号码。
    # 使用 InputWin 类创建一个新的窗口，标题为“检索名字号码”，包含两个输入项（姓名和电话号码），并指定回调函数为 _lookup