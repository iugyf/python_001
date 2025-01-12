a=int(input("start from:"))
b=int(input("end at:"))
c=int(input("step:"))

s=0
for n in range(a,b,c):
    s=s+n
    print("s=",s)

print("the sum is ",s)