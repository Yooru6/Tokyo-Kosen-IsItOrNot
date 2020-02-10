
###Imports###
from sklearn import datasets, model_selection, svm, metrics
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
import pandas as pd
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import distutils.dir_util
###Imports###
from sklearn import datasets, model_selection, svm, metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier


#Config values
neural_accuracy_raiting=1.0
svm_accuracy_raiting=0.0
list_neural_acc=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
list_svm_acc=[0.0,0.0,0.0,0.0,0.0,]
timerLoop=0

predictResult=[3]

train_size = 110
test_size = 0.2

#SVM model
def svmSquatPredict(data_set, kernel, gamma_value, c_value):
    location = ('Data/processed/combined/' + str(data_set))
    data_train = pd.read_csv(location)
    data_test = pd.read_csv(location)

    print(data_train.shape)

    X_all = data_train#data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)
    num_test = 10

    global test_size,train_size

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=.5)
    print("gamma: ",gamma_value,"\nc: ",c_value,"\nkernel: ",kernel)
    ###Classifier###
    clf = svm.SVC(gamma=gamma_value, C=c_value, kernel=kernel)
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

    folder = 'model/'
    filename = 'SVM_' + timestr + '_' +str(accuracy_score)+".model"

    ###MAKE FOLDER###
    #distutils.dir_util.mkpath(folder + filename)
    joblib.dump(clf, folder + '/' + filename)

def decisionTreeSquatPredict(datasetto):
    location = ('Data/processed/combined/' + str(datasetto))
    data_train = pd.read_csv(location)
    data_test = pd.read_csv(location)

    print(data_train.shape)

    X_all = data_train#data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)
    num_test = 10

   # test_size=10
    #train_size=50

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, random_state=2)

    ###Classifier###
    clf = DecisionTreeClassifier(criterion="gini",min_samples_split=2,splitter='best')

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

    folder = 'model/'
    filename = 'DT_' + timestr + '_' +str(accuracy_score)+".model"

    ###MAKE FOLDER###
   # distutils.dir_util.mkpath(folder + filename)
    joblib.dump(clf, folder +'/' + filename)


def decisionTreeSquatPredictFile(testData):

    data_train = pd.read_csv('Data/processed/combined/combined.csv')
    data_test = pd.read_csv(testData)

    print(data_train.shape)
    X_all = data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)
    num_test = 10

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size, random_state=2)

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

    folder = 'model/'
    filename = str(accuracy_score) + '_' + 'DT_' + timestr + '_' + str(train_size) + '_' + str(
        test_size)

    ###MAKE FOLDER###
   # distutils.dir_util.mkpath(folder + filename)
    joblib.dump(clf, folder + filename + '/' + filename)

#Neural model for predicting
def neuralSquatPredict(train_size_value, test_size_value,activation,hl_size,l_rate):

    ###Print info about data###
    data_train = pd.read_csv('Data/processed/combined/combined.csv')
    data_test = pd.read_csv('Data/processed/combined/combined.csv')
    print(data_test.shape)

    print('Training Neural Network...')

    X_all = data_train.drop(['output'], axis=1)#data_train
    #print(X_all)
    y_all = data_train['output']
    #print(y_all)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size)

    #Classifier
    clf = MLPClassifier(activation=activation, solver='adam', hidden_layer_sizes=hl_size,learning_rate_init=l_rate, batch_size=10, max_iter=2000)

    #Train
    clf.fit(X_train, y_train)

    #Predict
    pre = clf.predict(X_test)

    #Accuracy of Classifier
    accuracy_score = metrics.accuracy_score(y_test, pre)
    print(accuracy_score)

    #Confusion Matrix of results
    result_matrix = metrics.confusion_matrix(pre,y_test)
    print(result_matrix)

    #Accuracy of Classifier
    accuracy_score = metrics.accuracy_score(y_test, pre)
    list_neural_acc[0]=(accuracy_score * 100)
    print(accuracy_score)

    print(classification_report(y_test, pre))

    print('NN: ',accuracy_score)

    folder='model/'

    filename='NN_' + timestr + '_' +str(accuracy_score)

    ###MAKE FOLDER###
    import distutils.dir_util
    #distutils.dir_util.mkpath(folder+filename)
    joblib.dump(clf,folder+'/'+filename+".model")

    print(neural_accuracy_raiting," MachineLearning.py")

