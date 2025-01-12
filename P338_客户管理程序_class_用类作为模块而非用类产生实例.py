# 客户类
class Customer:
    def __init__(self, name):
        self._name = name
        self._total = 0.0  # 客户消费的总金额

    def pay(self, price):
        self._total += price
        return price
    
    def total(self):
        return self._total
    

# 将此类作为程序模块使用，而非用它来生产实例
class CustomerManager:
    _customers= {}  # 字典，用于记录所有的客户
    
    try:
        @classmethod    # 类方法
        def new_customer(cls, name):    # cls：类属性，是类默认的参数，它是第一个参数，名字可改，不过一般用它，
            if not isinstance(name, str):
                raise TypeError("create record error:", name)
            cls._customers[name] = Customer(name)

        @classmethod
        def pay_price(cls, name, price):
            if(not isinstance(name, str) or
            not isinstance(price, float)):
                raise TypeError("purshese error: ", name, price)
            if name not in cls._customers:
                cls._customers[name] = Customer(name)
            return cls._customers[name].pay(price)
        
        @classmethod
        def check_total(cls, name):
            if name not in cls._customers:
                raise KeyError("no this customer: ", name)
            return cls._customers[name].total()
    
    except Exception as ex:
        print(ex)

cm = CustomerManager    # 这是不用括号，说明cm不是该类创建的实例，而是指向类本身
cm.new_customer("Li Lei")
cm.new_customer("Han Meimei")
cm.new_customer("Zhang Shan")

print("Li Lei spends: ", cm.pay_price("Li Lei", 12.38))
print("Li Lei spends: ", cm.pay_price("Li Lei", 18.35))
print("Li Lei spends: ", cm.pay_price("Li Lei", 31.05))
print("Li Lei spends totally: ", cm.check_total("Li Lei"))


# print("Fuck spends totally: ", cm.check_total("Fuck"))        
    # 这里会抛出异常，而且处理完异常不会回原代码之下一行继续执行，
    # 这是因为： 在 Python 中，try-except 结构的设计原则是：
    # 一旦 try 块中抛出异常并被捕获，try 块中的剩余代码将被跳过，程序会从 except 或 finally 块之后的代码继续执行。
    # 因此，Python 并没有内置的机制让异常处理结束后自动返回到 try 块中抛出异常的地方继续执行。


print("new customer XYZ pay 10086", cm.pay_price("XYZ", 10086.00))