import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
import threading
from tkinter import filedialog, messagebox, Scrollbar
from tkinter import *
import time
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up
from idlelib.tooltip import Hovertip
import re
#import ScrolledText

# def TextEdit2():
#     def open_file():
#         """Open a file for editing."""
#         filepath = askopenfilename(
#             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#         )
#         if not filepath:
#             return
#         txt_edit.delete("1.0", tk.END)
#         with open(filepath, mode="r", encoding="utf-8") as input_file:
#             text = input_file.read()
#             txt_edit.insert(tk.END, text)
#         window.title(f"Simple Text Editor - {filepath}")
#
#     def save_file():
#         """Save the current file as a new file."""
#         filepath = asksaveasfilename(
#             defaultextension=".txt",
#             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#         )
#         if not filepath:
#             return
#         with open(filepath, mode="w", encoding="utf-8") as output_file:
#             text = txt_edit.get("1.0", tk.END)
#             output_file.write(text)
#         window.title(f"Simple Text Editor - {filepath}")
#
#
#     window = tk.Tk()
#     window.title("Simple Text Editor")
#
#     window.rowconfigure(0, minsize=800, weight=1)
#     window.columnconfigure(1, minsize=800, weight=1)
#
#     txt_edit = tk.Text(window)
#     frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
#     btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
#     btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
#
#     btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#     btn_save.grid(row=1, column=0, sticky="ew", padx=5)
#
#     frm_buttons.grid(row=0, column=0, sticky="ns")
#     txt_edit.grid(row=0, column=1, sticky="nsew")
#
#     window.mainloop()

class GUI:
    def __init__(self):
        of = [None] *5
        for bdw in range(5):
            of[bdw] = Frame(self.root, borderwidth=0)
            Label(of[bdw], text='borderwidth = %d' % bdw).pack(side=LEFT)
            for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
                Button(of[bdw], text=relief,
                 borderwidth=bdw, relief=relief, width=10,
                 command=lambda s=self, r=relief, b=bdw: s.prt(r,b))\
                .pack(side=LEFT, padx=7-bdw, pady=7-bdw)
            of[bdw].pack()
    def prt(self, relief, border):
        print ('%s:%d' % (relief, border))
