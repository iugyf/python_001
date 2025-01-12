from math import sin,cos

head = "{:<5} {:<12s} {:<12s}"            # ":"是转述描述。   "<"是左对齐     "12"是最小宽度    "s"是字符串
content = "{:5.3f} {:12.10f} {:12.10f}"   # 同上              同上            同上             "f"是浮点数       "."精度，即小数后位数

def gen_table(start, end, step):
    print(head.format("x","sin(x)","cos(x)"))
    x=start
    while x < end:
        print(content.format(x,sin(x),cos(x)))
        x+=step

print(gen_table(0.0,1.05,0.1))


