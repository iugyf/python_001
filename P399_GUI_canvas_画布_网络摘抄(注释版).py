# 通义千问2025-1-6
# 注释版

import tkinter as tk

class CanvasWin(tk.Frame):
    def __init__(self):
        """初始化窗口和小部件"""
        # 调用父类（tk.Frame）的构造函数，确保 Frame 的初始化
        tk.Frame.__init__(self)
        
        # 设置主窗口的标题为 "cavas window"
        self.master.title("cavas window")
        
        # 使用 grid() 方法将当前 Frame 放置在主窗口中
        self.grid()

        # 创建一个 Canvas 小部件，设置宽度为 380 像素，高度为 180 像素
        # 并将其放置在当前 Frame 中
        can = self.can = tk.Canvas(self, width=380, height=180)
        self.can.grid()
        
        # 加载一张图片，文件名为 'P399_图标.png'，并将其存储在 self._image 中
        # 注意：确保该图片文件存在于当前工作目录中，否则会引发 FileNotFoundError
        self._image = tk.PhotoImage(file='P399_图标.png')

        # 在 Canvas 上绘制各种图形元素：
        # 1. 创建一个弧形（arc），左上角坐标 (10, 10)，右下角坐标 (50, 50)
        x1 = can.create_arc(10, 10, 50, 50)

        # 2. 创建一个椭圆（oval），左上角坐标 (60, 10)，右下角坐标 (150, 60)
        x2 = can.create_oval(60, 10, 150, 60)

        # 3. 创建一个矩形（rectangle），左上角坐标 (160, 10)，右下角坐标 (240, 60)
        x3 = can.create_rectangle(160, 10, 240, 60)

        # 4. 在 Canvas 上显示之前加载的图片，图片的中心点位于 (300, 50)
        x4 = can.create_image(300, 50, image=self._image)

        # 5. 创建一条折线（line），经过多个点 (10, 60), (20, 140), (80, 80), (70, 130)
        x5 = can.create_line(10, 60, 20, 140, 80, 80, 70, 130)

        # 6. 创建一段文本（text），文本内容为 "hello, beijing"，位置在 (60, 165)
        x6 = can.create_text(60, 165, text='hello, beijing')

        # 7. 创建一个多边形（polygon），顶点坐标为 (110, 100), (120, 150), (200, 140), (180, 80)
        x7 = self.can.create_polygon(110, 100, 120, 150, 200, 140, 180, 80)

        # 创建一个新的 Frame 小部件，作为 Canvas 内的一个子窗口
        # 设置边框宽度为 5 像素，边框样式为凸起（RAISED）
        frm = tk.Frame(can, borderwidth=5, relief=tk.RAISED)
        
        # 在 Canvas 上创建一个窗口（window），将刚才创建的 Frame 放置在 (300, 150) 位置
        win = self.can.create_window(300, 150, window=frm)
        
        # 在 Frame 中添加一个 Label 小部件，显示文本 "i am here."
        tk.Label(frm, text='i am here.').grid()
        
        # 在 Frame 中添加一个 Button 小部件，按钮文本为 "move"，点击时调用 self._move 方法
        bn = tk.Button(frm, text='move', command=self._move)
        bn.grid(sticky=tk.W + tk.E)  # 按钮占据整个 Frame 的宽度

        # 将所有创建的图形对象的 ID 存储在一个列表中，方便后续操作
        self.objs = [x1, x2, x3, x4, x5, x6, x7]

    def _move(self):
        """移动 Canvas 上的图形对象"""
        # 移动第一个图形对象（弧形），向右移动 5 像素，向下移动 1 像素
        self.can.move(self.objs[0], 5, 1)
        
        # 移动第二个图形对象（椭圆），向左移动 1 像素，向下移动 3 像素
        self.can.move(self.objs[1], -1, 3)

# 创建 CanvasWin 实例，并启动主事件循环
CanvasWin().mainloop()





############################################################################3333
# 代码功能概述
# 窗口和框架的创建：
    # CanvasWin 继承自 tk.Frame，表示这是一个包含其他小部件的容器。
    # self.master.title("cavas window") 设置了主窗口的标题为 "cavas window"。
    # self.grid() 将 Frame 放置在主窗口中，使用 grid 布局管理器。
# Canvas 小部件的创建：
    # tk.Canvas(self, width=380, height=180) 创建了一个宽度为 380 像素、高度为 180 像素的画布（Canvas），用于绘制图形和显示图像。
    # self.can.grid() 将 Canvas 放置在当前 Frame 中。
# 加载图片：
    # tk.PhotoImage(file='P399_图标.png') 加载了一张 PNG 格式的图片，并将其存储在 self._image 中。
    # 确保该图片文件存在于当前工作目录中，否则会抛出 FileNotFoundError。
# 绘制图形：
    # 使用 create_arc、create_oval、create_rectangle、create_image、create_line、create_text 和 create_polygon 方法在 Canvas 上绘制了多种图形元素：
    # 弧形 (create_arc)
    # 椭圆 (create_oval)
    # 矩形 (create_rectangle)
    # 图像 (create_image)
    # 折线 (create_line)
    # 文本 (create_text)
    # 多边形 (create_polygon)
# 嵌入 Frame 和小部件：
    # tk.Frame(can, borderwidth=5, relief=tk.RAISED) 创建了一个带有边框的 Frame，并将其嵌入到 Canvas 中。
    # self.can.create_window(300, 150, window=frm) 在 Canvas 上创建了一个窗口，将 Frame 放置在 (300, 150) 位置。
    # 在 Frame 中添加了一个 Label 显示文本 "i am here."，以及一个 Button，按钮文本为 "move"，点击时调用 _move 方法。
# 图形对象的移动：
    # _move 方法用于移动 Canvas 上的图形对象。每次点击 "move" 按钮时，弧形和椭圆会根据指定的偏移量移动。
# 主事件循环：
    # CanvasWin().mainloop() 启动了主事件循环，等待用户与 GUI 进行交互。
# 关键点
    # Canvas 是 tkinter 中用于绘制图形和显示图像的小部件。它提供了多种方法来创建不同的图形元素，如弧形、椭圆、矩形、折线、文本等。
    # create_window 方法允许你在 Canvas 上嵌入其他小部件（如 Frame、Button 等），从而实现更复杂的布局。
    # move 方法可以用于动态移动 Canvas 上的图形对象，参数是对象的 ID 和水平、垂直方向上的偏移量。
# 注意事项
    # 图片路径：     确保 P399_图标.png 文件存在于当前工作目录中，或者提供正确的绝对路径。如果图片不存在，程序会抛出 FileNotFoundError。
    # 图形对象的 ID：create_* 方法返回的是图形对象的 ID，这些 ID 可以用于后续的操作，如移动、删除或修改图形。
    # 事件循环：     mainloop() 是 tkinter 应用程序的主事件循环，它会持续监听用户的输入并响应事件。
                 #  你需要确保 mainloop() 是最后一个执行的语句，以保持窗口打开。