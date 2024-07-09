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
import os
import re
import random

from multiprocessing import Process


LOGO =r"A:\Amini Amor\SHAINE\Marketing\Logo Work\18.png"

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

# class GUI:
#     def __init__(self):
#         of = [None] *5
#         for bdw in range(5):
#             of[bdw] = Frame(self.root, borderwidth=0)
#             Label(of[bdw], text='borderwidth = %d' % bdw).pack(side=LEFT)
#             for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
#                 Button(of[bdw], text=relief,
#                  borderwidth=bdw, relief=relief, width=10,
#                  command=lambda s=self, r=relief, b=bdw: s.prt(r,b))\
#                 .pack(side=LEFT, padx=7-bdw, pady=7-bdw)
#             of[bdw].pack()
#     def prt(self, relief, border):
#         print ('%s:%d' % (relief, border))
class TextEdit():
    def __init__(self, Text= '', UserConfirm = False,Mode = 'Story',Current_PROMTS_ALL = ''):
        d = 100
        self.UserResponseProvided = False
        self.UserResponseProvided2 = False

        self.UserConfirm = UserConfirm
        self.WindowClose = False
        self.Text = Text

        #Note if I make update later on I will need to make sure to fix this so the prompts are more dynamic/real time, this is an assumption that is was right when I passed it in
        self.Current_PROMTS_ALL = Current_PROMTS_ALL

        self.Colors = ['Dark Orchid', 'Orchid', 'plum', 'Blue Violet', 'Light Pink', 'Deep Pink', 'cherry-blossom-pink','Dark Magenta', 'Pink',
                  'Misty Rose', 'Medium Violet Red', 'Medium Spring Green', 'Medium Orchid', 'green yellow',
                  'Dark Goldenrod','alizarin','amaranth','amber','amethyst','apricot','aqua','aquamarine','asparagus','auburn','azure','beige','bistre',
                       'black','blue','blue-green','blue-violet','bondi-blue','brass','bronze','brown','buff','burgundy','camouflage-green','caput-mortuum',
                       'cardinal','carmine','carrot-orange','celadon','cerise','cerulean','champagne','charcoal','chartreuse','cherry-blossom-pink','chestnut',
                       'chocolate','cinnabar','cinnamon','cobalt','copper','coral','corn','cornflower','cream','crimson','cyan','dandelion','denim','ecru','emerald',
                       'eggplant','falu-red','fern-green','firebrick','flax','forest-green','french-rose','fuchsia','gamboge','gold','goldenrod','green','grey','han-purple','harlequin','heliotrope','hollywood-cerise','indigo','ivory','jade','kelly-green','khaki','lavender','lawn-green','lemon','lemon-chiffon','lilac','lime','lime-green','linen','magenta','magnolia','malachite','maroon','mauve','midnight-blue','mint-green','misty-rose','moss-green','mustard','myrtle','navajo-white','navy-blue','ochre','office-green','olive','olivine','orange','orchid','papaya-whip','peach','pear','periwinkle','persimmon','pine-green','pink','platinum','plum','powder-blue','puce','prussian-blue','psychedelic-purple','pumpkin','purple','quartz-grey','raw-umber','razzmatazz','red','robin-egg-blue','rose','royal-blue','royal-purple','ruby','russet','rust','safety-orange','saffron','salmon','sandy-brown','sangria','sapphire','scarlet','school-bus-yellow','sea-green','seashell','sepia','shamrock-green','shocking-pink','silver','sky-blue','slate-grey','smalt','spring-bud','spring-green','steel-blue','tan','tangerine','taupe','teal','tenné-(tawny)','terra-cotta','thistle','titanium-white','tomato','turquoise','tyrian-purple','ultramarine','van-dyke-brown','vermilion','violet','viridian','wheat','white','wisteria','yellow','zucchini']
        self.Colors_Greens_Blues = ['green yellow','aquamarine','aqua' ,'bondi-blue','emerald','denim','zucchini' ]
        self.UserEdits = ''

    # Load the image for the icon

        # Set the icon for the window


    def GetWordCountsSHAINE(self):
        d = 1
        TextEdit.GetUserText(self)


    def WordCount_SHAINE(self):
        try:
            TextEdit.GetWordCountsSHAINE
            self.CountCharacters  = len(self.Current_PROMTS_ALL)
            self.CountWords = cu.WordCount(self.Current_PROMTS_ALL)

            self.CountCharacters_w_EDIT = len(self.Current_PROMTS_ALL + self.UserEdits)
            self.CountWords_w_EDIT = cu.WordCount(self.Current_PROMTS_ALL + self.UserEdits)

            self.CountCharacters_RESPONSE= len(self.Text)
            self.CountWords_RESPONSE = cu.WordCount(self.Text)

        except:
            dn = 100

    def keyPress( self, event ):
        try:
            TextEdit.WordCount_SHAINE(self)

            # self.WordCountField = tk.Text(self.WordCounter, wrap=WORD, )

            if len(self.UserEdits) >0:
                TextEdit.UpdateWordCountField( str(self.CountWords_RESPONSE) + " Words in GPT Response " + str(
                    self.CountCharacters_RESPONSE) + " Characters in GPT Response " + up.LineBreak + str(
                    self.CountWords) + "Words in Prompt " + str(self.CountCharacters) + "Characters in Prompt" + up.LineBreak+str(self.CountWords_w_EDIT) +"Projected  WORDS (In Prompt w.USER EDITs): "+ ' Projected Characters: ' +  str(self.CountCharacters_w_EDIT))
            else:
                TextEdit.UpdateWordCountField(str(self.CountWords_RESPONSE) + " Words in GPT Response " + str(self.CountCharacters_RESPONSE)  +"Total Characters in GPT Response "  + up.LineBreak +  str(self.CountWords) + "Words in Prompt "  + str(self.CountCharacters) + " Characters in Prompt ")

            #self.WordCountField.grid( row=3, sticky="nsew")
            CrazyTip = Hovertip(self.WordCountField,
                                'WORD COUNT/CHARACTER COUNT/OTHER KEY STATS, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

        except:
            dn = 100

    def keyPress2(self, event):
        try:

            TextEdit.GetPrompts(self)

            #self.WordCountField = tk.Text(self.window, wrap=WORD, )
            TextEdit.UpdateWordCountField2(Text= str(self.CountWords) + "Words in Prompt " + str(self.CountCharacters) + " Characters in Prompt ")

            #self.WordCountField.grid( row=3, sticky="nsew")
            CrazyTip = Hovertip(self.WordCountField2,
                                'WORD COUNT/CHARACTER COUNT/OTHER KEY STATS, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')
        except:
            dn = 100


        #
        # self.CharCountField = tk.Text(self.window, wrap=WORD, )
        # self.CharCountField.insert(tk.END, "CHARACTER COUNT: " + str(self.CountCharacters))
        # self.CharCountField.grid(column=3, row=0, sticky="nsew")
        # CrazyTip = Hovertip(self.UserInput_fld_Crazy,'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')
        #


        # self.window.label.config( text = f'Words: {self.CountWords}'  + f'      Characters: {self.CountCharacters}' )



#step 1make basic window with all of the borders made in the proper color with SHAINE/MondeVert Branding
#Step 2 make basic frames that I can repetitively use that have the ability to update/cycle through prior options, eventually they will have button to go back/forth/ask GPT to help further (way down the line)
#Step 3 maybe if frames can have drop downs add these to all of them, at least a basic one (IDK)
#Step 4 once you have default Main Window, and default sub windows, and buttons accross the top,
#Dark Theme 1, Dark Theme 2, White/Bright/Light, Light Theme 1, Light Theme 2
    def BASE(self):
        self.UIversion = 1

        self.Text = Text
        self.current_file = None
        self.window = tk.Tk()
        self.icon = tk.PhotoImage(file=r"A:\Amini Amor\SHAINE\Marketing\Logo Work\18.png")
        self.window.iconphoto(False, self.icon)
        # self.window = Frame(self.window,borderwidth = 2, relief = tk.SOLID)


        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry(f'{width}x{height}')
        self.window.bind("<FocusIn>", self.undo)
        self.window.bind('<KeyRelease>', self.keyPress)
        self.window.focus()

        self.window.title('SHAINE')



        # txt_edit2 = tk.Text(self.window)
        frm_buttons = tk.Frame(self.window, relief=tk.RAISED, bg=self.Colors[0], pady=2, padx=2, height=44)
        frm_buttons.pack(side='top', fill="x")
        # frm_Text = tk.Frame(self.window, relief=tk.RAISED, bg='yellow'+ ' 4', pady=8, padx=8)
        Middle_Screen = tk.Frame(self.window, relief=tk.RAISED, bg=self.Colors[7], pady=8, padx=8)
        Middle_Screen.pack(ipadx=1600, padx=3, pady=3)
        frm_User = tk.Frame(Middle_Screen, relief=tk.RAISED, bg=self.Colors[2], pady=8, padx=8)
        frm_Text = tk.Frame(Middle_Screen, relief=tk.RAISED, bg=self.Colors[1], pady=8, padx=8)
        self.WordCounter = tk.Frame(self.window, relief=tk.SUNKEN, bg=self.Colors[4])

        frm_buttons.rowconfigure("all", weight=1, height=44)
        Middle_Screen.columnconfigure("all", weight=10, width=1000, height=250)
        Middle_Screen.rowconfigure("all", weight=10, height=100)



    def MakeWindow(self,WindowName = "SHAINE", Text= "",  USERLASTEDIT = '', Current_PROMTS_ALL = '', version = 1, UserConfirm = True):
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
        #self.window.bind("<FocusIn>", self.undo)
        #self.window.bind('<KeyRelease>', self.keyPress)
        #self.window.focus()

        self.window.title(WindowName)
        # self.window.state('zoomed')
        self.text_widget = tk.Text(self.window, wrap=WORD)

        # self.window.rowconfigure("all", minsize=1)
        # self.window.rowconfigure(0, minsize=10, weight=2)
        # self.window.rowconfigure(2, minsize=1, weight=1)
        # self.window.rowconfigure(1, minsize=1200, weight=10)


        self.UserEdits = ''


        # try:
        #     self.window.bind( '<KeyRelease>',  self.keyPress )
        #     self.window.focus()
        #
        # except:
        #     print("oops we did had an error due to word count")
        # # self.window.rowconfigure(1, minsize=1000, weight=10)



        #txt_edit2 = tk.Text(self.window)
        frm_buttons = tk.Frame(self.window, relief=tk.RAISED, bg=self.Colors[0], pady=2, padx=2, height=44)
        frm_buttons.pack(side='top', fill="x")
        #frm_Text = tk.Frame(self.window, relief=tk.RAISED, bg='yellow'+ ' 4', pady=8, padx=8)
        Middle_Screen = tk.Frame(self.window, relief=tk.RAISED, bg=self.Colors[7], pady=8, padx=8)
        Middle_Screen.pack(ipadx=1600,padx=3,pady=3)
        frm_User = tk.Frame(Middle_Screen, relief=tk.RAISED, bg=self.Colors[2], pady=8, padx=8)
        frm_Text = tk.Frame(Middle_Screen, relief=tk.RAISED, bg=self.Colors[1], pady=8, padx=8)
        self.WordCounter = tk.Frame(self.window, relief=tk.SUNKEN, bg=self.Colors[4])

        frm_buttons.rowconfigure("all", weight=1, height=44)
        Middle_Screen.columnconfigure("all",weight=10, width=1000, height=250)
        Middle_Screen.rowconfigure("all", weight=10, height=100)
        self.WordCounter.rowconfigure(0, weight=1)

        #frm_Text.master.maxsize(1000,400)
        #frm_Text.master.minsize(150, 400)
        #frm_User.master.minsize(150, 400)
        #frm_Text.master.maxsize(1800, 1600)
        #frm_User.master.maxsize(1800, 1600)
        #frm_buttons.master.maxsize = (1300, 10)
        #self.WordCounter.master.maxsize = (1,1)
        self.WordCounter.pack(fill="x", expand=0)



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

            self.WordCountField = tk.Text(self.WordCounter, wrap=WORD)
            TextEdit.UpdateWordCountField(self,str(self.CountWords_RESPONSE) + " Words in GPT Response " + str(
                self.CountCharacters_RESPONSE) + " Characters in GPT Response " + up.LineBreak + str(
                self.CountWords) + "Words in Prompt " + str(
                self.CountCharacters) + "Characters in Prompt" + up.LineBreak)
            # self.WordCountField.grid( row=2, sticky="nsew")

            #self.WordCountField.master.maxsize = (1, 1)

            #self.WordCountField.pack(side= "left", expand=0, anchor="nw", fill="x")
            #side= "left", expand=0, anchor="sw"

            #CrazyTip = Hovertip(self.WordCountField,'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

            frm_User.pack( side='right', expand=0, fill="both")
            frm_Text.pack(side='left', expand=0, fill="both")
            self.WordCounter.pack(expand=0, fill="x" )
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
        edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Shift+Z")
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

        self.icon = tk.PhotoImage(file=r"A:\Amini Amor\SHAINE\Marketing\Logo Work\18.png")
        self.window.iconphoto(False, self.icon)

        while self.WindowClose ==False:
            self.window.mainloop()
            #os._exit(1)
            # t = Process(target=self.window.mainloop)
            # t.start()
            # t.join()
            # t.terminate()




        return self.UserResponseProvided






    def MakeWindow2(self,WindowName,  System, Role, Format, Task, Background, Background2, Background3, crazy, version=2, Model='',
                    UserConfirm=False,Text="", Text_Title=''):

        try:
            self.WindowClose2 = False
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
            #self.window2 = tk.Tk()
            self.window2 = tk.Toplevel(self.window)

            self.window2.title(WindowName)
            self.window2.state('zoomed')
            # self.window.bind('<KeyRelease>', self.keyPress2)
            # self.window.focus()

            self.window2.rowconfigure(0, minsize=35, weight=1)
            self.window2.rowconfigure(1, minsize=400, weight=1)
            self.window2.rowconfigure(2, minsize=400, weight=1)
            self.window2.rowconfigure(3, minsize=10, weight=5)
            #self.window2.columnconfigure(1, minsize=400, weight=1)

            frm_buttons = tk.Frame(self.window2)
            # relief = tk.RAISED

            self.window2.columnconfigure(2, weight=1)
            self.window2.columnconfigure(3, weight=1)


            btn_Continue = tk.Button(frm_buttons, text="***Continue (No Changes)***", command=self.Continue_Button2)
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
            self.UserInput_fld_SYSTEM = tk.Text(self.window2, wrap=WORD)
            self.UserInput_fld_SYSTEM.insert(tk.END, self.System)

            self.UserInput_fld_SYSTEM.grid(column=0, row=1, sticky="nsew")
            SystemTip = Hovertip(self.UserInput_fld_SYSTEM, 'System Prompt')

            x = self.UserInput_fld_SYSTEM.get(1.0, END)
            print('Get Value:')
            print(x)

            self.UserInput_fld_ROLE = tk.Text(self.window2, wrap=WORD, )
            self.UserInput_fld_ROLE.insert(tk.END, self.Role)
            self.UserInput_fld_ROLE.grid(column=0, row=2, sticky="nsew")
            RoleTip = Hovertip(self.UserInput_fld_ROLE, 'Role Prompt')

            self.UserInput_fld_FORMAT = tk.Text(self.window2, wrap=WORD, )
            self.UserInput_fld_FORMAT.insert(tk.END, self.Format)
            self.UserInput_fld_FORMAT.grid(column=1, row=1, sticky="nsew")

            FormatTip = Hovertip(self.UserInput_fld_FORMAT, 'Format Prompt')

            self.UserInput_fld_TASK = tk.Text(self.window2, wrap=WORD, )
            self.UserInput_fld_TASK.insert(tk.END, self.Task)
            self.UserInput_fld_TASK.grid(column=3, row=2, sticky="nsew")
            TaskTip = Hovertip(self.UserInput_fld_TASK, 'Task Prompt')

            self.UserInput_fld_Background = tk.Text(self.window2, wrap=WORD, )
            self.UserInput_fld_Background.insert(tk.END, self.Background)
            self.UserInput_fld_Background.grid(column=2, row=1, sticky="nsew")
            BTip = Hovertip(self.UserInput_fld_Background, 'Background Prompt')

            self.UserInput_fld_Background2 = tk.Text(self.window2, wrap=WORD, )
            self.UserInput_fld_Background2.insert(tk.END, self.Background2)
            self.UserInput_fld_Background2.grid(column=1, row=2, sticky="nsew")
            B2Tip = Hovertip(self.UserInput_fld_Background2,
                             'Background Prompt 2 - Not ideal to have too long of prompts, but sometimes doing it this way makes it much simpler. ')

            self.UserInput_fld_Background3 = tk.Text(self.window2, wrap=WORD, )
            self.UserInput_fld_Background3.insert(tk.END, self.Background3)
            self.UserInput_fld_Background3.grid(column=2, row=2, sticky="nsew")
            B3Tip = Hovertip(self.UserInput_fld_Background3,
                             'Background Prompt 3 - Not ideal to have too long of prompts, but sometimes doing it this way makes it much simpler. ')

            self.UserInput_fld_Crazy = tk.Text(self.window2, wrap=WORD, )
            self.UserInput_fld_Crazy.insert(tk.END, self.crazy)
            self.UserInput_fld_Crazy.grid(column=3, row=1, sticky="nsew")
            CrazyTip = Hovertip(self.UserInput_fld_Crazy,
                                'Crazy/Temperature Prompt - Lower number means responses are less creative and more rigid, Too High of a number and it starts to make less sense')

            # TextEdit.GetPrompts(self)
            #
            # self.WordCountField2 = tk.Text(self.window2, wrap=WORD, )
            # text1 = "WORD COUNT: " + str(self.CountWords)
            # #TextEdit.UpdateWordCountField2(text1)
            #
            # self.WordCountField2.grid(row=3, sticky="nsew")
            # CrazyTip = Hovertip(self.WordCountField2,
            #                     'WORD COUNT, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

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
            # scroll_bar = tk.Scrollbar(self.UserInput_fld_SYSTEM)
            # scroll_bar = tk.Scrollbar(self.UserInput_fld_FORMAT)
            # scroll_bar = tk.Scrollbar(self.UserInput_fld_Crazy)
            # scroll_bar = tk.Scrollbar(self.UserInput_fld_Background)
            # scroll_bar = tk.Scrollbar(self.UserInput_fld_Background2)
            # scroll_bar = tk.Scrollbar(self.UserInput_fld_Background3)
            # scroll_bar = tk.Scrollbar(self.UserInput_fld_Crazy)

            frm_buttons.grid(row=0, column=0, sticky="ns")

            self.window2.state('zoomed')

            menu_bar = tk.Menu(self.window2)

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

            self.window2.config(menu=menu_bar)
            self.text_widget = tk.Text(self.window2)

            while self.WindowClose2== False:
                # TextEdit.GetPrompts(self)
                self.window2.mainloop()
            #     # time.sleep(1)

            print('test theory')

        except:
            dn = 100
            print("did not create window")

    def RestoreLastUserText(self):

        USERLASTEDIT = self.USERLASTEDIT
        TextEdit.GetUserText(self)
        TextEdit.UpdateUserText(self,self.USERLASTEDIT)
        self.USERLASTEDIT = self.UserEdits
        return self.USERLASTEDIT




    def GetUserText(self):
        print(self.UserEdits)
        return self.UserEdits

    def GetUserResponseMode(self):
        return self.UserResponseMode



    def GetUserResponseMain(self):
        self.UserConfirm = True
        TextEdit.MakeWindow(self)
        self.x = self.UserInput.get(1.0,END)
        #I May not want to do this, I may be closing windows I do not want to

        try:
            if self.WindowClose == True:
                self.window.destroy()
            if self.WindowClose2 == True:
                self.window2.destroy()
        except:
            print('Error With Window, continue, maybe look into later')
        return self.x




    def Continue_Button2(self, Mode = 0):


        try:

            self.WindowClose2 = True

        except:
            dn = 1
        TextEdit.UserResponse(self,Mode, UIversion=2)



        #self.UserEdits = "0"
        return "0"

    def Continue_Button(self, Mode = 0):


        try:
            self.FINALGPTOUTPUT = self.Printtxt.get(1.0, END)
            self.WindowClose = True



        except:
            dn = 1
        TextEdit.UserResponse(self,Mode, UIversion=1)

        #self.UserEdits = "0"
        return "0"

    def EndUserInput(self, Mode = 5):
        TextEdit.UserResponse(self,Mode, UIversion=1)
        #self.UserEdits = "5"
        return "5"

    def RestoreUserInput(self, Mode = 50):
        TextEdit.UserResponse(self,Mode, UIversion=1)
        #self.UserEdits = "5"
        return "50"


    def EndUserInputSmall(self, Mode = 6):
        TextEdit.UserResponse(self,Mode, UIversion=1)
        #self.UserEdits = "6"
        return "6"

    def EndUserInputMain(self, Mode = 7):
        TextEdit.UserResponse(self,Mode, UIversion=1)
        #self.UserEdits = "7"
        return "7"



    def MakeArt(self, Mode = 8):
        TextEdit.UserResponse(self,Mode, UIversion=1)
        #self.UserEdits = "8"
        return "8"


    def ReviewPrompt(self, Mode = 10):
        TextEdit.UserResponse(self,Mode, UIversion=1)
        #self.UserEdits = "8"
        return "10"

    def ReturnLast(self, Mode = 11):
        TextEdit.UserResponse(self,Mode, UIversion=1)
        closeWindow = True
        #self.UserEdits = "8"
        return "11"

    def ReturnOrig(self, Mode = 12):
        TextEdit.UserResponse(self,Mode, UIversion=1, closeWindow = True)

        #self.UserEdits = "8"
        return "12"

    def UpdateGPTResponse(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.Printtxt.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.Printtxt.insert(tk.END, Text)

    def UpdateUserText(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.UserInput.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.UserInput.insert(tk.END, Text)

    def UpdateWordCountField(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.WordCountField.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.WordCountField.insert(tk.END, Text)
    def UpdateWordCountField2(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.WordCountField2.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.WordCountField2.insert(tk.END, Text)
    def UpdateUserInput_fld_System(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.UserInput_fld_SYSTEM.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.UserInput_fld_SYSTEM.insert(tk.END, Text)


    def UpdateUserInput_fld_Role(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.UserInput_fld_ROLE.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.UserInput_fld_ROLE.insert(tk.END, Text)

    def UpdateUserInput_fld_FORMAT(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.UserInput_fld_FORMAT.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.UserInput_fld_FORMAT.insert(tk.END, Text)

    def UpdateUserInput_fld_TASK(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.UserInput_fld_TASK.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.UserInput_fld_TASK.insert(tk.END, Text)

    def UpdateUserInput_fld_Background(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        self.UserInput_fld_Background.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.UserInput_fld_Background.insert(tk.END, Text)

    def UpdateUserInput_fld_Background2(self, Text):
        # Delete existing content in the Text widget
        self.UserInput_fld_Background2.delete("1.0", tk.END)
        # Add the new data to the Text widget
        self.UserInput_fld_Background2.insert(tk.END, Text)

    def UpdateUserInput_fld_Background3(self, Text):
        self.UserInput_fld_Background3.delete("1.0", tk.END)
        self.UserInput_fld_Background3.insert(tk.END, Text)

    def UpdateUserInput_fld_Version(self, Text):
        self.UserInput_fld_version.delete("1.0", tk.END)
        self.UserInput_fld_version.insert(tk.END, Text)
    def UpdateUserInput_fld_Crazy(self, Text):
        self.UserInput_fld_Crazy.delete("1.0", tk.END)
        self.UserInput_fld_Crazy.insert(tk.END, Text)



    def UpdateGPTResponseWindow(self,NewGPTResponse, NewCurrentPrompt,NEWUSERLASTEDIT,NEWWINDOWNAME):
        self.UserResponseProvided = False
        TextEdit.UpdateGPTResponse(self,NewGPTResponse)
        self.Current_PROMTS_ALL = NewCurrentPrompt
        self.USERLASTEDIT = NEWUSERLASTEDIT
        #self.Window.title(NEWWINDOWNAME)

    def UpdatePromptWindow(self,NewSystem,NewRole,NewFormat, NewTask,NewBackground, NewBackground2, NewBackground3, NewCrazy, NewVersion, NewModel):
        self.UserResponseProvided2 = False
        TextEdit.UpdateUserInput_fld_System(self,NewSystem)
        TextEdit.UpdateUserInput_fld_Role(self,NewRole)
        TextEdit.UpdateUserInput_fld_FORMAT(self,NewFormat)
        TextEdit.UpdateUserInput_fld_TASK(self,NewTask)
        TextEdit.UpdateUserInput_fld_Background(self,NewBackground)
        TextEdit.UpdateUserInput_fld_Background2(self,NewBackground2)
        TextEdit.UpdateUserInput_fld_Background3(self,NewBackground3)
        TextEdit.UpdateUserInput_fld_Crazy(self,NewCrazy)
        #TextEdit.UpdateUserInput_fld_Version(self,NewVersion)


    def UpdateWindow(self,Text1= '',Text2 = '',Text3 = ''):
        if Text != '':
            x = 1





    def GetSpeakText(self):
        return self.Speak_Text

    def Speak(self, Mode = 9):
        TextEdit.UserResponse(self, Mode, UIversion=1, closeWindow = False)
        try:
            try:
                self.Speak_Text  = TextEdit.GetUserResponse(self)

                #threads.append(t)
            except:
                print("Error While trying to read outloud")
        except:
            print("Error While trying to read outloud #2")



        self.UserEdits = "9"
        return "9"




    def SmallEdit(self, Mode = 1):

        self.UserEdits = self.UserInput.get(1.0,END)
        TextEdit.UserResponse(self,Mode, UIversion=1, closeWindow = False)

        return "1"


    def ReWriteWithEdit(self, Mode = 2):

        self.UserEdits = self.UserInput.get(1.0,END)
        TextEdit.UserResponse(self,Mode, UIversion=1, closeWindow = False)

        return "2"

    def ReWrite(self, Mode = 3):
        TextEdit.UserResponse(self,Mode, UIversion=1, closeWindow = False)

        #self.UserEdits = "3"
        return "3"

    def UseUserText(self, Mode = 4):
        self.UserEdits = self.UserInput.get(1.0,END)
        self.WindowClose = True
        TextEdit.UserResponse(self,Mode, UIversion=1, closeWindow = True)

        #self.UserEdits = "4"
        return "4"


#Decide which numbers not to close window on, for instance, Speak, Review Responses, use prior response,

    def UserResponse(self, Mode,UIversion, closeWindow = True):
        self.UserResponseMode = Mode

        if UIversion == 2 and self.UserResponseProvided2 ==False:
            try:
                TextEdit.GetPrompts(self)# print(Mode)
                self.UserResponseProvided2 = True

                try:
                    if self.WindowClose2 == True:
                        self.window2.destroy()
                except:
                    print("Error Trying to close window")

            except:
                print("Error while trying to pull User Values from Prompt")


        elif UIversion == 1 and self.UserResponseProvided ==False:
            try:
                self.UserEdits = TextEdit.GetUserText(self)
                self.UserResponseProvided = True

                try:
                    if self.WindowClose == True:
                        self.window.destroy()
                        os._exit(1)

                except:
                    print("Error Trying to close window")

            except:
                print("Error while trying to pull User Values from Prompt")



        if Mode == 0:
            # print("Pass")
            c = 1




        return Mode
    def GetUserResponseProvided(self):
        return self.UserResponseProvided

    def GetUserResponseProvided2(self):
        return self.UserResponseProvided2
    def GetUserResponse(self):
        return self.UserResponseMode

    def GetFinalGPTOutput(self):
        return self.FINALGPTOUTPUT




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
            self.UserPromptCrazy1 = "Crazy: " + self.UserPromptCrazy

        except:
            print('Error Getting User prompt Crazy')

        # try:
        #     self.UserPromptversion = self.UserInput_fld_version.get(1.0,END)
        #     self.UserPromptversion1 = "Version: " + self.UserPromptversion
        #
        # except:
        #     print('Error Getting User prompt Version')









        self.Full_User_Prompt2 = self.UserPromptSystem +self.UserPromptRole +self.UserPromptFormat +self.UserPromptTask + self.UserPromptBackground +self.UserPromptBackground2 +self.UserPromptBackground3




        self.Full_User_Prompt = self.UserPromptSystem1 +self.UserPromptRole1 +self.UserPromptFormat1 +self.UserPromptTask1 + self.UserPromptBackground1 +self.UserPromptBackground21 +self.UserPromptBackground31


        self.CountCharacters = len(self.Full_User_Prompt2)
        self.CountWords = cu.WordCount(self.Full_User_Prompt2)




    def  UpdatePrompts1(self, Mode = 44):
        d = 1
        #TextEdit.GetPrompts(self)
        self.WindowClose2 = True
        TextEdit.UserResponse(self,Mode, UIversion=2)
        #self.UserEdits = "8"
        return "44"



    def RestorePrompt_original(self, Mode=14):

        TextEdit.UserResponse(self, Mode, UIversion=2)

        return "14"


    def RestorePrompt (self, Mode = 13):


        TextEdit.UserResponse(self,Mode, UIversion=2)



        return "13"



    def OPTIMIZEPROMPT (self, Mode = 2002):


        TextEdit.UserResponse(self,Mode, UIversion=2)



        return "2002"

    def ChangeVersion(self, Mode = 2000):

        TextEdit.UserResponse(self,Mode, UIversion=2)
        #self.version


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
        #self.window.quit
        self.WindowClose = True
        self.WindowClose2 = True
        self.UserResponseProvided = True
        self.UserResponseProvided2 = True

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

#edit_menu.add_command(label="Redo", command=self.redo(), accelerator="Ctrl+SHIFT+Z")

    def undo(self,event):
        d=1

    def redo(self,event):
        d=2




#Do the Same thing for the Characters, the summaries, the Scene by Scene Outline, The Scene Outline,
#Have a loader program where you can point certain files to the query and it allows you to not have to copy and paste the story in, we can have it let us select the files we need for various parts of the story.
    def MakeWindow3(self,Task,System, crazy,Text= "",UserConfirm = False, WindowName = "SHAINE", Text_Title = '', version = '', Model = ''):
        try:

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
            self.window.bind("<FocusIn>", self.undo)
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
            edit_menu.add_command(label="Undo", command=self.undo(), accelerator="Ctrl+Z")
            edit_menu.add_command(label="Redo", command=self.redo(), accelerator="Ctrl+Shift+Z")
            menu_bar.add_cascade(label="Edit", menu=edit_menu)
            # Help menu
            # Add more options to the menu as needed

            self.window.config(menu=menu_bar)
            self.text_widget = tk.Text(self.window)

            while self.WindowClose2 == False:
                # TextEdit.GetPrompts(self)
                self.window2.mainloop()
                os._exit(1)
                # time.sleep(1)
        except:
            dn = 100




#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMenu, QAction
# from PyQt5.QtGui import QColor, QPalette, QIcon
# from PyQt5.QtCore import Qt
#
# class CustomWindow(QMainWindow):
#     def __init__(self):
#         self.Colors_Greens_Blues = ['green yellow', 'aquamarine', 'aqua', 'bondi-blue', 'emerald', 'denim', 'zucchini']
#         super().__init__()
#
#         self.setWindowTitle("SHAINE")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui()
#
#         self.Colors = ['Dark Orchid', 'Orchid', 'plum', 'Blue Violet', 'Light Pink', 'Deep Pink', 'cherry-blossom-pink',
#                   'Dark Magenta', 'Pink',
#                   'Misty Rose', 'Medium Violet Red', 'Medium Spring Green', 'Medium Orchid', 'green yellow',
#                   'Dark Goldenrod', 'alizarin', 'amaranth', 'amber', 'amethyst', 'apricot', 'aqua', 'aquamarine',
#                   'asparagus', 'auburn', 'azure', 'beige', 'bistre',
#                   'black', 'blue', 'blue-green', 'blue-violet', 'bondi-blue', 'brass', 'bronze', 'brown', 'buff',
#                   'burgundy', 'camouflage-green', 'caput-mortuum',
#                   'cardinal', 'carmine', 'carrot-orange', 'celadon', 'cerise', 'cerulean', 'champagne', 'charcoal',
#                   'chartreuse', 'cherry-blossom-pink', 'chestnut',
#                   'chocolate', 'cinnabar', 'cinnamon', 'cobalt', 'copper', 'coral', 'corn', 'cornflower', 'cream',
#                   'crimson', 'cyan', 'dandelion', 'denim', 'ecru', 'emerald',
#                   'eggplant', 'falu-red', 'fern-green', 'firebrick', 'flax', 'forest-green', 'french-rose', 'fuchsia',
#                   'gamboge', 'gold', 'goldenrod', 'green', 'grey', 'han-purple', 'harlequin', 'heliotrope',
#                   'hollywood-cerise', 'indigo', 'ivory', 'jade', 'kelly-green', 'khaki', 'lavender', 'lawn-green',
#                   'lemon', 'lemon-chiffon', 'lilac', 'lime', 'lime-green', 'linen', 'magenta', 'magnolia', 'malachite',
#                   'maroon', 'mauve', 'midnight-blue', 'mint-green', 'misty-rose', 'moss-green', 'mustard', 'myrtle',
#                   'navajo-white', 'navy-blue', 'ochre', 'office-green', 'olive', 'olivine', 'orange', 'orchid',
#                   'papaya-whip', 'peach', 'pear', 'periwinkle', 'persimmon', 'pine-green', 'pink', 'platinum', 'plum',
#                   'powder-blue', 'puce', 'prussian-blue', 'psychedelic-purple', 'pumpkin', 'purple', 'quartz-grey',
#                   'raw-umber', 'razzmatazz', 'red', 'robin-egg-blue', 'rose', 'royal-blue', 'royal-purple', 'ruby',
#                   'russet', 'rust', 'safety-orange', 'saffron', 'salmon', 'sandy-brown', 'sangria', 'sapphire',
#                   'scarlet', 'school-bus-yellow', 'sea-green', 'seashell', 'sepia', 'shamrock-green', 'shocking-pink',
#                   'silver', 'sky-blue', 'slate-grey', 'smalt', 'spring-bud', 'spring-green', 'steel-blue', 'tan',
#                   'tangerine', 'taupe', 'teal', 'tenné-(tawny)', 'terra-cotta', 'thistle', 'titanium-white', 'tomato',
#                   'turquoise', 'tyrian-purple', 'ultramarine', 'van-dyke-brown', 'vermilion', 'violet', 'viridian',
#                   'wheat', 'white', 'wisteria', 'yellow', 'zucchini']
#
#
#     def setup_ui(self):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the buttons
#         button1 = QPushButton("Button 1")
#         button2 = QPushButton("Button 2")
#         button3 = QPushButton("Button 3")
#
#         # Connect button signals to slots
#         button1.clicked.connect(self.button1_clicked)
#         button2.clicked.connect(self.button2_clicked)
#         button3.clicked.connect(self.button3_clicked)
#
#         # Create the text widgets
#         gpt_response_window = QTextEdit("GPT Response Window")
#         user_input_window = QTextEdit("User Input Window")
#
#         # Set object names for easier access
#         gpt_response_window.setObjectName("GPTResponseWindow")
#         user_input_window.setObjectName("UserInputWindow")
#
#         # Add the buttons and text widgets to the layout
#         layout.addWidget(button1)
#         layout.addWidget(button2)
#         layout.addWidget(button3)
#         layout.addWidget(gpt_response_window)
#         layout.addWidget(user_input_window)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Create a menu
#         menu = self.menuBar().addMenu("Menu")
#
#         # Create actions for the menu
#         change_color_action1 = QAction("Change Color Theme - Green", self)
#         change_color_action1.triggered.connect(self.change_color_theme1)
#         change_color_action2 = QAction("Change Color Theme - Black", self)
#         change_color_action2.triggered.connect(self.change_color_theme2)
#         change_color_action3 = QAction("Change Color Theme - Red", self)
#         change_color_action3.triggered.connect(self.change_color_theme3)
#         change_color_action4 = QAction("Change Color Theme - Random", self)
#         change_color_action4.triggered.connect(self.change_color_theme4)
#         # Add actions to the menu
#         menu.addAction(change_color_action1)
#         menu.addAction(change_color_action2)
#         menu.addAction(change_color_action3)
#         menu.addAction(change_color_action4)
#         CustomWindow.change_color_theme4(self)
#
#         # Set window icon
#         self.setWindowIcon(QIcon(r"A:\Amini Amor\SHAINE\Marketing\Logo Work\18.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def button1_clicked(self):
#         print("Button 1 clicked")
#
#     def button2_clicked(self):
#         print("Button 2 clicked")
#
#     def button3_clicked(self):
#         print("Button 3 clicked")
#
#     def change_color_theme1(self, color= 'green'):
#         CustomWindow.change_color_theme(self,color)
#
#     def change_color_theme2(self, color= 'black'):
#         CustomWindow.change_color_theme(self,color)
#
#     def change_color_theme3(self, color= 'red'):
#         CustomWindow.change_color_theme(self,color)
#
#
#     def change_color_theme4(self):
#         color = random.choices(self.Colors_Greens_Blues)
#         CustomWindow.change_color_theme(self,color[0])
#
#
#     def change_color_theme(self,color):
#         # Change the color theme dynamically
#         color1 = QColor(color)
#         palette = self.palette()
#         palette.setColor(QPalette.Window, color1)
#         self.setPalette(palette)
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMenu, QAction, \
#     QRadioButton, QButtonGroup,QLabel
# from PyQt5.QtGui import QColor, QPalette, QIcon, QPainter, QBrush
# from PyQt5.QtCore import Qt
#
#
#
#
#
#
# class CustomWindow2(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Custom Window")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui()
#
#     def setup_ui(self):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the top bar label
#         topbar_label = QLabel(self.windowTitle())
#         topbar_label.setStyleSheet("background-color: black; color: white; padding: 5px;")
#
#         # Create the buttons
#         button1 = QPushButton("Button 1")
#         button2 = QPushButton("Button 2")
#         button3 = QPushButton("Button 3")
#
#         # Connect button signals to slots
#         button1.clicked.connect(self.button1_clicked)
#         button2.clicked.connect(self.button2_clicked)
#         button3.clicked.connect(self.button3_clicked)
#
#         # Create the text widgets
#         gpt_response_window = QTextEdit("GPT Response Window")
#         user_input_window = QTextEdit("User Input Window")
#
#         # Set object names for easier access
#         gpt_response_window.setObjectName("GPTResponseWindow")
#         user_input_window.setObjectName("UserInputWindow")
#
#         # Set the text fields to be read-only and auto-resizable
#         gpt_response_window.setReadOnly(True)
#         gpt_response_window.setAcceptRichText(False)
#         gpt_response_window.setLineWrapMode(QTextEdit.NoWrap)
#         gpt_response_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         gpt_response_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         gpt_response_window.setMinimumHeight(200)
#
#         user_input_window.setReadOnly(True)
#         user_input_window.setAcceptRichText(False)
#         user_input_window.setLineWrapMode(QTextEdit.NoWrap)
#         user_input_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         user_input_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         user_input_window.setMinimumHeight(200)
#
#         # Add the buttons and text widgets to the layout
#         layout.addWidget(topbar_label)
#         layout.addWidget(button1)
#         layout.addWidget(button2)
#         layout.addWidget(button3)
#         layout.addWidget(gpt_response_window)
#         layout.addWidget(user_input_window)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Create a menu
#         menu = self.menuBar().addMenu("Menu")
#
#         # Create actions for the menu
#         color_group = QButtonGroup(self)
#
#         color_names = ["Red", "Green", "Blue", "Yellow"]
#         color_actions = []
#
#         for color_name in color_names:
#             color_action = QAction(color_name, self)
#             color_action.setCheckable(True)
#             color_group.addAction(color_action)
#             menu.addAction(color_action)
#             color_actions.append(color_action)
#
#         # Connect the color actions to the slot
#         color_group.triggered.connect(self.change_color_theme)
#
#         # Set the default color
#         color_actions[0].setChecked(True)
#
#         # Set window icon
#         self.setWindowIcon(QIcon(r"A:\Amini Amor\SHAINE\Marketing\Logo Work\18.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def paintEvent(self, event):
#         # Draw a border around the window
#         painter = QPainter(self)
#         painter.setPen(Qt.black)
#         painter.drawRect(self.rect())
#
#     def button1_clicked(self):
#         print("Button 1 clicked")
#
#     def button2_clicked(self):
#         print("Button 2 clicked")
#
#     def button3_clicked(self):
#         print("Button 3 clicked")
#
#     def change_color_theme(self, action):
#         # Change the color theme based on the selected action
#         color_name = action.text()
#         color = QColor(color_name)
#
#         palette = self.palette()
#         palette.setColor(QPalette.Window, color)
#         self.setPalette(palette)
#
#
# Colors = ['Dark Orchid', 'Orchid', 'plum', 'Blue Violet', 'Light Pink', 'Deep Pink', 'cherry-blossom-pink','Dark Magenta', 'Pink',
#                   'Misty Rose', 'Medium Violet Red', 'Medium Spring Green', 'Medium Orchid', 'green yellow',
#                   'Dark Goldenrod','alizarin','amaranth','amber','amethyst','apricot','aqua','aquamarine','asparagus','auburn','azure','beige','bistre',
#                        'black','blue','blue-green','blue-violet','bondi-blue','brass','bronze','brown','buff','burgundy','camouflage-green','caput-mortuum',
#                        'cardinal','carmine','carrot-orange','celadon','cerise','cerulean','champagne','charcoal','chartreuse','cherry-blossom-pink','chestnut',
#                        'chocolate','cinnabar','cinnamon','cobalt','copper','coral','corn','cornflower','cream','crimson','cyan','dandelion','denim','ecru','emerald',
#                        'eggplant','falu-red','fern-green','firebrick','flax','forest-green','french-rose','fuchsia','gamboge','gold','goldenrod','green','grey','han-purple','harlequin','heliotrope','hollywood-cerise','indigo','ivory','jade','kelly-green','khaki','lavender','lawn-green','lemon','lemon-chiffon','lilac','lime','lime-green','linen','magenta','magnolia','malachite','maroon','mauve','midnight-blue','mint-green','misty-rose','moss-green','mustard','myrtle','navajo-white','navy-blue','ochre','office-green','olive','olivine','orange','orchid','papaya-whip','peach','pear','periwinkle','persimmon','pine-green','pink','platinum','plum','powder-blue','puce','prussian-blue','psychedelic-purple','pumpkin','purple','quartz-grey','raw-umber','razzmatazz','red','robin-egg-blue','rose','royal-blue','royal-purple','ruby','russet','rust','safety-orange','saffron','salmon','sandy-brown','sangria','sapphire','scarlet','school-bus-yellow','sea-green','seashell','sepia','shamrock-green','shocking-pink','silver','sky-blue','slate-grey','smalt','spring-bud','spring-green','steel-blue','tan','tangerine','taupe','teal','tenné-(tawny)','terra-cotta','thistle','titanium-white','tomato','turquoise','tyrian-purple','ultramarine','van-dyke-brown','vermilion','violet','viridian','wheat','white','wisteria','yellow','zucchini']
# Colors_Greens_Blues = ['green yellow','aquamarine','aqua' ,'bondi-blue','emerald','denim','zucchini' ]
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMenu, QAction, \
#     QLabel
# from PyQt5.QtGui import QColor, QPalette, QIcon, QPainter, QBrush
# from PyQt5.QtCore import Qt
#
#
# class CustomWindow3(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Custom Window")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui()
#
#     def setup_ui(self):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the top bar label
#         topbar_label = QLabel(self.windowTitle())
#         topbar_label.setStyleSheet("background-color: black; color: white; padding: 5px;")
#
#         # Create the buttons
#         button1 = QPushButton("Button 1")
#         button2 = QPushButton("Button 2")
#         button3 = QPushButton("Button 3")
#         continue_button = QPushButton("Continue")
#
#         # Connect button signals to slots
#         button1.clicked.connect(self.button1_clicked)
#         button2.clicked.connect(self.button2_clicked)
#         button3.clicked.connect(self.button3_clicked)
#         continue_button.clicked.connect(self.continue_button_clicked)
#
#         # Create the text widgets
#         self.gpt_response_window = QTextEdit("GPT Response Window")
#         self.user_input_window = QTextEdit("User Input Window")
#
#         # Set object names for easier access
#         self.gpt_response_window.setObjectName("GPTResponseWindow")
#         self.user_input_window.setObjectName("UserInputWindow")
#
#         # Set the text fields to be read-only and auto-resizable
#         self.gpt_response_window.setReadOnly(True)
#         self.gpt_response_window.setAcceptRichText(False)
#         self.gpt_response_window.setLineWrapMode(QTextEdit.NoWrap)
#         self.gpt_response_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.gpt_response_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.gpt_response_window.setMinimumHeight(200)
#
#         self.user_input_window.setReadOnly(True)
#         self.user_input_window.setAcceptRichText(False)
#         self.user_input_window.setLineWrapMode(QTextEdit.NoWrap)
#         self.user_input_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.user_input_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.user_input_window.setMinimumHeight(200)
#
#         # Add the buttons and text widgets to the layout
#         layout.addWidget(topbar_label)
#         layout.addWidget(button1)
#         layout.addWidget(button2)
#         layout.addWidget(button3)
#         layout.addWidget(self.gpt_response_window)
#         layout.addWidget(self.user_input_window)
#         layout.addWidget(continue_button)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def paintEvent(self, event):
#         # Draw a border around the window
#         painter = QPainter(self)
#         painter.setPen(Qt.black)
#         painter.drawRect(self.rect())
#
#     def button1_clicked(self):
#         self.gpt_response_window.setText("Button 1 clicked")
#
#     def button2_clicked(self):
#         self.gpt_response_window.setText("Button 2 clicked")
#
#     def button3_clicked(self):
#         self.gpt_response_window.setText("Button 3 clicked")
#
#     def continue_button_clicked(self):
#         self.close()
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QTextEdit, QMenu, QAction, QLabel
# from PyQt5.QtGui import QColor, QPalette, QIcon, QPainter, QBrush
# from PyQt5.QtCore import Qt
#
# class CustomWindow4(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Custom Window")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui()
#
#     def setup_ui(self):
#         # Create the main layout
#         layout = QGridLayout()
#
#         # Create the buttons
#         button1 = QPushButton("Button 1")
#         button2 = QPushButton("Button 2")
#         button3 = QPushButton("Button 3")
#         continue_button = QPushButton("Continue")
#
#         # Connect button signals to slots
#         button1.clicked.connect(self.button1_clicked)
#         button2.clicked.connect(self.button2_clicked)
#         button3.clicked.connect(self.button3_clicked)
#         continue_button.clicked.connect(self.continue_button_clicked)
#
#         # Create the text widgets
#         self.gpt_response_window = QTextEdit()
#         self.user_input_window = QTextEdit()
#         self.gpt_word_count = QLabel("Word Count: 0")
#         self.user_word_count = QLabel("Word Count: 0")
#
#         # Set object names for easier access
#         self.gpt_response_window.setObjectName("GPTResponseWindow")
#         self.user_input_window.setObjectName("UserInputWindow")
#
#         # Set the text fields to be auto-resizable
#         self.gpt_response_window.setAcceptRichText(False)
#         self.gpt_response_window.setLineWrapMode(QTextEdit.NoWrap)
#         self.gpt_response_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.gpt_response_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.gpt_response_window.setMinimumHeight(200)
#
#         self.user_input_window.setAcceptRichText(False)
#         self.user_input_window.setLineWrapMode(QTextEdit.NoWrap)
#         self.user_input_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.user_input_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.user_input_window.setMinimumHeight(200)
#
#         # Add the buttons and text widgets to the layout
#         layout.addWidget(button1, 0, 0)
#         layout.addWidget(button2, 0, 1)
#         layout.addWidget(button3, 0, 2)
#         layout.addWidget(self.gpt_response_window, 1, 0)
#         layout.addWidget(self.user_input_window, 1, 1)
#         layout.addWidget(self.gpt_word_count, 2, 0)
#         layout.addWidget(self.user_word_count, 2, 1)
#         layout.addWidget(continue_button, 3, 0, 1, 3)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def paintEvent(self, event):
#         # Draw a border around the window
#         painter = QPainter(self)
#         painter.setPen(Qt.black)
#         painter.drawRect(self.rect())
#
#     def button1_clicked(self):
#         self.gpt_response_window.setText("Button 1 clicked")
#
#     def button2_clicked(self):
#         self.gpt_response_window.setText("Button 2 clicked")
#
#     def button3_clicked(self):
#         self.gpt_response_window.setText("Button 3 clicked")
#
#     def continue_button_clicked(self):
#         self.close()
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMenu, QAction, QLabel
# from PyQt5.QtGui import QColor, QPalette, QIcon, QPainter, QBrush
# from PyQt5.QtCore import Qt
#
# class CustomWindow5(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Custom Window")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui()
#
#     def setup_ui(self):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the top bar menu
#         menu_bar = self.menuBar()
#         file_menu = menu_bar.addMenu("File")
#         edit_menu = menu_bar.addMenu("Edit")
#
#         # Create the menu items
#         open_action = QAction("Open", self)
#         save_action = QAction("Save", self)
#         exit_action = QAction("Exit", self)
#
#         # Add the menu items to the file menu
#         file_menu.addAction(open_action)
#         file_menu.addAction(save_action)
#         file_menu.addAction(exit_action)
#
#         # Add a separator to the menu
#         file_menu.addSeparator()
#
#         # Add a sub-menu to the file menu
#         sub_menu = QMenu("Sub Menu", self)
#         file_menu.addMenu(sub_menu)
#
#         # Create the buttons
#         button1 = QPushButton("Button 1")
#         button2 = QPushButton("Button 2")
#         button3 = QPushButton("Button 3")
#         continue_button = QPushButton("Continue")
#
#         # Connect button signals to slots
#         button1.clicked.connect(self.button1_clicked)
#         button2.clicked.connect(self.button2_clicked)
#         button3.clicked.connect(self.button3_clicked)
#         continue_button.clicked.connect(self.continue_button_clicked)
#
#         # Create the text widgets
#         self.gpt_response_window = QTextEdit()
#         self.user_input_window = QTextEdit()
#         self.gpt_word_count = QLabel("Word Count: 0")
#         self.user_word_count = QLabel("Word Count: 0")
#
#         # Set object names for easier access
#         self.gpt_response_window.setObjectName("GPTResponseWindow")
#         self.user_input_window.setObjectName("UserInputWindow")
#
#         # Set the text fields to be auto-resizable
#         self.gpt_response_window.setAcceptRichText(False)
#         self.gpt_response_window.setLineWrapMode(QTextEdit.NoWrap)
#         self.gpt_response_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.gpt_response_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.gpt_response_window.setMinimumHeight(200)
#
#         self.user_input_window.setAcceptRichText(False)
#         self.user_input_window.setLineWrapMode(QTextEdit.NoWrap)
#         self.user_input_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.user_input_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.user_input_window.setMinimumHeight(200)
#
#         # Add the buttons, titles, and text widgets to the layout
#         layout.addWidget(QLabel("GPT Response"))
#         layout.addWidget(self.gpt_response_window)
#         layout.addWidget(self.gpt_word_count)
#         layout.addWidget(button1)
#         layout.addWidget(QLabel("User Input"))
#         layout.addWidget(self.user_input_window)
#         layout.addWidget(self.user_word_count)
#         layout.addWidget(button2)
#         layout.addWidget(button3)
#         layout.addWidget(continue_button)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def paintEvent(self, event):
#         # Draw a border around the window
#         painter = QPainter(self)
#         painter.setPen(Qt.black)
#         painter.drawRect(self.rect())
#
#     def button1_clicked(self):
#         self.gpt_response_window.setText("Button 1 clicked")
#
#     def button2_clicked(self):
#         self.gpt_response_window.setText("Button 2 clicked")
#
#     def button3_clicked(self):
#         self.gpt_response_window.setText("Button 3 clicked")
#
#     def continue_button_clicked(self):
#         self.close()
#
#     def update_word_count(self):
#         gpt_text = self.gpt_response_window.toPlainText()
#         user_text = self.user_input_window.toPlainText()
#         gpt_word_count = len(gpt_text.split())
#         user_word_count = len(user_text.split())
#         self.gpt_word_count.setText(f"Word Count: {gpt_word_count}")
#         self.user_word_count.setText(f"Word Count: {user_word_count}")
#
#     def keyPressEvent(self, event):
#         super().keyPressEvent(event)
#         self.update_word_count()
#
#
#
#
# #
# # class CustomWindowother(wx.Frame):
# #     def __init__(self):
# #         super().__init__(parent=None, title="Custom Window", size=(600, 400))
# #         self.setup_ui()
# #
# #     def setup_ui(self):
# #         # Create the main panel
# #         panel = wx.Panel(self)
# #
# #         # Create the buttons
# #         button1 = wx.Button(panel, label="Button 1")
# #         button2 = wx.Button(panel, label="Button 2")
# #         button3 = wx.Button(panel, label="Button 3")
# #         continue_button = wx.Button(panel, label="Continue")
# #
# #         # Bind button events to handlers
# #         button1.Bind(wx.EVT_BUTTON, self.button1_clicked)
# #         button2.Bind(wx.EVT_BUTTON, self.button2_clicked)
# #         button3.Bind(wx.EVT_BUTTON, self.button3_clicked)
# #         continue_button.Bind(wx.EVT_BUTTON, self.continue_button_clicked)
# #
# #         # Create the text widgets
# #         self.gpt_response_window = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
# #         self.user_input_window = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
# #         self.gpt_word_count = wx.StaticText(panel, label="Word Count: 0")
# #         self.user_word_count = wx.StaticText(panel, label="Word Count: 0")
# #
# #         # Bind text events to handlers
# #         self.gpt_response_window.Bind(wx.EVT_TEXT, self.update_gpt_word_count)
# #         self.user_input_window.Bind(wx.EVT_TEXT, self.update_user_word_count)
# #
# #         # Add the buttons and text widgets to the sizer
# #         sizer = wx.GridBagSizer(10, 10)
# #         sizer.Add(button1, pos=(0, 0))
# #         sizer.Add(button2, pos=(0, 1))
# #         sizer.Add(button3, pos=(0, 2))
# #         sizer.Add(self.gpt_response_window, pos=(1, 0), span=(1, 3), flag=wx.EXPAND)
# #         sizer.Add(self.gpt_word_count, pos=(2, 0))
# #         sizer.Add(self.user_input_window, pos=(1, 3), span=(1, 3), flag=wx.EXPAND)
# #         sizer.Add(self.user_word_count, pos=(2, 3))
# #         sizer.Add(continue_button, pos=(3, 0), span=(1, 6), flag=wx.EXPAND)
# #
# #         # Set the sizer for the panel
# #         panel.SetSizer(sizer)
# #
# #         # Set window icon
# #         icon = wx.Icon("icon.png", wx.BITMAP_TYPE_PNG)
# #         self.SetIcon(icon)
# #
# #         # Show the window
# #         self.Show()
# #
# #     def button1_clicked(self, event):
# #         self.gpt_response_window.SetValue("Button 1 clicked")
# #
# #     def button2_clicked(self, event):
# #         self.gpt_response_window.SetValue("Button 2 clicked")
# #
# #     def button3_clicked(self, event):
# #         self.gpt_response_window.SetValue("Button 3 clicked")
# #
# #     def continue_button_clicked(self, event):
# #         self.Close()
# #
# #     def update_gpt_word_count(self, event):
# #         text = self.gpt_response_window.GetValue()
# #         word_count = len(text.split())
# #         self.gpt_word_count.SetLabel(f"Word Count: {word_count}")
# #
# #     def update_user_word_count(self, event):
# #         text = self.user_input_window.GetValue()
# #         word_count = len(text.split())
# #         self.user_word_count.SetLabel(f"Word Count: {word_count}")
# #
# # # Create an instance of the application
# # app = wx.App()
# #
# # # Create an instance of the custom window
# # window = CustomWindow()
# #
# # # Run the event loop
# # app.MainLoop()
#
#
#
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMenu, QAction, QLabel
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt
#
# class CustomWindow6(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Custom Window")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui()
#
#     def setup_ui(self):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the top bar menu
#         menu_bar = self.menuBar()
#         file_menu = menu_bar.addMenu("File")
#         edit_menu = menu_bar.addMenu("Edit")
#
#         # Create the menu items
#         open_action = QAction("Open", self)
#         save_action = QAction("Save", self)
#         exit_action = QAction("Exit", self)
#
#         # Add the menu items to the file menu
#         file_menu.addAction(open_action)
#         file_menu.addAction(save_action)
#         file_menu.addAction(exit_action)
#
#         # Create the buttons
#         button1 = QPushButton("Button 1")
#         button2 = QPushButton("Button 2")
#         button3 = QPushButton("Button 3")
#         continue_button = QPushButton("Continue")
#
#         # Connect button signals to slots
#         button1.clicked.connect(self.button1_clicked)
#         button2.clicked.connect(self.button2_clicked)
#         button3.clicked.connect(self.button3_clicked)
#         continue_button.clicked.connect(self.continue_button_clicked)
#
#         # Create the text widgets
#         self.gpt_response_window = QTextEdit()
#         self.user_input_window = QTextEdit()
#         self.gpt_word_count = QLabel("Word Count: 0")
#         self.user_word_count = QLabel("Word Count: 0")
#
#         # Set the word count labels to be dynamic
#         self.gpt_response_window.textChanged.connect(self.update_word_count)
#         self.user_input_window.textChanged.connect(self.update_word_count)
#
#         # Add the buttons, titles, and text widgets to the layout
#         layout.addWidget(QLabel("GPT Response"))
#         layout.addWidget(self.gpt_response_window)
#         layout.addWidget(self.gpt_word_count)
#         layout.addWidget(button1)
#         layout.addWidget(QLabel("User Input"))
#         layout.addWidget(self.user_input_window)
#         layout.addWidget(self.user_word_count)
#         layout.addWidget(button2)
#         layout.addWidget(button3)
#         layout.addWidget(continue_button)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def button1_clicked(self):
#         self.gpt_response_window.setText("Button 1 clicked")
#
#     def button2_clicked(self):
#         self.gpt_response_window.setText("Button 2 clicked")
#
#     def button3_clicked(self):
#         self.gpt_response_window.setText("Button 3 clicked")
#
#     def continue_button_clicked(self):
#         self.close()
#
#     def update_word_count(self):
#         gpt_text = self.gpt_response_window.toPlainText()
#         user_text = self.user_input_window.toPlainText()
#         gpt_word_count = len(gpt_text.split())
#         user_word_count = len(user_text.split())
#         self.gpt_word_count.setText(f"Word Count: {gpt_word_count}")
#         self.user_word_count.setText(f"Word Count: {user_word_count}")
#
#
#
#
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QCheckBox, QLabel,QHBoxLayout
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt
#
# class CustomWindow7(QMainWindow):
#     def __init__(self, window_title, text_fields):
#         super().__init__()
#
#         self.setWindowTitle(window_title)
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui(text_fields)
#
#     def setup_ui(self, text_fields):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the buttons
#         button_layout = QHBoxLayout()
#         for i, button_text in enumerate(text_fields):
#             button = QPushButton(button_text)
#             button_layout.addWidget(button)
#
#         # Create the checkbox
#         checkbox = QCheckBox("Checkbox")
#
#         # Create the text widgets
#         text_edit_layout = QVBoxLayout()
#         word_count_labels = []
#         for i, text in enumerate(text_fields):
#             text_edit = QTextEdit()
#             text_edit.setObjectName(f"TextEdit_{i}")
#             word_count_label = QLabel("Word Count: 0")
#             word_count_labels.append(word_count_label)
#             text_edit.textChanged.connect(lambda checked, label=word_count_label, index=i: self.update_word_count(label, index))
#             text_edit_layout.addWidget(QLabel(text))
#             text_edit_layout.addWidget(text_edit)
#             text_edit_layout.addWidget(word_count_label)
#
#         # Create the total word count label
#         total_word_count_label = QLabel("Total Word Count: 0")
#
#         # Add the buttons, checkbox, titles, text widgets, and total word count label to the layout
#         layout.addLayout(button_layout)
#         layout.addWidget(checkbox)
#         layout.addLayout(text_edit_layout)
#         layout.addWidget(total_word_count_label)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def update_word_count(self, label, index):
#         text_edit = self.findChild(QTextEdit, f"TextEdit_{index}")
#         text = text_edit.toPlainText()
#         word_count = len(text.split())
#         label.setText(f"Word Count: {word_count}")
#
#         # Update total word count
#         total_word_count = sum([int(label.text().split()[-1]) for label in self.centralWidget().findChildren(QLabel) if label.text().startswith("Word Count:")])
#         total_word_count_label = self.centralWidget().findChild(QLabel, "Total Word Count")
#         total_word_count_label.setText(f"Total Word Count: {total_word_count}")
#
# def create_windows(window_info):
#     app = QApplication([])
#     windows = []
#
#     for window_title, text_fields in window_info:
#         window = CustomWindow7(window_title, text_fields)
#         windows.append(window)
#
#     app.exec_()
#
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QCheckBox, QLabel, QHBoxLayout
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt
#
# class CustomWindow8(QMainWindow):
#     def __init__(self, window_title, text_fields):
#         super().__init__()
#
#         self.setWindowTitle(window_title)
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setup_ui(text_fields)
#
#     def setup_ui(self, text_fields):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the buttons
#         button_layout = QHBoxLayout()
#         for i, button_text in enumerate(text_fields):
#             button = QPushButton(button_text)
#             button_layout.addWidget(button)
#
#         # Create the checkbox
#         checkbox = QCheckBox("Checkbox")
#
#         # Create the text widgets
#         text_edit_layout = QVBoxLayout()
#         word_count_labels = []
#         for i, (title, default_text) in enumerate(text_fields):
#             text_edit = QTextEdit(default_text)
#             text_edit.setObjectName(f"TextEdit_{i}")
#             word_count_label = QLabel(f"Word Count: {len(default_text.split())}")
#             word_count_labels.append(word_count_label)
#             text_edit.textChanged.connect(lambda checked, label=word_count_label, index=i: self.update_word_count(label, index))
#             text_edit_layout.addWidget(QLabel(title))
#             text_edit_layout.addWidget(text_edit)
#             text_edit_layout.addWidget(word_count_label)
#
#         # Create the total word count label
#         total_word_count_label = QLabel("Total Word Count: 0")
#
#         # Add the buttons, checkbox, titles, text widgets, and total word count label to the layout
#         layout.addLayout(button_layout)
#         layout.addWidget(checkbox)
#         layout.addLayout(text_edit_layout)
#         layout.addWidget(total_word_count_label)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def update_word_count(self, label, index):
#         text_edit = self.findChild(QTextEdit, f"TextEdit_{index}")
#         text = text_edit.toPlainText()
#         word_count = len(text.split())
#         label.setText(f"Word Count: {word_count}")
#
#         # Update total word count
#         total_word_count = sum([int(label.text().split()[-1]) for label in self.centralWidget().findChildren(QLabel) if label.text().startswith("Word Count:")])
#         total_word_count_label = self.centralWidget().findChild(QLabel, "Total Word Count")
#         total_word_count_label.setText(f"Total Word Count: {total_word_count}")
#
# def create_windows2(window_info):
#     app = QApplication([])
#     windows = []
#
#     for window_title, text_fields in window_info:
#         window = CustomWindow8(window_title, text_fields)
#         windows.append(window)
#
#     app.exec_()
#
#
#
#
#
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QCheckBox, QLabel, QHBoxLayout, QStatusBar
# from PyQt5.QtGui import QIcon, QColor
# from PyQt5.QtCore import Qt
#
# class CustomWindow9(QMainWindow):
#     def __init__(self, window_title, window_type, window_size, internal_frames):
#         super().__init__()
#         self.setWindowTitle(window_title)
#         self.setGeometry(100, 100, *self.get_window_size(window_size))
#         self.setup_ui(internal_frames)
#
#
#     def get_window_size(self, window_size):
#         sizes = {
#             "small": (400, 300),
#             "medium": (600, 400),
#             "large": (800, 600),
#             "x-large": (1000, 800)
#         }
#         return sizes.get(window_size, (600, 400))
#
#     def get_window_size(self, window_size):
#         sizes = {
#             "small": (400, 300),
#             "medium": (600, 400),
#             "large": (800, 600),
#             "x-large": (1000, 800)
#         }
#         return sizes.get(window_size, (600, 400))
#
#     def setup_ui(self, internal_frames):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the internal frames
#         for frame in internal_frames:
#             frame_widget = self.create_internal_frame(frame)
#             layout.addWidget(frame_widget)
#
#         # Create the total word count label
#         self.total_word_count_label = QLabel("Total Word Count: 0")
#         layout.addWidget(self.total_word_count_label)
#
#         # Create a status bar
#         self.statusBar = QStatusBar()
#         self.setStatusBar(self.statusBar)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def create_internal_frame(self, frame_info):
#         frame_widget = QWidget()
#         frame_layout = QVBoxLayout()
#
#         title, text_value, buttons, checkboxes, color = frame_info
#
#         # Create the text widget
#         text_edit = QTextEdit(text_value)
#         text_edit.setObjectName("TextEdit")
#         text_edit.textChanged.connect(self.update_word_count)
#
#         # Create the word count label
#         word_count_label = QLabel(f"Word Count: {len(text_value.split())}")
#
#         # Create the character count label
#         character_count_label = QLabel(f"Character Count: {len(text_value)}")
#
#         # Create the buttons
#         button_layout = QHBoxLayout()
#         for button_text in buttons:
#             button = QPushButton(button_text)
#             button.clicked.connect(lambda checked, btn=button_text: self.update_text_edit(text_edit, btn))
#             button_layout.addWidget(button)
#
#         # Create the checkboxes
#         checkbox_layout = QHBoxLayout()
#         for checkbox_text in checkboxes:
#             checkbox = QCheckBox(checkbox_text)
#             checkbox_layout.addWidget(checkbox)
#
#         # Set the color scheme
#         if color:
#             frame_widget.setStyleSheet(f"background-color: {color};")
#
#         # Add the title, text widget, word count label, character count label, buttons, and checkboxes to the frame layout
#         frame_layout.addWidget(QLabel(title))
#         frame_layout.addWidget(text_edit)
#         frame_layout.addWidget(word_count_label)
#         frame_layout.addWidget(character_count_label)
#         frame_layout.addLayout(button_layout)
#         frame_layout.addLayout(checkbox_layout)
#
#         # Set the frame layout to the frame widget
#         frame_widget.setLayout(frame_layout)
#
#         return frame_widget
#
#     def update_word_count(self):
#         total_word_count = sum([len(text_edit.toPlainText().split()) for text_edit in self.findChildren(QTextEdit)])
#         self.total_word_count_label.setText(f"Total Word Count: {total_word_count}")
#
#     def update_text_edit(self, text_edit, button_text):
#         current_text = text_edit.toPlainText()
#         if current_text:
#             current_text += f" {button_text}"
#         else:
#             current_text = button_text
#         text_edit.setText(current_text)
#
# def create_windows3(window_info):
#     app = QApplication([])
#     windows = []
#
#     for info in window_info:
#         window = CustomWindow9(*info)
#         windows.append(window)
#
#     app.exec_()
#
#
#
#
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QCheckBox, QLabel, QHBoxLayout, QStatusBar, QMenuBar, QMenu, QAction
# from PyQt5.QtGui import QIcon, QColor
# from PyQt5.QtCore import Qt
#
# class CustomWindow9(QMainWindow):
#     def __init__(self, window_title, window_type, window_size, internal_frames):
#         super().__init__()
#
#         self.setWindowTitle(window_title)
#         self.setGeometry(100, 100, *self.get_window_size(window_size))
#         self.setup_ui(internal_frames)
#
#     def get_window_size(self, window_size):
#         sizes = {
#             "small": (400, 300),
#             "medium": (600, 400),
#             "large": (800, 600),
#             "x-large": (1000, 800)
#         }
#         return sizes.get(window_size, (600, 400))
#
#     def setup_ui(self, internal_frames):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the dropdown menu
#         menu_bar = self.menuBar()
#         file_menu = menu_bar.addMenu('File')
#         edit_menu = menu_bar.addMenu('Edit')
#         shaine_menu = menu_bar.addMenu('SHAINE')
#         help_menu = menu_bar.addMenu('Help')
#
#         # Create the buttons on the main screen
#         main_buttons_layout = QHBoxLayout()
#         main_buttons = ["Continue", "Cancel", "Go Back", "Review Prompts", "Review Outlines", "Need Internet Access",
#                         "Ask GPT"]
#
#
#         for button_text in main_buttons:
#             button = QPushButton(button_text)
#             button.clicked.connect(lambda checked, btn=button_text: self.update_status_bar(btn))
#             main_buttons_layout.addWidget(button)
#
#         internet_button = QPushButton("Internet")
#         internet_button.clicked.connect(self.open_web_browser)
#         main_buttons_layout.addWidget(internet_button)
#
#
#         layout.addLayout(main_buttons_layout)
#
#         # Create the internal frames
#         for frame in internal_frames:
#             frame_widget = self.create_internal_frame(frame)
#             layout.addWidget(frame_widget)
#
#         # Create the total word count label
#         self.total_word_count_label = QLabel("Total Word Count: 0")
#         layout.addWidget(self.total_word_count_label)
#
#         # Create a status bar
#         self.statusBar = QStatusBar()
#         self.setStatusBar(self.statusBar)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon("icon.png"))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#
#     def update_status_bar(self, button_text):
#         status_message = f"SHAINE: {button_text}"
#         self.statusBar.showMessage(status_message)
#
#     def create_internal_frame(self, frame_info):
#         frame_widget = QWidget()
#         frame_layout = QVBoxLayout()
#
#         title, text_value, buttons, checkboxes, color = frame_info
#
#         # Create the text widget
#         text_edit = QTextEdit(text_value)
#         text_edit.setObjectName("TextEdit")
#         text_edit.textChanged.connect(lambda: self.update_word_count(text_edit))
#
#         # Create the word count label
#         word_count_label = QLabel(f"Word Count: {len(text_value.split())}")
#
#         # Create the character count label
#         character_count_label = QLabel(f"Character Count: {len(text_value)}")
#
#         # Create the buttons
#         button_layout = QHBoxLayout()
#         for button_text in buttons:
#             button = QPushButton(button_text)
#             button.clicked.connect(lambda checked, btn=button_text: self.update_text_edit(text_edit, btn))
#             button_layout.addWidget(button)
#
#         # Create the checkboxes
#         checkbox_layout = QHBoxLayout()
#         for checkbox_text in checkboxes:
#             checkbox = QCheckBox(checkbox_text)
#             checkbox_layout.addWidget(checkbox)
#
#         # Set the color scheme
#         if color:
#             frame_widget.setStyleSheet(f"background-color: {color};")
#
#         # Add the title, text widget, word count label, character count label, buttons, and checkboxes to the frame layout
#         frame_layout.addWidget(QLabel(title))
#         frame_layout.addWidget(text_edit)
#         frame_layout.addWidget(word_count_label)
#         frame_layout.addWidget(character_count_label)
#         frame_layout.addLayout(button_layout)
#         frame_layout.addLayout(checkbox_layout)
#
#         # Set the frame layout to the frame widget
#         frame_widget.setLayout(frame_layout)
#
#         return frame_widget
#     def open_web_browser(self):
#         web_browser_thread = threading.Thread(target=create_web_browser_window)
#         web_browser_thread.start()
#     def update_word_count(self, text_edit):
#         word_count = len(text_edit.toPlainText().split())
#         character_count = len(text_edit.toPlainText())
#         for label in text_edit.parent().findChildren(QLabel):
#             if label.text().startswith("Word Count:"):
#                 label.setText(f"Word Count: {word_count}")
#             elif label.text().startswith("Character Count:"):
#                 label.setText(f"Character Count: {character_count}")
#
#         total_word_count = sum([len(text_edit.toPlainText().split()) for text_edit in self.findChildren(QTextEdit)])
#         self.total_word_count_label.setText(f"Total Word Count: {total_word_count}")
#
#     def update_text_edit(self, text_edit, button_text):
#         current_text = text_edit.toPlainText()
#         if current_text:
#             current_text += f" {button_text}"
#         else:
#             current_text = button_text
#         text_edit.setText(current_text)
#
#
#
# def create_windows4(window_info):
#     app = QApplication([])
#     windows = []
#
#     for info in window_info:
#         window = CustomWindow(*info)
#         windows.append(window)
#
#     sys.exit(app.exec_())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#





#
# # Import necessary libraries
# import sys
# import threading
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QCheckBox, QLabel, QHBoxLayout, QStatusBar, QMenuBar, QMenu, QAction, QColorDialog
# from PyQt5.QtGui import QIcon, QColor
# from PyQt5.QtCore import Qt
#
# class CustomWindow10(QMainWindow):
#     def __init__(self, window_title, window_type, window_size, internal_frames):
#         super().__init__()
#
#         self.setWindowTitle(window_title)
#         self.setGeometry(100, 100, *self.get_window_size(window_size))
#         self.setup_ui(internal_frames)
#
#     def get_window_size(self, window_size):
#         if window_size == "small":
#             return 300, 200
#         elif window_size == "medium":
#             return 500, 300
#         elif window_size == "large":
#             return 800, 500
#         elif window_size == "XL":
#             screen = QApplication.primaryScreen()
#             screen_geometry = screen.availableGeometry()
#             return screen_geometry.width(), screen_geometry.height()
#         elif window_size == "full_screen":
#             return QApplication.desktop().screenGeometry().width(), QApplication.desktop().screenGeometry().height()
#         else:
#             return 600, 400
#
#     def setup_ui(self, internal_frames):
#         # Create the main layout
#         layout = QVBoxLayout()
#
#         # Create the dropdown menu
#         menu_bar = self.menuBar()
#         file_menu = menu_bar.addMenu('File')
#         edit_menu = menu_bar.addMenu('Edit')
#         shaine_menu = menu_bar.addMenu('SHAINE')
#         help_menu = menu_bar.addMenu('Help')
#
#         # Create the buttons on the main screen
#         main_buttons_layout = QHBoxLayout()
#         main_buttons = ["Continue", "Cancel", "Go Back", "Review Prompts", "Review Outlines", "Need Internet Access",
#                         "Ask GPT"]
#
#         for button_text in main_buttons:
#             button = QPushButton(button_text)
#             button.clicked.connect(lambda checked, btn=button_text: self.update_status_bar(btn))
#             main_buttons_layout.addWidget(button)
#
#         internet_button = QPushButton("Internet")
#         internet_button.clicked.connect(self.open_web_browser)
#         main_buttons_layout.addWidget(internet_button)
#
#         layout.addLayout(main_buttons_layout)
#
#         # Create the internal frames
#         self.frames = []
#         for frame in internal_frames:
#             frame_widget = self.create_internal_frame(frame)
#             layout.addWidget(frame_widget)
#             self.frames.append(frame_widget)
#
#         # Create the total word count label
#         self.total_word_count_label = QLabel("Total Word Count: 0")
#         layout.addWidget(self.total_word_count_label)
#
#         # Create a status bar
#         self.statusBar = QStatusBar()
#         self.setStatusBar(self.statusBar)
#
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
#
#         # Set window icon
#         self.setWindowIcon(QIcon(LOGO))
#
#         # Set desktop thumbnail
#         self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
#         self.show()
#     def open_web_browser(self):
#         web_browser_thread = threading.Thread(target=create_web_browser_window)
#         web_browser_thread.start()
#     def update_status_bar(self, button_text):
#         status_message = f"SHAINE: {button_text}"
#         self.statusBar.showMessage(status_message)
#
#     def create_internal_frame(self, frame_info):
#         frame_widget = QWidget()
#         frame_layout = QVBoxLayout()
#
#         title, text_value, buttons, checkboxes, color = frame_info
#
#         # Create the text widget
#         text_edit = QTextEdit(text_value)
#         text_edit.setObjectName("TextEdit")
#         text_edit.setStyleSheet("background-color: white;")  # Set text field background color
#         text_edit.textChanged.connect(lambda: self.update_word_count(text_edit))
#
#         # Create the word count label
#         word_count_label = QLabel(f"Word Count: {len(text_value.split())}")
#
#         # Create the character count label
#         character_count_label = QLabel(f"Character Count: {len(text_value)}")
#
#         # Create the buttons
#         button_layout = QHBoxLayout()
#         for button_text in buttons:
#             button = QPushButton(button_text)
#             button.clicked.connect(lambda checked, btn=button_text: self.update_text_edit(text_edit, btn))
#             button_layout.addWidget(button)
#
#         # Create the checkboxes
#         checkbox_layout = QHBoxLayout()
#         for checkbox_text in checkboxes:
#             checkbox = QCheckBox(checkbox_text)
#             checkbox_layout.addWidget(checkbox)
#
#         # Set the color scheme
#         if color:
#             frame_widget.setStyleSheet(f"background-color: {color}; border: 2px solid black;")  # Set frame background color and border
#
#         # Add the title, text widget, word count label, character count label, buttons, and checkboxes to the frame layout
#         frame_layout.addWidget(QLabel(title))
#         frame_layout.addWidget(text_edit)
#         frame_layout.addWidget(word_count_label)
#         frame_layout.addWidget(character_count_label)
#         frame_layout.addLayout(button_layout)
#         frame_layout.addLayout(checkbox_layout)
#
#         # Set the frame layout to the frame widget
#         frame_widget.setLayout(frame_layout)
#
#         return frame_widget
#
#     def update_word_count(self, text_edit):
#         word_count = len(text_edit.toPlainText().split())
#         character_count = len(text_edit.toPlainText())
#         for label in text_edit.parent().findChildren(QLabel):
#             if label.text().startswith("Word Count:"):
#                 label.setText(f"Word Count: {word_count}")
#             elif label.text().startswith("Character Count:"):
#                 label.setText(f"Character Count: {character_count}")
#
#     def update_text_edit(self, text_edit, button_text):
#         current_text = text_edit.toPlainText()
#         if current_text:
#             current_text += f" {button_text}"
#         else:
#             current_text = button_text
#         text_edit.setText(current_text)
#
#     def update_status_bar(self, button_text):
#         status_message = f"SHAINE: {button_text}"
#         self.statusBar.showMessage(status_message)
#
# def create_windows5(window_info):
#     app = QApplication([])
#     windows = []
#
#     for info in window_info:
#         window = CustomWindow10(*info)
#         windows.append(window)
#
#     sys.exit(app.exec_())


from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QTextEdit, QCheckBox, QStatusBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import threading
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QStatusBar, QTextEdit, QCheckBox,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class CustomWindow11(QMainWindow):
    def __init__(self, window_title, window_type, window_size, main_buttons,main_checkboxes,internal_frames):
        self.main_buttons = main_buttons
        super().__init__()

        self.setWindowTitle(window_title + " - " + window_type)
        self.setGeometry(100, 100, *self.get_window_size(window_size))
        self.setup_ui(internal_frames)
        self.SHAINELOG = "SHAINE Actions Taken: "
        self.SHAINELOGCounter = 0


    def get_window_size(self, window_size):
        if window_size == "small":
            return 300, 200
        elif window_size == "medium":
            return 500, 300
        elif window_size == "large":
            return 800, 500
        elif window_size == "XL":
            screen = QApplication.primaryScreen()
            screen_geometry = screen.availableGeometry()
            return screen_geometry.width(), screen_geometry.height()
        elif window_size == "full_screen":
            return QApplication.desktop().screenGeometry().width(), QApplication.desktop().screenGeometry().height()
        else:
            return 600, 400

    def setup_ui(self, internal_frames):
        # Create the main layout
        layout = QGridLayout()

        # Create the dropdown menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        shaine_menu = menu_bar.addMenu('SHAINE')
        help_menu = menu_bar.addMenu('Help')

        # Create the buttons on the main screen
        main_buttons_layout = QHBoxLayout()


        for button_text in self.main_buttons:
            button = QPushButton(button_text)
            button.clicked.connect(lambda checked, btn=button_text: self.update_status_bar(btn))
            main_buttons_layout.addWidget(button)


        #Not ready for this option yet, it is buggy and causes it to crash
        # internet_button = QPushButton("Internet")
        # internet_button.clicked.connect(self.open_web_browser)
        # main_buttons_layout.addWidget(internet_button)

        layout.addLayout(main_buttons_layout, 0, 0, 1, 2)  # Add main buttons layout to grid layout

        # Create the internal frames
        self.frames = []
        num_columns = 2 if len(internal_frames) > 1 else 1
        for i, frame in enumerate(internal_frames):
            frame_widget = self.create_internal_frame(frame)
            layout.addWidget(frame_widget, i // num_columns + 1, i % num_columns)  # Add frame widget to grid layout
            self.frames.append(frame_widget)

        # Create the total word count label
        self.total_word_count_label = QLabel("Total Word Count: 0")
        layout.addWidget(self.total_word_count_label, len(internal_frames) // num_columns + 1, 0, 1,
                         num_columns)  # Add total word count label to grid layout

        # Create a status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set window icon
        self.setWindowIcon(QIcon(LOGO))

        # Set desktop thumbnail
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.show()

    def open_web_browser(self):
        web_browser_thread = threading.Thread(target=create_web_browser_window)
        web_browser_thread.start()

    def update_status_bar(self, button_text):
        status_message = f"SHAINE: {button_text}"
        self.statusBar.showMessage(status_message)

    def create_internal_frame(self, frame_info):
        frame_widget = QWidget()
        frame_layout = QVBoxLayout()

        title, text_value, buttons, checkboxes, color = frame_info
        #print(frame_info)

        # Create the text widget
        text_edit = QTextEdit(text_value)
        text_edit.setObjectName("TextEdit")
        text_edit.setStyleSheet("background-color: white;")  # Set text field background color
        text_edit.textChanged.connect(lambda: self.update_word_count(text_edit))

        # Create the word count label
        word_count =len(text_value.split())
        character_count=  len(text_value)
        word_count_label = QLabel(f"Word Count: {word_count}" + f"Character Count: {character_count}")
        word_count_label.setStyleSheet("font-weight: bold;")  # Set label font weight
        word_count_label.setStyleSheet("background-color: #f0f0f0;")  # Set text field background color


        # # Create the character count label
        # character_count_label = QLabel(f"Character Count: {len(text_value)}")
        # character_count_label.setStyleSheet("font-weight: bold;")  # Set label font weight
        #

        # Create the buttons
        button_layout = QHBoxLayout()
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("background-color: #f0f0f0;")  # Set button background color
            button.clicked.connect(lambda checked, btn=button_text: self.update_text_edit(text_edit, btn))
            button_layout.addWidget(button)

        TITLE = QLabel(title)
        TITLE.setStyleSheet("font-weight: bold; color: white;")  # Set label font weight and color
        TITLE.setStyleSheet("background-color: #f0f0f0;")  # Set text field background color


        # Create the checkboxes
        checkbox_layout = QHBoxLayout()
        for checkbox_text in checkboxes:
            checkbox = QCheckBox(checkbox_text)
            checkbox_layout.addWidget(checkbox)

        # Set the color scheme
        if color:
            frame_widget.setStyleSheet(
                f"background-color: {color}; border: 4px solid black;")  # Set frame background color and border

        # Add the title, text widget, word count label, character count label, buttons, and checkboxes to the frame layout
        frame_layout.addWidget(TITLE)
        frame_layout.addLayout(checkbox_layout)
        frame_layout.addLayout(button_layout)
        frame_layout.addWidget(text_edit)
        frame_layout.addWidget(word_count_label)
        #frame_layout.addWidget(character_count_label)


        # Set the frame layout to the frame widget
        frame_widget.setLayout(frame_layout)

        return frame_widget

    def update_word_count(self, text_edit):
        word_count = len(text_edit.toPlainText().split())
        character_count = len(text_edit.toPlainText())
        for label in text_edit.parent().findChildren(QLabel):
            # if label.text().startswith("Word Count:"):
            #     label.setText()
            if label.text().startswith("Word Count:"):
                label.setText(f"Word Count: {word_count}" + f"Character Count: {character_count}")

        total_word_count = sum([len(text_edit1.toPlainText().split()) for text_edit1 in self.findChildren(QTextEdit)])
        total_Char_count = sum([len(text_edit1.toPlainText()) for text_edit1 in self.findChildren(QTextEdit)])
        self.total_word_count_label.setText(f"Total Word Count: {total_word_count}" + f"Total Word Count: {total_Char_count}")

    def update_text_edit(self, text_edit, button_text):
        self.SHAINELOGCounter +=1
        self.SHAINELOG += str(self.SHAINELOGCounter) + '). ' + button_text + up.LineBreak_1
        current_text = text_edit.toPlainText()
        if current_text:
            current_text += f" {button_text}"
        else:
            current_text = button_text
        text_edit.setText(current_text)





    def update_status_bar(self, button_text):
        status_message = f"SHAINE: {button_text}"
        self.statusBar.showMessage(status_message)

def create_windows6(window_info):
    app = QApplication([])
    windows = []

    for info in window_info:
        window = CustomWindow11(*info)
        windows.append(window)

    app.exec_()


import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QCheckBox, QLabel, QHBoxLayout, QStatusBar, QMenuBar, QMenu, QAction, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
class WebBrowserWindow(CustomWindow11):
    def __init__(self, window_title, window_type, window_size, internal_frames):
        super().__init__(window_title, window_type, window_size, internal_frames)
        self.web_view = None  # Add this line to initialize the web_view attribute

    def setup_ui(self, internal_frames):
        super().setup_ui(internal_frames)

        # Create the URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL")
        self.url_bar.returnPressed.connect(self.load_url)
        self.statusBar.addPermanentWidget(self.url_bar)

        # Create the web view frame
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://www.you.com"))
        self.setCentralWidget(self.web_view)


        # Create the back button
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.web_view.back)
        self.statusBar.addPermanentWidget(back_button)

        # Create the forward button
        forward_button = QPushButton("Forward")
        forward_button.clicked.connect(self.web_view.forward)
        self.statusBar.addPermanentWidget(forward_button)

        # Create the refresh button
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.web_view.reload)
        self.statusBar.addPermanentWidget(refresh_button)



    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.web_view.load(QUrl(url))

# Function to create the web browser window
def create_web_browser_window():
    app = QApplication([])
    web_browser_window = WebBrowserWindow("Web Browser", "Web Browser", "large", [])
    web_browser_window.show()
    app.exec_()

# Create a separate thread to run the web browser window

def WindowSetUp(Type= "GPT", GPTResponse = '', UserEdits = '', System = '', Role= '', Task= '', Format= '', Background= '', Background2= '', Background3= '', Crazy= .5):

    #self.GPTResponse = "Default text 1"
    main_buttons1 = ["Continue", "Cancel", "ReGenerate", "ReGenerate with Edit", "ReWrite Edit" , "Review Prompts",	"SPEAK","ALL", "BIG", "MEDIUM", "SMALL"]
    main_buttons2 = ["Continue", "Cancel", "<", ">", "SAVE ALL", "OG","SPEAK"]


    FrameButtons_User = ["<", ">", "OG", "Save", "Generate", "Regenerate", "Speak", "Speak Input"]
    FrameButtons_GPT = ["<", ">", "OG", "Save", "Generate", "Regenerate with Edit", "Rewrite with User Edits", "Use User Text", "Speak", "Speak Input"]
    FrameButtons2 = ["<", ">", "OG", "Save", "Speak", "Generate"]
    FrameButtons2.append("Optimize Prompt")
    CurrentTest = "Prompt Test1"

    WindowInfo1 = "Test1"
    WindowInfo2 = "Test2"


    if Type== "GPT":
        WindowName = "SHAINE"
        WindowSize = "large"
        internal_frame = [("GPT Response", GPTResponse, FrameButtons_GPT, [], "black"),("USER EDITS", UserEdits, FrameButtons_User, [], "lightgreen")]
        window_type = WindowInfo1
        main_buttons = main_buttons1
        window_info = [
        (WindowName,window_type , WindowSize,main_buttons,["ALL", "BIG", "MEDIUM", "SMALL"], internal_frame)]

    else:
        WindowName = "PROMPTS REVIEW"
        WindowSize = "large"
        window_type = WindowInfo1
        main_buttons = main_buttons2
        internal_frame =[("System", System, FrameButtons2, [], "lightyellow"),
            ("Role", Role, FrameButtons2, [], "lightpink"),
            ("Format", Format,  FrameButtons2, [], "green"),
            ("Task", Task, FrameButtons2, [], "lightgreen"),
            ("Background", Background, FrameButtons2, [], "lightblue"),
            ("Background2", Background2, FrameButtons2, [], "blue"),
            ("Background3", Background3, FrameButtons2, [], "purple"),("Crazy", Crazy, FrameButtons2, [], "yellow")]
        window_info = [(WindowName, window_type,WindowSize ,main_buttons, [],internal_frame)]

    # Create a separate thread to run the GUI
    x = create_windows6(window_info=window_info)
    #gui_thread = threading.Thread(target=create_windows6, args=(window_info,))
    #gui_thread.start()

    return window_info

