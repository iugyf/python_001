from random import randint

#输出10个字符宽度，右对齐
for i in range(5):
    print(str(randint(1,100)**4).rjust(10),
          str(randint(1,100)**4).rjust(10),
          str(randint(1,100)**4).rjust(10),
          )