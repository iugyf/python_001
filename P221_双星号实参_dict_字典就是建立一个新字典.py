#双星号实参：它的值是一个自动建立的新字典

def print_data(x,**dic):
    print(x)
    for k, v in dic.items():        #'k':字典中的关键字     'v':该关键字对应的值
        print("{:6}{}".format(str(k)+":",v))

    print("--------------------------------")
    for k, v in dic.items():
        print("{:>16}{}".format(str(k)+":",v))      #  '>'是右对齐  ‘16’：是最小宽度
        print("{:<16}{}".format(str(k)+":",v))      #  '<'是左对齐

#输出的顺序是内部确定，不一定按关键字的字典序列排列
print_data("PUK:",mathljkwlwjkgowrjigm=114,phys=247,chem=336,bio=361)