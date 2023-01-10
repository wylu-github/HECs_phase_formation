import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, cross_val_predict, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


LR = LogisticRegression(C=1e5, max_iter=1000)
NB = GaussianNB()
RF = RandomForestClassifier(random_state=120)
SVM_linear = SVC(kernel='linear')
SVM_rbf = SVC(kernel='rbf')
SVM_sigmoid = SVC(kernel='sigmoid')


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


clf_set = [LR, NB, RF, SVM_linear, SVM_rbf, SVM_sigmoid]
data1 = pd.read_excel('ml_dataset_17.xlsx')
data_116 = data1.dropna(axis=0, how='any')
data_116.index = range(0, 116)
data_predict = pd.DataFrame(data_116.iloc[:, 1:2])
for clf in clf_set:
    data1 = pd.read_excel('ml_dataset_17.xlsx')
    data1.iloc[:, 2:-1] = StandardScaler().fit_transform(data1.iloc[:, 2:-1])
    data1 = data1.dropna(axis=0, how='any')
    data2 = pd.read_excel('ml_dataset_{}.xlsx'.format(namestr(clf, globals())[0]))
    data2 = data2.dropna(axis=0, how='any')
    for data in [data1, data2]:
        X = data.iloc[:, 2:-1]
        y = data.iloc[:, -1]
        score = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
        phase_predict = cross_val_predict(clf, X, y, cv=5).reshape(116, 1)
        phase_predict = pd.DataFrame(phase_predict)
        data_predict = pd.concat([data_predict, phase_predict], axis=1)
        print('the accuracy of {} is：{}'.format(namestr(clf, globals())[0], score))
        print('the validation accuracy of {} is: {}'.format(namestr(clf, globals())[0], score.mean()))

data_predict.index = range(1, 117)
data_predict.columns = ['formula','LR_17', 'LR_SFS', 'NB_17', 'NB_SFS', 'RF_17', 'RF_SFS', 'SVM_linear_17',
                        'SVM_linear_SFS', 'SVM_rbf_17', 'SVM_rbf_SFS', 'SVM_sigmoid_17', 'SVM_sigmoid_SFS']
data_predict.to_excel('phase_prediction_116.xlsx')
