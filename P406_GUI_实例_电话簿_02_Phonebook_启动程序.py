# 第二个文件：电话簿功能模块设计与实现，同时也是程序启动文件    


######################################################################################
"""
关于程序的启动：

有两种启动方式:1. 基于正文交互的UI模块。
                 使用到的文件: P406_GUI_实例_电话簿_01_phone_TUI.py
                              P406_GUI_实例_电话簿_02_Phonebook.py
              2. 基于图形界面的UI
                 使用到的文件:P406_GUI_实例_电话簿_02_Phonebook.py
                             P406_GUI_实例_电话簿_03_GUI模块.py
                             P406_GUI_实例_电话簿_04_GUI_UI图形界面.py

其中: “P406_GUI_实例_电话簿_02_Phonebook.py” 是负责功能实现，所以两种界面都会用到。
      程序的入口也在该文件中 “Phonebook” 类

总结: 也就是说用哪个UI做头文件, 那个UI的模式就是启动模式
"""

# 二选一
# from P406_GUI_实例_电话簿_01_phone_TUI import UI      # 基于正文交互的UI模块
from P406_GUI_实例_电话簿_04_GUI_UI图形界面 import UI    # 基于图形界面的UI
#######################################################################################

import pickle


class Phonebook():
    def __init__(self, fbfile):     # fbfile: 是从程序启动时用户输入的 “电话簿” 文件名参数



        #----------------------------------------------------------------
        # 这里调用哪个头文件的UI，就启动哪种用户模式(图形界面 或 正文交互)。   调用 “UI” 界面类，将自身(self)当成参数传过去
        self._ui = UI(self)  
        #----------------------------------------------------------------
        
        
        self._fbfile = fbfile   # 电话簿文件
        self._loadok = True     # 标志：是否打开成功旧电话簿

        # 打开旧电话簿
        try:
            with open(fbfile + '.pickle', 'rb') as inf:
                self._phonebook = pickle.load(inf)      # 加载文件数据
        except:
            self._phonebook = {}
            self._loadok = False

        self._ui.start(self._loadok)        # 程序开始，传入参数：成功打开文件的标志(True)

    #########################################################################
    # 以下四个是程序功能的具体实现
        
    # 添加新联系人
    def add(self, name, num):
        if name in self._phonebook:
            return '名字重复'
        if not num.isdigit():
            return '电话号码包含非数字字符'
        self._phonebook[name] = num
    
    # 根据名字查找联系人
    def lookup_name(self, name):
        try:
            num = self._phonebook[name]
            return (name, num)
        except: return None

    # 根据号码查找联系人
    def lookup_num(self, num):
        for name, n in self._phonebook.items():
            if n == num: return (name, num)
        return None
    
    # 保存
    def save(self):
        with open(self._fbfile + '.pickle', 'wb') as outf:
            pickle.dump(self._phonebook, outf)





#----------------------------------------------------------------
# 程序启动，实际上启动哪种UI界面，取决于：选择上面的哪个头文件
Phonebook("P406_电话簿")
#----------------------------------------------------------------