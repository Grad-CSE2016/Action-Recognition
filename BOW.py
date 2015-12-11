import numpy as np
import csv
import pandas as pd
import pickle


filenames=['Testing/running_rslt.txt','Testing/walking_rslt.txt','Testing/jogging_rslt.txt','Testing/boxing_rslt.txt','Testing/handclapping_rslt.txt','Testing/handwaving_rslt.txt']

k_means = pickle.load(open('kMeanModel.pickle', 'rb'))

actionCode=1
BagOfWords=np.empty(3001)
for fName in filenames:
    f=open(fName,'rt')
    content=f.read()
    examples=content.split(',')
    for ex in examples:
        lines=ex.splitlines()
        pts=[]
        for i in range(len(lines)):
            p=[float(x) for x in lines[i].split()]
            pts.append(p)
        arr=np.array(pts)
        hogHof = arr[:,9:]
        Bow=np.zeros(3001)
        Bow[3000]=actionCode
        for x in range(len(hogHof)):
            Bow[k_means.predict(hogHof[x])]+=1
        BagOfWords=np.vstack([BagOfWords,Bow])
    actionCode+=1
BagOfWords=BagOfWords[1:,:]
np.savetxt("bagOfWords_testing.csv",BagOfWords, delimiter=",")
