from math import sqrt 

def triangle(a,b,c):
    if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
        s = (a+b+c)/2
        return sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        raise ValueError("wrong argument(s) for triangle",(a,b,c))
    
def test_tril():
    try:
        print(triangle(3,5,6))
        print("1.--------------------------------")
        print(triangle(2,4,7))  # 此处会抛出异常, 此句之后的正常代码就不执行了，只执行except的代码
        print("2.--------------------------------")
        print(triangle(3,5,6))
    except ValueError as msg: 
        print("3.--------------------------------")
        print("msg: ",msg)
        print("Exception happens:")
        print("  Error type:",type(msg))
        print("  Error message:",msg.args[0])
        print("  Error details:",msg.args[1])
        # print("  Error ???:",msg.args[2])     #没有了
    finally: pass
        

test_tril()