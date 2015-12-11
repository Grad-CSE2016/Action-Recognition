from sklearn.svm import SVC
from sklearn import svm
import numpy as np
import csv
import pickle
from sklearn import metrics
from sklearn.multiclass import OneVsRestClassifier

csv_file_object = csv.reader(open('bow_testing.csv', 'rt'))

test=[]
for row in csv_file_object:
    test.append(row)

test = np.array(test)

X_test=test[:,:3000]
Y_test=test[:,3000]

classif= pickle.load(open('oneVsAll.pickle', 'rb'))

predicted = classif.predict(X_test)
expected=Y_test

print(metrics.accuracy_score(expected,predicted))