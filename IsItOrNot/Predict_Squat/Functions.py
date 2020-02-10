###Imports###
from tkinter import messagebox
#from sklearn.neural_network import MLPClassifier
#from sklearn.externals import joblib
import pandas as pd
import time

from sklearn.neural_network import MLPClassifier

timestr = time.strftime("%Y%m%d-%H%M%S")
import distutils.dir_util
###Imports###
from sklearn import *#datasets, model_selection, svm, metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import joblib

#Config values
neural_accuracy_raiting=1.0
svm_accuracy_raiting=0.0
list_neural_acc=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
list_svm_acc=[0.0,0.0,0.0,0.0,0.0,]
timerLoop=0

predictResult=[3]

train_size = 59
test_size = 1




def svmSquatPredict(kernel, gamma_value, c_value):

    data_train = pd.read_csv('Data/processed/combined/combined.csv')
    data_test = pd.read_csv('Data/processed/combined/combined.csv')

    print(data_train.shape)
    X_all = data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)

    test_size=10
    train_size=50

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size)

    ###Classifier###
    clf = svm.SVC(gamma=gamma_value, C=c_value, kernel =kernel)

    ###Train###
    clf.fit(X_train, y_train)

    ###Predict###
    pre = clf.predict(X_test)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    print(accuracy_score)

    #Matrix of results
    result_matrix = metrics.confusion_matrix(pre,y_test)
    print(result_matrix)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    list_svm_acc[0]=(accuracy_score * 100)
    print(accuracy_score)

    print(classification_report(y_test, pre))

    folder = 'model/SVM/'
    filename = str(accuracy_score) + '_' + 'SVM_' + timestr + '_' + str(train_size) + '_' + str(test_size) + '_' + kernel + '_' + str(gamma_value) + '_' + str(c_value)

    ###MAKE FOLDER###
    distutils.dir_util.mkpath(folder + filename)
    joblib.dump(clf, folder + filename + '/' + filename)

def decisionTreeSquatPredict():


    data_train = pd.read_csv('Data/processed/combined/combined.csv')
    data_test = pd.read_csv('Data/processed/combined/combined.csv')

    print(data_train.shape)

    X_all = data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)
    num_test = 10

   # test_size=10
    #train_size=50

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size)

    ###Classifier###
    clf = DecisionTreeClassifier(criterion="gini",min_samples_split=50,splitter='best')

    ###Train###
    clf.fit(X_train, y_train)

    ###Predict###
    pre = clf.predict(X_test)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    print(accuracy_score)

    #Matrix of results
    result_matrix = metrics.confusion_matrix(pre,y_test)
    print(result_matrix)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    list_svm_acc[0]=(accuracy_score * 100)
    print(accuracy_score)
    print(classification_report(y_test, pre))

    folder = 'model/DT/'
    filename = str(accuracy_score) + '_' + 'DT_' + timestr + '_' + str(train_size) + '_' + str(test_size)

    ###MAKE FOLDER###
    distutils.dir_util.mkpath(folder + filename)
    joblib.dump(clf, folder + filename + '/' + filename)


def decisionTreeSquatPredictFile(testData):

    data_train = pd.read_csv('Data/processed/combined/combined.csv')
    data_test = pd.read_csv(testData)

    print(data_train.shape)

    X_all = data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)
    num_test = 10

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size, random_state=0.2)

    ###Classifier###
    clf = DecisionTreeClassifier(criterion="gini",min_samples_split=50,splitter='best')

    ###Train###
    clf.fit(X_train, y_train)

    ###Predict###
    pre = clf.predict(X_test)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    print(accuracy_score)

    #Matrix of results
    result_matrix = metrics.confusion_matrix(pre,y_test)
    print(result_matrix)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    list_svm_acc[0]=(accuracy_score * 100)
    print(accuracy_score)

    print(classification_report(y_test, pre))

    folder = 'model/DT/'
    filename = str(accuracy_score) + '_' + 'DT_' + timestr + '_' + str(train_size) + '_' + str(
        test_size)

    ###MAKE FOLDER###
    distutils.dir_util.mkpath(folder + filename)
    joblib.dump(clf, folder + filename + '/' + filename)


def neuralSquatPredict(train_size_value, test_size_value,activation,hl_size,l_rate):


    ###Read and Print info about data###

    data_train = pd.read_csv('Data/processed/combined/combined.csv')
    data_test = pd.read_csv('Data/processed/combined/combined.csv')
    print(data_test.shape)

    print('Training Neural Network...')

    X_all = data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size)

    clf = MLPClassifier(activation=activation, solver='adam', hidden_layer_sizes=hl_size,
                        learning_rate_init=l_rate,batch_size=10, max_iter=2000, )

    ###Train###
    clf.fit(X_train, y_train)

    ###Predict###
    pre = clf.predict(X_test)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    print(accuracy_score)

    #Matrix of results
    result_matrix = metrics.confusion_matrix(pre,y_test)
    print(result_matrix)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    list_neural_acc[0]=(accuracy_score * 100)

    print(accuracy_score)
    print(classification_report(y_test, pre))
    print('NN: ',accuracy_score)

    folder='model/NN/'
    filename=str(accuracy_score)+'_'+'NN_'+timestr+'_'+str(train_size)+'_'+str(test_size)+'_'+activation+'_'+'_'+str(l_rate) #str(hl_size)+

    ###MAKE FOLDER###
    import distutils.dir_util
    distutils.dir_util.mkpath(folder+filename)
    joblib.dump(clf,folder+filename+'/'+filename)

    print(neural_accuracy_raiting," MachineLearning.py")


def SquatLoadPredict(testFile,neuralModel):
    global predictResult
    try:
        #data_train = pd.read_csv('Data/processed/combined/combined.csv')
        data_test = pd.read_csv(testFile)

       # X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size)
        clf = joblib.load("model/"+neuralModel)

        ###Predict###
        pre = clf.predict(data_test)
        print("IT IS: ",pre)
        predictResult[0]=pre[0]
        print("result pre: ",predictResult)

    except Exception as e:
        messagebox.showinfo("ERROR while trying to evaluate!", "Did you fill in all the required information?")
        print(e)
