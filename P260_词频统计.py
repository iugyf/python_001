def text_stat(infname, statfile):
    worddict = {}
    num = 0
    textfile = open(infname)

    for line in textfile:
        wordlist = line.split()
        for word in wordlist:
            word = word.strip(", . : ' ; ! ? ( ) - _ $ /` ~ @ # $ % ^ & *   \\")
            # word = word.strip(",.:';!?()-_$/`~\#$%^&*\\")
            if word == "":
                continue
            worddict[word] = worddict.get(word,0)+1
            num += 1
    textfile.close()

    outfile = open(statfile,'w')
    for word in sorted(worddict.keys()):
        outfile.write(word + ", " +str(worddict[word]) + '\n')
    outfile.close()
    return num, len(worddict)

x1 = "P260_词频统计_被统计文件.txt"
x2 = "P260_词频统计_结果.dat"

wn, dn =text_stat(x1, x2)
print(wn,"words in the text.")
print(dn, "different words in the text.")
print("finished, and the result is in ",x2)