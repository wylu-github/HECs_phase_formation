import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold
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
clf_set = [LR, NB, RF, SVM_linear, SVM_rbf, SVM_sigmoid]


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


data_sum = pd.DataFrame(pd.read_excel('ml_dataset_17.xlsx').iloc[:, 1:2])
for clf in clf_set:
    data = pd.read_excel('ml_dataset_{}.xlsx'.format(namestr(clf, globals())[0]))
    data1 = data.dropna(axis=0, how='any')
    X_train = data1.iloc[:, 2:-1].values
    y_train = data1.iloc[:, -1].values
    X_predict = data.iloc[:, 2:-1].values
    skf = StratifiedKFold(n_splits=5)
    for train_index, test_index in skf.split(X_train, y_train):
        X_4, X_1 = X_train[train_index], X_train[test_index]
        y_4, y_1 = y_train[train_index], y_train[test_index]
        clf.fit(X_4, y_4)
        phase_predict = clf.predict(X_predict).reshape(382, 1)
        data_predict = pd.DataFrame(phase_predict)
        data_sum = pd.concat([data_sum, data_predict], axis=1)

data_sum.index = range(1, 383)
data_sum.columns = ['formula', 'LR_SFS_1', 'LR_SFS_2', 'LR_SFS_3', 'LR_SFS_4', 'LR_SFS_5', 'NB_SFS_1', 'NB_SFS_2',
                    'NB_SFS_3', 'NB_SFS_4', 'NB_SFS_5', 'RF_SFS_1', 'RF_SFS_2', 'RF_SFS_3', 'RF_SFS_4', 'RF_SFS_5',
                    'SVM_linear_SFS_1', 'SVM_linear_SFS_2', 'SVM_linear_SFS_3', 'SVM_linear_SFS_4',
                    'SVM_linear_SFS_5', 'SVM_rbf_SFS_1', 'SVM_rbf_SFS_1', 'SVM_rbf_SFS_1', 'SVM_rbf_SFS_1',
                    'SVM_rbf_SFS_1', 'SVM_sigmoid_SFS_1', 'SVM_sigmoid_SFS_1', 'SVM_sigmoid_SFS_1',
                    'SVM_sigmoid_SFS_1', 'SVM_sigmoid_SFS_1']
data_sum.to_excel('phase_prediction_382.xlsx')