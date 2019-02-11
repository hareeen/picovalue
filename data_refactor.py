from pandas import DataFrame
import os

s = list()
file_list = ['mathematics', 'physicalscience', 'English', 'history', 'medicalscience', 'religion']
for file in file_list:
    res = list()
    fr = open(os.getcwd()+"/static/dt/"+file+".txt", "r")
    fw = open(os.getcwd()+"/static/dt/"+file+"2.txt", "w")
    exec("s="+fr.read())
    for i in s:
        res += i[1]
    data = {"ws": res}
    frame = DataFrame(data).T
    freq_df = DataFrame(frame.ix['ws'].value_counts())
    g = None
    for i in range(len(freq_df)):
        if freq_df["ws"][i] < 4:
            g = i
            break
    fw.write(str(freq_df[0:g]['ws'].to_dict()))
    fr.close()
    fw.close()
