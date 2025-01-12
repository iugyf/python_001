for i in range(10):
    print("ord(",i,")=",ord(str(i)))

for i in range(108,150):
    print("chr(",i,")=",chr(i))

print(chr(10987))
print(chr(25105))


################################################################
print("-----------------------------------")
print("#字符串比较")
print("bad" in "not very bad")
print("is is true" == "It is True")
