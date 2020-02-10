
from tkinter import messagebox
from tkinter import filedialog
import os
from Project.Programs.SquatOrNot.DO_SQUAT.Functions import *
THREAD_LOCK = threading.Lock()
import datetime
from timeit import default_timer as timer
from tkinter import *


class TrainModel_Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Is it squat?")

        '''-------------     MENU      -------------'''

        def nothing():
            print("Nothing Nothing Nothing....")

        def hello():
            print
            "hello!"

        menubar = Menu(self)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=hello)
        filemenu.add_command(label="Save", command=hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.master.config(menu=menubar)

        #Button.config(width=200, height=200)
        MasterFrame = Frame(master)



        '''-------------     FRAME NEURAL      -------------'''

        Frame1 = Frame(master)
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Grid.columnconfigure(Frame1,1,weight=1)
    #    Grid.columnconfigure(root, 3, weight=1)

    # --- FONTS ---
        labelFont="Cambria"
        labelFontSize=14
        labelTitleSize = 22

        entryFont="Cambria"
        entryFontSize=13


        padX=10
        padY=2

    # ---TITLE---
        label_title1 = Label(Frame1, text='Neural Network')
        label_title1.config(font=(labelFont, labelTitleSize))
        label_title1.grid(row=0,column=1, padx=15, pady=10, sticky=W+E+N+S)

    # ---LABELS---
        label_neuron = Label(Frame1, text='Neurons')
        label_neuron.config(font=(labelFont,labelFontSize))

        label_lrate = Label(Frame1, text='Learning rate')
        label_lrate.config(font=(labelFont,labelFontSize))

        label_accuResult = Label(Frame1, text='Accuracy')
        label_accuResult.config(font=(labelFont,labelFontSize))

        label_neural_result = Label(Frame1, text="?",width=10)
        label_neural_result.config(font=(labelFont,labelFontSize))

        label_neuron.grid(row=1, padx=padX, pady=padY, sticky=W+E+N+S)
        label_lrate.grid(row=2, padx=padX, pady=padY, sticky=W+E+N+S)
        label_accuResult.grid(row=4, column=0, padx=padX, pady=padY, sticky=W+E+N+S)
        label_neural_result.grid(row=4, column=1, padx=padX, pady=padY, sticky=W+E+N+S)



    # ---ENTRYS---
        entry_neuron = Entry(Frame1)
        entry_lrate = Entry(Frame1)

        entry_neuron.grid(row=1, column=1, padx=padX, pady=padY, sticky=W+E+N+S)
        entry_neuron.config(font=(entryFont,entryFontSize))

        entry_lrate.grid(row=2, column=1, padx=padX, pady=padY,sticky=W+E+N+S )
        entry_lrate.config(font=(entryFont,entryFontSize))

    # ---Opitonmenu---

        label_activation_neural = Label(Frame1, text='Activation(f)')
        label_activation_neural.config(font=(labelFont,labelFontSize))

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
        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Grid.columnconfigure(Frame2, 1, weight=1)


    # ---TITLE---
        label_title2 = Label(Frame2, text='Support Vector Machine')
        label_title2.config(font=(labelFont, labelTitleSize))
        label_title2.grid(row=0,column=1, padx=15, pady=10, sticky=W+E+N+S)

    # ---LABELS---
        label_gamma = Label(Frame2, text='Gamma',width=10)
        label_gamma.config(font=(labelFont,labelFontSize))

        label_c = Label(Frame2, text='C Value')
        label_c.config(font=(labelFont,labelFontSize))

        label_accuResult_svm = Label(Frame2, text='Accuracy')
        label_accuResult_svm.config(font=(labelFont,labelFontSize))

        label_svm_result = Label(Frame2, text="?",width=10)
        label_svm_result.config(font=(labelFont,labelFontSize))

        label_gamma.grid(row=1, padx=padX, pady=padY, sticky=W+E+N+S)
        label_c.grid(row=2, padx=padX, pady=padY, sticky=W+E+N+S)
        label_accuResult_svm.grid(row=4, column=0, padx=padX, pady=padY, sticky=W+E+N+S)
        label_svm_result.grid(row=4, column=1, padx=padX, pady=padY, sticky=W+E+N+S)



    # ---ENTRIES---
        entry_gamma = Entry(Frame2,width=40)
        entry_c = Entry(Frame2)

        entry_gamma.grid(row=1, column=1, padx=padX, pady=padY, sticky=W+E+N+S)
        entry_gamma.config(font=(entryFont,entryFontSize))

        entry_c.grid(row=2, column=1, padx=padX, pady=padY,sticky=W+E+N+S )
        entry_c.config(font=(entryFont,entryFontSize))

        # ---Opitonmenu---

        label_kernel_svm = Label(Frame2, text='Kernel')
        label_kernel_svm.config(font=(labelFont, labelFontSize))

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


        '''-------------     FRAME3      -------------'''

        Frame3 = Frame(master)
        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)
        Grid.columnconfigure(Frame3, 1, weight=0)


        img = PhotoImage(file=("img/brain.png"))
        labelPhoto= Label(Frame3,image=img)
        labelPhoto.image = img
        labelPhoto.grid(row=2, padx=20, pady=20, sticky=W+E+N+S)

        label_battleTime = Label(Frame3, text='',width=10)
        label_battleTime.config(font=(labelFont,12))
        label_battleTime.grid(row=3, padx=padX, pady=padY, sticky=W + E + N + S)



        '''-------------     FRAME4      -------------'''

        Frame4 = Frame(master)
        Frame4.grid(row = 6, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Grid.columnconfigure(Frame4, 1, weight=1)


        label_title4 = Label(Frame4, text='Decision Tree')
        label_title4.config(font=(labelFont, labelTitleSize))
        label_title4.grid(row=0,column=1, padx=15, pady=10, sticky=W+E+N+S)


        '''-------------     FRAME5      -------------'''

        Frame5 = Frame(master)
        Frame5.grid(row = 9, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
        Grid.columnconfigure(Frame5, 1, weight=0)


        label_battleTime = Label(Frame5, text='',width=10)
        label_battleTime.config(font=(labelFont,12))
        label_battleTime.grid(row=3, padx=padX, pady=padY, sticky=W + E + N + S)



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

        def runNeural():
            try:
                label_neural_result.config(text="Learning...")
                threading.Thread(target=train_neural,args=(1000, 100, activationVariable.get(), int(entry_neuron.get()), float(entry_lrate.get()))).start()
            except Exception as e:
                messagebox.showinfo("ERROR in NN input!", "Are the fields filled?")
                print(e)
           # print(neuralit[0])


        def runSquatNeural():
            try:
                label_neural_result.config(text="Learning...")
                threading.Thread(target=neuralSquatPredict,args=(1000, 100, activationVariable.get(), int(entry_neuron.get()), float(entry_lrate.get()))).start()
            except Exception as e:
                messagebox.showinfo("ERROR in NN input!", "Are the fields filled?")
                print(e)
           # print(neuralit[0])

        def runSvm():
            try:
                threading.Thread(target=train_svm,args=(1000, 100, kernelVariable.get(), float(entry_gamma.get()), int(entry_c.get()))).start()
            except Exception as e:
                messagebox.showinfo("ERROR in SVM input!", "Are the fields filled?")
                print(e)
           # print(neuralit[0])

        def resultClock():

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
            # lab['text'] = time
            self.after(1000, resultClock)  # run itself again after 1000 ms


        def runSquatSvm():
            try:
                threading.Thread(target=svmSquatPredict,args=(kernelVariable.get(), float(entry_gamma.get()), int(entry_c.get()))).start()
            except Exception as e:
                messagebox.showinfo("ERROR in SVM input!", "Are the fields filled?")
                print(e)
           # print(neuralit[0])


        def runSquatDecisionTree():
            try:
                threading.Thread(target=decisionTreeSquatPredict).start()
            except Exception as e:
                messagebox.showinfo("ERROR in SVM input!", "Are the fields filled?")
                print(e)
           # print(neuralit[0])


        def resultClock():

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
            # lab['text'] = time
            self.after(500, resultClock)  # run itself again after 1000 ms


        def openFile():
            file=filedialog.askopenfile(filetypes=(('CSV files','*.csv'),('All files','*.*')))
            filename=os.path.basename(file.name)

            print('Chosenfile: '+str(file.name))

            label_file=Label(Frame5,text=filename)

            label_file.grid(row=3,column=0,padx=15,pady=2,sticky=W+E+S)


        '''-------------     BUTTONS      -------------'''
        btnList=["Neural Network","SVM",'DecisionTree','Choose a Squat',"Battle"]
        for i in range(6):
            Frame5.rowconfigure(i, weight=1)

        for j in range(4):
            Frame5.columnconfigure(j, weight=1)


        Grid.columnconfigure(Frame5,(4,1),weight=0)


        Frame4.columnconfigure(1,weight=1)
        Frame4.rowconfigure(0,weight=1)

        buttonWidth=30
        buttonWidthSquat=38

        Button(Frame5, text="{0}".format(btnList[0]),width=buttonWidth,command= runSquatNeural,font=("Cambria",13),bg="#f4f4f1").grid(row=5,column=0, padx=15, pady=10,sticky=E+W)
        Button(Frame5, text="{0}".format(btnList[1]),width=buttonWidth,command=runSquatSvm,font=("Cambria",13),bg="#f4f4f1").grid(row=5,column=1, padx=15, pady=10,sticky=E+W)
        Button(Frame5, text="{0}".format(btnList[2]),width=buttonWidth,command= runSquatDecisionTree,font=("Cambria",13),bg="#f4f4f1").grid(row=5,column=2, padx=15, pady=10,sticky=E+W)
        Button(Frame5, text="{0}".format(btnList[3]), command=openFile,font=("Cambria", 13), bg="#ffffff").grid(row=4, column=0, padx=15, pady=10, sticky=E+W)

        resultClock()

'''
root = Tk()
app = Application(master=root)
app.mainloop()

'''