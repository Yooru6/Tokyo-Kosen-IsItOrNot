from tkinter import messagebox
import pandas as pd
import os
import os.path

'''-------VARIABLES-------'''
list_of_good_data_folders=[]
list_of_bad_data_folders=[]

list_of_goodData_file_names=[]
list_of_badData_file_names=[]

list_of_good_dataFrames=[]
list_of_bad_dataFrames=[]

'''-------FUNCTIONS-------'''

def makeFolderList(folderPath):
    list_foldernames=[]
    directoryPath=folderPath
    for i,file in enumerate(os.listdir(directoryPath)):
        if file.endswith(""):
            folder_name=str(os.path.basename(file))
            list_foldernames.append(folder_name)
            print(folder_name, ' added')

    return list_foldernames

def makeCsvFileList(goodOrBad,folderList):
    list_filenames=[]
    list_foldernames=folderList
    for i in range (len(list_foldernames)):
        directoryPath="data/"+goodOrBad+"/"+list_foldernames[i]
        for i,file in enumerate(os.listdir(directoryPath)):
            if file.endswith(".csv"):
                file_name=str(os.path.basename(file))
                list_filenames.append(file_name)
                print(file_name, ' added')
    #print(list_filenames)
    return list_filenames

'''Function for searching Files from the sub folders '''
def findCsvFiles(goodFolderPath,badFolderPath):

    '''find sub folders from given paths:'''
    ###sub folders in good folder path###
    list_good_foldernames=[]
    directoryPath=goodFolderPath

    for dirName, subdirList, fileList in os.walk(goodFolderPath):
        print('Found directory: %s' % dirName)
        list_good_foldernames.append(dirName)

    ###sub folders in bad folder path###
    list_bad_foldernames=[]
    directoryPath=badFolderPath

    for dirName, subdirList, fileList in os.walk(badFolderPath):
        print('Found directory: %s' % dirName)
        list_bad_foldernames.append(dirName)

    ###for good data:###
    totalgood=0
    list_good_filenames = []
    for i in list_good_foldernames:
        print(len(list_good_foldernames))
    for i in range (len(list_good_foldernames)):
        #directoryPath=list_good_foldernames[i]
        for file in os.listdir(list_good_foldernames[i]):
            if file.endswith(".csv"):
                file_name=str(list_good_foldernames[i]+("\\")+str(os.path.basename(file)))
                list_good_filenames.append(file_name)
                print(file_name, ' csv added(good)')
                totalgood+=1

    ###for bad data:###
    list_bad_filenames = []
    totalbad=0
    for i in range (len(list_bad_foldernames)):
        #directoryPath=badFolderPath+list_bad_foldernames[i]
        for file in os.listdir(list_bad_foldernames[i]):
            if file.endswith(".csv"):
                file_name=str(list_bad_foldernames[i]+("\\")+str(os.path.basename(file)))
                list_bad_filenames.append(file_name)
                print(file_name, ' csv added(bad)')
                totalbad+=1

    print('Good data added: ',totalgood,"\nBad data added: ",totalbad)

    global list_of_bad_data_folders,list_of_good_data_folders,list_of_badData_file_names,list_of_goodData_file_names

    '''Update changes on global lists'''
    list_of_bad_data_folders=list_bad_foldernames
    list_of_good_data_folders = list_good_foldernames

    list_of_badData_file_names=list_bad_filenames
    list_of_goodData_file_names=list_good_filenames


    '''-------PANDA FUNCTIONS--------'''
''''Make new .CSV files from csv files. Adding row with value to present movements quality. Removing Unnecessary rows'''

