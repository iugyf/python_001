


def read_large_file(file_path):
    with open(file_path, 'r',encoding='utf_8') as file:
        for line in file:
            yield line.strip()

# 使用生成器逐行读取大文件
for line in read_large_file('P261_yield_网络摘抄_大文件.txt'):
    print(line)