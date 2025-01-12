#简单总计
name = input("please give the name of the goods:")
price = float(input("Price of one piece of the good:"))
amount = int(input("amount:"))

if price >0 and amount >0:
    print(amount, "pieces of ",name,
          "totally: ",price*amount)
else:
    print("Error. Price and amount should be positive.")