oplist = ('+', '-', '*', '/')       #使用四则运算符，来判定要分割字符串的位置

while True:
    line = input("Exp to calculate: ")  #默认输入的就是字符串
    if line == "quit":                   #退出语句
        break
    exp = line.split()                 #根据空格切分字符串, 输入的时候数字与运算符之间要有空格。
    if len(exp) != 3:
        print("Exp should be 'x op y'. \n"
              "Try again, or 'quit' to stop.")
        continue
    
    op=exp[1]           #操作符，即：四则运算符号：+ - * /
    if op not in oplist:
        print("Operator is not corect.")
        continue


    #检查输入的操作数是否能转换成浮点数。
    #虽然输入的数是负数时还是会报错，但这只能用float()函数抛出异常来捕获解决，但本书到此还没教，以后再说。
    if exp[0].isnumeric():
        x = float(exp[0]) #第一个操作数
    else:
        print("Operator is not corect.")
        continue
    if exp[2].isdigit():
        y = float(exp[2]) #第二个操作数
    else:
        print("Operator is not corect.")
        continue
    
    
    if op == '+':
        z=x+y
    elif op == '-':
        z=x-y
    elif op == '*':
        z=x*y
    elif op == '/':
        if y == '0':
            print("Error: divider is 0 . ")
            continue
        z=x/y
    
    print("Result: ",z)
    