str_1 = "The {} of 2 + 3 is {}".format("result",2+5)        #format方法中：{}之内是替换域
print(str_1)

str_2 = "{{}}".format()      #format方法：单纯输出"{}"
print(str_2)

str_3 = "{}"                 #不用format方法，直接输出
print(str_3)

arg0 = 'a'
arg1 = 'b'
arg2 = 'c'
str_4 = "A {2} is {0} but {1}".format(arg0,arg1,arg2)       #format方法中：{}内的数字就是参数的下标
print(str_4)
