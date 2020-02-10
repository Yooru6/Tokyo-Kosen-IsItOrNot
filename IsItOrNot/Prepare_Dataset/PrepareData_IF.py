from Prepare_Dataset.PrepareData_Functions import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter import *
import threading
#from Project.Programs.SquatOrNot.DO_SQUAT.Functions import *
#THREAD_LOCK = threading.Lock()
import datetime
from timeit import default_timer as timer

path_goodData= ""
path_badData=""

'''Programs Main Menu'''
class PrepareDataset_Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.frame = tk.Frame(self.master)
        self.grid()
        self.master.title("DATA PREPARER")

        '''-------------     MENU      -------------'''
        def nothing():
            print("Nothing Nothing Nothing....")

        def hello():
            print
            "hello!"

        menubar = Menu(self)

        ### Creating a pulldown menu, and adding it on the menu bar###
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=hello)
        filemenu.add_command(label="Save", command=hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        bgColor="#292929"
        self.master.config(menu=menubar,bg=bgColor)

        ###---TITLE CONFIG---###
        img = PhotoImage(file=("img/preparedata_title_52.png"))
        labelPhoto= Label(self.master,image=img)
        labelPhoto.config(bg=bgColor)
        labelPhoto.image = img
        labelPhoto.grid(row=0,column=0, padx=15, pady=10, sticky=W+E+N+S)

        '''-------------    MAIN FRAME      -------------'''
        FrameMain = Frame(master)
        FrameMain.config(bg=bgColor)
        FrameMain.grid(row = 1, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)
        Grid.columnconfigure(FrameMain,1,weight=1)

        '''-------------    BUTTON FRAME      -------------'''
        Frame1 = Frame(FrameMain)
        Frame1.config(bg=bgColor)

        Frame1.grid(row = 0, column = 1, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
        Grid.columnconfigure(Frame1,0,weight=1)
    #    Grid.columnconfigure(root, 3, weight=1)

    ###---Label function for selected data---###
        def openFolderPathGood():
            global path_goodData
            self.master.wm_attributes('-topmost', 0)

            file=filedialog.askdirectory(parent=master, initialdir='Data/', title='Select folder containing good data')
            filename="Chosen folder: "+str(os.path.basename(file))
            path_goodData=str(file)

            print('Chosen Folder for Good Data: '+str(file))
            print("Update")

            label_file=Label(Frame1,text=filename)
            label_file.config(bg=bgColor,foreground='yellow')
            label_file.grid(row=0,column=1,padx=70,pady=2,sticky=W+E+S)
            self.master.wm_attributes('-topmost', 1)

        def openFolderPathBad():
            global path_badData
            self.master.wm_attributes('-topmost', 0)

            file=filedialog.askdirectory(parent=master, initialdir='Data/', title='Select folder containing bad data')
            filename="Chosen folder: "+str(os.path.basename(file))
            path_badData=str(file)

            print('Chosen Folder for bad Data: '+str(file))
            print("Update")

            label_file=Label(Frame1,text=filename)
            label_file.config(bg=bgColor,foreground='yellow')
            label_file.grid(row=0,column=2,padx=70,pady=2,sticky=W+E+S)
            self.master.wm_attributes('-topmost', 1)

        v = IntVar()
        def prepareData_training():
            checkbox=v.get()
            if checkbox ==1:
                print(1)
            elif checkbox ==2:
                print(2)
            try:
                threading.Thread(target=runDataPreparer_training, args=(path_goodData, path_badData, str(entry_dataSetName.get()))).start()

            except Exception as e:
                messagebox.showinfo("ERROR while preparing data!", "Have you filled in all the required information?")
                print(e)

    ###---Creating Buttons to BUTTON FRAME---###
        buttonWidth=36
        v.set(1)

        Radiobutton(Frame1, text="Training Data", variable=v, value=1,font=("Cambria",13),bg="#ffffff").grid(row=0, column=1, padx=10, pady=30, sticky=W + E + S + N)
        Radiobutton(Frame1, text="Test Data", variable=v, value=2,foreground="black", font=("Cambria",13),bg="#ffffff").grid(row=0, column=2, padx=10, pady=30, sticky=W + E + S + N)

        print(v.get)

        Button(Frame1, text="GOOD DATA", height=2, width=buttonWidth, command=openFolderPathGood, font=("Cambria", 13), bg="#ffffff").grid(row=1, column=1, padx=70, pady=30, sticky=W + E + S + N)
        Button(Frame1, text="BAD DATA", height=2, width=buttonWidth, command=openFolderPathBad, font=("Cambria", 13),bg="#ffffff").grid(row=1, column=2, padx=70, pady=30, sticky=W + E + S + N)

        label_dataSetName = Label(FrameMain, text='Dataset Name:')
        label_dataSetName.grid(row=8,column=1, padx=200, pady=2, sticky=W+N+S)

        entry_dataSetName = Entry(FrameMain)
        entry_dataSetName.grid(row=9, column=1, padx=200, pady=10, sticky=W+E+N+S)

        Button(FrameMain, text="PREPARE DATA", height=2, width=50, command=prepareData_training, font=("Cambria", 13),bg="#ffffff").grid(row=10, column=1, padx=200    , pady=15, sticky=W + E + S + N)

        '''-------------    FONTS & COLORS     -------------'''
        ###Backgrounds###
        bgColor = "#292929"
        label_fontColor="#e575ff"
        label_accuracyColor="#ff3a3a"
        labelFontSize=14
        labelFont="Cambria"
        entryFont="Cambria"
        entryFontSize=20

        entry_dataSetName.config(font=(entryFont, entryFontSize))
        label_dataSetName.config(font=(labelFont, labelFontSize), foreground=label_fontColor, bg=bgColor)
        self.master.wm_attributes('-topmost', 1)