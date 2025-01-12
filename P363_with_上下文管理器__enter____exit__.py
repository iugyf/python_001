# with的上下文管理器：

    # 开始方法：
        # def __enter__(self): 
            # pass
            # return self       # __enter__ 方法的返回值会被赋值给 as 后面的变量，
                                # 如果没有返回值，就会抛出：AttributeError: 'NoneType' object has no attribute 'action' 错误

    # 结束方法：
        # def __exit__(self, type, value, trace):    # 后面三个参数是解释器自动赋值，如果正常退出则三个值都是None； 异常退出就会赋异常信息
            # pass                                   # 没要求一定要返回值



###################################################################################################3
from random import random       # 随机数库


class Context:

    # # 初始化      没啥用，不需要它    
    # def __init__(self):
    #     pass

    # "上下方管理器" 的 “开始方法”   
    def __enter__(self):
        print("__enter__() executed")
        return self     # 这个要有返回值，返回自身self. 这是解决 AttributeError: 'NoneType' object has no attribute 'action' 错误的关键。
                        # 在 Python 的上下文管理器中(with语句中):
                            # __enter__ 方法的返回值会被赋值给 as 后面的变量（即 con）。
                            # 如果你的 __enter__ 方法没有显式返回任何值（或者返回 None），那么 con 就会被赋值为 None，
                            # 从而导致你在调用 con.action() 时出现 AttributeError。




    # "上下方管理器" 的 “结束方法”   如果正常结束，则 type, value, trace 都是None。 非正常结束，则解释器自动提供数据
    def __exit__(self, type, value, trace):
        print("__exit__() executed", type, value, trace)


    def action(self):
        print("action() executed")
        rm = random()   # 默认随机数在[0.0, 1.0)
        if rm < 0.5:
            return "正常结束。"
        else:
            raise RuntimeError("非正常结束",rm)


def test_with(n):
    for i in range(n):
        print("\n-----------" + str(i+1) + "-----------")
        try:
            with Context() as con:

                print("Context: ", con.action())
        except RuntimeError as ex:         
            # print(type(ex), ex.args[0])
            pass


test_with(5)