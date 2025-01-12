from P351_实例_学校人事管理_本科生类_硕士类_博士类_教职工类 import Undergraduate



# 开关：用于下面的测试、打印、输出
switching_3 = 1



# “本科生登记表”类， 这是个类控制台，只创建一个实例即可，控制所有登记数据。
class Register():
    def __init__(self):
        self._entries = {}  # 创建字典，用于学生登记信息。  关键字:student.id(),即：本科生的id号；   值：Undergraduate(本科生类)的实例
    
    # 特殊方法：显示字典中数据个数
    def __len__(self):
        return len(self._entries)
    
    # 从下标获取字典数据，这里的下标号就是关键字，也就是本科生的id
    def __getitem__(self, sid):
        if not isinstance(sid, str):
            raise ValueError("Student ID, 登记时出错")
        if sid not in self._entries:
            raise KeyError("No this student id, 登记时出错")
        return self._entries[sid]
    
    # 添加数据到字典
    def add(self, student):
        if not isinstance(student, Undergraduate):
            raise ValueError("not a student")
        self._entries[student.id()] = student       # .id()方法：见“大学人员类”里有定义此方法

    # 特殊方法：判断item是否在sid中, 就是类外使用的in语句
    def __contains__(self, sid):
        return sid in self._entries
    
    # 特殊方法：设置直接输出实例的信息
    def __str__(self):
        return "\n".join(self._id_names())
    

    # 特殊方法: 创建生成器函数，返回一个迭代器，用于逐个显示id
    def __iter__(self):
        for sid in sorted(self._entries):
            yield self._entries[sid]


    # 自定义方法: 生成器函数，返回一个迭代器, 用于逐个显示注册信息
    def _id_names(self):
        for st in self.__iter__():
            yield st.id() + ', ' + st.name()        # .name()定义在Person(人员类)中

    # 设置输出格式
    st_display = "学号:{}, 姓名:{:>4}, 性别:{}, 出生年月日:{}\n 院系:{:>8}, 入学:{:6}, 平均成绩:{:4.1f} 共{}门课"
    # 输出
    def display(self,sid):
        if sid not in self._entries:
            raise KeyError("No this sutdent id: 没有这个学生")
        st = self._entries[sid]
        scores = [cs[1] for cs in st.scores()]      # .scores()此方法在学生类中定义，是一个字典类型：关键字是课程名，值是分数。 
                                                    # 这里cs[1]就是返回分数，   这里scores是将所有的“分数”作成表
        average = sum(scores)/len(scores) if scores else 0         # 这里如果scores是空表，则返回：平均分为0
        # if scores:
        #     if type(scores) is int:
        #         average = sum(scores)/len(scores)
        #     else:
        #         average = 0 
        # else:
        #     average = 0
        
        print(Register.st_display.format(               # 使用st_display格式输出，共8个参数
            st.id(), st.name(), st.sex(), st.birthday(),
            st.department(), st.en_year(), average, len(scores)))




# ====================================================================================
    # 这是原书代码：用于设定成绩，但只能用于当前学号的学生设置，没在当前学号下试过。
    def record(self, course, scores):       # 此函数有问题，因为原书设定是要先设置课程名，之后才能加成绩分数
        entries = self._entries
        for sc in scores:
            try:
                entries[sc[0]].set_score(course, sc[1])       # set_score方法是在“学生类”中定义。    这里sc[0]是课程名； sc[1]是成绩分数
            except KeyError as ex:
                print("no this student id:", ex.args[0], '\n')

    # 这是自己编的代码，能设置对应学号的成绩
    def record_2(self, sid, course, scores):       # 此函数有问题，因为原书设定是要先设置课程名，之后才能加成绩分数
        entries = self._entries[sid]
        entries.set_score(course, scores)       # set_score方法是在“学生类”中定义。 
# ====================================================================================









##################################################################################################################3
if switching_3:   # 如果上面的开关打开，就测试，并输出
    print("\n-------------------------本科生登记表类-------------------------------")

    # 注册到Undergraduate(本科生类)
    r_us1 = Undergraduate("钱一", "男", (2000,1,1),"文学系","四班")    
    r_us2 = Undergraduate("钱二", "男", (1990,1,1),"数学系","三班")    

    # 给us1选课，并设成绩 （先选课，再调成绩，否则出错)
    r_us1.set_course("英语")   # 选课
    r_us1.set_course("俄语")
    r_us1.set_course("法语")
    r_us1.set_course("德语")
    # 给r_us2选课，并设成绩 （先选课，再调成绩，否则出错)
    r_us2.set_course("高数")   # 选课
    r_us2.set_course("线代")
    r_us2.set_course("拓扑")
    r_us2.set_course("数论")

    # 给r_us1设课程的成绩   
    r_us1.set_score("英语", 90)    
    r_us1.set_score("俄语", 80)
    r_us1.set_score("法语", 70)
    r_us1.set_score("德语", 70)
    print("---------------------------1-------------------------")
    print("选课后：\n\t",r_us1.department(), r_us1.en_year(), r_us1.scores(),r_us1.get_class())  
    print("---------------------------2-------------------------") 
    print(r_us1)


    # 在 “本科生登记表类” 中添加 “本科生类” 成员
    r1 = Register()     # 这个r1就是个控制台，控制所有成员实例。
    r1.add(r_us1)
    r1.add(r_us2)


    print("---------------------------3-------------------------")
    # 给r_us2设课程的成绩，r_us2的id号：1202500002，是事先找到的，没什么特别技巧，下次ID号一变，程序就玩蛋
    # 非原书原代码，原书原代码是：record() 它不能这样用
    r1.record_2("1202500002", "高数", 80)      
    r1.record_2("1202500002", "线代", 80)
    r1.record_2("1202500002", "拓扑", 70)
    r1.record_2("1202500002", "数论", 70)
    print("选课后：\n\t",r_us1.department(), r_us1.en_year(), r_us1.scores(),r_us1.get_class())   
    print(r_us2)

    print("---------------------------4-------------------------")
    print(len(r1))
    print(r_us1 in r1)
    print(r1)

    print("---------------------------5-------------------------")
    for x in r1:
        print(x)

    print("---------------------------6-------------------------")
    # 第一个参数是学号
    r1.display('1202500001')

    print("---------------------------7-------------------------")
    print(r1["1202500002"])

    print("---------------------------8-------------------------")
    # rnum = r1[0].key      # 这个语法不对，因为r1的下标不是从0到len(r1)的数字。 因为r1是字典，它的下标是关键字，也就是学生id
    # r1.display(rnum)