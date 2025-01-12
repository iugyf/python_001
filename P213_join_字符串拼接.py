# join()方法： 在 “threading” 库中有等待线程结束的功能，见书P420页

list1 = ["break","continue","return"]
sep = "fuck~~~~~~~~~~~~~~~~"
list2 = ',  '.join(list1)
list3 = ',  '.join(["break","continue","return"])

print(list1,type(list1))
print(list2,type(list2))
print(list3,type(list3))
print(sep.join(list1))
# print(list1.join(sep))