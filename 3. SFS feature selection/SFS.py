import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.feature_selection import SequentialFeatureSelector
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


data = pd.read_excel('ml_dataset_17.xlsx')
data.iloc[:, 2:-1] = StandardScaler().fit_transform(data.iloc[:, 2:-1])
data1 = data.dropna(axis=0, how='any')
X = data1.iloc[:, 2:-1]
y = data1.iloc[:, -1]
feature_names = range(1, 18)
LR = LogisticRegression(C=1e5, max_iter=1000)
NB = GaussianNB()
RF = RandomForestClassifier(random_state=120)
SVM_linear = SVC(kernel='linear')
SVM_rbf = SVC(kernel='rbf')
SVM_sigmoid = SVC(kernel='sigmoid')
clf_set = [LR, NB, RF, SVM_linear, SVM_rbf, SVM_sigmoid]
for clf in clf_set:
    sfs = SequentialFeatureSelector(clf, k_features=17, forward=True, scoring='accuracy', cv=5)
    sfs = sfs.fit(X, y)
    d = sfs.subsets_

    score = 0
    for i in range(17):
        if d[i+1]['avg_score'] > score:
            score = d[i+1]['avg_score']
            feature = list(d[i+1]['feature_idx'])
    dataset_clf = data.iloc[:, 1:2]
    for f in feature:
        dataset_clf = pd.concat([dataset_clf, data.iloc[:, f+2]], axis=1)
    dataset_clf = pd.concat([dataset_clf, data.iloc[:, -1]], axis=1)
    dataset_clf.index = range(1, 383)
    dataset_clf.to_excel('ml_dataset_{}.xlsx'.format(namestr(clf, globals())[0]))
    #
    m = []
    n = []
    for i in range(17):
        i = i+1
        if i > 1:
            a = list(d[i]['feature_idx'])
            a = [i+1 for i in a]
            b = list(d[i-1]['feature_idx'])
            b = [i+1 for i in b]
            c = 'd' + str(list(set(a) - set(b))[0])
        else:
            c = 'd' + str(d[i]['feature_idx'][0] + 1)
        m.append(c)
        n.append(d[i]['avg_score'])

    plt.plot(m, n)
    plt.show()






