from random import choice, seed
from sys import stdout

# 读取文件中所有单词，逐个读取，yield生成器函数每次返回一个单词
def get_word(fname):
    try:
        infile = open(fname, encoding="utf-8")
    except FileNotFoundError as msg:
        print(type(msg))
        print(msg.filename,"File not found")
        print(msg.args[0])
        print(msg.args[1])
        # print(__name__)         #它不能显示当前执行的函数名，只能显示这个文件的主函数名
        return

    while True:
        line = infile.readline()
        if not line:
            infile.close()
            return
        for s in line.split():
            yield s


# 构造字典
def build_dic(fname):
    prefix = (" ", " ")     #元组
    word_dic = {}           #创建字典
    for word in get_word(fname):
        try:
            word_dic[prefix].append(word)       #字典word_dic里面：关键字prefix，对应的值是一个列表，在此列表里面增加word
                                                #即：  word_dic = {  prefix_1:[word_11,word_12,...],   prefix_2:[word_21,word_22,...],   ...  }
        except KeyError:                #如果上面字典中没有当前前缀prefix这个关键字，则抛出异常，在此捕获，然后下一名新建该新前缀
            word_dic[prefix]=[word]     #在字典中新建一个新前缀项，这里word 加 “[]”  是因为这个值要建成一个列表。
        prefix = (prefix[1],word)       #建立新前缀
    return word_dic     

#生成文本
def generate(outfile, word_dic, length):
    prefix = (" ", " ")
    seed()      #随机种子

    for i in range(length):
        try:
            word = choice(word_dic[prefix])     #choice随机选择一个元素，即随机选中一个词
            outfile.write(word)
            prefix = (prefix[1], word)
            if i != length -1:          #每个词后加空格
                outfile.write(" ")
        except KeyError:
            return
        

#main program
if __name__ == "__main__":    
    in_fname = input("please give a file name: ")
    wdic = build_dic(in_fname)
    generate(stdout, wdic, 100)     # stdout:输出到屏幕