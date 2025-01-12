# 各类之间派生关系：object => Person(人员类) => UniPerson(大学人员类) => Student(学生类) => Undergratuate(本科生类)
#                                                     ||                    ||                     
#                                                      V                     V
#                                               Staff(教职工类)          MasterStudent(硕士生类)  =>  DoctorStudent(博士生类)


from P351_实例_学校人事管理_人员类_大学人员类_学生类 import *


# 开关：用于下面的测试、打印、输出
switching_2 = 0

########################################################################
########################################################################
# 本科生类，继承自：“学生类”
class Undergraduate(Student):
    _us_num = 0     # 本科生人数总计

    def __init__(self, name, sex, birthday, department, sclass):
        super().__init__(name, sex, birthday, department)
        self._class = sclass  # 班级
        Undergraduate._us_num += 1      # 用类名，做类属性。（如果用self，则是实例属性，不能统计所有的实例)
    
    # 覆盖父类同名方法
    def details(self):
        return ", ".join((super().details(),
                          "班级：" + self._class))
    # 覆盖父类同名方法
    def __str__(self):   
        return " ".join((super().__str__(),"班级：" + self._class))

    # 覆盖父类同名方法，  另：特殊方法： <   （排序用）
    def __lt__(self, another):
        if not isinstance(another, Undergraduate):
            raise PersonTypeError("person comparison: not Undergraduate")
        return self._class < another._class       # 根据班级比大小
    
    # 接口方法：输出数据
    def get_class(self): return self._class
    def get_us_num(self): return self._us_num




if switching_2:   # 如果上面的开关打开，就测试，并输出
    print("\n-------------------------本科生类-------------------------------")
    # 测试
    us1 = Undergraduate("李一", "男", (2000,1,1),"文学系","四班")
    us2 = Undergraduate("李二", "男", (2000,2,1),"数学系","三班")
    us3 = Undergraduate("李三", "男", (2000,3,1),"物理系","二班")
    us4 = Undergraduate("李四", "男", (2000,4,1),"化学系","一班")
    print("本科生人数： ", us1.get_us_num())

    print("本科生信息明细：")
    print(us1.details())
    print(us2.details())
    print(us3.details())
    print(us4.details())

    print("\n")
    print(us1,'\n')           # 调用类中"__str__"方法

    # 给us1选课，并设成绩 （先选课，再调成绩，否则出错)
    print("选课前：\n\t", us1.department(), us1.en_year(), us1.scores(),us1.get_class()) 
    us1.set_course("语文")   # 选课
    us1.set_course("数学")
    us1.set_course("物理")
    us1.set_course("化学")
    us1.set_score("语文", 90)    # 设课程的成绩
    us1.set_score("数学", 80)
    us1.set_score("物理", 70)
    us1.set_score("化学", 70)
    print("选课后：\n\t",us1.department(), us1.en_year(), us1.scores(),us1.get_class())   

    print("\n班级：", us1.get_class())


    # 排序：此类是根据班级排序
    print("\nAfter sorting 根据班级排序: ")
    uslist1 = [us1, us2, us3, us4]   # 这里先将Undergraduate的实例组成一个表
    uslist1.sort()               # 再用表的方法sort调用Undergraduate类中的"__lt__"特殊方法(即：<) 进行比较大小，返回比较后的顺序。
    for us in uslist1:
        print(us)





########################################################################
########################################################################
# 硕士生类，继承自：“学生类”
class MasterStudent(Student):
    _num = 0
    def __init__(self, name, sex, birthday, department):
        super().__init__(name, sex, birthday, department)
        self._id = "5" + self._id[1:]       # 硕士生的id是以5开头，位数与学生的一样         self._id[1:]是取self._id列表中：第2位开始到最后一位结束
        self._supervisor = "Undetermined" # 导师未定
        self._field = "Undetermined"    # 研究领域未定

        # 在此类中判断：是不是由子类创建的实例.   
        # 这是为了 “不” 计算 “本类的子类：博士生”的人数
        # if isinstance(self,MasterStudent):    # 不能用这句判断，因为isinstance会包含子类，如果第一个参数是第二个参数的子类，也会返回True
        if type(self) is MasterStudent:
            MasterStudent._num += 1  # 这里要用类名做对象。因为此属性是“类属性”，而不是“本类中某个实例”的属性。
    
    # 类方法：返回本类所有实例的个数
    @classmethod    
    def get_num(cls):
        return cls._num
    
    # 覆盖父类同名方法
    def details(self):
        return ", ".join((super().details(),
                          "导师：" + self._supervisor,
                          "方向：" + self._field ))
    # 覆盖父类同名方法
    def __str__(self):   
        return " ".join((super().__str__(),"导师：" + self._supervisor, "方向：" + self._field ))

    # 覆盖父类同名方法，  另：特殊方法： <   （排序用）
    def __lt__(self, another):
        if not isinstance(another, MasterStudent):
            raise PersonTypeError("person comparison: not MasterStudent")
        return self._field < another._field       # 根据领域比大小
    
    # 接口方法：输出数据
    def get_supervisor(self): return self._supervisor
    def get_field(self): return self._field

    # 接口方法：可变接口   设置研究领域
    def set_field(self, sfield):
        self._field = sfield

    # 接口方法：可变接口   设置导师
    def set_supervisor(self, supervisor):
        # 暂时先不验证导师是不是“人员类”，因为教师这个子类还没建立
        # if not isinstance(supervisor, Person):
        #     raise PersonTypeError("person comparison.")        
        self._supervisor = supervisor




