from P338_客户管理程序_class_用类作为模块而非用类产生实例 import *

print("----------------------------------------------------------")
print("-----------以上的头文件自带的输出，别管它-----------------")
print("----------------------------------------------------------\n")

# VIP客户
class VIP(Customer):    # 父类：Customer
    _discount = 0.98    # _开头是本类私有数据，外部勿用

    def __init__(self, name, total):
        super().__init__(name)  # 初始化父类
        self._total = total

    def pay(self, price):
        paid = round(price * VIP._discount, 2)  # round：类似四舍五入的舍入法，第三个参数(2)是保留两个小数位
        #-------------------------------------------------------------
        # self._total += price      # 原书的总消费额是加上未折扣的价格
        self._total += paid         # 但我这里改成折扣后的实际消费额
        #-------------------------------------------------------------
        return paid
    
# VIP客户管理
class VIPCusManager(CustomerManager):   # 继承 “客户管理” 类
    _VIP_price = 1000.0     # VIP的门槛是1000元

    @classmethod    # 类方法
    def is_VIP(cls, name):  # 第一个参数是系统默认为：本类参数，指向本类自身
        if (name not in cls._customers or
            not isinstance(cls._customers[name], VIP)):
            return False
        return True
    
    @classmethod
    def pay_price(cls, name, price):
        if (not isinstance(name, str) or        # 名字或价格的数据类型不对，就抛出异常
            not isinstance(price, float)):
            raise TypeError("purshese error: ", name, price)
        if name not in cls._customers:      # 无此客户时，自动添加
            cls._customers[name] = Customer[name]
        customer = cls._customers[name]     # cls._customers 在父类中，是存储客户数据的字典
        paid = customer.pay(price)
        total = customer.total()
        if (not isinstance(customer, VIP) and 
            total > cls._VIP_price):
            cls._customers[name] = VIP(name, total)
        
        return paid

cm = VIPCusManager
cm.new_customer("fuck1")
cm.new_customer("fuck2")
cm.new_customer("fuck3")

print("fuck1 spends: ", cm.pay_price("fuck1", 250.00))
print("fuck1 spends: ", cm.pay_price("fuck1", 751.00))
print("fuck1 is VIP:", cm.is_VIP("fuck1"))
print("fuck1 spends: ", cm.pay_price("fuck1", 100.00))
print("fuck1 spends totally: ", cm.check_total("fuck1"))

