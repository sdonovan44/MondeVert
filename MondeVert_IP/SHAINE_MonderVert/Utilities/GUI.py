import tkinter as tk
from tkinter import ttk
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up
from math import ceil
import tkinter as tk
import threading
from tkinter import filedialog, messagebox, Scrollbar
from tkinter import *
import time
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up
from idlelib.tooltip import Hovertip
import os

class GUIWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.RunWindow = True
        self.Colors = ['Dark Orchid', 'Orchid', 'plum', 'Blue Violet', 'Light Pink', 'Deep Pink', 'cherry-blossom-pink',
                       'Dark Magenta', 'Pink',
                       'Misty Rose', 'Medium Violet Red', 'Medium Spring Green', 'Medium Orchid', 'green yellow',
                       'Dark Goldenrod', 'alizarin', 'amaranth', 'amber', 'amethyst', 'apricot', 'aqua', 'aquamarine',
                       'asparagus', 'auburn', 'azure', 'beige', 'bistre',
                       'black', 'blue', 'blue-green', 'blue-violet', 'bondi-blue', 'brass', 'bronze', 'brown', 'buff',
                       'burgundy', 'camouflage-green', 'caput-mortuum',
                       'cardinal', 'carmine', 'carrot-orange', 'celadon', 'cerise', 'cerulean', 'champagne', 'charcoal',
                       'chartreuse', 'cherry-blossom-pink', 'chestnut',
                       'chocolate', 'cinnabar', 'cinnamon', 'cobalt', 'copper', 'coral', 'corn', 'cornflower', 'cream',
                       'crimson', 'cyan', 'dandelion', 'denim', 'ecru', 'emerald',
                       'eggplant', 'falu-red', 'fern-green', 'firebrick', 'flax', 'forest-green', 'french-rose',
                       'fuchsia', 'gamboge', 'gold', 'goldenrod', 'green', 'grey', 'han-purple', 'harlequin',
                       'heliotrope', 'hollywood-cerise', 'indigo', 'ivory', 'jade', 'kelly-green', 'khaki', 'lavender',
                       'lawn-green', 'lemon', 'lemon-chiffon', 'lilac', 'lime', 'lime-green', 'linen', 'magenta',
                       'magnolia', 'malachite', 'maroon', 'mauve', 'midnight-blue', 'mint-green', 'misty-rose',
                       'moss-green', 'mustard', 'myrtle', 'navajo-white', 'navy-blue', 'ochre', 'office-green', 'olive',
                       'olivine', 'orange', 'orchid', 'papaya-whip', 'peach', 'pear', 'periwinkle', 'persimmon',
                       'pine-green', 'pink', 'platinum', 'plum', 'powder-blue', 'puce', 'prussian-blue',
                       'psychedelic-purple', 'pumpkin', 'purple', 'quartz-grey', 'raw-umber', 'razzmatazz', 'red',
                       'robin-egg-blue', 'rose', 'royal-blue', 'royal-purple', 'ruby', 'russet', 'rust',
                       'safety-orange', 'saffron', 'salmon', 'sandy-brown', 'sangria', 'sapphire', 'scarlet',
                       'school-bus-yellow', 'sea-green', 'seashell', 'sepia', 'shamrock-green', 'shocking-pink',
                       'silver', 'sky-blue', 'slate-grey', 'smalt', 'spring-bud', 'spring-green', 'steel-blue', 'tan',
                       'tangerine', 'taupe', 'teal', 'tenné-(tawny)', 'terra-cotta', 'thistle', 'titanium-white',
                       'tomato', 'turquoise', 'tyrian-purple', 'ultramarine', 'van-dyke-brown', 'vermilion', 'violet',
                       'viridian', 'wheat', 'white', 'wisteria', 'yellow', 'zucchini']
        self.Colors_Greens_Blues = ['green yellow', 'aquamarine', 'aqua', 'bondi-blue', 'emerald', 'denim', 'zucchini']

    def GetWordCountsSHAINE(self):
        d = 1
        self.GetUserText(self)

    def WordCount_SHAINE(self):
        try:
            self.GetWordCountsSHAINE
            self.CountCharacters = len(self.Current_PROMTS_ALL)
            self.CountWords = cu.WordCount(self.Current_PROMTS_ALL)

            self.CountCharacters_w_EDIT = len(self.Current_PROMTS_ALL + self.UserEdits)
            self.CountWords_w_EDIT = cu.WordCount(self.Current_PROMTS_ALL + self.UserEdits)

            self.CountCharacters_RESPONSE = len(self.Text)
            self.CountWords_RESPONSE = cu.WordCount(self.Text)

        except:
            dn = 100

    def keyPress(self, event):
        try:
            self.WordCount_SHAINE()

            # self.WordCountField = tk.Text(self.WordCounter, wrap=WORD, )

            if len(self.UserEdits) > 0:
                self.UpdateWordCountField(str(self.CountWords_RESPONSE) + " Words in GPT Response " + str(
                    self.CountCharacters_RESPONSE) + " Characters in GPT Response " + up.LineBreak + str(
                    self.CountWords) + "Words in Prompt " + str(
                    self.CountCharacters) + "Characters in Prompt" + up.LineBreak + str(
                    self.CountWords_w_EDIT) + "Projected  WORDS (In Prompt w.USER EDITs): " + ' Projected Characters: ' + str(
                    self.CountCharacters_w_EDIT))
            else:
                self.UpdateWordCountField(str(self.CountWords_RESPONSE) + " Words in GPT Response " + str(
                    self.CountCharacters_RESPONSE) + "Total Characters in GPT Response " + up.LineBreak + str(
                    self.CountWords) + "Words in Prompt " + str(self.CountCharacters) + " Characters in Prompt ")

            # self.WordCountField.grid( row=3, sticky="nsew")
            CrazyTip = Hovertip(self.WordCountField,
                                'WORD COUNT/CHARACTER COUNT/OTHER KEY STATS, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')

        except:
            dn = 100

    def keyPress2(self, event):
        try:

            self.GetPrompts()

            # self.WordCountField = tk.Text(self.window, wrap=WORD, )
            self.UpdateWordCountField2(Text=str(self.CountWords) + "  Words in Prompt " + str(self.CountCharacters) + " Characters in Prompt ")

            # self.WordCountField.grid( row=3, sticky="nsew")
            CrazyTip = Hovertip(self.WordCountField2,
                                'WORD COUNT/CHARACTER COUNT/OTHER KEY STATS, KEEP AN EYE ON THIS, IF RESULTS ARE WONKY TRY TO GET THIS NUMBER DOWN. ALSO IF ITS TOO LOW, YOU PROBABLY NEED TO ADD MORE INFO TO MAKE THE TOOL WORK PROPER')
        except:
            dn = 100

    def CreateWindow(self,window_title, window_size, main_buttons,main_checkboxes, internal_frames):
        self.WindowClose = False

        self.title(window_title)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f'{width}x{height}')
        #self.geometry(f"{window_size[0]}x{window_size[1]}")
        self.frames = {}
        self.frameslabel = {}
        self.UserResponseProvided = False
        frm_buttons = tk.Frame(self, relief=tk.RAISED, bg=self.Colors[0], pady=2, padx=2, height=44)
        frm_buttons.pack(side='top', fill="x")
        frm_buttons.rowconfigure("all", weight=1, height=44)
        # self.Middle_Screen = tk.Frame( self,relief=tk.RAISED, bg=self.Colors[7], pady=8, padx=8)
        # self.Middle_Screen.pack(ipadx=1600, padx=3, pady=3)
        # self.WordCounter = tk.Frame(self, relief=tk.SUNKEN, bg=self.Colors[4])
        #
        # self.Middle_Screen.columnconfigure("all",weight=10, width=1000, height=250)
        # self.Middle_Screen.rowconfigure("all", weight=10, height=100)
        # self.WordCounter.rowconfigure(0, weight=1)

        self.WindowTitle = window_title
        # Create main buttons
        for idx, button_text in enumerate(main_buttons):
            button = ttk.Button(frm_buttons, text=button_text, command=lambda btn=button_text: self.update_status_bar(btn, "Main_Window", window_title))
            button.grid(row=0, column=idx)

        frm_buttons.grid(row=0, sticky="ns")

        # Calculate frame size
        #frame_width = window_size[0] // ceil(len(internal_frames) / 2)
        #frame_height = window_size[1] // ceil(len(internal_frames) / 2)

        # Create internal frames
        countFrames = 0
        for frame_info in internal_frames:
            countFrames+=1

        if countFrames ==1:
            rows = 1
            cols = 1
        elif countFrames ==2:
            rows = 1
            cols = 2
        elif countFrames >2 and countFrames <6:
            cols = 2
            rows = 2
            if countFrames > 4:
                rows = 3

        elif countFrames < 16 and countFrames > 6:
            cols = 3
            rows = 2
            if countFrames > 6 and countFrames < 10:
                rows = 3
            elif countFrames > 9:
                cols = 4
                if countFrames > 13:
                    rows = 4


        for idx, frame_info in enumerate(internal_frames):
            self.create_internal_frame(idx // 2 + 1, idx % 2, width, height, frame_info)


        # self.icon = tk.PhotoImage(file=r"A:\Amini Amor\SHAINE\Marketing\Logo Work\18.png")
        # self.iconphoto(False, self.icon)

        # self.WordCount_SHAINE()
        # self.WordCountField = tk.Text(self.WordCounter, wrap=WORD)
        # self.UpdateWordCountField( str(self.CountWords_RESPONSE) + " Words in GPT Response " + str(
        #     self.CountCharacters_RESPONSE) + " Characters in GPT Response " + up.LineBreak + str(
        #     self.CountWords) + "Words in Prompt " + str(
        #     self.CountCharacters) + "Characters in Prompt" + up.LineBreak)
        #


        while self.WindowClose ==False :
            # if self.WindowClose == True:
            #     self.quit()
                #self.destroy()
            self.mainloop()


    def create_internal_frame(self, row, column, width, height, frame_info):
        frame_title, frame_text, frame_buttons,frame_checkboxes, frame_color = frame_info
        self.frameslabel[frame_title] = ttk.LabelFrame(self, text=frame_title)
        self.frameslabel[frame_title].grid(row=row, column=column, padx=10, pady=10, sticky='nsew')
        #self.frames[frame_title].config(width=width, height=height)

        # Create text widget
        self.frames[frame_title] = tk.Text(self.frameslabel[frame_title])
        self.frames[frame_title].insert(tk.END, frame_text)
        self.frames[frame_title].pack()

        # Create buttons
        for button_text in frame_buttons:
            button = ttk.Button(self.frameslabel[frame_title], text=button_text, command=lambda btn=button_text: self.update_status_bar(btn,frame_title, self.WindowTitle))
            button.pack(side=tk.LEFT, padx=5)

        #self.frames[frame_title]  = frame





    def update_status_bar(self, button_name, Frame, Window):
        print(f"Button '{button_name}' pressed")
        print(f"Window '{Window}' Impacted")
        print(f"Frame '{Frame}' Impacted")
        status_message = f"SHAINE: {button_name} - {Frame} - {Window}"
        print(status_message)

        #self.statusBar.showMessage(status_message)
        # Call the respective function based on the button name
        if self.UserResponseProvided == False:
            if button_name == "<":
                #self.last_function()

                if "GPT" in Frame.upper():
                    self.ReturnLast()
                elif "PROMPT" in Window.upper():
                    self.RestorePrompt()

            elif button_name == "OG":
                #self.original_function()
                if "GPT" in Frame.upper():
                    self.ReturnOrig()
                elif "PROMPT" in Window.upper():
                    self.RestorePrompt_original()


            elif button_name == "Use User Text":
                self.UseUserText()
                #self.use_user_text_function()
            elif button_name == "Rewrite with User Edits":
                self.ReWriteWithEdit()
                #self.rewrite_with_edits_function()

            elif button_name == "User Edits":
                #self.user_edits_function()
                self.SmallEdit()
            elif button_name == "ReWrite":
                #self.rewrite_function()
                self.ReWrite()
            elif button_name == "Speak":
                #self.speak_function()
                if "PROMPT" in Window.upper():
                    self.Speak2()
                else:
                    if 'GPT' in Frame.upper():
                        self.FINALGPTOUTPUT = self.frames["CHAT GPT"].get(1.0, END)
                        self.Speak(Text= self.FINALGPTOUTPUT)
                    else:
                        self.UserEdits = self.frames["USER EDITS"].get(1.0, END)
                        self.Speak(Text=self.UserEdits)
                    #self.Speak()

            elif button_name == "Continue":
                #self.continue_function()
                if "PROMPT" in Window.upper():
                    self.Continue_Button2()
                else:
                    # print("Frame")
                    # print(Frame)
                    self.Continue_Button()

            elif button_name == "Review Prompts":
                self.ReviewPrompt()
                #self.review_prompt_function()


            elif button_name == "Next":
                self.next_function()
            elif button_name == ">":
                dn = 100
            # elif button_name == "<":
            #     dn = 100
            elif button_name == "Save":
                self.save_function()
            elif button_name == "Generate":
                self.generate_function()
            elif button_name == "Speak Input":
                self.speak_input_function()
            elif button_name == "Review Outlines":
                self.review_outlines_function()
            elif button_name == "Review Story(s)":
                self.review_stories_function()
            elif button_name == "See Full Prompt":
                self.see_full_prompt_function()
            elif button_name == "Prompt History":
                self.prompt_history_function()

            elif button_name == "IGNORE SMALL":
                self.EndUserInputSmall()

            # elif button_name == "MEDIUM":
            #     self.EndUserInputSmall()

            elif button_name == "IGNORE BIG":
                self.EndUserInputMain()
            elif button_name == "IGNORE ALL":
                self.EndUserInput()

            elif button_name == "RESTORE ALL":
                self.RestoreUserInput()







    def RestoreLastUserText(self):

        USERLASTEDIT = self.USERLASTEDIT
        GUIWindow.GetUserText(self)
        GUIWindow.UpdateUserText(self, self.USERLASTEDIT)
        self.USERLASTEDIT = self.UserEdits
        return self.USERLASTEDIT

    def GetUserText(self):

        self.UserEdits = self.frames["USER EDITS"].get(1.0, END)

        print("self.UserEdits")
        print(self.UserEdits)
        return self.UserEdits

    def GetUserResponseMode(self):
        return self.UserResponseMode

    def GetUserResponseMain(self):
        self.UserConfirm = True
        #GUIWindow.MakeWindow(self)
        self.x = self.frames["USER EDITS"].get(1.0, END)

        # I May not want to do this, I may be closing windows I do not want to

        # try:
        #     if self.WindowClose == True:
        #         self.quit()
        #         #self.window.destroy()
        #     if self.WindowClose2 == True:
        #         self.quit()
                #self.window2.destroy()
        # except:
        #     print('Error With Window, continue, maybe look into later')
        return self.x

    def Continue_Button2(self, Mode=0):

        try:

            self.WindowClose2 = True
            self.WindowClose = True

        except:
            dn = 1
        GUIWindow.UserResponse(self, Mode, UIversion=2)

        # self.UserEdits = "0"
        return "0"

    def Continue_Button(self, Mode=0):

        try:
            #self.FINALGPTOUTPUT = self.FrameText["CHAT GPT"].toPlainText()
            Window = self.frames["CHAT GPT"]
            #self.FINALGPTOUTPUT = self.frames["CHAT GPT"].toPlainText()
            self.FINALGPTOUTPUT = self.frames["CHAT GPT"].get(1.0, END)
            # self.FINALGPTOUTPUT = self.FrameText["CHAT GPT"].toPlainText()
            self.WindowClose = True





        except Exception as e:

            print(e)

            print("Error with User Input Process1")
            dn = 1
            self.WindowClose = True



        self.UserResponse( Mode, UIversion=1)

        # self.UserEdits = "0"
        return "0"

    def EndUserInput(self, Mode=5):
        GUIWindow.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "5"
        return "5"

    def RestoreUserInput(self, Mode=50):
        GUIWindow.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "5"
        return "50"

    def EndUserInputSmall(self, Mode=6):
        GUIWindow.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "6"
        return "6"

    def EndUserInputMain(self, Mode=7):
        GUIWindow.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "7"
        return "7"

    def MakeArt(self, Mode=8):
        GUIWindow.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "8"
        return "8"

    def ReviewPrompt(self, Mode=10):
        GUIWindow.UserResponse(self, Mode, UIversion=1)
        # self.UserEdits = "8"
        return "10"

    def ReturnLast(self, Mode=12):
        GUIWindow.UserResponse(self, Mode, UIversion=1)

        # self.UserEdits = "8"
        return "12"

    def ReturnOrig(self, Mode=11):
        GUIWindow.UserResponse(self, Mode, UIversion=1, closeWindow=True)

        # self.UserEdits = "8"
        return "11"

    def UpdateGPTResponse(self, Text):
        # Get the new data from some source
        new_data = "New data"

        # Delete existing content in the Text widget
        # self.Printtxt.delete("1.0", tk.END)
        # Add the new data to the Text widget
        # self.Printtxt.insert(tk.END, Text)
        # print("self.FrameText[title]:")
        # print(self.FrameText[title])

        # self.TE_APP.text_changed.emit(Text, title)
        #self.FrameText[title].setText(Text)
        title = "CHAT GPT"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)


    def UpdateUserText(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        # self.UserInput.delete("1.0", tk.END)
        # Add the new data to the Text widget
        # self.UserInput.insert(tk.END, Text)

        #self.FrameText["USER EDITS"].setText(Text)
        self.FrameText["USER EDITS"].delete("1.0", tk.END)
        self.FrameText["USER EDITS"].insert(tk.END, Text)


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
        #self.UserInput_fld_SYSTEM.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.UserInput_fld_SYSTEM.insert(tk.END, Text)
        #self.FrameText["System"].setText(Text)
        title = "System"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateUserInput_fld_Role(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        #self.UserInput_fld_ROLE.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.UserInput_fld_ROLE.insert(tk.END, Text)
        #self.FrameText["Role"].setText(Text)
        title = "Role"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateUserInput_fld_FORMAT(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        #self.UserInput_fld_FORMAT.delete("1.0", tk.END)
        # Add the new data to the Text widget
        #self.UserInput_fld_FORMAT.insert(tk.END, Text)
        #self.FrameText["Format"].setText(Text)
        title = "Format"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateUserInput_fld_TASK(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        # self.UserInput_fld_TASK.delete("1.0", tk.END)
        # # Add the new data to the Text widget
        # self.UserInput_fld_TASK.insert(tk.END, Text)
        #self.FrameText["Task"].setText(Text)
        title = "Task"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateUserInput_fld_Background(self, Text):
        # Get the new data from some source
        new_data = "New data"
        # Delete existing content in the Text widget
        # self.UserInput_fld_Background.delete("1.0", tk.END)
        # # Add the new data to the Text widget
        # self.UserInput_fld_Background.insert(tk.END, Text)
        #self.FrameText["Background"].setText(Text)
        title = "Background"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateUserInput_fld_Background2(self, Text):
        # Delete existing content in the Text widget
        # self.UserInput_fld_Background2.delete("1.0", tk.END)
        # # Add the new data to the Text widget
        # self.UserInput_fld_Background2.insert(tk.END, Text)
        #self.FrameText["Background2"].setText(Text)
        title = "Background2"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateUserInput_fld_Background3(self, Text):
        # self.UserInput_fld_Background3.delete("1.0", tk.END)
        # self.UserInput_fld_Background3.insert(tk.END, Text)
        #self.FrameText["Background3"].setText(Text)
        title = "Background3"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateUserInput_fld_Version(self, Text):
        # self.UserInput_fld_version.delete("1.0", tk.END)
        # self.UserInput_fld_version.insert(tk.END, Text)
        #self.FrameText["Version"].setText(Text)
        title = "Version"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)


    def UpdateUserInput_fld_Crazy(self, Text):
        #self.UserInput_fld_Crazy.delete("1.0", tk.END)
        #self.FrameText["Crazy"].setText(Text)
        title = "Crazy"
        self.FrameText[title].delete("1.0", tk.END)
        self.FrameText[title].insert(tk.END, Text)

    def UpdateGPTResponseWindow(self, NewGPTResponse, NewCurrentPrompt, NEWUSERLASTEDIT):
        self.UserResponseProvided = False
        GUIWindow.UpdateGPTResponse(self, NewGPTResponse)
        self.Current_PROMTS_ALL = NewCurrentPrompt
        self.USERLASTEDIT = NEWUSERLASTEDIT
        # self.Window.title(NEWWINDOWNAME)

    def UpdatePromptWindow(self, NewSystem, NewRole, NewFormat, NewTask, NewBackground, NewBackground2, NewBackground3,
                           NewCrazy, NewVersion, NewModel):
        self.UserResponseProvided = False
        GUIWindow.UpdateUserInput_fld_System(self, NewSystem)
        GUIWindow.UpdateUserInput_fld_Role(self, NewRole)
        GUIWindow.UpdateUserInput_fld_FORMAT(self, NewFormat)
        GUIWindow.UpdateUserInput_fld_TASK(self, NewTask)
        GUIWindow.UpdateUserInput_fld_Background(self, NewBackground)
        GUIWindow.UpdateUserInput_fld_Background2(self, NewBackground2)
        GUIWindow.UpdateUserInput_fld_Background3(self, NewBackground3)
        GUIWindow.UpdateUserInput_fld_Crazy(self, NewCrazy)
        # TextEdit.UpdateUserInput_fld_Version(self,NewVersion)

    def UpdateWindow(self, Text1='', Text2='', Text3=''):
        if Text != '':
            x = 1

    def GetSpeakText(self):
        return self.Speak_Text

    def Speak(self, Mode=9, Text = ""):

        try:
            try:
                self.Speak_Text = Text
                GUIWindow.UserResponse(self, Mode, UIversion=1, closeWindow=False)
                # threads.append(t)
            except:
                print("Error While trying to read outloud")
        except:
            print("Error While trying to read outloud #2")

        #self.UserEdits = "9"
        return "9"

    def SmallEdit(self, Mode=1):

        #self.UserEdits = self.UserInput.get(1.0, END)
        #self.UserEdits = self.FrameText["USER EDITS"].toPlainText()
        self.UserEdits = self.frames["USER EDITS"].get(1.0, END)
        GUIWindow.UserResponse(self, Mode, UIversion=1, closeWindow=False)

        return "1"

    def ReWriteWithEdit(self, Mode=2):

        #self.UserEdits = self.UserInput.get(1.0, END)
        #self.UserEdits = self.FrameText["USER EDITS"].toPlainText()
        self.UserEdits = self.frames["USER EDITS"].get(1.0, END)
        GUIWindow.UserResponse(self, Mode, UIversion=1, closeWindow=False)

        return "2"

    def ReWrite(self, Mode=3):
        GUIWindow.UserResponse(self, Mode, UIversion=1, closeWindow=False)

        # self.UserEdits = "3"
        return "3"

    def UseUserText(self, Mode=4):
        #self.UserEdits = self.FrameText["USER EDITS"].toPlainText()
        self.UserEdits = self.frames["USER EDITS"].get(1.0, END)
        #might want to change this eventually
        #self.CloseWindow = True
        GUIWindow.UserResponse(self, Mode, UIversion=1, closeWindow=True)

        # self.UserEdits = "4"
        return "4"

        # Decide which numbers not to close window on, for instance, Speak, Review Responses, use prior response,

    def UserResponse(self, Mode, UIversion, closeWindow=True):
        self.UserResponseMode = Mode

        self.WindowClose = True


        if UIversion == 2 and self.UserResponseProvided == False:
            try:
                GUIWindow.GetPrompts(self)  # print(Mode)
                self.UserResponseProvided = True

                try:
                    if self.WindowClose == True:
                        #self.window2.destroy()
                        self.quit()
                        #GUIWindow.closeWindow(self)
                        #self.TE_APP.quit()
                        dn = 100

                        #self.TE_APP.close()
                        #os._exit(1)
                        # self.central_widget.close()
                        #sys.exit()
                except:

                    print("Error Trying to close window")

            except:
                print("Error while trying to pull User Values from Prompt")


        elif UIversion == 1 and self.UserResponseProvided == False:
            try:

                self.UserResponseProvided = True
                try:
                    self.FINALGPTOUTPUT = self.frames["CHAT GPT"].get("1.0", END)
                    self.UserEdits = self.frames["USER EDITS"].get("1.0", END)
                except:
                    dn = 100
                try:
                    if self.WindowClose == True:
                        self.quit()
                        #self.destroy()
                        #self.closeWindow()
                        #self.central_widget.close()

                        #self.TE_APP.quit()
                        dn = 100

                        #self.TE_APP.close()
                        #os._exit(1)
                        #sys.exit()

                except:
                    print("Error Trying to close window")

            except:
                print("Error while trying to pull User Values from Prompt")


        self.CloseWindow = True


        self.UserResponseProvided = True
        if Mode == 0:
            # print("Pass")
            c = 1

        return Mode


    def TriggerCloseWindow(self):
        self.destroy()

    def GetUserResponseProvided(self):
        #print(self.UserResponseProvided)
        return self.UserResponseProvided


    def GetWindowClose(self):
        return self.WindowClose

    def GetWindowClose2(self):
        return self.WindowClose2

    def GetCloseWindow(self):
        return self.CloseWindow


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
        # TextEdit.GetPrompts(self)
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
            self.UserPromptRole = self.frames["System"].get(1.0, END)
            #self.UserPromptSystem = self.FrameText["System"].toPlainText()

            self.UserPromptSystem1 = "System: " + self.UserPromptSystem
        except:
            print('Error Getting User prompt System')

        try:
            self.UserPromptRole = self.frames["Role"].get(1.0, END)

            #self.UserPromptRole = self.FrameText["Role"].toPlainText()
            self.UserPromptRole1 = "Role: " + self.UserPromptRole
        except:
            print('Error Getting User prompt Role')

        try:
            self.UserPromptRole = self.frames["Format"].get(1.0, END)
            #self.UserPromptFormat = self.FrameText["Format"].toPlainText()
            self.UserPromptFormat1 = "Format: " + self.UserPromptFormat
        except:
            print('Error Getting User prompt Format')

        try:

            self.UserPromptRole = self.frames["Task"].get(1.0, END)
            #self.UserPromptTask = self.FrameText["Task"].toPlainText()
            self.UserPromptTask1 = "Task: " + self.UserPromptTask
        except:
            print('Error Getting User prompt Task')

        try:


            self.UserPromptRole = self.frames["Background"].get(1.0, END)
            #self.UserPromptBackground = self.FrameText["Background"].toPlainText()
            self.UserPromptBackground1 = "Background : " + self.UserPromptBackground
        except:
            print('Error Getting User prompt Background')

        try:

            self.UserPromptRole = self.frames["Background2"].get(1.0, END)
            #self.UserPromptBackground2 = self.FrameText["Background2"].toPlainText()
            self.UserPromptBackground21 = "Background 2: " + self.UserPromptBackground2
        except:
            print('Error Getting User prompt Background2')

        try:

            self.UserPromptRole = self.frames["Background3"].get(1.0, END)
            #self.UserPromptBackground3 = self.FrameText["Background3"].toPlainText()
            self.UserPromptBackground31 = "Background 3: " + self.UserPromptBackground3
        except:
            print('Error Getting User prompt Background3')

        try:
            # self.UserPromptCrazy = self.UserInput_fld_Crazy.get(1.0, END)

            self.UserPromptRole = self.frames["Crazy"].get(1.0, END)
            self.UserPromptCrazy1 = "Crazy: " + self.UserPromptCrazy

        except:
            print('Error Getting User prompt Crazy')



        self.Full_User_Prompt2 = self.UserPromptSystem + self.UserPromptRole + self.UserPromptFormat + self.UserPromptTask + self.UserPromptBackground + self.UserPromptBackground2 + self.UserPromptBackground3

        self.Full_User_Prompt = self.UserPromptSystem1 + self.UserPromptRole1 + self.UserPromptFormat1 + self.UserPromptTask1 + self.UserPromptBackground1 + self.UserPromptBackground21 + self.UserPromptBackground31

        self.CountCharacters = len(self.Full_User_Prompt2)
        self.CountWords = cu.WordCount(self.Full_User_Prompt2)

    def UpdatePrompts1(self, Mode=44):
        d = 1
        # TextEdit.GetPrompts(self)
        self.WindowClose2 = True
        GUIWindow.UserResponse(self, Mode, UIversion=2)
        # self.UserEdits = "8"
        return "44"

    def RestorePrompt_original(self, Mode=14):

        GUIWindow.UserResponse(self, Mode, UIversion=2)

        return "14"

    def RestorePrompt(self, Mode=13):

        GUIWindow.UserResponse(self, Mode, UIversion=2)

        return "13"

    def OPTIMIZEPROMPT(self, Mode=2002):

        GUIWindow.UserResponse(self, Mode, UIversion=2)

        return "2002"

    def ChangeVersion(self, Mode=2000):

        GUIWindow.UserResponse(self, Mode, UIversion=2)
        # self.version

        return 2000

    def Speak2(self, Mode=9, Text= ''):
        try:
            try:
                try:
                    GUIWindow.GetPrompts(self)
                    self.Speak_Text = self.Full_User_Prompt
                    GUIWindow.UserResponse(self, Mode, UIversion=2)
                    #t = threading.Thread(target=cu.speak, args=(Text,)).start()
                    # threads.append(t)
                except:
                    print("Error While trying to read outloud")
            except:
                print("Error While trying to read outloud #2")
        except:
            print("Error While trying to read outloud #3")

        self.UserEdits = "9"
        return "9"

# if __name__ == "__main__":
#     window_title = "Dynamic GUI"
#     window_size = (600, 400)
#     main_buttons = ["Button 1", "Button 2", "Continue"]
#     internal_frames = [
#         ("Internal Frame 1", "Some text for Frame 1", ["Frame 1 Button 1", "Frame 1 Button 2"], "lightblue"),
#         ("Internal Frame 2", "Some text for Frame 2", ["Frame 2 Button 1", "Frame 2 Button 2"], "lightgreen")
#     ]
#
#     GUI = GUIWindow(window_title, window_size, main_buttons, internal_frames)
#     GUI.mainloop()
