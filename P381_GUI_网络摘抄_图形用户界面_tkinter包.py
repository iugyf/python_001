import tkinter as tk  # tk是tkinter的别名

# 创建主窗口
win = tk.Tk()

# 添加标签
tk.Label(win, text="Hello!").grid()     # grid()： tkinter 提供了三种常见的布局管理器：pack()、grid() 和 place()。
                                        # grid()： 它是一个非常灵活的布局管理器，适用于表格形式的布局。
                                        # 如果使用 pack() 或 place()，请确保只使用一种布局管理器，否则可能会导致布局混乱。

# 添加输入框
tk.Entry(win).grid()

win.geometry("300x200")  # 设置窗口大小为 300x200 像素
win.title("My Tkinter App")  # 设置窗口标题


# 窗口关闭事件：   如果你想在用户关闭窗口时执行某些操作（例如保存数据或显示提示信息），可以绑定窗口的关闭事件。
def on_closing():
    print("Window is closing")
    win.destroy()

win.protocol("WM_DELETE_WINDOW", on_closing)


# 启动主事件循环:  这一段代码是窗口建立最后的代码，有关窗口的设定要执行在它之前，它一旦执行，其它对窗口的设定要么无效，要么异常。
win.mainloop()   # 在 tkinter 中，主事件循环是必须的，它负责处理用户的输入、窗口更新等任务。 如果没有启动主事件循环，窗口将不会显示。
                 # 因为程序会在创建窗口后立即结束，而不会等待用户交互或显示窗口，程序也不会响应任何事件。 