if switching_2:   # 如果上面的开关打开，就测试，并输出
    print("\n-------------------------硕士生类-------------------------------")
    # 测试
    ms1 = MasterStudent("王一", "男", (2000,1,1),"文学系")
    ms2 = MasterStudent("王二", "男", (2000,2,1),"数学系")
    ms3 = MasterStudent("王三", "男", (2000,3,1),"物理系")
    ms4 = MasterStudent("王四", "男", (2000,4,1),"化学系")

    print("硕士生信息明细：")
    print("硕士生总人数：", MasterStudent.get_num())
    print(ms1.details())
    print(ms2.details())
    print(ms3.details())
    print(ms4.details())

    print("\n")
    print(ms1,'\n')           # 调用类中"__str__"方法

    # 给ms1选课，并设成绩 （先选课，再调成绩，否则出错)
    print("选课前：\n\t", ms1.department(), ms1.en_year(), ms1.scores(), ms1.get_supervisor(),ms1.get_field()) 
    ms1.set_course("语文")   # 选课
    ms1.set_course("数学")
    ms1.set_course("物理")
    ms1.set_course("化学")
    ms1.set_score("语文", 90)    # 设课程的成绩
    ms1.set_score("数学", 80)
    ms1.set_score("物理", 70)
    ms1.set_score("化学", 70)
    print("选课前：\n\t", ms1.department(), ms1.en_year(), ms1.scores(), ms1.get_supervisor(),ms1.get_field()) 


    print("\n设置研究领域与导师，设置前：")
    mslist1 = [ms1, ms2, ms3, ms4]   # 这里先将MasterStudent的实例组成一个表
    for ms in mslist1:
        print(ms)

    ms1.set_field("4天文")
    ms2.set_field("3地理")
    ms3.set_field("2世道")
    ms4.set_field("1人心")
    ms1.set_supervisor("老师4")
    ms2.set_supervisor("老师3")
    ms3.set_supervisor("老师2")
    ms4.set_supervisor("老师1")
    print("设置后，根据领域排序: ")
    mslist1.sort()            # 排序：此类是根据领域排序   排序方法：用表的方法sort方法，调用MasterStudent类中的"__lt__"特殊方法(即：<) 进行比较大小，返回比较后的顺序。
    for ms in mslist1:
        print(ms)








########################################################################
########################################################################
# 博士生类，继承自：“硕士生类”
class DoctorStudent(MasterStudent):
    _num = 0

    def __init__(self, name, sex, birthday, department,
                 field, supervisor):
        super().__init__(name, sex, birthday, department)
        self._id = "8" + self._id[1:]       # 博士生的id是以8开头，位数与学生的一样         self._id[1:]是取self._id列表中：第2位开始到最后一位结束
        self._supervisor = supervisor
        self._field = field
        DoctorStudent._num += 1     # 博士生人数加1，这里要用类名计算，因为如果用self会计入“类中的某个实例”，而我要计的是这个类的“所有实例”
    # 其它方法沿用"硕士生类"的方法，没有改动

    # 类方法：获取博士生总人数
    @classmethod
    def get_num(cls):
        return cls._num



if switching_2:   # 如果上面的开关打开，就测试，并输出
    print("\n-------------------------博士生类-------------------------------")
    # 测试
    ds1 = DoctorStudent("赵一", "男", (2000,1,1),"文学系","4文学","导师1")
    ds2 = DoctorStudent("赵二", "男", (2000,2,1),"数学系","3历史","导师2")
    ds3 = DoctorStudent("赵三", "男", (2000,3,1),"物理系","2船舶","导师3")
    ds4 = DoctorStudent("赵四", "男", (2000,4,1),"化学系","1汽车","导师4")

    print("博士生信息明细：")
    print("博士生总人数：", DoctorStudent.get_num())
    print(ds1.details())
    print(ds2.details())
    print(ds3.details())
    print(ds4.details())

    print("\n")
    print(ds1,'\n')           # 调用类中"__str__"方法


    dslist1 = [ds1, ds2, ds3, ds4]   # 这里先将DoctorStudent的实例组成一个表
    for ds in dslist1:
        print(ds)
    print("\n根据领域排序：")
    dslist1.sort()            # 排序：此类是根据领域排序   排序方法：用表的方法sort方法，调用DoctorStudent类中的"__lt__"特殊方法(即：<) 进行比较大小，返回比较后的顺序。
    for ds in dslist1:
        print(ds)








