from Predict_Squat.Predict_IF import *
from Make_Model.TRAIN_GUI import *
import tkinter as tk
from Prepare_Dataset.PrepareData_IF import PrepareDataset_Application

'''Programs Main Menu'''
class StartGui(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.frame = tk.Frame(self.master)
        self.grid()
        self.master.title("Motion or not?")

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

        img = PhotoImage(file=("img/motion_or_not.png"))
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

        Frame1.grid(row = 3, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)
        Grid.columnconfigure(Frame1,0,weight=1)
    #    Grid.columnconfigure(root, 3, weight=1)

    ###---Creating Buttons to BUTTON FRAME---###
        buttonWidth=36

        Button(Frame1, text="EVALUATE", height=2, width=buttonWidth, command=self.open_SquatGui, font=("Cambria", 13), bg="#ffffff").grid(row=1, column=0, padx=70, pady=10, sticky=W + E + S + N)
        Button(Frame1, text="MAKE MODEL", height=2, width=buttonWidth, command=self.open_TrainModel, font=("Cambria", 13),bg="#ffffff").grid(row=2, column=0, padx=70, pady=10, sticky=W + E + S + N)
        Button(Frame1, text="PREPARE DATASET", height=2, width=buttonWidth, command=self.open_PrepareDataset, font=("Cambria", 13),bg="#ffffff").grid(row=3, column=0, padx=70, pady=10, sticky=W + E + S + N)
        Button(FrameMain, text="QUIT""", height=2, width=15, command=self.quit, font=("Cambria", 13),bg="grey").grid(row=10, column=2, padx=70, pady=10, sticky=W)

        '''-------------    Functions for opening new windows     -------------'''
    def open_SquatGui(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Squat_Application(self.newWindow)
        self.lift()
    def open_TrainModel(self):
        self.newWindow = tk.Toplevel(self.master)

        self.app = TrainModel_Application(self.newWindow)

    def open_PrepareDataset(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = PrepareDataset_Application(self.newWindow)

root = Tk()
app = StartGui(master=root)
#root.wm_attributes('-topmost', 1)
app.mainloop()
