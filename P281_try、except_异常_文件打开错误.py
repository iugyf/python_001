while True:
    fname = input("please give the file name:")
    try:
        infile = open(fname,encoding = "utf_8")
        infile.close()
        break
    except OSError:
        print("cann't open " + fname + ".", "Another: ")    

