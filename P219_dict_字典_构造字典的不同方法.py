#构造字典：math是关键字，114是值
dic1={'math': 114, 'phys': 247}    
print(dic1)


#空字典
dic={}     
print(dir)

#用类型名dict构造字典
faculty = dict([('math',114),('phys',247),('chem',306)])        #dict(二元组）构造方法   另外：表是可变对象，它之内必须是不变对象（比如元组）才能构造字典
print(faculty)


#用字符串构造字典
faculty_2 = dict(math=114, phys=247, chem=306)
print(faculty_2)