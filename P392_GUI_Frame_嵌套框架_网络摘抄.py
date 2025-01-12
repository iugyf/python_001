# 摘自：通义千问2025-1-4

# 你提供的代码中存在几个问题，导致程序无法正常运行。我们将逐一分析这些问题，并提供修复建议。

# 1. InputWin.labels 未定义
    # 问题：在 __init__ 方法中，代码尝试遍历 InputWin.labels，但 InputWin.labels 并没有在类中定义。这会导致 AttributeError，因为 Python 无法找到 InputWin 类的 labels 属性。
    # 解决方案：你需要在类中定义 labels 属性，或者在实例化时传递一个标签列表。你可以选择将 labels 定义为类属性或实例属性。
# 2. tk.entry 应为 tk.Entry
    # 问题：在 _build 方法中，entry = tk.entry(frm, ...) 应该是 entry = tk.Entry(frm, ...)。Entry 是 tkinter 中用于创建输入框的小部件，而 entry 不是有效的类名。
    # 解决方案：将 tk.entry 改为 tk.Entry。
# 3. label.grid(row=1, column=0, sticky=tk.E+tk.W) 的行号固定
    # 问题：在 _build 方法中，label.grid(row=1, column=0, sticky=tk.E+tk.W) 和 entry.grid(row=1, column=1) 的行号都是固定的 row=1。这意味着所有标签和输入框都会被放置在同一行，
        # 导致它们重叠在一起。
    # 解决方案：你应该使用动态的行号 row=i，以便每个标签和输入框都位于不同的行。
# 4. sticky=tk.E + tk.W 的写法不规范
    # 问题：sticky=tk.E + tk.W 的写法虽然可以工作，但更常见的写法是使用逗号分隔的参数，例如 sticky=(tk.E, tk.W) 或 sticky=tk.EW。
    # 解决方案：建议使用 sticky=tk.EW 或 sticky=(tk.E, tk.W)，以提高代码的可读性。
# 5. callback 参数的默认值
    # 问题：callback=lambda x:None 的默认值是一个 lambda 函数，它接受一个参数 x 但不返回任何值。虽然这不是错误，但如果你希望 callback 接受多个参数或有其他行为，可能需要调整这个默认值。
    # 解决方案：如果你不需要 callback 做任何事情，保持现有的默认值是可以的。如果你希望 callback 可以接受不同类型的参数，可以考虑使用 *args 或 **kwargs。
# 6. mainloop() 的调用位置
    # 问题：InputWin(callback=print).mainloop() 这行代码直接调用了 mainloop()，但这应该由 Tk 窗口管理器来调用，而不是 Frame。Frame 本身没有 mainloop() 方法。
    # 解决方案：你应该创建一个 Tk 实例，并将 InputWin 作为其子框架。然后调用 Tk 的 mainloop() 方法。


#################################################################################################################
# 修改后的代码

import tkinter as tk

