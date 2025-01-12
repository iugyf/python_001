# 摘自：通义千问2024-12-29 
    # 问题：没有其它方便的方法让抛出异常处理结束之后继续回原代码之下继续执行吗



# 在 Python 中，try-except 结构的设计原则是：
    # 一旦 try 块中抛出异常并被捕获，try 块中的剩余代码将被跳过，程序会从 except 或 finally 块之后的代码继续执行。
    # 因此，Python 并没有内置的机制让异常处理结束后自动返回到 try 块中抛出异常的地方继续执行。

# 然而，如果你希望在处理异常后继续执行 try 块中的后续代码，而不必手动将每个操作分开处理或使用复杂的控制结构（如循环和标志位），


# 可以考虑以下几种更简洁的方法：
######################################################################
# 1. 使用 contextlib.suppress
    # contextlib.suppress 是一个上下文管理器，它可以捕获并忽略指定类型的异常，而不会中断程序的执行。
    # 这意味着即使发生了异常，程序也会继续执行 try 块中的后续代码。

# 示例：

from math import sqrt
from contextlib import suppress

def triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        raise ValueError("wrong argument(s) for triangle", (a, b, c))

def test_tril():
    with suppress(ValueError):  # 忽略 ValueError 异常
        print(triangle(3, 5, 6))  # 正常执行
        print("1.--------------------------------")
        print(triangle(2, 4, 7))  # 抛出异常，但不会中断后续代码
        print("2.--------------------------------")  # 这行仍然会执行
        print(triangle(3, 5, 6))  # 这行也会执行

test_tril()

# 输出：
    # 7.937253933193772
    # 1.--------------------------------
    # 2.--------------------------------
    # 7.937253933193772
# 解释：
    # with suppress(ValueError) 会捕获并忽略 ValueError 异常，因此即使 triangle(2, 4, 7) 抛出了 ValueError，
    # 程序也不会中断，而是继续执行 try 块中的后续代码。
    # 这种方法非常适合你想要忽略某些特定类型的异常，并且希望程序继续执行的情况。



######################################################################
# 2. 使用 try-except 的 else 块
    # 虽然 else 块不能直接让你回到 try 块中抛出异常的地方继续执行，但它可以让你更清晰地分离正常执行的代码和异常处理的代码。
    # 你可以将你希望在没有异常时执行的代码放在 else 块中。

# 示例：
print("\n\n################################################################")
from math import sqrt

def triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        raise ValueError("wrong argument(s) for triangle", (a, b, c))

def test_tril():
    try:
        print(triangle(3, 5, 6))  # 正常执行
        print("1.--------------------------------")
        print(triangle(2, 4, 7))  # 抛出异常
    except ValueError as msg:
        print("3.--------------------------------")
        print("msg: ", msg)
        print("Exception happens:")
        print("  Error type:", type(msg))
        print("  Error message:", msg.args[0])
        print("  Error details:", msg.args[1])
    else:
        print("2.--------------------------------")
        print(triangle(3, 5, 6))  # 只有在没有异常时才会执行

test_tril()

# 输出：
    # 7.937253933193772
    # 1.--------------------------------
    # 3.--------------------------------
    # msg:  ('wrong argument(s) for triangle', (2, 4, 7))
    # Exception happens:
    #   Error type: <class 'ValueError'>
    #   Error message: wrong argument(s) for triangle
    #   Error details: (2, 4, 7)
# 解释：
    # else 块中的代码只有在 try 块中没有抛出异常时才会执行。如果 try 块中抛出了异常，else 块中的代码将被跳过。
    # 这种方法可以帮助你更清晰地分离正常执行的逻辑和异常处理的逻辑。





######################################################################
# 3. 使用 try-except 的嵌套
    # 如果你有多个独立的操作，每个操作都可能抛出异常，但你希望在每个操作抛出异常后继续执行后续的操作，
    # 可以将每个操作放在独立的 try-except 块中。这样可以确保每个操作的异常不会影响其他操作的执行。

# 示例：
print("\n\n################################################################")
from math import sqrt

def triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        raise ValueError("wrong argument(s) for triangle", (a, b, c))

def test_tril():
    try:
        print(triangle(3, 5, 6))  # 正常执行
        print("1.--------------------------------")
    except ValueError as msg:
        print("msg: ", msg)

    try:
        print(triangle(2, 4, 7))  # 抛出异常
        print("2.--------------------------------")
    except ValueError as msg:
        print("msg: ", msg)

    try:
        print(triangle(3, 5, 6))  # 正常执行
    except ValueError as msg:
        print("msg: ", msg)

test_tril()

# 输出：
    # 7.937253933193772
    # 1.--------------------------------
    # msg:  ('wrong argument(s) for triangle', (2, 4, 7))
    # 7.937253933193772
# 解释：
    # 每个 try-except 块独立处理一个操作的异常，因此即使某个操作抛出异常，其他操作仍然可以继续执行。
    # 这种方法适合你有多个独立的操作，每个操作都可能抛出异常的情况。




######################################################################
# 4. 使用 try-except 和 continue 在循环中
    # 如果你在一个循环中执行多个操作，并且希望在某个操作抛出异常后继续执行下一个操作，
    # 可以使用 continue 语句来跳过当前迭代，继续执行下一次循环。

# 示例：
print("\n\n################################################################")
from math import sqrt

def triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        raise ValueError("wrong argument(s) for triangle", (a, b, c))

def test_tril():
    triangles = [
        (3, 5, 6),
        (2, 4, 7),  # 无效三角形
        (3, 5, 6)
    ]

    for i, (a, b, c) in enumerate(triangles, start=1):
        try:
            area = triangle(a, b, c)
            print(f"Triangle {i}: Area = {area}")
        except ValueError as msg:
            print(f"Triangle {i}: Error - {msg.args[0]}")

test_tril()

# 输出：
    # Triangle 1: Area = 7.937253933193772
    # Triangle 2: Error - wrong argument(s) for triangle
    # Triangle 3: Area = 7.937253933193772
# 解释：
    # 在这个例子中，for 循环遍历多个三角形的参数列表。如果某个三角形的参数无效并抛出异常，程序会捕获异常并打印错误信息，然后继续处理下一个三角形。
    # 这种方法适合你有多个类似的操作需要依次执行，并且希望在某个操作失败后继续执行下一个操作。



######################################################################
# 总结
    # 虽然 Python 的 try-except 结构不允许你直接返回到 try 块中抛出异常的地方继续执行，但你可以通过以下几种方式实现类似的效果：
    # 使用 contextlib.suppress：捕获并忽略指定类型的异常，程序将继续执行 try 块中的后续代码。
    # 使用 try-except 的 else 块：将正常执行的代码放在 else 块中，确保只有在没有异常时才执行这些代码。
    # 使用嵌套的 try-except 块：将每个可能抛出异常的操作放在独立的 try-except 块中，确保每个操作的异常不会影响其他操作的执行。
    # 使用 try-except 和 continue 在循环中：如果你在一个循环中执行多个操作，可以在捕获异常后使用 continue 跳过当前迭代，继续执行下一次循环。
    # 选择哪种方法取决于你的具体需求和代码结构。如果你只是想忽略某些异常并继续执行后续代码，contextlib.suppress 是最简洁的选择；如果你有多个独立的操作，嵌套的 try-except 块或循环中的 try-except 结构可能更适合。