#Neural2 model for predicting
def neuralSquatPredict2(datasetto,train_size_value, test_size_value,activation,hl_size,l_rate):


    #Print info about data###
    location=('Data/processed/combined/'+str(datasetto))
    data_train = pd.read_csv(location)
    data_test = pd.read_csv(location)
    print(data_test.shape)

    print('Training Neural Network...')

    X_all = data_train#data_train.drop(['output'], axis=1)#data_train
    print(X_all)
    y_all = data_train['output']
    print(y_all)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=0.2, random_state=123)#train_size=train_size)

    clf = MLPClassifier(activation=activation, solver='adam', hidden_layer_sizes=hl_size,
                        learning_rate_init=l_rate )

    #Train
    clf.fit(X_train, y_train)

    #Predict
    pre = clf.predict(X_test)

    #Accuracy of Classifier
    accuracy_score = metrics.accuracy_score(y_test, pre)
    print(accuracy_score)

    #Confusion Matrix of results
    result_matrix = metrics.confusion_matrix(pre,y_test)
    print(result_matrix)

    #Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    list_neural_acc[0]=(accuracy_score * 100)
    print(accuracy_score)

    print(classification_report(y_test, pre))

    print('NN: ',accuracy_score)

    folder='model/'

    filename='NN_' + timestr + '_' +str(accuracy_score)+".model"

    ###MAKE FOLDER###
    import distutils.dir_util
   # distutils.dir_util.mkpath(folder+filename)

    joblib.dump(clf,folder+'/'+filename)

    print(neural_accuracy_raiting," MachineLearning.py")


def SquatLoadPredict(testFile,neuralModel):

    ###Loading data
    data_train = pd.read_csv('Data/processed/combined/combined.csv')
    data_test = pd.read_csv(testFile)
    print(data_test.shape)
    print(data_train.shape)

    data_test=data_test.drop(['output'], axis=1)
    X_all = data_train.drop(['output'], axis=1)#data_train
    print(data_test)
    y_all = data_train['output']
   # print(y_all)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size)
    clf = joblib.load("model/"+neuralModel)

    ###Predict###
    print("Predicting...")
    pre = clf.predict(data_test)
    print("IT IS: ",pre[0])

    global predictResult
    predictResult[0]=int(pre[0])
    print("result pre: ",predictResult)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
   # print(accuracy_score)

    #Matrix of results
    result_matrix = metrics.confusion_matrix(pre,y_test)
   # print(result_matrix)

    ###Accuracy of Classifier###
    accuracy_score = metrics.accuracy_score(y_test, pre)
    list_neural_acc[0]=(accuracy_score * 100)
   # print(accuracy_score)

   # print(classification_report(y_test, pre))

    print('NN: ',accuracy_score)
    #print(neural_accuracy_raiting," MachineLearning.py")

def SquatLoadPredict2(testFile, neuralModel):
        # data_train = pd.read_csv('Data/processed/combined/combined.csv')
        data_test = pd.read_csv(testFile)
        #   X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=test_size, train_size=train_size)
        clf = joblib.load("model/" + neuralModel)

        ###Predict###
        pre = clf.predict(data_test)
        print("IT IS: ", pre[0])

        global predictResult
        predictResult[0] = int(pre[0])
        print("result pre: ", predictResult)

def SVMSquatPredict2(kernel, gamma_value, c_value):
        ###Print info about data###

        data_train = pd.read_csv('Data/processed/combined/combined.csv')
        data_test = pd.read_csv('Data/processed/combined/combined.csv')
        print(data_test.shape)

        print('Training Neural Network...')

        X_all = data_train  # data_train.drop(['output'], axis=1)#data_train
        print(X_all)
        y_all = data_train['output']
        print(y_all)

        X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, y_all, test_size=0.2,
                                                                            random_state=123)  # train_size=train_size)

        clf = svm.SVC(gamma=gamma_value, C=c_value, kernel=kernel)

        ###Train###
        clf.fit(X_train, y_train)

        ###Predict###
        pre = clf.predict(X_test)

        ###Accuracy of Classifier###
        accuracy_score = metrics.accuracy_score(y_test, pre)
        print(accuracy_score)

        # Matrix of results
        result_matrix = metrics.confusion_matrix(pre, y_test)
        print(result_matrix)

        ###Accuracy of Classifier###
        accuracy_score = metrics.accuracy_score(y_test, pre)
        list_neural_acc[0] = (accuracy_score * 100)
        print(accuracy_score)

        print(classification_report(y_test, pre))

        print('SVM: ', accuracy_score)

        folder = 'model/'

        filename = 'SVM_' + timestr + '_' + str(accuracy_score) + ".pkl"

        ###MAKE FOLDER###
        import distutils.dir_util
        # distutils.dir_util.mkpath(folder+filename)

        joblib.dump(clf, folder + '/' + filename + ".model")

        print(neural_accuracy_raiting, " MachineLearning.py")