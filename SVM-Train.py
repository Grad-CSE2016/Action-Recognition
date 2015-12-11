from sklearn.svm import SVC
from sklearn import svm
import numpy as np
import csv
import pickle
from sklearn import metrics
from sklearn.multiclass import OneVsRestClassifier


csv_file_object = csv.reader(open('bow_training.csv', 'rt'))

data = []
for row in csv_file_object:
    data.append(row)


data = np.array(data)

X=data[:,:3000]
Y=data[:,3000]

C = 1.0

classif = OneVsRestClassifier(SVC(kernel='rbf',degree=3))
classif.fit(X, Y)
pickle.dump(classif, open('oneVsAll.pickle', 'wb'))





