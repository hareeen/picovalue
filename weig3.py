from scipy.linalg import eig
import numpy as np
import os
import matplotlib.pyplot as plt


sub_list = ['rel', 'his', 'math', 'eng', 'ph', 'med']

n = len(sub_list)


vect_list = []

for sub in sub_list:
    l = eval(open('/Users/cottonova/Downloads/'+sub+'_vect.txt', 'r').read())
    vect_list += l


sig = np.zeros([50*6, 50*6])
mean = np.zeros([50*6])

for v in vect_list:
    mean += v

mean /= 100.0*n

for v in vect_list:
    v = np.array(v-mean)
    sig += v.T.dot(v)

sig /= 100.0*n

w, v = eig(sig)

a = w.max()
a_index = list(w).index(a)
w[a_index] = -10000

b = w.max()
b_index = list(w).index(b)


V = np.array([v[a_index], v[b_index]])






## out

out_list = []
for x in vect_list:
    out_list.append(list(V.dot(x-mean)))

tmp_list = []
for i in range(n):
    co_1 = np.array([j[0] for j in out_list[100*i:100*(i+1)]]).mean()
    co_2 = np.array([j[1] for j in out_list[100*i:100*(i+1)]]).mean()
    tmp_list.append([co_1, co_2])



x = [i[0] for i in tmp_list]
y = [i[1] for i in tmp_list]

plt.scatter(x, y)

plt.show()
