from os import scandir


def file_display(dname = None, space_2 = ""):
    # try:      # 真实的程序要加入异常处理，但这里为看的清，分的清主次，就不写了
    with scandir(dname) as entries:         # 使用with, 当前过程完毕就自动关闭entries对象，scandir返回的是表对象
        for entry in entries:
            if entry.is_dir():          #默认情况下，is_dir() 和 is_file() 不会跟随符号链接。如果你的目录结构中包含符号链接，并且你希望递归进入符号链接指向的目录，可以考虑使用 follow_symlinks=True。不过，通常情况下，你不应该跟随符号链接，以避免循环引用问题。
                print("\n显示文件夹相对地址：",entry.path)
                print(space_2, "directory:", entry.name)
                next_space = space_2 + "    "
                file_display(entry.path, next_space)            #.path是相对路径
            elif entry.is_file():
                print(space_2, "file:",entry.name)
            else:
                print("something wrong.")





file_display('P310_测试文件夹')

print("================================================================")
print("================================================================")
print("================================================================")

file_display()      # 默认地址是当前文件夹地址






# print("================================================================")
# print("================================================================")
# print("================================================================")
## 以下原书代码
# for entry in scandir(None):
#     if entry.is_dir():
#         print("    directory:", entry.name)
#     elif entry.is_file():
#         print("file:",entry.name)
#     else:
#         print("something wrong.")


