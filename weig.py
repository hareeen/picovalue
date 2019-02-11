import math
from konlpy.tag import Mecab
import ssl
import os
from newspaper import Article
ssl._create_default_https_context = ssl._create_unverified_context


def get_weight(url, f_l):
    mecab=Mecab()
    d_l=dict()
    for f in f_l:
        exec("d="+open(os.getcwd()+"/static/dt/"+f+"2.txt").read(), globals())
        d_l[f] = d
    soup = ""
    try:
        a = Article(url, language='ko')
        a.download()
        a.parse()
        soup=a.text
    except:
        return -1
    print(soup)
    me=list()
    for i in mecab.pos(soup):
        if i[1] == "NNG" or i[1] == "NNP":
            me.append(i[0])
    print(me)
    W_l = dict()
    for f in f_l:
        W = 0.0
        for i in d_l[f]:
            if i in me:
                W = W + math.log(d_l[f][i])
        print(W)
        print(len(me), len(d_l[f]))
        if len(me)==0 or len(d_l[f])==0:
            W=0
        else:
            W = float(int((W/(float((len(me)**0.7)*(len(d_l[f])**0.5)))*(10**6)))/10.0)
        W_l[f] = W
    return W_l
