# 以下是生成器对象，不是函数，不能像函数一样被调用
def test_gen(value=None):
    print("starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)       # 函数x是一个生成器对象，返回的是一个迭代器。它不是以return语句为返回值的一般函数。所以本段代码是生成器函数（非一般函数）
                print("receive value: ", value)
            except Exception as e:
                value = e
    finally:
        print("remember to clean up when 'close()' is called.")



print("1. ------------------------------------")
gen = test_gen(3)
print(gen)      # 显示gen对象


print("2------------------------------------")
test_gen(6)     #这里创建的是新对象，与上面的gen无关了
print(gen) 


# print("3------------------------------------")
# gen()
# print(gen())    # generator 对象不能被调用, 即：生成器对象不能像一般函数一样被调用

print("4. ------------------------------------")
print(next(gen))    # 此时gen函数第一次调用

print("5. ------------------------------------")
gen.send(8)

print("6. ------------------------------------")
gen.throw(ValueError,5)

print("7. ------------------------------------")
gen.close()

# print("8. ------------------------------------")
# next(gen) # 上面.close()之后，就不会再有next迭代数据了

# print("9. ------------------------------------")
# gen.send(10)  # 同理：# 上面.close()之后，就不会再有被send的迭代数据了
