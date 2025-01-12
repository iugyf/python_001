def total(invoice):
    assert isinstance(invoice,list)
    sum = 0.0
    for price, quantity in invoice:     #给列表list中的字段取名，一共两个字段，取两个名字：price与quantity
        sum += price * quantity
    return sum

inv1=[[2.10,12.4],[1.25,2.44],[17.34,3.6]]
print("Total price:",round(total(inv1),2))

#----------------------------------------------------------------


def total0(invoice):
    assert isinstance(invoice,list)
    sum = 0.0
    for entry in invoice:
        sum += entry[0] * entry[1]
    return sum

inv1=[[2.10,12.4],[1.25,2.44],[17.34,3.6]]
print("Total0 price:",round(total0(inv1),2))        #round标准函数：四舍五入为整数