class InputWin(tk.Frame):
    # 定义类属性 labels，包含标签文本
    labels = ["姓名", "年龄", "电话"]                             # 你可以根据需要添加更多标签

    def __init__(self, parent=None, callback=lambda x: None):
        """构建一个带边框的窗口。"""
        tk.Frame.__init__(self, parent)
        self._callback = callback
        self.master.title("数据录入")
        self.grid()

        frm = tk.Frame(self)                                     # 第一个框架：用于存储文本框与输入框
        frm.grid(sticky=tk.EW)                                   # 使用 sticky=tk.EW 使框架占据整个宽度

        # 创建按钮框架，并使其跨越两列
        button_frame = tk.Frame(self)                            # 第二个框架：用于存储按钮
        button_frame.grid(sticky=tk.EW, columnspan=2)

        # 创建“输入”按钮
        but1 = tk.Button(button_frame, text="输入", command=self._input_data)
        but1.grid(column=0, row=0, padx=32, pady=2)              # padx:x轴间距

        # 创建“结束”按钮
        but2 = tk.Button(button_frame, text="结束", command=self.master.destroy)
        but2.grid(column=1, row=0, padx=32, pady=2)

        self._varlist = []                                       # 表，用于接收输入框传入的数据
        for i, title in enumerate(InputWin.labels):              # enumerate：枚举类型，代码功能：0 "姓名", 1 "年龄", 2 "电话"
            v = self._build(frm, i, title)                       # 创建三组标签与输入框，并接收数据
            self._varlist.append(v)                              # 这里的 v 是tk.StrVar控制变量

    def _build(self, frm, i, lname):
        """构建标签和输入框。"""
        label = tk.Label(frm, text=lname, anchor=tk.W)
        label.grid(row=i, column=0, sticky=tk.EW)               # 使用动态行号 i

        v = tk.StringVar()                                      # 控制变量物件：字符串
        entry = tk.Entry(frm, textvariable=v, justify=tk.RIGHT) # justify=tk.RIGHT 右对齐       textvariable: 物件与其它物件交换信息的关键。不同物件关键同一控制变量时，它们的信息就是共享的
        entry.grid(row=i, column=1, sticky=tk.EW)               # 使用动态行号 i
        return v

    # "输入"按键调用这个方法
    def _input_data(self):
        """获取输入框中的数据并调用回调函数。"""
        data = [v.get() for v in self._varlist]     # get():获取关键字对应的值。  _varlist是表，此表存储的是StringVar控制变量。 而.get()方法从这个控制变量中获取值。
        self._callback(data)                        # 调用回调函数，传递数据
        for v in self._varlist:                     # v是GUI的字符串控件变量
            v.set("")                               # 清空输入框     因为前面“输入框”已经通过textvariable共享了此控件，所以对v的操作就会影响“输入框”已有的数据

# 创建主窗口并启动主事件循环
if __name__ == "__main__":
    root = tk.Tk()                          # 创建 Tk 主窗口
    app = InputWin(root, callback=print)    # 将 InputWin 作为 Tk 的子框架，并传入回调函数
    root.mainloop()                         # 启动主事件循环



# 代码解释
    # InputWin.labels：
        # 我们在类中定义了一个类属性 labels，它包含了一些标签文本（如 "姓名"、"年龄"、"电话"）。你可以根据需要修改或扩展这个列表。
    # _build 方法：
        # 在 _build 方法中，我们使用了动态的行号 row=i，确保每个标签和输入框都位于不同的行。这样可以避免它们重叠在一起。
        # sticky=tk.EW 使得标签和输入框占据整个单元格的宽度，使布局更加美观。
    # 按钮框架：
        # 我们为按钮创建了一个独立的框架 button_frame，并使用 columnspan=2 使其跨越两列。这样可以确保按钮居中显示，并且不会影响其他小部件的布局。
    # mainloop()：
        # 我们创建了一个 Tk 实例 root，并将 InputWin 作为 root 的子框架。然后调用 root.mainloop() 来启动主事件循环，而不是直接在 InputWin 上调用 mainloop()。
    # 回调函数：
        # callback 参数允许你在用户点击“输入”按钮时执行自定义的操作。在这个例子中，我们传入了 print 函数，因此当用户点击“输入”按钮时，输入的数据会打印到控制台。

# 运行效果
    # 当你运行这个程序时，会弹出一个窗口，窗口中有三个标签和对应的输入框（分别对应“姓名”、“年龄”、“电话”），以及两个按钮：“输入”和“结束”。
    # 用户可以在输入框中输入数据，点击“输入”按钮后，输入的数据会通过 callback 函数（在这个例子中是 print）输出到控制台。
    # 点击“结束”按钮会关闭窗口。

# 总结
    # 通过修复上述问题，代码现在可以正常运行，并且实现了预期的功能。你可以根据需要进一步扩展或修改代码，例如添加更多的标签和输入框，或者更改回调函数的行为。