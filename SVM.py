from sklearn.svm import SVC
from sklearn import svm
import numpy as np
import csv
import pickle


csv_file_object = csv.reader(open('bagOfWords.csv', 'rt'))
data = []
for row in csv_file_object:
    data.append(row)

data = np.array(data)
X=data[:,:3000]
Y=data[:,3000]

C = 1.0
# rbf_svc = svm.SVC(kernel='rbf',gamma=0.7,C=C).fit(X,Y)
# pickle.dump(rbf_svc, open('SVMmodel.pickle', 'wb'))
rbf_svc= pickle.load(open('SVMmodel.pickle', 'rb'))

print(rbf_svc.score(X,Y))



