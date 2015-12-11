import numpy as np
import sklearn
from sklearn.cluster import KMeans
import time
import pickle

with open("results.txt") as f:
    content = f.readlines()

floats=[]

for i in range(len(content)):
    f=[float(x) for x in content[i].split()]
    floats.append(f)


arr = np.array(floats)
arr = arr.astype(np.float16)

dimensions = arr[:,1:9]
# np.savetxt("dimensions.csv",dimensions , delimiter=",")

hogHof = arr[:,9:]
# np.savetxt("Hog_Hof.csv",hogHof , delimiter=",")

tic = time.time()
k_means = KMeans(n_clusters=3000,n_jobs=-1)
k_means.fit(hogHof)
toc = time.time()
print((toc-tic)/60)
pickle.dump(k_means, open('kMeanModel.pickle', 'wb'))
