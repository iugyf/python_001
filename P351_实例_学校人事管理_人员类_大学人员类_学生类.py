# 各类之间派生关系：object => Person(人员类) => UniPerson(大学人员类) => Student(学生类) => Undergratuate(本科生类)
#                                                     ||                    ||                     
#                                                      V                     V
#                                               Staff(教职工类)          MasterStudent(硕士生类)  =>  DoctorStudent(博士生类)


# 开关：用于下面的测试、打印、输出
switching_1 = 0



import datetime

# 自定义异常类
class PersonTypeError(TypeError):   # 人员，类型错误
    pass

class PersonValueError(ValueError): # 人员，值错误
    pass



########################################################################
########################################################################
# 公共基类: 人员类
class Person:
    # 初始化方法
    def __init__(self, name, sex, birthday):
        if not (isinstance(name, str) and
                sex in ("男","女")):
            raise PersonValueError("sex:",sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("wrong date:", birthday)

        self._name = name
        self._sex = sex
        self._birthday = birth
    

    
    # 以下返回数据接口，不变函数
    def name(self): return self._name
    def sex(self): return self._sex
    def birthday(self): return self._birthday
    def age(self): return (datetime.date.today().year -
                           self._birthday.year)
    
    # “<” 小于， 比较用，排序用
    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError("person comparison.")
        return self._name < another._name   # 根据姓名比较，返回布尔值
    
    # 特殊方法：在类外使用print(类实例1)，显示的值是调用本方法显示的,见原书P329-P331页
    def __str__(self):
        return " ".join((self._name, self._sex,         # join: 将后面的参数组成一个字符串，中间空格隔开，返回。
                         str(self._birthday))
                         )
    
    def details(self):
        return " ".join(("姓名：",self._name, 
                         "性别：",self._sex,        
                         "出生日期：",str(self._birthday))
                         )
    
    # 以下是变动函数，可改变类实例的数据
    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name error: ", name)
        self._name = name




if switching_1:   # 如果上面的开关打开，就测试，并输出
    print("\n\n-----------------------------人员类----------------------------------")
    p1 = Person("谢雨浩", "女", (1995,7,30))
    p2 = Person("汪力强", "男", (1990,2,17))
    p3 = Person("廖晓溪", "女", (1996,10,16))
    p4 = Person("李羽飞", "男", (1994,5,24))

    print(p1)
    print(p2)
    print(p3)
    print(p4)

    print("\nTest x.details():")
    print(p1.details())

    print("\nTest x.age():")
    print(p1.name(), p1.age(), "years")
    print(p2.name(), p2.age(), "years")

    print("\nTest__str__: ")
    print(p1)
    print(p2)

    # 排序：
    print("\nAfter sorting 根据姓名排序: ")
    plist1 = [p1, p2, p3, p4]   # 这里先将Person的实例组成一个表
    plist1.sort()               # 再用表的方法sort调用Person类中的"__lt__"特殊方法(即：<) 进行比较大小，返回比较后的顺序。
    for p in plist1:
        print(p)
        print(p.details())






########################################################################
########################################################################
# 大学人员类，继承自“人员类”
class UniPerson(Person):
    _pnum = 0

    def __init__(self, name, sex, birthday, ident):
        super().__init__(name, sex, birthday)
        self._id = ident
        UniPerson._pnum += 1

    # 输出学生和教员的id
    def id(self): return self._id

    # 特殊方法： <   （排序用）
    def __lt__(self, another):
        if not isinstance(another, UniPerson):
            raise PersonTypeError("person comparison: not UniPerson")
        return self._id < another._id
    
    #类方法
    @classmethod
    def num(cls): return UniPerson._pnum        # 显示本类总人数

    def __str__(self):
        return " ".join((self._id, super().__str__()))
    
    def detail(self):
        return ", ".join(("ID: " + self._id,
                          super().details()))
    







########################################################################
########################################################################
# 学生类，继承自：“大学人员类”
class Student(UniPerson):
    _id_num = 0     # 类属性：存储学生总人数, 也同时用作ID序号部分

    # 类方法， 设置学生ID，并累计学生人数
    @classmethod
    def _id_get(cls):
        cls._id_num += 1
        year = datetime.date.today().year       # 调用本方法的日期，就是学生入学日期
        return "1{:04}{:05}".format(year,cls._id_num)   # 格式化输出，分三段，第一段是“1”， 第二段：{:04} 取自日期里前四位：年    第三段："{:05}" 取自"cls._id_num"方法。
    
    # 初始化本类
    def __init__(self, name, sex, birthday, department):
        super().__init__(name, sex, birthday, 
                         Student._id_get())
        self._department = department   # 学院
        self._enroll_date = datetime.date.today()   # 入学时间
        self._courses = {}      # 成绩，  使用 {} 是定义成字典类型。   关键字是：课程名；   值是：成绩分数

    # 选课
    def set_course(self, course_name):
        self._courses[course_name] = None
    
    # 设置成绩 （要先选课，后再设置成绩)
    def set_score(self, course_name, score):
        if self._courses.get(course_name, False) is not None:       # 这里的get是＂字典类型＂自带方法(self._courses是字典类型)，
                                                                    # 用于获取关键字（course_name)对应的值，
                                                                    # 其中第二个参数False，作用是：如果关键字不存在，则返回False (默认返回None)。
            raise KeyError("set_score meets error. 要先选课，后设置成绩")
        self._courses[course_name] = score

    # 接口方法：输出数据
    def department(self): return self._department
    def en_year(self): return self._enroll_date.year
    def scores(self): return [(cname, self._courses[cname]) for cname in self._courses]
    def num(cls): return cls._id_num    # _id_num即是ID序号部分，也统计学生总人数

    # 覆盖父类同名方法
    def __str__(self):   
        return " ".join((super().__str__(),self.department(), str(self.en_year()), str(self.scores())))
    # 覆盖父类同名方法
    def details(self):
        return ", ".join((super().details(),     # 调用父类同名方法
                         "ID:", super().id(),      # 调用的是父类的方法, 奇怪的是为什么这个数字 不用做类型转换，难道它已经是str？
                         "院系：", self.department(),  
                         "入学：", str(self.en_year()),          # 要将int类型转换成str类型，否则报错
                         "成绩：", str(self.scores())))          # 要将int类型转换成str类型，否则报错    

    # 覆盖父类同名方法，  另：特殊方法： <   （排序用）
    def __lt__(self, another):
        if not isinstance(another, Student):
            raise PersonTypeError("person comparison: not Student")
        return self._department < another._department       # 根据院系比大小
    



if switching_1:   # 如果上面的开关打开，就测试，并输出
    print("\n-------------------------学生类-------------------------------")
    # 测试
    s1 = Student("张一", "男", (2000,1,1),"文学系")
    s2 = Student("张二", "男", (2000,2,1),"数学系")
    s3 = Student("张三", "男", (2000,3,1),"物理系")
    s4 = Student("张四", "男", (2000,4,1),"化学系")

    print("学生类总人数：", s1.num(), "\n")     # 随便任一实例，都能返回该类下的公共数据：总人数。

    print("学生信息明细：",s1.details(),'\n') 

    print(s1,'\n')           # 调用类中"__str__"方法

    # 给s1选课，并设成绩 （先选课，再调成绩，否则出错)
    print("选课前：\n\t", s1.department(), s1.en_year(), s1.scores()) 
    s1.set_course("语文")   # 选课
    s1.set_course("数学")
    s1.set_course("物理")
    s1.set_course("化学")
    s1.set_score("语文", 90)    # 设课程的成绩
    s1.set_score("数学", 80)
    s1.set_score("物理", 70)
    s1.set_score("化学", 70)
    print("选课后：\n\t",s1.department(), s1.en_year(), s1.scores())   


    # 排序：此类是根据院系排序
    print("\nAfter sorting 根据院系排序: ")
    slist1 = [s1, s2, s3, s4]   # 这里先将Student的实例组成一个表
    slist1.sort()               # 再用表的方法sort调用Student类中的"__lt__"特殊方法(即：<) 进行比较大小，返回比较后的顺序。
    for s in slist1:
        print(s)