########################################################################
########################################################################
# 教职工类，继承自：“大学人员类”（原书代码错误的写成Person类）
class Staff(UniPerson):
    _id_num = 0

    @classmethod    # 类方法, 第一个参数要代表类自身，即：cls  (而不是实例：self)
    def _id_get(cls, birthday):     # 设置ID，并统计教职工总人数
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year      # *birthday: 表示这个参数是个表，能拆解并传入任意多个参数，即每个表元素就是一个参数
        return "0{:04}{:05}".format(birth_year, cls._id_num)  #  "0{:04}{:05}" 其中：   “0”：显示0； 
                                                                                 # {:04}：显示日期的前4位； 
                                                                                 # {:05}：显示cls._id_num，不够5位的补0。
    
    # 初始化
    def __init__(self, name, sex, birthday,entry_date = None):
        super().__init__(name, sex, birthday,
                         Staff._id_get(birthday))
        
        # 设定入职日期，如果创建该人员资料时未输入，则默认为创建当日为入职日期
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("wrong date:", 
                                       entry_date)
        else:
            self._entry_date = datetime.date.today()

        self._salary = 1720     # 默认最低工资
        self._department = "未定"
        self._position = "未定"     # 职位

    # 设置工资
    def set_salary(self, amount):
        # if not isinstance(amount, int):     # isinstance检查类型时，如果amount是int的子类，也会返回True.  
                                              # 所以若要完全匹配int类型，就要用更严格的type语句
        #     raise TypeError("工资数据类型错误！")
        if not type(amount) is int:
            raise TypeError("工资数据类型错误！")
        self._salary = amount

    # 设置职位
    def set_position(self, position):
        self._position = position
    
    # 设置院系
    def set_department(self, department):
        self._department = department
    
    # 返回工资
    def get_salary(self):
        return self._salary

    # 返回职位
    def get_position(self):
        return self._position
    
    # 返回院系
    def get_department(self):
        return self._department
    
    # 类方法： 返回教职工总人数
    @classmethod    
    def get_num(cls):      
        return cls._id_num
    
    # 覆盖父类同名方法
    def details(self):
        return ", ".join((super().details(),
                         "入职日期：" + str(self._entry_date),
                         "院系：" + self._department,
                         "职位：" + self._position,
                         "工资：" + str(self._salary)))
    
    # 特殊方法： <      排序用"<"符
    def __lt__(self, another):
        if not isinstance(another, Staff):
            raise PersonTypeError("person comparison: not Staff")
        return self._position < another._position       # 根据职位比大小
    
    # 特殊方法： 直接输出实例信息
    def __str__(self):   
        return " ".join((super().__str__(),
                         "入职日期：" + str(self._entry_date),
                         "院系：" + self._department,
                         "职位：" + self._position,
                         "工资：" + str(self._salary)))
    







if switching_2:   # 如果上面的开关打开，就测试，并输出
    print("\n-------------------------教职工类-------------------------------")
    # 测试
    sta1 = Staff("老师一", "男", (1980,1,1))
    sta2 = Staff("老师二", "男", (1970,2,1))
    sta3 = Staff("老师三", "男", (1990,3,1))
    sta4 = Staff("老师四", "男", (2000,4,1))

    print("教职工信息明细：")
    print("教职工总人数：", Staff.get_num()) # 返回该类共同的数据, 要用类名做函数
    print(sta1.details())
    print(sta2.details())
    print(sta3.details())
    print(sta4.details())

    print("\n")
    # 设置工资
    sta1.set_salary(10086)
    sta2.set_salary(20086)
    sta3.set_salary(30086)
    sta4.set_salary(40086)    
    # 设置职位
    sta1.set_position("校长")
    sta2.set_position("校长他爹")
    sta3.set_position("大大")
    sta4.set_position("职位1")
    # 设置院系
    sta1.set_department("院系1")
    sta2.set_department("院系2")
    sta3.set_department("院系3")    
    sta4.set_department("院系4")

    print("\n设置完工资，职位，院系后，再显示一次：")
    sta_list1 = [sta1, sta2, sta3, sta4]   # 这里先将Staff的实例组成一个表
    for sta in sta_list1:
        print(sta)          # 调用类中"__str__"方法

    print("\n根据职位排序：")
    sta_list1.sort()            # 排序：此类是根据"职位"排序   排序方法：用表的方法sort方法，调用Staff类中的"__lt__"特殊方法(即：<) 进行比较大小，返回比较后的顺序。
    for sta in sta_list1:
        print(sta)



    # 博士生类是硕士生类的子类，统计人数时会不会错，做以下检查。
    print("\n\n硕士生总人数（是否包含博士生人数？）：",MasterStudent.get_num())
    print("博士生总人数：",DoctorStudent.get_num())