#P222_字典_通过拆分字典的方式为函数提供一组关键字(字典的关键字字段)实参

def print_them(math, phys, chem, **others):
    form1="{:6}{}"
    print(form1.format("math:",math))
    print(form1.format("phys:",phys))
    print(form1.format("chem:",chem))
    print("others:",others)

#uni={"bio":234,"fuck":666,"chem":336, "math":114, }            #如果传入的字典中没有对应的实参，会报错，此处就没有 "phys":247
uni = {"bio":234,"fuck":666,"chem":336, "math":114, "phys":247, "ak47":4747}           

print_them(**uni)       #将字典当成实参传入函数，字典会被拆分，其中字典的关键字字段会与函数的形参名匹配，匹配后的值就是传入函数的值
                        #！！！传入的参数会按关键字匹配，与字典中排列顺序无关。没匹配上的会存入函数最后新建的一个字典中
print("uni顺序：",uni)  