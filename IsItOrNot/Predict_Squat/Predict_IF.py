
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter import *
import threading
from Predict_Squat.Functions import *
import datetime
from timeit import default_timer as timer

pathToTestFile=""
class Squat_Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.frame=Frame(master)
        self.grid()
        self.master.wm_attributes('-topmost', 1)
        self.master.title("Is It or Not?")

        '''-------------     MENU      -------------'''
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

        bgColor="#292929"
        self.master.config(menu=menubar,bg=bgColor)

        # ---TITLE(PIC)---
        img = PhotoImage(file=("img/IsOrNot_52.png"))
        labelPhoto_squatGui= Label(self.master,image=img)
        labelPhoto_squatGui.config(bg=bgColor)
        labelPhoto_squatGui.image = img
        labelPhoto_squatGui.grid(row=0,column=0, padx=15, pady=10, sticky=W+E+N+S)

        '''-------------     FRAME EVERYTHING      -------------'''
        FrameMain = Frame(master)
        FrameMain.config(bg=bgColor)
        FrameMain.grid(row = 1, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)
        Grid.columnconfigure(FrameMain,1,weight=1)

        '''-------------     FRAME Squat      -------------'''

        Frame1 = Frame(FrameMain)
        Frame1.config(bg=bgColor)
        Frame1.grid(row = 3, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
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

    # ---Button---

         #Open filedialog and choose file for predicting.
        def openPredictFile():
            filename=None
            self.master.wm_attributes('-topmost', 0)
            file=filedialog.askopenfile(filetypes=(('CSV files','*.csv'),('All files','*.*')),initialdir='C:\\Users\\Yooru\\Desktop\\School\\Git\\S-il-\\SquatOrNot\\GUI_START\\Data\\Testidata')
            filename=str(os.path.basename(file.name))
            print(filename)
            global pathToTestFile

            pathToTestFile=str(file.name)

            print('Chosenfile: '+str(file.name))
            print("Update")

            label_file=Label(Frame1,text=filename)
            label_file.config(bg=bgColor,foreground='yellow')
            label_file.grid(row=0,column=0,padx=70,pady=2,sticky=W+E+S)
            self.master.wm_attributes('-topmost', 1)

        middlepadx=42
        Button(Frame1, text="CHOOSE MOVEMENT",height=2,width=40, command=openPredictFile,font=("Cambria", 13), bg="#ffffff").grid(row=1, column=0, padx=70, pady=10, sticky=W+E+S+N)


    # ---IMAGE---
        img = PhotoImage(file=("img/squatMust-sensor.png"))
        labelPhoto_squatGui= Label(Frame1,image=img)
        labelPhoto_squatGui.config(bg=bgColor)
        labelPhoto_squatGui.image = img
        labelPhoto_squatGui.grid(row=3,column=0, padx=100, pady=10, sticky= E)

    # ---Opitonmenu---
        list_models=[]
        for i, file in enumerate(os.listdir("model/")):
            if file.endswith(".model"):
                folder_name = str(os.path.basename(file))
                list_models.append(folder_name)

        chosenModel = StringVar(Frame1)
        chosenModel.set("Choose Model")  # default value
        #Variable is gettable .get()

        activation_dropdown = OptionMenu(Frame1, chosenModel, *list_models)
        activation_dropdown.config(bg="#ffffff",width=20)
        activation_dropdown.grid(row=2,column=0,padx=140,pady=padY, sticky=W+E+N+S)

        '''-------------    BUTTON FRAME      -------------'''
        Frame5 = Frame(FrameMain)
        Frame5.config(bg=bgColor)
        Frame5.grid(row = 12, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)
        Grid.columnconfigure(Frame5, 1, weight=1)

        label_battleTime = Label(Frame5, text='',width=10)
        label_battleTime.config(font=(labelFont,12))
        label_battleTime.grid(row=3, padx=padX, pady=padY, sticky=W + E + N + S)

        '''-------------     Functions      -------------'''
        ###Button functions###
        def runEvaluate():
            print(pathToTestFile)
            try:
                #label_neural_result.config(text="Squatting...")
                threading.Thread(target=SquatLoadPredict, args=(pathToTestFile, (chosenModel.get()))).start()
            except Exception as e:
                messagebox.showinfo("ERROR in NN input!", "Are the fields filled?")
                print(e)


        def resultClock():
            time = datetime.datetime.now().strftime("Time: %H:%M:%S")
            try:
                if predictResult[0]==0:
                    #    global labelPhoto
                    img = PhotoImage(file=("img/bad.png"))
                    labelPhoto_squatGui.image = img
                    labelPhoto_squatGui.config(image=img)
                elif predictResult[0]==1:
                #    global labelPhoto
                    img = PhotoImage(file=("img/good.png"))
                    labelPhoto_squatGui.image = img
                    labelPhoto_squatGui.config(image=img)

            except:
                print("fail")
            # lab['text'] = time
            self.after(500, resultClock)  # run itself again after 1000 ms

        '''-------------     BUTTONS      -------------'''
        btnList=["Neural Network","SVM",'DecisionTree','Choose a Squat',"Battle"]

        Grid.columnconfigure(Frame5,(1),weight=1)

        buttonWidth=36
        buttonHeight=5
        Button(Frame5, text="GOOD OR BAD?",width=buttonWidth,height=buttonHeight,command= runEvaluate,font=("Arial",15),bg="#ffffff").grid(row=1,column=0, padx=100, pady=20,sticky=W)

        resultClock()
