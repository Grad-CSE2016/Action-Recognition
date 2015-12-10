import numpy as np
import csv
import pandas as pd
import pickle


filenames=['actions/running_rslt.txt','actions/walking_rslt.txt','actions/jogging_rslt.txt','actions/boxing_rslt.txt','actions/handclapping_rslt.txt','actions/handwaving_rslt.txt']
# actionCodes=range(1,7)

k_means = pickle.load(open('kMeanModel.pickle', 'rb'))

actionCode=1
BagOfWords=np.empty(3001)
for fName in filenames:
    f=open(fName,'rt')
    content=f.read()
    examples=content.split(',')
    print(len(examples))
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
np.savetxt("bagOfWords.csv",BagOfWords, delimiter=",")

# print(BagOfWords[:,3000])