# 原始字符串：用于文件地址的"\"符号输入。
# 使用方法： r'...\...'   在''之内的\会被直接解释成\\。而\\又被python认为是一个\

print(r'ab\ncd')
print(r'abd\"can')
print(r"abd\"can")
print(len(r'abd\'can'))