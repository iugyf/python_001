
#----------------------------------------------------------------
# 4. 进程池（Pool）
    # Pool 可以简化管理多个工作进程的过程，尤其适合于需要并行执行的任务集合。
print("\n-----------------------------------------\n")
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool:  # 创建包含4个进程的池
        result = pool.map(f, range(10))  # 并行计算f(0), f(1), ..., f(9)
        print(result)
