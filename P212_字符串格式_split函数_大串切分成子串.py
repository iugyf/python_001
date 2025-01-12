# s.split()  :以连续空白字符（空格、换行符、制表符）将字符串切分成一个个子串。  见P212页

str_1 = "sldfjloijvqe oqefn \t  \n   \  rq \\ eno / iqe // rnn qn qlernoe  irn lkn lwekn lqenlen r"
print(str_1)

list_1 = []
for c in str_1.split():
    list_1.append(c)
print(list_1)
print("注意反斜杠与斜杠")