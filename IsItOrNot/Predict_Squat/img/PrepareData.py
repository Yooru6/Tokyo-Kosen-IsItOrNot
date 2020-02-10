import pandas as pd
import os


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

def findCsvFiles(goodFolderPath,badFolderPath):

    #folders

    list_good_foldernames=[]
    directoryPath=goodFolderPath
    for i,file in enumerate(os.listdir(directoryPath)):
        if file.endswith(""):
            folder_name=str(os.path.basename(file))
            list_good_foldernames.append(folder_name)
            #print(folder_name, ' folder added')

    list_bad_foldernames=[]
    directoryPath=badFolderPath
    for i,file in enumerate(os.listdir(directoryPath)):
        if file.endswith(""):
            folder_name=str(os.path.basename(file))
            list_bad_foldernames.append(folder_name)
            #print(folder_name, ' folder added')

    #CSV

    totalgood=0
    list_good_filenames = []
    for i in range (len(list_good_foldernames)):
        directoryPath=goodFolderPath+list_good_foldernames[i]
        for i,file in enumerate(os.listdir(directoryPath)):
            if file.endswith(".csv"):
                file_name=str(os.path.basename(file))
                list_good_filenames.append(file_name)
                print(file_name, ' csv added(good)')
                totalgood+=1

    list_bad_filenames = []
    totalbad=0
    for i in range (len(list_bad_foldernames)):
        directoryPath=badFolderPath+list_bad_foldernames[i]
        for i,file in enumerate(os.listdir(directoryPath)):
            if file.endswith(".csv"):
                file_name=str(os.path.basename(file))
                list_bad_filenames.append(file_name)
                print(file_name, ' csv added(bad)')
                totalbad+=1

    print('Good data added: ',totalgood,"\nBad data added: ",totalbad)

    global list_of_bad_data_folders,list_of_good_data_folders,list_of_badData_file_names,list_of_goodData_file_names

    list_of_bad_data_folders=list_bad_foldernames
    list_of_good_data_folders = list_good_foldernames

    list_of_badData_file_names=list_bad_filenames
    list_of_goodData_file_names=list_good_filenames


    '''-------PANDA FUNCTIONS--------'''

def makeGoodCsvFiles():
    global list_of_good_data_folders,list_of_good_dataFrames
    for i in range (30):
        path='data/good/'+list_of_good_data_folders[0]+'/'+list_of_goodData_file_names[i]
        df_good = pd.read_csv(path)
        df_good.columns = ['First', 'Second', 'ACC X', 'ACC Y', 'ACC Z', 'AX X', 'AX Y', 'AX Z']
        #df_good['output'] = 1

        columns = ['XACC_mean', 'XACC_var', "YACC_mean", "YACC_var", "ZACC_mean", "ZACC_var", "XAX_mean", "XAX_var",
                   "YAX_mean", "YAX_var"]
        new_df_good = pd.DataFrame()
        muuttuja1 = df_good.loc[:, 'ACC X'].std()
        muuttuja2=df_good['ACC X'].mean()
        muuttuja3=df_good['ACC X'].min()
        muuttuja4=df_good['ACC X'].max()

            
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
        new_df_good['output'] = 1
        list_of_good_dataFrames.append(new_df_good)

        new_df_good.to_csv('Data/processed/good_data/'+str(i+1)+'_learning.csv', index=False)

def makeBadCsvFiles():
    global list_of_bad_data_folders, list_of_bad_dataFrames
    for i in range(30):
        path = 'data/bad/' + list_of_bad_data_folders[0] + '/' + list_of_badData_file_names[i]
        df_bad = pd.read_csv(path)
        df_bad.columns = ['First', 'Second', 'ACC X', 'ACC Y', 'ACC Z', 'AX X', 'AX Y', 'AX Z']
        # df_good['output'] = 1

        columns = ['XACC_mean', 'XACC_var', "YACC_mean", "YACC_var", "ZACC_mean", "ZACC_var", "XAX_mean",
                   "XAX_var",
                   "YAX_mean", "YAX_var"]
        new_df_bad = pd.DataFrame()

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
        new_df_bad['output'] = 0
        list_of_bad_dataFrames.append(new_df_bad)
        new_df_bad.to_csv('Data/processed/bad_data/' + str(i+1) + '_learning.csv',index=False)


def combineCsv():

    global list_of_bad_dataFrames,list_of_good_dataFrames,combined_df


    list_combined_frames=list_of_good_dataFrames+list_of_bad_dataFrames
    df=pd.concat(list_combined_frames)
    df.to_csv('Data/processed/combined/combined.csv',index=False)


    #df_help.append(list_combined_frames[5])
    print(df)
    return df




findCsvFiles("data/good/","data/bad/")

makeGoodCsvFiles()
makeBadCsvFiles()

combineCsv()

#print(list_of_good_dataFrames)

#print(makeFolderList("data/hyvdata"), " GG")
'''list_goodData_folder=makeFolderList("data/good")
list_badData_folder=makeFolderList("data/bad")

makeCsvFileList('good',list_goodData_folder)
makeCsvFileList('bad',list_badData_folder)'''




'''------PANDA CODE-------'''