###Good files:###
def makeGoodCsvFiles():
    global list_of_good_data_folders,list_of_good_dataFrames

    ###Taking XYZ values from the files###
    for i in range (len(list_of_goodData_file_names)):
        path=list_of_goodData_file_names[i]
        df_good = pd.read_csv(path)
        df_good.columns = ['First', 'Second', 'ACC X', 'ACC Y', 'ACC Z', 'AX X', 'AX Y', 'AX Z']

        ###Calculating mean and standard deviation for X, Y and Z AXIS and adding values in the new dataframe###
        new_df_good = pd.DataFrame({'XACC_mean': [df_good['ACC X'].mean()],
                               'XACC_var': [df_good['ACC X'].std()],
                               "YACC_mean": [df_good['ACC Y'].mean()],
                               "YACC_var": [df_good['ACC Y'].std()],
                               "ZACC_mean": [df_good.loc[:, 'ACC Z'].mean()],
                               "ZACC_var": [df_good.loc[:, 'ACC Z'].std()],
                               "XAX_mean": [df_good.loc[:, 'AX X'].mean()],
                               "XAX_var": [df_good.loc[:, 'AX X'].std()],
                               "YAX_mean": [df_good.loc[:, 'AX Y'].mean()],
                               "YAX_var": [df_good.loc[:, 'AX Y'].std()],
                               "ZAX_mean": [df_good.loc[:, 'AX Z'].mean()],
                               "ZAX_var": [df_good.loc[:, 'AX Z'].std()],
                                   })

        ###Giving value that presents quality of movement(0=bad, 1=good)###
        new_df_good['output'] = 1
        list_of_good_dataFrames.append(new_df_good)

        import os.path
        location=os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        ###Saving new file to destinated folder###
        new_df_good.to_csv(location+'/GUI_START/Data/processed/good_data/'+str(i+1)+'_learning.csv', index=False)

###Bad files:###
def makeBadCsvFiles():
    global list_of_bad_data_folders, list_of_bad_dataFrames

    ###Taking XYZ values from the files###
    for i in range(len(list_of_badData_file_names)):
        path = list_of_badData_file_names[i]
        df_bad = pd.read_csv(path)
        df_bad.columns = ['First', 'Second', 'ACC X', 'ACC Y', 'ACC Z', 'AX X', 'AX Y', 'AX Z']

        ###Calculating mean and standard deviation for X, Y and Z AXIS and adding values in the new dataframe###
        new_df_bad = pd.DataFrame({'XACC_mean': [df_bad.loc[:, 'ACC X'].mean()],
                                    'XACC_var': [df_bad.loc[:, 'ACC X'].std()],
                                    "YACC_mean": [df_bad.loc[:, 'ACC Y'].mean()],
                                    "YACC_var": [df_bad.loc[:, 'ACC Y'].std()],
                                    "ZACC_mean": [df_bad.loc[:, 'ACC Z'].mean()],
                                    "ZACC_var": [df_bad.loc[:, 'ACC Z'].std()],
                                    "XAX_mean": [df_bad.loc[:, 'AX X'].mean()],
                                    "XAX_var": [df_bad.loc[:, 'AX X'].std()],
                                    "YAX_mean": [df_bad.loc[:, 'AX Y'].mean()],
                                    "YAX_var": [df_bad.loc[:, 'AX Y'].std()],
                                    "ZAX_mean": [df_bad.loc[:, 'AX Z'].mean()],
                                    "ZAX_var": [df_bad.loc[:, 'AX Z'].std()],
                                    })
        ###Giving value that presents quality of movement(0=bad, 1=good)###
        new_df_bad['output'] = 0
        list_of_bad_dataFrames.append(new_df_bad)

        location=os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        ###Saving new file to destinated folder###
        new_df_bad.to_csv(location+'/GUI_START/Data/processed/bad_data/' + str(i+1) + '_learning.csv',index=False)


'''Combining good and bad data into single list'''
def combineCsv(dataSetName):
    global list_of_bad_dataFrames,list_of_good_dataFrames,combined_df

    list_combined_frames=list_of_good_dataFrames+list_of_bad_dataFrames
    df=pd.concat(list_combined_frames)

    location = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    df.to_csv(location+'/GUI_START/Data/processed/combined/'+dataSetName+'.csv',index=False)

    #df_help.append(list_combined_frames[5])
    print(df)
    return df

'''Functions for GUI'''

def runDataPreparer_training(goodFolderPath, badFolderPath, dataSetName):
    try:
        findCsvFiles(goodFolderPath,badFolderPath)
        makeGoodCsvFiles()
        makeBadCsvFiles()

        combineCsv(dataSetName)
    except Exception as e:
        messagebox.showinfo("ERROR while preparing dataset!", "Have you filled in all the required information?")
        print(e)

def runDataPreparer_testing(goodFolderPath, badFolderPath,dataSetName):
    findCsvFiles(goodFolderPath,badFolderPath)

    makeGoodCsvFiles()
    makeBadCsvFiles()
