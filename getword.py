import os

f_l = ['mathematics', 'physicalscience', 'English', 'history', 'medicalscience', 'religion']
s = list()
word_freq = dict()
res = list()
res2 = list()
for f in f_l:
    d = set()
    exec("s="+open(os.getcwd()+"/static/dt/"+f+".txt").read(), globals())
    for i in s:
        for j in i[1]:
            d.add(j)
    for i in d:
        b = 0
        for j in s:
            if i in j[1]:
                b = b + 1
        word_freq[i] = b
    for i in range(20):
        tmp = list(word_freq.values())
        tmp2 = list(word_freq.keys())
        maxval = max(tmp)
        maxindex = tmp.index(maxval)
        maxkey = tmp2[maxindex]
        word_freq[maxkey] = 0
        res.append(maxkey)
        res2.append(maxval)
open(os.getcwd()+"/words.txt", "w").write(str(res))
open(os.getcwd()+"/values.txt", "w").write(str(res2))
