from math import sin, pi


list1=[2*pi*(x/100) for x in range(101)]
sin_list=[]
for x in list1:
    sin_list.append(sin(x))

print("list1:",list1)
print("--------------------------------")
print("sin_list:",sin_list)