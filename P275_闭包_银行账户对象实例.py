import random

idnum = random.randint(0,9999)      #随机[0~9999]范围内整数

def account(user, init=0):
    def deposit(v):
        nonlocal amount, history
        history.append(("deposit",v))       #两对括号是因为内括号代表一个元组，该元组存储两个元素
        amount += v
        print(user_name, "depositing", v, "done")
    
    def withdrew(v):
        nonlocal amount, history
        if v > amount:
            print("no enough money in account.")
            return
        history.append(("withdrew",v))       #两对括号是因为内括号代表一个元组，该元组存储两个元素
        amount -= v
        print(user_name, "withdrewing", v, "done")

    def dispatcher(command, v=0):
        if command == 'id':
            return idnum
        elif command == 'name':
            return user_name
        elif command == 'amount':
            return amount
        elif command =='history':
            return history[:]   #返回一个拷贝
        elif command == 'deposit':
            deposit(v)
        elif command == 'withdrew':
            withdrew(v)
        else:
            return "Not understood."
        
    if (not isinstance(user,str) or
        not isinstance(init, int) or init <0 ):
        print("name should be str",
              "and init should be non-negative integer.")
        print("please try again.")
        return None
    
    amount = init
    user_name = user
    history = [init]


    print("Account for", user,
          "created, with initially", str(amount) + ".")
    
    return dispatcher

act1 = account("Liu",3000)
act2 = account("Lei")

act1("deposit",340)
act1("withdrew",90)
act2("deposit",400)
act2("deposit",280)

print("account for", act1("name") + ":", act1("amount"))
print("account for id" , act2("id") , ":", act2("amount"))
print(act1("name") + " history:", act1("history"))
