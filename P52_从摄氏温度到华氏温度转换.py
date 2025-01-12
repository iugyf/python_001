#计算公式：F=C*9/5+32

begin=int(input("start from:"))
end=int(input("end at:"))
step=int(input("step:"))

for x in range(begin, end,step):
    print(x,"->",x*9/5+32)
