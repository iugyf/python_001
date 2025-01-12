def v2n(word):
    if word[-1]=='e':
        return word+'r'

    if word[-1]=='y':
        return word[:-1]+'ier'      #冒号是切片语法，取word表从第一个元素到倒2个元素之间所有的元素。   即：list[开始元素下标:结束元素下标:步长]
        #return word[-1]+'ier'      #如果没有冒号，则是取word中的最后一个元素再加上ier

    return word+'er'

def v2n_list(verbs):
    nouns = []
    for w in verbs:
        nouns.append(v2n(w))
    return nouns

verbs=['compute','work','supply','walk','write']
print(verbs)
print("----------------------")
print(v2n_list(verbs))