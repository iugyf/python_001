def get_data_file():
    while True:
        fname = input("please give the file name: ")
        try: 
            infile=open(fname, encoding='utf_8')
            infile.close()
            return infile
        except OSError:
            print("cannot open" + fname + ".", "Another: ")

fs = get_data_file()