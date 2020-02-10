from tkinter import messagebox
from tkinter import filedialog
import os
from Make_Model.Functions import *
import threading
THREAD_LOCK = threading.Lock()
import datetime
from timeit import default_timer as timer
from tkinter import *
import joblib

class TrainModel_Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.wm_attributes('-topmost', 1)
        self.master.title("Model Makerrrrr")

        '''-------------     MENU      -------------'''
        def hello():
            print
            "hello!"
        # ---Fonts----
        padX=40
        padY=2

        menubar = Menu(self)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=hello)
        filemenu.add_command(label="Save", command=hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.master.config(menu=menubar)

        Grid.columnconfigure(self.master, 1, weight=1)

        '''-------------     FRAME Dataset      -------------'''
        Frame0 = Frame(master)
        Frame0.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = W+E+N+S)
        Grid.columnconfigure(Frame0,1,weight=1)

        # --- TITLE ---
        img = PhotoImage(file=("img\\model_title_50.png"))
        label_title_photo= Label(Frame0,image=img)
        label_title_photo.image = img
        label_title_photo.grid(row=0,column=1, padx=padX, pady=padY, sticky=W+E+N+S)
        #Button.config(width=200, height=200)
        MasterFrame = Frame(master)

        Grid.columnconfigure(Frame0, 1, weight=1)
        # ---Opitonmenu---

        label_dataset = Label(Frame0, text='Dataset  ')
        label_dataset.grid(row=1, padx=padX, pady=padY, sticky= W)

        list_models = []
        for i, file in enumerate(os.listdir("Data\\processed\\combined")):
            if file.endswith(""):
                folder_name = str(os.path.basename(file))
                list_models.append(folder_name)

        chosenDataset = StringVar(Frame0)
        chosenDataset.set("Choose Dataset")  # default value
        # Variable is gettable .get()

        dataset_dropdown = OptionMenu(Frame0, chosenDataset, *list_models)
        dataset_dropdown.config(bg="#f6ddff", width=20)
        dataset_dropdown.grid(row=1, column=1, padx=70, pady=padY, sticky=W + E + N + S)

        '''-------------     FRAME NEURAL      -------------'''
        Frame1 = Frame(master)
        Frame1.grid(row = 3, column = 0, rowspan = 2, columnspan = 2, sticky = W+E+N+S)
        Grid.columnconfigure(Frame1,1,weight=1)
    #    Grid.columnconfigure(root, 3, weight=1)

    # --- FONTS ---
        labelFont="Cambria"
        labelFontSize=14
        labelTitleSize = 22

        entryFont="Cambria"
        entryFontSize=13

    # ---TITLE---
        img = PhotoImage(file=("img\\nn_label_25.png"))
        label_neural_photo= Label(Frame1,image=img)
        label_neural_photo.image = img
        label_neural_photo.grid(row=0,column=1, padx=15, pady=10, sticky=W+E+N+S)


    # ---LABELS---
        label_neuron = Label(Frame1, text='Neurons')
        label_neuron.grid(row=1, padx=padX, pady=padY, sticky=W+E+N+S)

        label_lrate = Label(Frame1, text='Learning rate')
        label_lrate.grid(row=2, padx=padX, pady=padY, sticky=W + E + N + S)

        label_accuResult = Label(Frame1, text='Accuracy')
        label_accuResult.grid(row=4, column=0, padx=padX, pady=padY, sticky=W + E + N + S)

        label_neural_result = Label(Frame1, text="?",width=10)
        label_neural_result.grid(row=4, column=1, padx=padX, pady=padY, sticky=W + E + N + S)


    # ---ENTRYS---
        entry_neuron = Entry(Frame1)
        entry_neuron.grid(row=1, column=1, padx=padX, pady=padY, sticky=W+E+N+S)

        entry_lrate = Entry(Frame1)
        entry_lrate.grid(row=2, column=1, padx=padX, pady=padY,sticky=W+E+N+S )

    # ---Opitonmenu---
        label_activation_neural = Label(Frame1, text='Activation(f)')
        label_activation_neural.grid(row=3, column=0, padx=padX, pady=padY, sticky=W+E+N+S)

        activationOptions=[
            'relu',
            'tanh',
            'logistic',
            'identity'
        ]

        activationVariable = StringVar(Frame1)
        activationVariable.set(activationOptions[0])  # default value
        #Variable is gettable .get()

        activation_dropdown = OptionMenu(Frame1, activationVariable, *activationOptions)
        activation_dropdown.grid(row=3,column=1,padx=padX,pady=padY, sticky=W+E+N+S)

        '''-------------     FRAME SVM      -------------'''
        Frame2 = Frame(master)
        Frame2.grid(row = 6, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Grid.columnconfigure(Frame2, 1, weight=1)

    # ---TITLE---
        img = PhotoImage(file=("img\\svm_label_25.png"))
        label_svm_photo= Label(Frame2,image=img)
        label_svm_photo.image = img
        label_svm_photo.grid(row=0,column=1, padx=15, pady=10, sticky=W+E+N+S)

    # ---LABELS---
        label_gamma = Label(Frame2, text='Gamma',width=10)
        label_c = Label(Frame2, text='C Value')
        label_accuResult_svm = Label(Frame2, text='Accuracy')
        label_svm_result = Label(Frame2, text="?",width=10)

        label_gamma.grid(row=1, padx=padX, pady=padY, sticky=W+E+N+S)
        label_c.grid(row=2, padx=padX, pady=padY, sticky=W+E+N+S)
        label_accuResult_svm.grid(row=4, column=0, padx=padX, pady=padY, sticky=W+E+N+S)
        label_svm_result.grid(row=4, column=1, padx=padX, pady=padY, sticky=W+E+N+S)

    # ---ENTRIES---
        entry_gamma = Entry(Frame2,width=40)
        entry_c = Entry(Frame2)

        entry_gamma.grid(row=1, column=1, padx=padX, pady=padY, sticky=W+E+N+S)
        entry_c.grid(row=2, column=1, padx=padX, pady=padY,sticky=W+E+N+S )

        # ---Opitonmenu---
        label_kernel_svm = Label(Frame2, text='Kernel')
        label_kernel_svm.grid(row=3, column=0, padx=padX, pady=padY, sticky=W + E + N + S)
        kernelOptions = [
            'rbf',
            'sigmoid',
            'poly',
            'linear'
        ]

        kernelVariable = StringVar(Frame2)
        kernelVariable.set(kernelOptions[0])  # default value
        # Variable is gettable .get()

        kernel_dropdown = OptionMenu(Frame2, kernelVariable, *kernelOptions)
        kernel_dropdown.grid(row=3, column=1, padx=padX, pady=padY, sticky=W + E + N + S)

        '''-------------     DECISIONTREE FRAME      -------------'''
        Frame3 = Frame(master)
        Frame3.grid(row = 9, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Grid.columnconfigure(Frame3, 1, weight=1)

        img = PhotoImage(file=("img\\dt_label_25.png"))
        label_dt_photo= Label(Frame3,image=img)
        label_dt_photo.image = img
        label_dt_photo.grid(row=0,column=1, padx=15, pady=10, sticky=W+E+N+S)

        # ---Labels---
        label_minSampleSplit = Label(Frame3, text='Min Sample Split')
        label_minSampleSplit.grid(row=1, padx=padX, pady=padY, sticky=W+E+N+S)

        # ---Entiers---
        entry_minSampleSplit = Entry(Frame3)
        entry_minSampleSplit.grid(row=1, column=1, padx=padX, pady=padY, sticky=W + E + N + S)

        # ---Opitonmenu---

            #criterion#
        label_criterion_dt = Label(Frame3, text='Criterion')
        label_criterion_dt.grid(row=2, column=0, padx=padX, pady=padY, sticky=W + E + N + S)
        activationOptions = [
            'gini',
            'entropy'
        ]

        criterionVariable = StringVar(Frame3)
        criterionVariable.set(activationOptions[0])  # default value
        # Variable is gettable .get()

        criterion_dropdown = OptionMenu(Frame3, criterionVariable, *activationOptions)
        criterion_dropdown.grid(row=2, column=1, padx=padX, pady=padY, sticky=W + E + N + S)

            #Splitter#
        label_splitter_dt = Label(Frame3, text='Splitter')
        label_splitter_dt.grid(row=3, column=0, padx=padX, pady=padY, sticky=W + E + N + S)
        splitterOptions = [
            'best',
            'random'
        ]

        splitterVariable = StringVar(Frame3)
        splitterVariable.set(splitterOptions[0])  # default value
        # Variable is gettable .get()

        splitter_dropdown = OptionMenu(Frame3, splitterVariable, *splitterOptions)
        splitter_dropdown.grid(row=3, column=1, padx=padX, pady=padY, sticky=W + E + N + S)

        '''-------------     FRAME5      -------------'''
        Frame5 = Frame(master)
        Frame5.grid(row = 12, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
        Grid.columnconfigure(Frame5, 1, weight=0)

        label_battleTime = Label(Frame5, text='',width=10)
        label_battleTime.config(font=(labelFont,12))
        #label_battleTime.grid(row=3, padx=padX, pady=padY, sticky=W + E + N + S)

        '''-------------     Functions      -------------'''
        def timerClock():

            start_time = timer()
            while True:
                seconds="%.2f" % float(timer()- start_time)
                #print(seconds)
                label_battleTime.config(text='Battle in progress: '+seconds+" seconds")
                time.sleep(0.01)

                if list_neural_acc[0]>0and list_svm_acc[0]>0:
                    label_battleTime.config(text='Battle has ended after: ' + seconds+" seconds")
                    break

        ###Button functions###
        def runBoth():
            try:
                neural = threading.Thread(target=train_neural,args=(1000,100,"relu",int(entry_neuron.get()),float(entry_lrate.get())))
                svm= threading.Thread(target=train_svm,args=(1000,100,'rbf',float(entry_gamma.get()),int(entry_c.get())))

                neural.start()
                svm.start()
                threading.Thread(target=timerClock).start()

                time = datetime.datetime.now().strftime("Time: %H:%M:%S")

            except Exception as e:
                messagebox.showinfo("ERROR!", "Are the fields filled?")
                print(e)

        def runSquatNeural():
            try:
                label_neural_result.config(text="Learning...")
                print(chosenDataset.get())
                threading.Thread(target=neuralSquatPredict2,args=(chosenDataset.get(),1000, 100, activationVariable.get(), int(entry_neuron.get()), float(entry_lrate.get()))).start()
            except Exception as e:
                messagebox.showinfo("ERROR in NN input!", "Are the fields filled?")
                print(e)
           # print(neuralit[0])

        def runSquatSvm():
            try:
                threading.Thread(target=svmSquatPredict,args=(chosenDataset.get(),kernelVariable.get(), float(entry_gamma.get()), int(entry_c.get()))).start()
            except Exception as e:
                messagebox.showinfo("ERROR in SVM input!", "Are the fields filled?")
                print(e)
           # print(neuralit[0])

        def runSquatDecisionTree():
            try:
                muuttuja=chosenDataset.get()
                threading.Thread(target=decisionTreeSquatPredict(muuttuja)).start()
            except Exception as e:
                messagebox.showinfo("ERROR in SVM input!", "Are the fields filled?")
                print(e)

        def accuracyUpdate():
            time = datetime.datetime.now().strftime("Time: %H:%M:%S")
            try:
                label_neural_result.config(text=str("%.2f" % list_neural_acc[0]) + "%")
                label_svm_result.config(text=str("%.2f" % list_svm_acc[0]) + "%")
                if list_neural_acc[0]==0:
                    label_neural_result.config(text=str("Unknown"))
                    list_neural_acc[0]=0.0
                if list_svm_acc[0]== 0:
                    label_svm_result.config(text=str("Unknown"))
                    list_svm_acc[0]=0.0

            except:
                print("fail")
            self.after(500, accuracyUpdate)  # run itself again after 1000 ms

        def openFile():
            file=filedialog.askopenfile(filetypes=(('CSV files','*.csv'),('All files','*.*')))
            filename=os.path.basename(file.name)

            print('Chosenfile: '+str(file.name))

            label_file=Label(Frame5,text=filename)

            label_file.grid(row=3,column=0,padx=15,pady=2,sticky=W+E+S)

        '''-------------     BUTTONS      -------------'''
        for j in range(4):
            Grid.columnconfigure(Frame5, j, weight=1)

        btnList = ["Neural Network", "SVM", 'DecisionTree', 'Choose a Squat', "Battle"]
        #Grid.columnconfigure(Frame5,(4,1),weight=0)

        Frame3.columnconfigure(1,weight=1)
        Frame3.rowconfigure(0,weight=1)
        buttonWidth=20
        buttonWidthSquat=38
        buttonHeight=2

        Button(Frame5, text="{0}".format(btnList[0]),width=buttonWidth,height=buttonHeight,command= runSquatNeural,font=("Cambria",13),bg="#f4f4f1").grid(row=5,column=1, padx=15, pady=20,sticky=E+W)
        Button(Frame5, text="{0}".format(btnList[1]),width=buttonWidth,height=buttonHeight,command=runSquatSvm,font=("Cambria",13),bg="#f4f4f1").grid(row=5,column=2, padx=15, pady=20,sticky=E+W)
        Button(Frame5, text="{0}".format(btnList[2]),width=buttonWidth,height=buttonHeight,command= runSquatDecisionTree,font=("Cambria",13),bg="#f4f4f1").grid(row=5,column=3, padx=15, pady=20,sticky=E+W)
        #Button(Frame5, text="{0}".format(btnList[3]), command=openFile,font=("Cambria", 13), bg="#ffffff").grid(row=4, column=0, padx=15, pady=10, sticky=E+W)

        '''-----------     FONTS & COLOURS     -------------'''
        ###Backgrounds###
        bgColor = "#292929"
        label_fontColor="#e575ff"
        label_accuracyColor="#ff3a3a"

        ###FRAMES###
        self.master.config(bg=bgColor)
        Frame0.config(bg=bgColor)
        Frame1.config(bg=bgColor)
        Frame2.config(bg=bgColor)
        #Frame4.config(bg=bgColor)
        Frame3.config(bg=bgColor)
        Frame5.config(bg=bgColor)

        ###LABELS & ENTRIES###
         #---Title
        label_title_photo.config(bg=bgColor)
        label_dataset.config(font=(labelFont, labelFontSize), foreground=label_fontColor, bg=bgColor)

         #---Neural
        label_neural_photo.config(bg=bgColor)

        #label_title1.config(font=(labelFont, labelTitleSize))
        label_neuron.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_lrate.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_activation_neural.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_accuResult.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_neural_result.config(font=(labelFont, labelFontSize),foreground=label_accuracyColor, bg=bgColor)

        entry_neuron.config(font=(entryFont, entryFontSize))
        entry_lrate.config(font=(entryFont, entryFontSize))

        #---SVM
        label_svm_photo.config(bg=bgColor)

        #label_title2.config(font=(labelFont, labelTitleSize))
        label_gamma.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_c.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_kernel_svm.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_accuResult_svm.config(font=(labelFont, labelFontSize),foreground=label_fontColor, bg=bgColor)
        label_svm_result.config(font=(labelFont, labelFontSize),foreground=label_accuracyColor, bg=bgColor)

        entry_gamma.config(font=(entryFont, entryFontSize))
        entry_c.config(font=(entryFont,entryFontSize))

        #---DT
        label_dt_photo.config(bg=bgColor)

        label_minSampleSplit.config(font=(labelFont, labelFontSize), foreground=label_fontColor, bg=bgColor)
        label_criterion_dt.config(font=(labelFont, labelFontSize), foreground=label_fontColor, bg=bgColor)

        #label_Splitter.config(font=(labelFont, labelFontSize), foreground=label_fontColor, bg=bgColor)
        label_splitter_dt.config(font=(labelFont, labelFontSize), foreground=label_fontColor, bg=bgColor)

            #---Side PIC
        label_battleTime.config(font=(labelFont, 12))

        ###Entries###
        accuracyUpdate()