class TextEdit():
    def __init__(self, Text= '', UserConfirm = False,Mode = 'Story',Current_PROMTS_ALL = ''):
        d = 100
        self.UserResponseProvided = False
        self.UserConfirm = UserConfirm
        self.Text = Text
        #Note if I make update later on I will need to make sure to fix this so the prompts are more dynamic/real time, this is an assumption that is was right when I passed it in
        self.Current_PROMTS_ALL = Current_PROMTS_ALL

    def GetWordCountsSHAINE(self):
        d = 1
        TextEdit.GetUserText(self)


    def WordCount_SHAINE(self):
        TextEdit.GetWordCountsSHAINE
        self.CountCharacters  = len(self.Current_PROMTS_ALL)
        self.CountWords = cu.WordCount(self.Current_PROMTS_ALL)

        self.CountCharacters_w_EDIT = len(self.Current_PROMTS_ALL + self.UserEdits)
        self.CountWords_w_EDIT = cu.WordCount(self.Current_PROMTS_ALL + self.UserEdits)

        self.CountCharacters_RESPONSE= len(self.Text)
        self.CountWords_RESPONSE = cu.WordCount(self.Text)



    def keyPress( self, event ):
        TextEdit.WordCount_SHAINE(self)

        self.WordCountField = tk.Text(self.window, wrap=WORD, )

        if len(self.UserEdits) >0:
            self.WordCountField.insert(tk.END, "WORDS(Current GPT Response): " + str(self.CountWords_RESPONSE) + " TOTAL CHARACTERS: "  +str(self.CountCharacters_RESPONSE)  + " WORDS (with prompts): " + str(self.CountWords) + " CHARACTERS: " + str(self.CountCharacters) + ' WORDS (w.USER EDITs): '+ str(self.CountWords_w_EDIT) + ' TOTAL CHARACTERS: ' +  str(self.CountCharacters_w_EDIT))
        else:
            self.WordCountField.insert(tk.END,"WORDS(Current GPT Response): " + str(self.CountWords_RESPONSE) + " TOTAL CHARACTERS: "  +str(self.CountCharacters_RESPONSE)  + "CURRENT PROMPTS - WORDS: " + str(self.CountWords) + " CHARACTERS: " + str(self.CountCharacters) )

        #self.WordCountField.grid( row=3, sticky="nsew")
        CrazyTip = Hovertip(self.WordCountField,
                            'WORD COUNT/CHARACTER COUNT/OTHER KEY STATS, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

    def keyPress2(self, event):
        TextEdit.GetPrompts(self)

        self.WordCountField = tk.Text(self.window, wrap=WORD, )
        self.WordCountField.insert(tk.END,
                                   "WORD COUNT: " + str(self.CountWords) + " CHARACTER COUNT: " + str(
                                       self.CountCharacters))
        #self.WordCountField.grid( row=3, sticky="nsew")
        CrazyTip = Hovertip(self.WordCountField,
                            'WORD COUNT/CHARACTER COUNT/OTHER KEY STATS, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

        #
        # self.CharCountField = tk.Text(self.window, wrap=WORD, )
        # self.CharCountField.insert(tk.END, "CHARACTER COUNT: " + str(self.CountCharacters))
        # self.CharCountField.grid(column=3, row=0, sticky="nsew")
        # CrazyTip = Hovertip(self.UserInput_fld_Crazy,'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')
        #


        # self.window.label.config( text = f'Words: {self.CountWords}'  + f'      Characters: {self.CountCharacters}' )





    def MakeWindow(self,Text= "",UserConfirm = False, WindowName = "SHAINE", USERINPUTDEFAULT = """ ### USER EDIT/REQUIREMENT PLEASE TAKE ACTION:      ###""", USERLASTEDIT = '', Current_Prompt = '', version = ''):
        self.UIversion = 1
        self.UserConfirm = UserConfirm
        self.Text = Text
        self.current_file = None
        self.window = tk.Tk()

        #self.window = Frame(self.window,borderwidth = 2, relief = tk.SOLID)
        self.USERLASTEDIT = USERLASTEDIT

        width =  self.window .winfo_screenwidth()
        height =  self.window .winfo_screenheight()
        self.window.geometry(f'{width}x{height}')

        self.window.title(WindowName)
        # self.window.state('zoomed')
        self.text_widget = tk.Text(self.window, wrap=CHAR)

        # self.window.rowconfigure("all", minsize=1)
        # self.window.rowconfigure(0, minsize=10, weight=2)
        # self.window.rowconfigure(2, minsize=1, weight=1)
        # self.window.rowconfigure(1, minsize=1200, weight=10)


        self.UserEdits = ''
        self.window.bind( '<KeyRelease>',  self.keyPress )
        self.window.focus()

        Colors = ['Dark Orchid','Orchid','plum','Blue Violet','Light Pink','Deep Pink', 'Dark Magenta','Pink', 'Misty Rose', 'Medium Violet Red', 'Medium Spring Green','Medium Orchid' , 'green yellow','Dark Goldenrod' ]




        # self.window.rowconfigure(1, minsize=1000, weight=10)



        #txt_edit2 = tk.Text(self.window)
        frm_buttons = tk.Frame(self.window, relief=tk.RAISED, bg=Colors[0], pady=2, padx=2, height=44)
        frm_buttons.pack(side='top', fill="x")
        #frm_Text = tk.Frame(self.window, relief=tk.RAISED, bg='yellow'+ ' 4', pady=8, padx=8)
        Middle_Screen = tk.Frame(self.window, relief=tk.RAISED, bg=Colors[7], pady=8, padx=8)
        Middle_Screen.pack(ipadx=1600,padx=3,pady=3)
        frm_User = tk.Frame(Middle_Screen, relief=tk.RAISED, bg=Colors[2], pady=8, padx=8)
        frm_Text = tk.Frame(Middle_Screen, relief=tk.RAISED, bg=Colors[1], pady=8, padx=8)
        WordCounter = tk.Frame(self.window, relief=tk.SUNKEN, bg=Colors[4])

        frm_buttons.rowconfigure("all", weight=1, height=44)
        Middle_Screen.columnconfigure("all",weight=10, width=1000, height=250)
        Middle_Screen.rowconfigure("all", weight=10, height=100)
        WordCounter.rowconfigure(0, weight=1)

        #frm_Text.master.maxsize(1000,400)
        #frm_Text.master.minsize(150, 400)
        #frm_User.master.minsize(150, 400)
        #frm_Text.master.maxsize(1800, 1600)
        #frm_User.master.maxsize(1800, 1600)
        #frm_buttons.master.maxsize = (1300, 10)
        WordCounter.master.maxsize = (1,1)
        WordCounter.pack(fill="x", expand=0)



        btn_open = tk.Button(frm_buttons, text="Open", command=self.open_file)
        btn_save = tk.Button(frm_buttons, text="Save As...", command=self.save_file)
        btn_new = tk.Button(frm_buttons, text="New Window...", command=self.openNewWindow)
        btn_KeepRunning = tk.Button(frm_buttons, text="Keep Running", command=self.KeepRunning_Button)

        # btn_open.grid(row=0, column=0, sticky="ew", padx=5)
        # btn_save.grid(row=0, column=1, sticky="ew", padx=5)
        # btn_new.grid(row=0, column=2, sticky="ew", padx=5)
        # btn_KeepRunning.grid(row=0, column=3, sticky="ew", padx=5)

        if self.UserConfirm == True:
            #self.window.columnconfigure(1, minsize=1400, weight=1)
            #self.window.columnconfigure(0, minsize=500, weight=2)
            #self.window.columnconfigure(1, minsize=700, weight=1)
            # btn_Continue = tk.Button(frm_buttons, text="***Continue***", command=self.Continue_Button,highlightbackground= 'green', highlightcolor = 'white',style="Custom.TLabel")
            # btn_SmallEdit = tk.Button(frm_buttons, text="User Small Edit**", command=self.SmallEdit,highlightbackground= 'gray', highlightcolor = 'yellow',style="Custom.TLabel")
            # btn_ReWriteWithEdit = tk.Button(frm_buttons, text="ReWrite with Edit", command=self.ReWriteWithEdit,highlightbackground= 'yellow', highlightcolor = 'cyan',style="Custom.TLabel")
            # btn_ReWrite = tk.Button(frm_buttons, text="ReWrite",command=self.ReWrite,highlightbackground= 'cyan', highlightcolor = 'red',style="Custom.TLabel")
            # btn_UseUserText = tk.Button(frm_buttons, text="*User Text provided*", command=self.UseUserText,highlightbackground= 'red', highlightcolor = 'black',style="Custom.TLabel")

            btn_Continue = tk.Button(frm_buttons, text="***Continue***", command=self.Continue_Button)
            btn_SmallEdit = tk.Button(frm_buttons, text="Small USER Edit", command=self.SmallEdit)
            btn_ReWriteWithEdit = tk.Button(frm_buttons, text="ReWrite with Edit", command=self.ReWriteWithEdit)
            btn_ReWrite = tk.Button(frm_buttons, text="ReWrite", command=self.ReWrite)
            btn_UseUserText = tk.Button(frm_buttons, text="*User Text provided*", command=self.UseUserText)
            btn_PullLastEdit= tk.Button(frm_buttons, text="Pull Last Edit (REUSE)", command=self.RestoreLastUserText)



            btn_ReviewPrompt = tk.Button(frm_buttons, text="~REVIEW PROMPT USED BY GPT~", command=self.ReviewPrompt)
            btn_ReturnLast = tk.Button(frm_buttons, text="Revert to Prior GPT Response", command=self.ReturnLast)
            btn_ReturnOrig = tk.Button(frm_buttons, text="Revert to Original GPT Response", command=self.ReturnOrig)

            btn_RestoreUserInputs = tk.Button(frm_buttons, text="Activate GPT FULL Review Mode",
                                                      command=self.RestoreUserInput)
            btn_NoMoreUserInputs_RuntoEnd = tk.Button(frm_buttons, text="RUN TO COMPLETION", command=self.EndUserInput)
            btn_NoMoreUserInputs_RuntoEnd2 = tk.Button(frm_buttons, text="QUICK MODE - IGNORE Small Inquiries",command=self.EndUserInputSmall)
            btn_NoMoreUserInputs_RuntoEnd3 = tk.Button(frm_buttons, text="SKIP  (All Scene Outline/Next Part)",command=self.EndUserInputMain)
            btn_MakeArt = tk.Button(frm_buttons, text="Make Art",command=self.MakeArt)
            btn_Speak = tk.Button(frm_buttons, text="Speak Text", command=self.Speak)






            btn_Continue.grid(row=0, column=14, sticky="ew", padx=10, pady=10)
            btn_UseUserText.grid(row=0, column=13, sticky="ew", padx=10, pady=10)
            btn_PullLastEdit.grid(row=0, column=12, sticky="ew", padx=10, pady=10)
            btn_SmallEdit.grid(row=0, column=9, sticky="ew", padx=5, pady=5)
            btn_ReWriteWithEdit.grid(row=0, column=10, sticky="ew", padx=5)
            btn_ReWrite.grid(row=0, column=11, sticky="ew", padx=5)

            btn_ReviewPrompt.grid(row=0, column=8, sticky="ew", padx=5)
            btn_ReturnLast.grid(row=0, column=7, sticky="ew", padx=5)
            btn_ReturnOrig.grid(row=0, column=6, sticky="ew", padx=5)

            btn_RestoreUserInputs.grid(row=0, column=2, sticky="ew", padx=5)
            btn_NoMoreUserInputs_RuntoEnd.grid(row=0, column=5, sticky="ew", padx=5)
            btn_NoMoreUserInputs_RuntoEnd2.grid(row=0, column=4, sticky="ew", padx=5)
            btn_NoMoreUserInputs_RuntoEnd3.grid(row=0, column=3, sticky="ew", padx=5)
            btn_Speak.grid(row=0, column=0, sticky="ew", padx=5)
            btn_MakeArt.grid(row=0, column=1, sticky="ew", padx=5)


            # self.UserInput = tk.StringVar()
            # self.UserInput = tk.Entry(self.window, textvariable = self.UserInput)
            # #self.UserInput.set(USERINPUTDEFAULT)


            # self.UserInput.pack()
            # self.UserInput.grid(row=0, column=2, sticky="nsew")
            #


            self.UserInput = tk.Text(frm_User, wrap=CHAR)
            #self.UserInput.insert(tk.END,USERINPUTDEFAULT )
            #self.UserInput.grid( row=1, sticky="nsew", columnspan=1, column=1, rowspan=2)
            self.UserInput.pack(fill="both",ipady=(333),ipadx=(333))


            # txt_edit.grid(row=0, column=1, sticky="nsew")
            #columnspan=1, column=0, rowspan=2
            self.Printtxt = tk.Text(frm_Text, wrap=CHAR)
            self.Printtxt.insert(tk.END, self.Text)
            #self.Printtxt.grid(row=1, sticky="nsew")
            self.Printtxt.pack(fill="both", ipady=(333), ipadx=(333))
            TextEdit.WordCount_SHAINE(self)


            # Create a scrollbar
            # scroll_bar = tk.Scrollbar(self.window)

            # # Pack the scroll bar
            # # Place it to the right side, using tk.RIGHT
            # scroll_bar.pack(side=tk.RIGHT)
            #
            # # Pack it into our tkinter application
            # # Place the text widget to the left side
            # self.text_widget.pack(side=tk.LEFT)

            TextEdit.WordCount_SHAINE(self)

            self.WordCountField = tk.Text(WordCounter, wrap=CHAR)
            self.WordCountField.insert(tk.END, "WORDS(GPT Response): " + str(self.CountWords_RESPONSE) + " CHARACTERS: "  +str(self.CountCharacters_RESPONSE)  + " WORDS (GPT prompts): " + str(self.CountWords) + " CHARACTERS: " + str(self.CountCharacters) + up.LineBreak + "Current Prompt: "+  up.LineBreak + Current_Prompt )
            #self.WordCountField.grid( row=2, sticky="nsew")

            #self.WordCountField.master.maxsize = (1, 1)

            self.WordCountField.pack(side= "left", expand=0, anchor="nw", fill="x")
            #side= "left", expand=0, anchor="sw"

            CrazyTip = Hovertip(self.WordCountField,
                                'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

            frm_User.pack( side='right', expand=0, fill="both")
            frm_Text.pack(side='left', expand=0, fill="both")
            WordCounter.pack(expand=0, fill="x" )
            # frm_User.pack(side= 'right',fill = "both")
            # frm_Text.pack(side= 'left',fill = "both")
            #frm_buttons.pack(side='top', fill="none")

           #  frm_User.master.state('zoomed')
           #  frm_Text.master.state('zoomed')
            #self.window.state('zoomed')




        #self.text_widget.grid(row=1, column=2, sticky="nsew")




        menu_bar = tk.Menu(self.window)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menu_bar.add_cascade(label="File", menu=file_menu)




        # Edit menu
        # Add more options to the menu as needed
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)



        SHAINE = tk.Menu(menu_bar, tearoff=0)
        SHAINE.add_command(label="Continue", command=self.Continue_Button, accelerator="Ctrl+Q")
        SHAINE.add_command(label="Use User Text", command=self.UseUserText, accelerator="Ctrl+U")
        SHAINE.add_command(label="ReWrite Response", command=self.ReWrite, accelerator="Ctrl+R")
        SHAINE.add_command(label="Review Prompts", command=self.ReviewPrompt, accelerator="Ctrl+P")


        menu_bar.add_cascade(label="SHAINE", menu=SHAINE)


         # Help menu
        # Add more options to the menu as needed

        self.window.config(menu=menu_bar)
        self.text_widget = tk.Text(self.window, wrap=WORD)



        while self.UserResponseProvided ==False:
            self.window.mainloop()
            #time.sleep(1)


        return self.UserEdits
    #
    # def PullLastEdit(self):
    #     self.UserInput.insert(tk.END, self.Text)
    def RestoreLastUserText(self):

        self.UserInput.insert(tk.END, self.USERLASTEDIT)
        return self.UserEdits


    def GetUserText(self):
        self.UserEdits = self.UserInput.get(1.0,END)
        return self.UserEdits

    def GetUserResponseMode(self):
        return self.UserResponseMode

    def GetUserResponseMain(self):
        self.UserConfirm = True
        TextEdit.MakeWindow(self)
        self.x = self.UserInput.get()
        try:
            self.window.destroy()
        except:
            print('Error With Window, continue, maybe look into later')
        return self.x

    def Continue_Button(self, Mode = 0):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "0"
        return "0"

    def EndUserInput(self, Mode = 5):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "5"
        return "5"

    def RestoreUserInput(self, Mode = 50):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "5"
        return "50"


    def EndUserInputSmall(self, Mode = 6):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "6"
        return "6"

    def EndUserInputMain(self, Mode = 7):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "7"
        return "7"



    def MakeArt(self, Mode = 8):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "8"
        return "8"


    def ReviewPrompt(self, Mode = 10):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "8"
        return "10"

    def ReturnLast(self, Mode = 11):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "8"
        return "11"

    def ReturnOrig(self, Mode = 12):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "8"
        return "12"






    def Speak(self, Mode = 6):

        try:
            try:
                Text = self.Text
                t = threading.Thread(target= cu.speak, args=(Text,)).start()
                #threads.append(t)
            except:
                print("Error While trying to read outloud")
        except:
            print("Error While trying to read outloud #2")



        self.UserEdits = "9"
        return "9"




    def SmallEdit(self, Mode = 1):

        self.UserEdits = TextEdit.GetUserText(self)
        TextEdit.UserResponse(self,Mode, self.UIversion)
        return "1"


    def ReWriteWithEdit(self, Mode = 2):

        self.UserEdits = TextEdit.GetUserText(self)
        TextEdit.UserResponse(self,Mode, self.UIversion)
        return "2"

    def ReWrite(self, Mode = 3):
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "3"
        return "3"

    def UseUserText(self, Mode = 4):
        self.UserEdits = TextEdit.GetUserText(self)
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "4"
        return "4"




    def UserResponse(self, Mode,UIversion):
        self.UserResponseMode = Mode

        if UIversion == 2:
            TextEdit.GetPrompts(self)# print(Mode)
        elif UIversion == 1:
            try:
                self.UserEdits = TextEdit.GetUserText(self)
            except:
                print("Error while trying to pull User Values from Prompt")



        if Mode == 0:
            # print("Pass")
            c = 1
        self.UserResponseProvided = True

        try:
            self.window.destroy()
        except:
            print("Error Trying to close window")
        return Mode

    def GetUserResponse(self):
        return self.UserResponseMode




    def Get_System(self):
        return self.UserPromptSystem

    def Get_Role(self):
        return self.UserPromptRole

    def Get_Format(self):
        return self.UserPromptFormat

    def Get_Task(self):
        return self.UserPromptTask

    def Get_Background(self):
        return self.UserPromptBackground

    def Get_Background2(self):
        return self.UserPromptBackground2

    def Get_Background3(self):
        return self.UserPromptBackground3

    def Get_version(self):
        #TextEdit.GetPrompts(self)
        return self.UserPromptversion


    def Get_Crazy(self):
        return self.UserPromptCrazy








    def GetPrompts(self):
        x = 1

        self.UserPromptSystem = ''
        self.UserPromptRole = ''
        self.UserPromptFormat = ''
        self.UserPromptTask = ''
        self.UserPromptBackground = ''
        self.UserPromptBackground2 = ''
        self.UserPromptBackground3 = ''
        self.UserPromptCrazy = ''
        self.UserPromptversion = ''
        self.UserPromptSystem1 = ''
        self.UserPromptRole1 = ''
        self.UserPromptFormat1 = ''
        self.UserPromptTask1 = ''
        self.UserPromptBackground1 = ''
        self.UserPromptBackground21 = ''
        self.UserPromptBackground31 = ''
        self.UserPromptCrazy1 = ''
        self.UserPromptversion1 = ''


        try:
            self.UserPromptSystem = self.UserInput_fld_SYSTEM.get(1.0,END)
            self.UserPromptSystem1 = "System: " + self.UserPromptSystem
        except:
            print('Error Getting User prompt System')

        try:
            self.UserPromptRole = self.UserInput_fld_ROLE.get(1.0,END)
            self.UserPromptRole1 = "Role: " + self.UserPromptRole
        except:
            print('Error Getting User prompt Role')

        try:
            self.UserPromptFormat = self.UserInput_fld_FORMAT.get(1.0,END)
            self.UserPromptFormat1 = "Format: " + self.UserPromptFormat
        except:
            print('Error Getting User prompt Format')

        try:
            self.UserPromptTask = self.UserInput_fld_TASK.get(1.0,END)
            self.UserPromptTask1 = "Task: " + self.UserPromptTask
        except:
            print('Error Getting User prompt Task')

        try:
            self.UserPromptBackground = self.UserInput_fld_Background.get(1.0,END)
            self.UserPromptBackground1 = "Background : " + self.UserPromptBackground
        except:
            print('Error Getting User prompt Background')

        try:
            self.UserPromptBackground2 = self.UserInput_fld_Background2.get(1.0,END)
            self.UserPromptBackground21 = "Background 2: " + self.UserPromptBackground2
        except:
            print('Error Getting User prompt Background2')

        try:
            self.UserPromptBackground3 = self.UserInput_fld_Background3.get(1.0,END)
            self.UserPromptBackground31 = "Background 3: " + self.UserPromptBackground3
        except:
            print('Error Getting User prompt Background3')

        try:
            self.UserPromptCrazy = self.UserInput_fld_Crazy.get(1.0,END)
            self.UserPromptCrazy1 = "Crazy: " +self.UserPromptCrazy

        except:
            print('Error Getting User prompt Crazy')

        try:
            self.UserPromptversion = self.UserInput_fld_version.get(1.0,END)
            self.UserPromptversion1 = "Version: " +self.UserPromptversion

        except:
            print('Error Getting User prompt Crazy')









        self.Full_User_Prompt2 = self.UserPromptSystem +self.UserPromptRole +self.UserPromptFormat +self.UserPromptTask + self.UserPromptBackground +self.UserPromptBackground2 +self.UserPromptBackground3




        self.Full_User_Prompt = self.UserPromptSystem1 +self.UserPromptRole1 +self.UserPromptFormat1 +self.UserPromptTask1 + self.UserPromptBackground1 +self.UserPromptBackground21 +self.UserPromptBackground31


        self.CountCharacters = len(self.Full_User_Prompt2)
        self.CountWords = cu.WordCount(self.Full_User_Prompt2)




    def  UpdatePrompts1(self, Mode = 44):
        d = 1
        #TextEdit.GetPrompts(self)
        TextEdit.UserResponse(self,Mode, self.UIversion)
        #self.UserEdits = "8"
        return "44"

    def RestorePrompt_original(self, Mode=14):

        TextEdit.UserResponse(self, Mode, self.UIversion)

        return "14"


    def RestorePrompt (self, Mode = 13):


        TextEdit.UserResponse(self,Mode, self.UIversion)



        return "13"



    def OPTIMIZEPROMPT (self, Mode = 2002):


        TextEdit.UserResponse(self,Mode, self.UIversion)



        return "2002"

    def ChangeVersion(self, Mode = 2000):

        TextEdit.UserResponse(self,Mode, self.UIversion)
        self.version

        return 2000

    def Speak2(self, Mode =9 ):
        try:
            try:
                try:
                    TextEdit.GetPrompts(self)
                    Text = self.Full_User_Prompt
                    t = threading.Thread(target= cu.speak, args=(Text,)).start()
                    #threads.append(t)
                except:
                    print("Error While trying to read outloud")
            except:
                print("Error While trying to read outloud #2")
        except:
            print("Error While trying to read outloud #3")



        self.UserEdits = "9"
        return "9"


    def UpdateUI(self):

        d = 1




    def new_file(self):


        self.text_widget.delete("1.0", tk.END)
        self.current_file = None

    def openNewWindow(self):

        # Toplevel object which will
        # be treated as a new window

        self.txt_edit3 = tk.Text(self.window)
        self.txt_edit3.grid(row=0, column=2, sticky="nsew")

        newWindow = tk.Toplevel( self.window)

        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        tk.Label(newWindow,
              text="This is a new window").pack()

    def KeepRunning_Button(self):
        self.window.quit
    def open_file(self):


        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, file.read())
        self.current_file = file_path

    def save_file(self):


        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))
        else:
            self.save_file_as

    def save_file_as(self):


        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))
        self.current_file = file_path

    def exit_editor(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            try:
                self.window.destroy()
            except:
                print("Error Trying to close window")

    def cut_text(self):
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text_widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.window.clipboard_clear()
        self.window.clipboard_append(selected_text)

    def copy_text(self):
        selected_text = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.window.clipboard_clear()
        self.window.clipboard_append(selected_text)

    def paste_text(self):
        text_to_paste = self.window.clipboard_get()
        self.text_widget.insert(tk.INSERT, text_to_paste)







#Do the Same thing for the Characters, the summaries, the Scene by Scene Outline, The Scene Outline,
#Have a loader program where you can point certain files to the query and it allows you to not have to copy and paste the story in, we can have it let us select the files we need for various parts of the story.
    def MakeWindow3(self,Task,System, crazy,Text= "",UserConfirm = False, WindowName = "SHAINE", Text_Title = '', version = '', Model = ''):
        self.UserConfirm = UserConfirm
        self.UIversion = 2
        self.System = System

        self.Task = Task
        self.crazy = crazy
        self.Text = System
        self.version = version

        self.current_file = None
        self.window = tk.Tk()

        self.window.title(WindowName)
        self.window.state('zoomed')
        self.window.bind( '<KeyRelease>',  self.keyPress2 )
        self.window.focus()


        self.window.rowconfigure(0, minsize=35, weight=1)
        self.window.rowconfigure(1, minsize=400, weight=1)
        self.window.rowconfigure(2, minsize=10, weight=1)
        self.window.rowconfigure(3, minsize=10, weight=1)

        self.window.columnconfigure(1, minsize=400, weight=1)



        frm_buttons = tk.Frame(self.window)
        #relief = tk.RAISED

        self.window.columnconfigure(2,  weight=1)
        self.window.columnconfigure(3,  weight=1)
        #self.window.columnconfigure(4, minsize=444, weight=1)
        # btn_Continue = tk.Button(frm_buttons, text="***Continue (No Changes)***", command=self.Continue_Button, highlightbackground='white', style="Custom.TLabel")
        # btn_UpdatePrompts1 = tk.Button(frm_buttons, text="**Update GPT Prompts with User Input**", command=self.UpdatePrompts1, highlightbackground='yellow', highlightcolor = 'red',style="Custom.TLabel")
        # btn_RestorePrompt = tk.Button(frm_buttons, text="Restore Prior Prompts",command=self.RestorePrompt, style="Custom.TLabel", highlightbackground= 'black',highlightcolor = 'cyan')
        # btn_RestorePrompt_original = tk.Button(frm_buttons, text="Restore Prior Prompts", command=self.RestorePrompt_original, highlightbackground= 'black', highlightcolor = 'red',style="Custom.TLabel")
        # btn_Speak2 = tk.Button(frm_buttons, text="Speak Prompt", command=self.Speak2, highlightbackground= 'red', highlightcolor = 'black',style="Custom.TLabel")
        #
        #


        btn_Continue = tk.Button(frm_buttons, text="***Continue (No Changes)***", command=self.Continue_Button)
        btn_UpdatePrompts1 = tk.Button(frm_buttons, text="**Update GPT Prompts with User Input**", command=self.UpdatePrompts1)
        btn_RestorePrompt = tk.Button(frm_buttons, text="Restore Prior Prompts",command=self.RestorePrompt)
        btn_RestorePrompt_original = tk.Button(frm_buttons, text="Restore Original Prompts", command=self.RestorePrompt_original)
        btn_Speak2 = tk.Button(frm_buttons, text="Speak Prompt", command=self.Speak2)
        btn_OPTIMIZEPrompt_original = tk.Button(frm_buttons, text="OPTIMIZE Prompt", command=self.OPTIMIZEPROMPT)
        btn_ChangeVersion = tk.Button(frm_buttons, text="CHange SHAINE Version", command=self.ChangeVersion)

        btn_Continue.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_UpdatePrompts1.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        btn_Speak2.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
        btn_RestorePrompt.grid(row=0, column=3, sticky="ew", padx=5)
        btn_RestorePrompt_original.grid(row=0, column=4, sticky="ew", padx=5)
        btn_OPTIMIZEPrompt_original.grid(row=0, column=5, sticky="ew", padx=5)
        btn_ChangeVersion.grid(row=0, column=6, sticky="ew", padx=5)

        RoleTip = Hovertip(btn_Continue, 'Continue - Back to the Review UI (SHAINE)')
        UpdatePrompts1Tip = Hovertip(btn_UpdatePrompts1, 'USER Manually inputs the Chat GPT Prompts')
        SpeakTip = Hovertip(btn_Speak2, 'Click Here to Here Text to Speech/AudioBook Preview')
        RestorePromptTip = Hovertip(btn_RestorePrompt, 'Click Here to Restore the Prompts to their original State')
        RestorePrompt_originalTip = Hovertip(btn_RestorePrompt_original, 'Click Here to Restore the Prompts to their original State')

        # self.UserInput_fld_SYSTEM = tk.Entry(self.window)
        # self.UserInput_fld_SYSTEM.pack(side='left')
        # self.UserInput_fld_SYSTEM.grid(row=0, column=0, sticky="nsew")
        #


        print(self.Text)
        self.UserInput_fld_SYSTEM = tk.Text(self.window, wrap=WORD)
        self.UserInput_fld_SYSTEM.insert(tk.END, self.System)

        self.UserInput_fld_SYSTEM.grid(column=0, row=1, sticky="nsew")
        SystemTip = Hovertip(self.UserInput_fld_SYSTEM, 'System Prompt')





        self.UserInput_fld_TASK = tk.Text(self.window, wrap=WORD,)
        self.UserInput_fld_TASK.insert(tk.END, self.Task)
        self.UserInput_fld_TASK.grid(column=1, row=1, sticky="nsew")
        TaskTip = Hovertip(self.UserInput_fld_TASK, 'Task Prompt')


        self.UserInput_fld_version = tk.Text(self.window, wrap=WORD,)
        self.UserInput_fld_version.insert(tk.END, self.version)
        self.UserInput_fld_version.grid(column=0,columnspan=1, row=2, sticky="nsew")
        verzTip = Hovertip(self.UserInput_fld_version, 'Version Option, The original is Version 1 where it has smaller System message and a few User inputs, Version 2 is new and it puts background info and details into System and just has 1 prompt for USER which is the task')



        self.UserInput_fld_Crazy = tk.Text(self.window, wrap=WORD,)
        self.UserInput_fld_Crazy.insert(tk.END, self.crazy)
        self.UserInput_fld_Crazy.grid(column=1,columnspan=1, row=2, sticky="nsew")
        CrazyTip = Hovertip(self.UserInput_fld_Crazy, 'Crazy/Temperature Prompt - Lower number means responses are less creative and more rigid, Too High of a number and it starts to make less sense')




        TextEdit.GetPrompts(self)


        self.WordCountField = tk.Text(self.window, wrap=WORD, )
        self.WordCountField.insert(tk.END, "WORD COUNT: " + str(self.CountWords))
        self.WordCountField.grid( row=3, sticky="nsew")
        CrazyTip = Hovertip(self.WordCountField,
                            'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

        frm_buttons.grid(row=0, column=0, sticky="ns")

        self.window.state('zoomed')

        menu_bar = tk.Menu(self.window)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        # Add more options to the menu as needed
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        # Help menu
        # Add more options to the menu as needed

        self.window.config(menu=menu_bar)
        self.text_widget = tk.Text(self.window)

        while self.UserResponseProvided == False:
            # TextEdit.GetPrompts(self)
            self.window.mainloop()
            # time.sleep(1)

    def MakeWindow2(self, System, Role, Format, Task, Background, Background2, Background3, crazy, Text="",
                    UserConfirm=False, WindowName="SHAINE", Text_Title='',version = 2 , Model = ''):
        self.UserConfirm = UserConfirm
        self.UIversion = 2
        self.Role = Role
        self.System = System
        self.Format = Format
        self.Task = Task
        self.Background = Background
        self.Background2 = Background2
        self.Background3 = Background3
        self.crazy = crazy
        self.Text = Text
        self.current_file = None
        self.window = tk.Tk()

        self.window.title(WindowName)
        self.window.state('zoomed')
        self.window.bind('<KeyRelease>', self.keyPress2)
        self.window.focus()

        self.window.rowconfigure(0, minsize=35, weight=1)
        self.window.rowconfigure(1, minsize=400, weight=1)
        self.window.rowconfigure(2, minsize=400, weight=1)
        self.window.rowconfigure(3, minsize=10, weight=5)
        self.window.columnconfigure(1, minsize=400, weight=1)


        frm_buttons = tk.Frame(self.window)
        # relief = tk.RAISED

        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        # self.window.columnconfigure(4, minsize=444, weight=1)
        # btn_Continue = tk.Button(frm_buttons, text="***Continue (No Changes)***", command=self.Continue_Button, highlightbackground='white', style="Custom.TLabel")
        # btn_UpdatePrompts1 = tk.Button(frm_buttons, text="**Update GPT Prompts with User Input**", command=self.UpdatePrompts1, highlightbackground='yellow', highlightcolor = 'red',style="Custom.TLabel")
        # btn_RestorePrompt = tk.Button(frm_buttons, text="Restore Prior Prompts",command=self.RestorePrompt, style="Custom.TLabel", highlightbackground= 'black',highlightcolor = 'cyan')
        # btn_RestorePrompt_original = tk.Button(frm_buttons, text="Restore Prior Prompts", command=self.RestorePrompt_original, highlightbackground= 'black', highlightcolor = 'red',style="Custom.TLabel")
        # btn_Speak2 = tk.Button(frm_buttons, text="Speak Prompt", command=self.Speak2, highlightbackground= 'red', highlightcolor = 'black',style="Custom.TLabel")
        #
        #

        btn_Continue = tk.Button(frm_buttons, text="***Continue (No Changes)***", command=self.Continue_Button)
        btn_UpdatePrompts1 = tk.Button(frm_buttons, text="**Update GPT Prompts with User Input**",
                                       command=self.UpdatePrompts1)
        btn_RestorePrompt = tk.Button(frm_buttons, text="Restore Prior Prompts", command=self.RestorePrompt)
        btn_RestorePrompt_original = tk.Button(frm_buttons, text="Restore Original Prompts",
                                               command=self.RestorePrompt_original)
        btn_Speak2 = tk.Button(frm_buttons, text="Speak Prompt", command=self.Speak2)

        btn_OPTIMIZEPrompt_original = tk.Button(frm_buttons, text="OPTIMIZE Prompt", command=self.OPTIMIZEPROMPT)
        btn_ChangeVersion = tk.Button(frm_buttons, text="CHange SHAINE Version", command=self.ChangeVersion)
        btn_OPTIMIZEPrompt_original.grid(row=0, column=5, sticky="ew", padx=5)
        btn_ChangeVersion.grid(row=0, column=6, sticky="ew", padx=5)


        btn_Continue.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_UpdatePrompts1.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        btn_Speak2.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
        btn_RestorePrompt.grid(row=0, column=3, sticky="ew", padx=5)
        btn_RestorePrompt_original.grid(row=0, column=4, sticky="ew", padx=5)

        RoleTip = Hovertip(btn_Continue, 'Continue - Back to the Review UI (SHAINE)')
        UpdatePrompts1Tip = Hovertip(btn_UpdatePrompts1, 'USER Manually inputs the Chat GPT Prompts')
        SpeakTip = Hovertip(btn_Speak2, 'Click Here to Here Text to Speech/AudioBook Preview')
        RestorePromptTip = Hovertip(btn_RestorePrompt, 'Click Here to Restore the Prompts to their original State')
        RestorePrompt_originalTip = Hovertip(btn_RestorePrompt_original,
                                             'Click Here to Restore the Prompts to their original State')

        # self.UserInput_fld_SYSTEM = tk.Entry(self.window)
        # self.UserInput_fld_SYSTEM.pack(side='left')
        # self.UserInput_fld_SYSTEM.grid(row=0, column=0, sticky="nsew")
        #

        print(self.Text)
        self.UserInput_fld_SYSTEM = tk.Text(self.window, wrap=WORD)
        self.UserInput_fld_SYSTEM.insert(tk.END, self.System)

        self.UserInput_fld_SYSTEM.grid(column=0, row=1, sticky="nsew")
        SystemTip = Hovertip(self.UserInput_fld_SYSTEM, 'System Prompt')

        x = self.UserInput_fld_SYSTEM.get(1.0, END)
        print('Get Value:')
        print(x)

        self.UserInput_fld_ROLE = tk.Text(self.window, wrap=WORD, )
        self.UserInput_fld_ROLE.insert(tk.END, self.Role)
        self.UserInput_fld_ROLE.grid(column=0, row=2, sticky="nsew")
        RoleTip = Hovertip(self.UserInput_fld_ROLE, 'Role Prompt')

        self.UserInput_fld_FORMAT = tk.Text(self.window, wrap=WORD, )
        self.UserInput_fld_FORMAT.insert(tk.END, self.Format)
        self.UserInput_fld_FORMAT.grid(column=1, row=1, sticky="nsew")

        FormatTip = Hovertip(self.UserInput_fld_FORMAT, 'Format Prompt')

        self.UserInput_fld_TASK = tk.Text(self.window, wrap=WORD, )
        self.UserInput_fld_TASK.insert(tk.END, self.Task)
        self.UserInput_fld_TASK.grid(column=3, row=2, sticky="nsew")
        TaskTip = Hovertip(self.UserInput_fld_TASK, 'Task Prompt')

        self.UserInput_fld_Background = tk.Text(self.window, wrap=WORD, )
        self.UserInput_fld_Background.insert(tk.END, self.Background)
        self.UserInput_fld_Background.grid(column=2, row=1, sticky="nsew")
        BTip = Hovertip(self.UserInput_fld_Background, 'Background Prompt')

        self.UserInput_fld_Background2 = tk.Text(self.window, wrap=WORD, )
        self.UserInput_fld_Background2.insert(tk.END, self.Background2)
        self.UserInput_fld_Background2.grid(column=1, row=2, sticky="nsew")
        B2Tip = Hovertip(self.UserInput_fld_Background2,
                         'Background Prompt 2 - Not ideal to have too long of prompts, but sometimes doing it this way makes it much simpler. ')

        self.UserInput_fld_Background3 = tk.Text(self.window, wrap=WORD, )
        self.UserInput_fld_Background3.insert(tk.END, self.Background3)
        self.UserInput_fld_Background3.grid(column=2, row=2, sticky="nsew")
        B3Tip = Hovertip(self.UserInput_fld_Background3,
                         'Background Prompt 3 - Not ideal to have too long of prompts, but sometimes doing it this way makes it much simpler. ')

        self.UserInput_fld_Crazy = tk.Text(self.window, wrap=WORD, )
        self.UserInput_fld_Crazy.insert(tk.END, self.crazy)
        self.UserInput_fld_Crazy.grid(column=3, row=3, sticky="nsew")
        CrazyTip = Hovertip(self.UserInput_fld_Crazy,
                            'Crazy/Temperature Prompt - Lower number means responses are less creative and more rigid, Too High of a number and it starts to make less sense')

        TextEdit.GetPrompts(self)

        self.WordCountField = tk.Text(self.window, wrap=WORD, )
        self.WordCountField.insert(tk.END, "WORD COUNT: " + str(self.CountWords))
        self.WordCountField.grid( row=3, sticky="nsew")
        CrazyTip = Hovertip(self.WordCountField,
                            'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

    #
    #
    # self.CharCountField = tk.Text(self.window, wrap=WORD, )
    # self.CharCountField.insert(tk.END, "CHARACTER COUNT: " + str(self.CountCharacters))
    # self.CharCountField.grid(column=3, row=0, sticky="nsew")
    # CrazyTip = Hovertip(self.UserInput_fld_Crazy,'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')
    #
    #



    #



    #

    # # Create a scrollbar
    #scroll_bar = tk.Scrollbar(self.UserInput_fld_SYSTEM)
    # scroll_bar = tk.Scrollbar(self.UserInput_fld_FORMAT)
    # scroll_bar = tk.Scrollbar(self.UserInput_fld_Crazy)
    # scroll_bar = tk.Scrollbar(self.UserInput_fld_Background)
    # scroll_bar = tk.Scrollbar(self.UserInput_fld_Background2)
    # scroll_bar = tk.Scrollbar(self.UserInput_fld_Background3)
    # scroll_bar = tk.Scrollbar(self.UserInput_fld_Crazy)







        frm_buttons.grid(row=0, column=0, sticky="ns")

        self.window.state('zoomed')



        menu_bar = tk.Menu(self.window)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menu_bar.add_cascade(label="File", menu=file_menu)




        # Edit menu
        # Add more options to the menu as needed
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
         # Help menu
        # Add more options to the menu as needed

        self.window.config(menu=menu_bar)
        self.text_widget = tk.Text(self.window)



        while self.UserResponseProvided ==False:
            #TextEdit.GetPrompts(self)
            self.window.mainloop()
            #time.sleep(1)




    #        self.window.pack()

    # self.UserInput_fld_ROLE = tk.Entry(self.window)
    # self.UserInput_fld_ROLE.pack()
    # self.UserInput_fld_ROLE.grid(row=1, column=2, sticky="nsew")
    #
    # self.UserInput_fld_FORMAT = tk.Entry(self.window)
    # self.UserInput_fld_FORMAT.pack()
    # self.UserInput_fld_FORMAT.grid(row=1, column=1, sticky="nsew")
    #
    # self.UserInput_fld_TASK = tk.Entry(self.window)
    # self.UserInput_fld_TASK.pack(side='right')
    # self.UserInput_fld_TASK.grid(row=2, column=0, sticky="nsew")
    #
    # self.UserInput_fld_Background = tk.Entry(self.window)
    # self.UserInput_fld_Background.pack()
    # self.UserInput_fld_Background.grid(row=2, column=3, sticky="nsew")
    #
    # self.UserInput_fld_Background2 = tk.Entry(self.window)
    # self.UserInput_fld_Background2.pack()
    # self.UserInput_fld_Background2.grid(row=3, column=2, sticky="nsew")
    #
    # self.UserInput_fld_Background3 = tk.Entry(self.window)
    # self.UserInput_fld_Background3.pack()
    # self.UserInput_fld_Background3.grid(row=3, column=1, sticky="nsew")
    #
    # self.UserInput_fld_Crazy = tk.Entry(self.window)
    #
    # self.UserInput_fld_Crazy.grid(row=3, column=1, sticky="nsew")
