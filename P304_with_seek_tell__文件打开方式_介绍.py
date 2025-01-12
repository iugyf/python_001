# with ... as ...：    过程结束时自动关闭as之后的对象
# .tell()： 返回文件当前位置                                 另见书P309-310
# .seek(0):  重新定位文件位置， 参数0表示定位到文件头          另见书P309-310

from datetime import datetime       #时间库

with open("P304_自动关闭文件.txt","a+") as f:       # a：追加模式。如果文件存在，则会在文件末尾追加内容；如果文件不存在，则会创建新文件。
                                                   # +：更新模式。与上述模式结合使用，表示文件可以同时进行读取和写入。
    str_1 = str(datetime.now()) + "\n"
    f.write(str_1)
    
    try:
        print("当前文件指针：",f.tell())
        content = f.read()
        print("当前文件位置的内容：",content)  # 文件末尾只读出："\n"
        f.seek(0)                            # 文件重定位到开头      
        print("\n文件重定位到开头：")
        content = f.read()  
        print(content)

    # 捕获所有非系统退出异常
    # except Exception as ex:
    #     print(ex)
        
    # 捕获所有异常，包含系统退出
    except:
        print("with中读文件有异常")


# 以下用再次读取文件的方式来测试文件是否已经被上面的with自动关闭
try:    
    content = f.read()
    print(content)
except ValueError as e:
    print(f"Error: {e}, 即：文件已被with自动关闭")  # 输出: Error: I/O operation on closed file.