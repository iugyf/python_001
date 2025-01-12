print("起始断点,调试用")



# 实际执行保存文件的函数
def save_phonebook(book, outfile):
    for name, record in book.items():
        outfile.write("name "+ name + "\n")
        for field, value in record.items():
            outfile.write(field + " " + value + "\n")


# 实际执行加载文件的函数
def load_phonebook(infile):
    book = {}
    line = infile.readline()
    if line[:4] != "name":
        raise ValueError            #文件开头不是name时报错，所以输入文件要以name开头
    try:
        while True:
            name = line[5:].strip()
            book[name] = {}
            while True:
                line = infile.readline()
                if line == "":
                    raise StopIteration
                if line =="\n":
                    continue
                if line[:4] == "name":
                    break
                entry = line.split(maxsplit=1)
                book[name][entry[0]] = entry[1].strip()
    except StopIteration:
        pass
    return book


phonebook = None


# 查找联系人电话
def phone():
    if phonebook == None:
        print("phonebook has not loaded.")
        return
    
    name = input("name: ")
    try:
        print(phonebook[name]["phone"])
    except KeyError:
        print("no such name in the phonebook.")

    
# 主界面接口：加载文件
def load():
    global phonebook
    try:
        infile = open(input("file name: ") + ".bok")
    except OSError as ex:
        print("file open error: ", ex.args[1])
        return
    
    phonebook = load_phonebook(infile)
    infile.close()


# 主界面接口：保存文件
def save():
    if phonebook == None:
        print("phonebook has not loaded.")
        return
    
    try:
        outfile = open(input("file name: ") + '.bok', 'w')
    except OSError as ex:
        print("file open error: ", ex.args[1])
        return
    
    save_phonebook(phonebook, outfile)
    outfile.close()


# 添加
def add():
    global phonebook
    try:
        name = input("name: ")
        if name not in phonebook:           #如果程序一开始就执行add，则phonebook对象还是none，一定会报错。
            phonebook[name] = {}
        number = input("phone number: ")
        phonebook[name]["phone"] = number
        yesno = input("other entry (yes/no)? ")
        if yesno.lower() != "yes":
            return
        print("entry form: entry-name entry-value")
        print("empty line to stop.")
        while True:
            line = input("next entry:")
            if line == "":
                return
            entry = line.split(maxsplit=1)
            phonebook[name][entry[0]]=entry[1].strip()
    except Exception as ex:
        print("input is not in correct form. stop command add.  另外：先要加载文件，然后才能添加新号码。")
        pass

# 命令用字典。  这里就是数据驱动程序设计的关键，把字典作成函数入口，字典里的字符串拼接成函数名与参数，使被拼接的字符串作为对应的函数名进行调用
commands = {
    "load":(load, "load a phonebook file"),         # 字典中值是个表，这个表的第一项是函数对象(load)，可用于调用对应函数
    "save":(save, "save the phonebook into a file"),
    "phone":(phone, "search the telephone number for a name"),
    "add":(add, "add a phone"),
}


# 主界面
print("""this is a phonebook grogram. please type command:
      quit: quit the program""")
for cmd, value in commands.items():     #cmd是字典里的关键字。   value是字典里的值，这个值是列表类型，所以value[1]是列表里的第二项
    print(cmd + ":", value[1])
print("please load a phonebook before use.")

# 主界面上循环询问命令
while True:
    try:
        cmd = input("command>> ")
        commands[cmd][0]()     # 通过字典调用函数
    except KeyError:
        if cmd == "quit":
            if not phonebook:
                break
            yesno = input("resave the phonebook (yes/no)? ")
            if yesno.lower() != "no":
                save()
            print("bye!")
            break
        else:
            print("no such a command!")

