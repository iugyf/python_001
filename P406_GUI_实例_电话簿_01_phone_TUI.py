# 第一个文件：基于正文交互的UI模块

help_info = """电话簿命令（请输入数字）：
                1. 添加新联系人
                2. 给定姓名查找电话号码
                3. 给定电话号码查找姓名
                4. 存储当前电话簿
                0. 结束工作
                """

class UI():
    def __init__(self, host):
        self._host = host   # 这个 “host” 就是 “Phonebook” 类实例对象
        self._commands = {'1': self.add,
                          '2': self.lookup_name,
                          '3': self.lookup_num,
                          '4': self.save_phonebook}
    
    def start(self, load_ok):
        if not load_ok:
            print("cannot find phonebook with give file name.\n" "begin from an empty phonebook.""")
        print(help_info)
        
        # 主循环
        while True:
            n = input('next command:')
            if n == '0':
                yesno = input('结束使用(yes/no)?')
                if yesno.lower() in {'yes', 'y'}: return    # lower() 将字母小写
                continue
            try:
                self._commands[n]()     # 数据驱动技术, 即：根据上面_commands字典中下标对应的字符串，来调用函数
            except Exception as ex:
                print(ex)
                print(help_info)

    def add(self):
        name = input('联系人姓名：')
        num = input("电话号码：")
        info = self._host.add(name, num)        # ._host已关联 “Phonebook” 类实例对象，  后面跟.add是在那个类中的方法
        if info: print(info)
    
    def lookup_name(self):
        name = input("请输入姓名：")
        entry = self._host.lookup_name(name)
        if entry: print(*entry)         # “*”：允许输入多个参数
        else: print('找不到这个联系人。')
        
    def lookup_num(self):
        num = input('电话号码：')
        entry = self._host.lookup_num(num)
        if entry: print(*entry)
        else: print('找不到这个电话号码。')

    def save_phonebook(self):
        self._host.save()
