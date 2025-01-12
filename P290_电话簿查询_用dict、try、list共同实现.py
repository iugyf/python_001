# 双重字典，外重是  { 联系人名:{联系人信息} }
#          内重是  {          {email:..., address:..., telephone:...} }
pho =  {"fuck_1":{"email":"fuck_1@example.com", "address":"fuck_1_address", "telephone":"10086"},
        "fuck_2":{"email":"fuck_2@example.com", "address":"fuck_2_address", "telephone":"20086"},
        "fuck_3":{  "address":"fuck_2_address", "telephone":"30086"},           #没有email
        "fuck_4":{"email":"fuck_4@example.com", "address":"fuck_4_address", "telephone":"40086"}}



#获取邮箱地址
def get_email_address(phonebk):
    mlist = []
    for name, record in phonebk.items():            #.items 是字典的方法， items() 返回的是一个视图对象，而不是列表。如果你需要一个列表，可以使用 list() 函数进行转换
        if "email" in record:
            try:
                mlist.append((name,record["email"]))
            except KeyError:    #如果表中没有email就忽略
                pass
    return mlist


#打印名字与email
em = get_email_address(pho)
for x in em:
    print(x)
