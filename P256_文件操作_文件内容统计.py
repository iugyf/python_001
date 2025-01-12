def count_file(fname):
    digits = letters = spaces = others = 0
    infile = open(fname, encoding='utf_8')
    for line in infile:
        for c in line:
            if c.isdigit():
                digits += 1 
            if c.isalpha():
                letters += 1
            if c.isspace():
                spaces += 1
            else:
                others += 1
    infile.close()

    print("in the file, there are:")
    print("\t",digits,"digits;")
    print("\t",letters,"letters;")
    print("\t",spaces,"blank chars;")
    print("\t",others,"other chars;")

x1 = str(input("请输入当前文件夹下要统计字数的文件名："))
count_file(x1)