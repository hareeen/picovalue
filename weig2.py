from scipy.linalg import eig
import numpy as np
import os
import matplotlib.pyplot as plt

word_file = open('words.txt', 'r')
word_vect = eval(word_file.read())

tmp = 0
file_list = ['mathematics', 'physicalscience', 'English', 'history', 'medicalscience', 'religion']

sig = np.zeros([120, 120])

doc_list = []
doc_mean = np.zeros([120])
for file in file_list:
    tmp += 1
    exec("subject = " + open(os.getcwd() + "/static/dt/" + file + ".txt", 'r').read())
    for s in subject:
        x = np.zeros(120)
        for i, w in enumerate(word_vect):
            x[i] = s[1].count(w)
        doc_list.append(x)
        doc_mean += x
        sig += x.T.dot(x)

doc_mean /= len(doc_list)

for i in range(len(doc_list)):
    doc_list[i] -= doc_mean


sig /= 6000.0

w, v = eig(sig)

a = w.max()
a_index = list(w).index(a)
w[a_index] = -10000

b = w.max()
b_index = list(w).index(b)


V = np.array([v[a_index], v[b_index]])


out_list = []
for x in doc_list[0:6000]:
    out_list.append(list(V.dot(x)))

tmp_list = []
for i in range(6):
    co_1 = np.array([j[0] for j in out_list[1000*i:1000*(i+1)]]).mean()
    co_2 = np.array([j[1] for j in out_list[1000*i:1000*(i+1)]]).mean()
    tmp_list.append([co_1, co_2])



x = [i[0] for i in out_list]
y = [i[1] for i in out_list]

plt.scatter(x, y)

plt.show()
