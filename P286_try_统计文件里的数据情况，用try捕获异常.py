def summary_datafile(fname):
    """fname is the name of a data file. the function
    returns numbers of floats and wrong-formated entries
    in file fname, and thesummation of the floats
    as a tuple (num, errnum, summation). """

    try:
        datafile = open(fname, errors="ignore", encoding="utf-8")
    except OSError:
        print("file cannot open: ",fname)
        raise # re-raise original OSError exception
  
    num = 0
    errnum = 0
    accum = 0.0

    for line in datafile:
        for s in line.split():  # split方法: 根据空字符将一个大的字符串分解成一个个小的子串
            try:
                x = float(s)
                accum += x
                num += 1
            except ValueError:
                errnum += 1
    datafile.close()

    print("in file " + fname + ":")
    print("read correct numbers:", num)
    print("format-error entries:", errnum)
    return(num, errnum, accum)

if __name__ == "__main__":
    num = 0
    errnum = 0
    accum = 0.0
    while True:
        fname = input("next file name (None to quit): ")
        if fname == "None":
            print("correct numbers in files: ",num)
            print("format-error entries:", errnum)
            print("Accumulated value:", accum)
            break

        try:
            n, e, a = summary_datafile(fname)
            num += n
            errnum += e
            accum += a
        except OSError as msg:
            print("details:",msg.args)


            