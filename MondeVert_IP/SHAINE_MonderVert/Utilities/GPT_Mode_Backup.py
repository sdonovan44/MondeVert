import datetime
import sys
from pathlib import Path, PureWindowsPath

from MondeVert_IP.SHAINE_MonderVert.Utilities import TextEdit as TextEdit
import platform
import pandas as pd
global Record
from  MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Wedding_Prompts as WeddingP
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Social_Media_SHAINE as sms, Comedy_Wizard as CW,Music_Wizard as MW, Music_Lyrics as ML, Music_Maker as MM
from secrets import randbelow
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Long_User_Prompts as lup, User_Prefs as up,Poetry_Wizard as PW, SuperSHAINE_WIZARD  as SSW,\
    Stories_For_Audio_Files as SAF, StoryMode_Wizard as StoryMode, ReWrites as RW, StoryPrompts as SP,Comedy_Ideas as CI
from threading import Event
from gingerit.gingerit import GingerIt
import numpy
import time
import re
#from MondeVert_IP.SHAINE_MonderVert.Testing_Files import AWS_Speech_Test  as AWS
# from exceptions import PendingDeprecationWarning
Record = ''
#import urllib2
import webbrowser
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu, ShakesBot as s
from MondeVert_IP.SHAINE_MonderVert import Story as SHAINE
import platform
import subprocess
import requests
import random
import string
import openai
import pyttsx3
# Import the speech recognition library
from dotenv import load_dotenv
from MondeVert_IP.SHAINE_MonderVert.Utilities.DoNotCommit import API_Key
import threading
import shutil
import os
import MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS.StoryOutlines  as ShaneOriginals
from MondeVert_IP.SHAINE_MonderVert.Utilities import TextEdit as TextEdit

from multiprocessing import Process
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QStatusBar, QTextEdit, QCheckBox,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication



class GPT_Mode():
    def __init__(self, IDEA = '' ,UserConfirm=False, ConfirmInput=False, UserMode='UI', Mode='MVAA', Writer='',
                 UserInputs_Config='AI Only', OutputTypes=["Play", "Novel", "ScreenPlay"], voice=4, Logic_AI=0,
                 language_settings=1, Chunk_Limit=777, SavePath=up.AI_AudioBook_Path, Writer_Style='', Artist='',
                 Artist_Style='', Story_Type='ScreenPlay', Seasons=1, Episodes=3, Books='', Acts='', Scenes='',
                 Movies='', Text_Output_Config=[''], IDEA_Source='AI', Output_Audio_Config=''):
        self.UserPrompts = ''
        self.Full_Transcript = ''
        self.Full_Story = ''
        self.UserPromptsCount = 0
        self.Prompts_System = []
        self.Prompts_Role = []
        self.Prompts_Format = []
        self.Prompts_Task = []
        self.Prompts_Background = []
        self.Prompts_Background2 = []
        self.Prompts_Background3 = []
        self.Prompts_Crazy= []
        self.Prompts_Version = []
        self.Prompts_Model = []
        self.GPT_Responses = []
        self.Current_GPTResponse = ''
        self.SaveTranscript= True
        self.current_time1 = datetime.datetime.now()
        self.current_time = self.current_time1.strftime('%m-%d-%Y_%H.%M')
        self.Speak = False
        self.EDIT = ''
        self.SmallPromptUser = ''
        self.MainPromptUser = ''
        self.UserConfirm = ''
        self.CurrentWindowName = ''

    def Basic_GPT_Query(self,   Line2_Role  , Line3_Format ,Line4_Task ,Full_Transcript= '',FULL_Story = '',UserPrompts = '',UserPromptsCount = '',Big = False ,Background = '' ,Background2 = '', Background3 = '' ,Model = "gpt-3.5-turbo" ,upgradeLimit = 3000 ,Special = '' ,Line1_System_Rule = SP.System, crazy = .5, Subject= '', Outline = '', Allowed_Fails = 8, SaveFile = False ,MakeArt = False, Mode = 'SHAINE SAYS', SavePath= up.AI_AudioBook_Path, FileName= 'MONDEVERT PRESENTS - A No Named Story', User_Confirm = False, WINDOWNAME = "SHAINE Basic - ", ReviewPrompts = False,  version = 1, Retry= True,UserMode='UI', CurrentTime= "", Test = False)  :  # use this to create art style for the work
        Test = True

        self.UserPrompts = UserPrompts
        self.Full_Transcript = Full_Transcript
        self.Full_Story = FULL_Story
        self.UserPromptsCount = UserPromptsCount

        self.PermanentSetPrompt = False
        ReviewPrompts_Original = ReviewPrompts
        self.UserMode = UserMode
        if CurrentTime!= '':
            self.current_time = CurrentTime

        if SavePath != '':
            self.SavePath = SavePath

        if FileName != '':
            self.FileName = FileName

        if Subject != '':
            Line2_Role = Line2_Role + """Your role and subject matter expertise should fit the following Subject and or style and mood in the {Text} provided by the user Text:###""" + Subject + """###"""


        if Retry == True:
            self.OriginalSystem = Line1_System_Rule
            self.OriginalRole = Line2_Role
            self.OriginalFormat = Line3_Format
            self.OriginalTask = Line4_Task
            self.OriginalBackground = Background
            self.OriginalBackground2 = Background2
            self.OriginalBackground3 = Background3
            self.Original_crazy= crazy
            self.Originalversion = version
            self.OriginalModel = Model
            self.OriginalWindowName = WINDOWNAME

        self.CurrentSystem = Line1_System_Rule
        self.CurrentRole = Line2_Role
        self.CurrentFormat = Line3_Format
        self.CurrentTask = Line4_Task
        self.CurrentBackground = Background
        self.CurrentBackground2 = Background2
        self.CurrentBackground3 = Background3
        self.Current_crazy = crazy
        self.Currentversion = version
        self.CurrentModel = Model
        self.CurrentWindowName = WINDOWNAME
        self.FULLPROMPTONLY = self.CurrentSystem + self.CurrentRole + self.CurrentFormat + self.CurrentTask +self.CurrentBackground + self.CurrentBackground2 + self.CurrentBackground3

        self.Prompts_System.append(Line1_System_Rule)
        self.Prompts_Role.append(Line2_Role)
        self.Prompts_Format.append(Line3_Format)
        self.Prompts_Task.append(Line4_Task)
        self.Prompts_Background3.append(Background)
        self.Prompts_Background2.append(Background2)
        self.Prompts_Background3.append(Background3)
        self.Prompts_Crazy.append(crazy)
        self.Prompts_Version.append(version)
        self.Prompts_Model.append(Model)




        TryCount = 0
        KeepGoing = False
        KillSwitch = 0
        while ((KeepGoing == False and KillSwitch < Allowed_Fails ) or self.Current_GPTResponse ==''):
            TryCount += 1
            try:

                if ReviewPrompts == True or ReviewPrompts_Original == True:
                    GPT_Mode.GPT_Confirm_Prompts(self, System=self.CurrentSystem, Role=self.CurrentRole,
                                              Format=self.CurrentFormat, Task=self.CurrentTask,
                                              Background=self.CurrentBackground, Background2=self.CurrentBackground2,
                                              Background3=self.CurrentBackground3, User_Confirm=User_Confirm,
                                              crazy=self.Current_crazy, TryCount=TryCount,
                                              WINDOWNAME="CONFIRM CHAT GPT PROMPTS - " + self.CurrentWindowName,
                                              version=self.Currentversion, Model=self.CurrentModel)

                if TryCount > 1:
                    GPT_Mode.SaveLastGPTResponse(self, GPT_Response=self.Current_GPTResponse)
                    GPT_Mode.SaveLast_Prompt(self, System=self.CurrentSystem, Role=self.CurrentRole, Format=self.CurrentFormat,
                                          Task=self.CurrentTask, Background=self.CurrentBackground,
                                          Background2=self.CurrentBackground2, Background3=self.CurrentBackground3,
                                          crazy=self.Current_crazy, version=self.Currentversion, Model=self.CurrentModel)

                self.Full_User_Prompt = """User Inputs to Chat GPT: 
                    1). System:  """ + self.CurrentSystem + up.LineBreak + """
                    2).Role: """ + self.CurrentRole + up.LineBreak + """
                    3). Format: """ + self.CurrentFormat + up.LineBreak + """
                    4).Task: """ + self.CurrentTask + up.LineBreak + """
                    Background (If Any Provided): """ + self.CurrentBackground + up.LineBreak + """
                    Additional Background: """ + self.CurrentBackground2 + self.CurrentBackground3 + up.LineBreak + """
                    Crazy:""" + str(self.Current_crazy) + up.LineBreak + "Model: " + self.CurrentModel + up.LineBreak + "Version: " + str(self.Currentversion)

                if version == 2:
                    self.NewSystem = cu.Version2GPTSetUp(Format=self.CurrentFormat, System=self.CurrentSystem,
                                                         Role=self.CurrentRole,
                                                         Background=self.CurrentBackground,
                                                         Background3=self.CurrentBackground3,
                                                         Background2=self.CurrentBackground2)
                    self.Full_User_Prompt = """User Inputs to Chat GPT: 
                        System: """ + self.NewSystem + """
                        USER: """ + self.CurrentTask

                if len(self.Full_User_Prompt) > upgradeLimit:
                    self.CurrentModel = "gpt-3.5-turbo-16k-0613"
                elif len(self.Full_User_Prompt) < upgradeLimit:
                    self.CurrentModel = "gpt-3.5-turbo"

                if Big == True:
                    self.CurrentModel = "gpt-3.5-turbo-16k-0613"

                if Test ==False:
                    self.Current_GPTResponse = cu.ASKGPT(System=self.CurrentSystem, Role=self.CurrentRole,
                                                     Format=self.CurrentFormat, Task=self.CurrentTask,
                                                     Background=self.CurrentBackground, Background2=self.CurrentBackground2,
                                                     Background3=self.CurrentBackground3, crazy=self.Current_crazy,
                                                     Model=self.CurrentModel, version=self.Currentversion)
                else: self.Current_GPTResponse = "Shane Testing"

            except:
                d = 1


            self.GPT_Responses.append(self.Current_GPTResponse)

                # GPT_Mode.SaveOriginalGPTResponse(self, GPT_Response=self.Current_GPTResponse)
            try:

                if TryCount == 1:
                    self.Original_GPTResponse = self.Current_GPTResponse

                self.UserPromptsCount += 1

                self.UserPrompts += 'User Input #' + str(self.UserPromptsCount)

                self.UserPrompts += self.Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2
                self.Full_Transcript += 'User Input #' + str(
                    self.UserPromptsCount) + self.Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2
                self.Full_Story += up.breakupOutput + "****Original GPT Response****" + self.Current_GPTResponse
                self.Full_Transcript += up.breakupOutput + "****Original GPT Response****" + up.breakupOutput + self.Current_GPTResponse

                if User_Confirm == True:
                    KeepGoing = GPT_Mode.GPT_UserInput_Confirm_Tool(self, GPT_Response=self.Current_GPTResponse,
                                                                 System=self.CurrentSystem, Role=self.CurrentRole,
                                                                 Format=self.CurrentFormat, Task=self.CurrentTask,
                                                                 Background=self.CurrentBackground,
                                                                 Background2=self.CurrentBackground2,
                                                                 Background3=self.CurrentBackground3,
                                                                 crazy=self.Current_crazy, TryCount=TryCount,
                                                                 UserConfirm=User_Confirm, version=self.Currentversion,
                                                                 WINDOWNAME=self.CurrentWindowName)


                else:
                    self.Full_Story += "Final Text used for Response: " + up.LineBreak + self.Current_GPTResponse + up.LineBreak + up.breakupOutput2
                    print("Used the following Text  for Response: " + + up.LineBreak + self.Current_GPTResponse)
                    KeepGoing = True




            except:
                print(
                    ' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                KillSwitch += 1
                print(self.Full_User_Prompt)
                # ReviewPrompts = True

                # as written this does not run but if I got rid of +1 it could
                if KillSwitch == Allowed_Fails + 1:
                    print('could not create a writer persona, redoing it now')
                    if User_Confirm == True:
                        GPT_Mode.GPT_Confirm_Prompts(self, System=self.CurrentSystem, Role=self.CurrentRole,
                                                  Format=self.CurrentFormat, Task=self.CurrentTask,
                                                  Background=self.CurrentBackground, Background2=self.CurrentBackground2,
                                                  Background3=self.CurrentBackground3, crazy=self.Current_crazy,
                                                  Model=self.CurrentModel)
                    if Retry == True:
                        self.Last_GPTResult = self.Current_GPTResponse
                        self.Current_GPTResponse = GPT_Mode.Basic_GPT_Query(self, Line2_Role='You are a skilled writer',
                                                             Line3_Format=Line3_Format, Line4_Task=Line4_Task,
                                                             Line1_System_Rule=self.systemPrompt, Retry=False,
                                                             Allowed_Fails=3, WINDOWNAME="FAILED SEVERAL TIMES, NEEDS HELP OR WILL FAIL" +  WINDOWNAME)
                        self.GPT_Responses.append(self.Current_GPTResponse)

                    continue

            # print(up.breakupOutput)

        if self.SaveTranscript == True:
            try:
                cu.SaveCSV(Text=WINDOWNAME + self.Full_Story, SavePath=SavePath,
                           Title=self.FileName + ' All Responses Transcript (no Prompts)')
                cu.SaveCSV(Text=WINDOWNAME + self.Full_Transcript, SavePath=SavePath,
                           Title=self.FileName + ' All Responses and prompts')

            except:
                print("could not save files")

        Title = Mode + '_' + self.current_time
        if SaveFile == True:
            SaveText = self.current_time + up.breakupOutput2 + self.UserPrompts + up.breakupOutput2 + 'SHAINE SAYS: ' + GPT_Response
            print(SaveText)
            cu.SaveCSV(Text=SaveText, SavePath=SavePath, Title=Title)

        try:
            if MakeArt == True:
                config = self.Art_Type_Config + StoryMode.artDetailsPrompt
                GPT_Response1 = self.Current_GPTResponse[:3000]
                AP = GPT_Mode.GPTArt2(self, User_Subject=GPT_Response1, ArtFormat=StoryMode.artDetailsFormat,
                                   prompt=config)
                ArtPrompt = self.Art_Style_For_Story + AP

                print(ArtPrompt)
                originalFilepath = GPT_Mode.makeArt(self, Prompt=ArtPrompt)
                if self.Mode.upper() not in str(SavePath).upper():
                    PicNewPath1 = Path(PureWindowsPath(SavePath, self.Mode))
                    cu.Check_Folder_Exists(PicNewPath1)
                else:
                    PicNewPath1 = self.SavePath
                PicNewPath = Path(PureWindowsPath(PicNewPath1, self.FileName + '.png'))
                shutil.copyfile(originalFilepath, PicNewPath)
        except:
            print("Could not move art to new folder")

        return self.Current_GPTResponse


    def SaveLast_Prompt(self, System, Role, Format, Task, Background, Background2, Background3, crazy=.5, Model='',
                        version=''):
        d = 100
        self.LastSystem = System
        self.LastRole = Role
        self.LastFormat = Format
        self.LastTask = Task
        self.LastBackground = Background
        self.LastBackground2 = Background2
        self.LastBackground3 = Background3
        self.LastCrazy = crazy
        self.LastModel = Model
        self.LastVersion = version






    # This is redundant/not needed
    # def SaveOriginal_Prompt(self, GPT_Response, System, Role, Format, Task, Background, Background2, Background3, crazy=.5,
    #                         Model='', version=''):
    #     self.OriginalSystem = System
    #     self.OriginalRole = Role
    #     self.OriginalFormat = Format
    #     self.OriginalTask = Task
    #     self.OriginalBackground = Background
    #     self.OriginalBackground2 = Background2
    #     self.OriginalBackground3 = Background3
    #     self.Original_crazy = crazy
    #     self.OriginalModel = Model
    #     self.Originalversion = version


    def SaveCurrentGPTResponse(self, GPT_Response):
        self.Current_GPTResponse = GPT_Response


    def SaveLastGPTResponse(self, GPT_Response, crazy=.5):
        self.Last_GPTResult = GPT_Response


    def SaveOriginalGPTResponse(self, GPT_Response, crazy=.5):
        self.Original_GPTResponse = GPT_Response


    def Get_Text_Values_From_Query(self):
        d = 1



    def GPT_Confirm_Prompts(self, TryCount=0, WINDOWNAME="CHAT GPT USER REVIEW PROMPTS"):
        query = ''
        UserResponseProvided = False
        KeepGoing = False
        FirstResponse = True
        WindowOpen = False
        #self.TE = TextEdit.TextEdit(UserConfirm=True)
        # query = self.TE2.MakeWindow2(Text=self.Full_User_Prompt, UserConfirm=True,
        #                              WindowName=self.CurrentWindowName + str(
        #                                  TryCount) + "GPT Prompt Reviewer - V1", System=self.CurrentSystem,
        #                              Role=self.CurrentRole, Format=self.CurrentFormat, Task=self.CurrentTask,
        #                              Background=self.CurrentBackground, Background2=self.CurrentBackground2,
        #                              Background3=self.CurrentBackground3, crazy=self.Current_crazy,
        #                              version=self.Currentversion, Model=self.CurrentModel)
        # t = threading.Thread(target=self.TE.MakeWindow2, args=(self.CurrentSystem, self.CurrentRole,self.CurrentFormat,self.CurrentTask,self.CurrentBackground,self.CurrentBackground2,self.CurrentBackground3,self.Current_crazy,self.Currentversion,self.CurrentModel, True, self.CurrentWindowName + "Confirm Prompts"))
        # t.start()

        while KeepGoing == False:

            try:
                UserMode2 = -1



                if self.Currentversion == 1:


                    #note in current set up you would have the creation outside while loop, you would update the values here so each time it runs through bam!
                    # , and also you would want to set up a loop that is looking for where RunCode ==True, and you would be running a get from the window constantly looking for the ok to move forward with code
                    #moving forward happens anytime the user presses the button
                    #
                        WindowOpen = False
                        if UserResponseProvided == True and WindowOpen == True:
                            UserResponseProvided = False
                            self.TE2.UpdatePromptWindow(self.CurrentSystem, self.CurrentRole, self.CurrentFormat,
                                                   self.CurrentTask, self.CurrentBackground, self.CurrentBackground2,
                                                   self.CurrentBackground3, self.Current_crazy, self.Currentversion,
                                                   self.CurrentModel)

                        elif WindowOpen == False:
                            try:
                                t.join()
                            except:
                                dn = 100
                            UserResponseProvided = False

                            self.TE2 = TextEdit.CustomWindow11()
                            WindowInfo = GPT_Mode.WindowSetUp(Type="Prompts", System=self.CurrentSystem,Role= self.CurrentRole,Format= self.CurrentFormat, Task=self.CurrentTask,
                            Background=self.CurrentBackground, Background2=self.CurrentBackground2, Background3=self.CurrentBackground3, Crazy=self.Current_crazy)

                            t = threading.Thread(target=self.TE2.CreateWindow, args=(
                            self.WindowName, self.window_type, self.WindowSize, self.main_buttons, self.main_checkboxes,
                            self.internal_frame))
                            t.start()
                            # t = threading.Thread(target=self.TE2.MakeWindow, args=( self.WindowName, self.window_type, self.WindowSize, self.main_buttons,self.main_checkboxes,self.internal_frame))
                            # t.start()


                        #UserResponseProvided = False


                        while UserResponseProvided ==False :
                                        UserResponseProvided = self.TE2.GetUserResponseProvided()
                                        WindowOpen = True





                else:

                    print ("Error, not running other version yet")
                    # self.NewSystem = cu.Version2GPTSetUp(Format=self.CurrentFormat, System=self.CurrentSystem,
                    #                                      Role=self.CurrentRole,
                    #                                      Background=self.CurrentBackground,
                    #                                      Background3=self.CurrentBackground3,
                    #                                      Background2=self.CurrentBackground2)
                    #
                    # self.Full_User_Prompt = """User Inputs to Chat GPT:
                    #                         System: """ + self.NewSystem + """
                    #                         USER: """ + self.CurrentTask
                    #
                    # self.TE3 = TextEdit.TextEdit(UserConfirm=True)
                    # query = self.TE3.MakeWindow3(Text=self.Full_User_Prompt, UserConfirm=True,
                    #                             WindowName=self.CurrentWindowName + 'Try: ' + str(
                    #                                 TryCount) + " - GPT Prompt Reviewer - V2 ",
                    #                             System=self.NewSystem, Task=self.CurrentTask, crazy=self.Current_crazy,
                    #                             version=self.Currentversion, Model=self.CurrentModel)

                UserMode2 = -1
                UserMode2 = self.TE2.GetUserResponseMode()
                # query = self.TE.GetUserText()
                print("UserMode2:")
                print(UserMode2)

                # TE = TextEdit.TextEdit()
                # UserMode2 = -1
                # UserMode2 = TE.MakeWindow2(Text=self.Full_User_Prompt, UserConfirm=True, System=System, Role= Role, Format=Format, Task=Task, Background=Background, Background2= Background2, Background3=Background3, crazy=crazy, )
                # query = TE.GetUserText()

                # if user presses continue it means no change keep going

                if UserMode2 == 0:
                    KeepGoing = True
                    ReviewPrompts = False
                    t.join()



                # Write code for what happens to pull values from User input and set temporarily
                #Note for 44 I am setting the value and then moving forward for 2002 I am Optimizing the prompt

                elif UserMode2 == 44 or UserMode2 == 2002:
                    if UserMode2 == 44:
                        KeepGoing = True
                        WindowOpen = False
                        t.join()

                    ReviewPrompts = False

                    # note rather than original version we want to pull the values from Class/Text Edit
                    # this is not ready yet need to reevaluate

                    try:
                        Prompts1 = []
                        Prompts2 = []
                        self.LastSystem = self.CurrentSystem
                        self.LastFormat = self.CurrentFormat
                        self.LastTask = self.CurrentTask
                        self.LastRole = self.CurrentRole
                        self.LastBackground = self.CurrentBackground
                        self.LastBackground2 = self.CurrentBackground2
                        self.LastBackground3 = self.CurrentBackground3
                        self.LastCrazy = self.Current_crazy
                        self.LastVersion = self.Currentversion
                        self.LastModel = self.CurrentModel

                        self.Prompts_System.append(self.CurrentSystem)
                        self.Prompts_Role.append( self.CurrentRole)
                        self.Prompts_Format.append(self.CurrentFormat)
                        self.Prompts_Task.append(self.CurrentTask)
                        self.Prompts_Background3.append(self.CurrentBackground)
                        self.Prompts_Background2.append(self.CurrentBackground2)
                        self.Prompts_Background3.append(self.CurrentBackground3)
                        self.Prompts_Crazy.append(self.Current_crazy)
                        self.Prompts_Version.append(self.Currentversion)
                        self.Prompts_Model.append(self.CurrentModel)


                    except:

                        d = 10

                    if self.Currentversion == 2:

                        self.CurrentFormat = ''
                        self.CurrentRole = ''
                        self.CurrentBackground = ''
                        self.CurrentBackground2 = ''
                        self.CurrentBackground3 = ''

                        try:
                            CurrentSystem = self.TE2.Get_System()
                            self.LastSystem = self.CurrentSystem
                            if CurrentSystem != '':
                                self.CurrentSystem = CurrentSystem
                                Prompts1.append(self.CurrentSystem)
                                Prompts2.append(Prompts2.append(
                                    "Please refer to the ChatGPT Request Code provided as Reference, You Are currently updating the portion where it says 'NewSystem' within the openai.ChatCompletion.create function under the messages parameter. Make the best possible query based on this.   Note: You are using Model = " + self.CurrentModel + "CHAT GPT PROMPT BEING REVIEWED: {Role: 'system',content: " + self.CurrentTask))
                        except:
                            c = 1

                        try:
                            CurrentTask = self.TE2.Get_Task()
                            self.LastTask = self.CurrentTask
                            if CurrentTask != '':
                                self.CurrentTask = CurrentTask
                                Prompts1.append(self.CurrentTask)
                                Prompts2.append(
                                    "Please refer to the ChatGPT Request Code provided as Reference, You Are currently updating the portion where it says 'USER' within the openai.ChatCompletion.create function under the messages parameter. Make the best possible query based on this.   Note: You are using Model = " + self.CurrentModel + "CHAT GPT PROMPT BEING REVIEWED: {Role: 'user',content: " + self.CurrentTask)
                        except:
                            c = 1

                        try:
                            crazy = self.TE2.Get_Crazy()

                        except:
                            c = 1

                        try:
                            if cu.check_numeric(crazy) and crazy != '':
                                self.crazy = crazy

                        except:
                            c = 1

                        try:
                            Currentversion = self.TE2.Get_version()
                            if Currentversion != '':
                                self.Currentversion = Currentversion
                                Prompts1.append(self.CurrentSystem)
                                Prompts2.append("System")

                        except:
                            c = 1


                    else:

                        try:
                            CurrentSystem = self.TE2.Get_System()
                            self.LastSystem = self.CurrentSystem
                            if CurrentSystem != '':
                                self.CurrentSystem = CurrentSystem
                        except:
                            c = 1
                        try:
                            CurrentRole = self.TE2.Get_Role()
                            self.LastSystem = self.CurrentSystem
                            if CurrentRole != '':
                                self.CurrentRole = CurrentRole
                        except:
                            c = 1
                        try:
                            CurrentFormat = self.TE2.Get_Format()
                            self.LastFormat = self.CurrentFormat
                            if CurrentFormat != '':
                                self.CurrentFormat = CurrentFormat
                        except:
                            c = 1

                        try:
                            CurrentTask = self.TE2.Get_Task()
                            self.LastTask = self.CurrentTask

                            if CurrentTask != '':
                                self.CurrentTask = CurrentTask
                        except:
                            c = 1

                        try:
                            CurrentBackground = self.TE2.Get_Background()
                            self.LastBackground = self.CurrentBackground

                            if CurrentBackground != '':
                                self.CurrentBackground = CurrentBackground
                        except:
                            c = 1

                        try:
                            CurrentBackground2 = self.TE2.Get_Background2()
                            self.LastBackground2 = self.CurrentBackground2

                            if CurrentBackground2 != '':
                                self.CurrentBackground2 = CurrentBackground2
                        except:
                            c = 1
                        try:
                            CurrentBackground3 = self.TE2.Get_Background3()
                            self.LastBackground3 = self.CurrentBackground3
                            if CurrentBackground3 != '':
                                self.CurrentBackground3 = CurrentBackground3
                        except:
                            c = 1

                        try:
                            crazy = self.TE2.Get_Crazy()
                            self.LastCrazy = self.Current_crazy
                        except:
                            c = 1

                        try:
                            if cu.check_numeric(crazy) and crazy != '':
                                self.Current_crazy = crazy

                        except:
                            c = 1

                        try:
                            Currentversion = self.TE2.Get_version()
                            self.LastVersion = self.Currentversion
                            if Currentversion != '':
                                self.Currentversion = Currentversion

                        except:
                            c = 1

                    self.Full_User_Prompt = """User Inputs to Chat GPT: 
                        1). System:  """ + self.CurrentSystem + up.LineBreak + """
                        2).Role: """ + self.CurrentRole + up.LineBreak + """
                        3). Format: """ + self.CurrentFormat + up.LineBreak + """
                        4).Task: """ + self.CurrentTask + up.LineBreak + """
                        Background (If Any Provided): """ + self.CurrentBackground + up.LineBreak + """
                        Additional Background: """ + self.CurrentBackground2 + self.CurrentBackground3 + up.LineBreak + """
                        Crazy:""" + str(
                        self.Current_crazy) + up.LineBreak + "Model: " + self.CurrentModel + up.LineBreak + "Version: " + str(
                        self.Currentversion)

                    self.UserPrompts += up.breakupOutput + "****Provided New Prompt for Chat GPT Request:" + self.Full_User_Prompt + up.breakupOutput
                    self.Full_Transcript += up.breakupOutput + "****Provided New Prompt for Chat GPT Request:" + self.Full_User_Prompt + up.breakupOutput





                        # This is the mode for optimizing prompts
                        # Get GPT To give System Prompt
                        # Get GPT To give USER PROMPT
                    if UserMode2 == 2002:
                        if self.Currentversion == 1:
                            print("Error not currently set up to optimize for Version 1")

                        else:
                            # P1_length = len(Prompts1)
                            #
                            # for i in range (0,P1_length)
                            try:

                                self.LastWindowName = self.CurrentWindowName

                                SystemQuestion = GPT_Mode()

                                self.CurrentTask = SystemQuestion.Basic_GPT_Query(System=SSW.PROMPTFIX_System,
                                                                         Line2_Role=SSW.PROMPTFIX_ROLE,
                                                                         Line3_Format=SSW.PROMPTFIX_Format,
                                                                         Background=SSW.ChatGPT_CodeRef,
                                                                         Line4_Task=SSW.PROMPTFIX_USER + """Note, You are providing a revised version of  'USER' values provided to you in the following code where I show you how I am using the messages arg while calling the 'openai.ChatCompletion.create' function (see code for reference) Here is the portion of code you are to review and provide with an updated value for the USER text    messages = [{"role": "system", "content": """ + self.CurrentSystem + """}),
                                                                             {"role": "user", "content":""" + self.CurrentSystem + """}]""",
                                                                         crazy=.5,
                                                                         WINDOWNAME='PROMPT Optimizer - Task' + self.CurrentWindowName)
                                self.CurrentSystem = SystemQuestion.Basic_GPT_Query(System=SSW.PROMPTFIX_System,
                                                                           Line2_Role=SSW.PROMPTFIX_ROLE,
                                                                           Line3_Format=SSW.PROMPTFIX_Format,
                                                                           Background=SSW.ChatGPT_CodeRef,
                                                                           Line4_Task=SSW.PROMPTFIX_USER + """Note, You are providing a revised version of  'NewSystem' values provided to you in the following code where I show you how I am using the messages arg while calling the 'openai.ChatCompletion.create' function (see code for reference) Here is the portion of code you are to review and provide with an updated value for the USER text    messages = [{"role": "system", "content": """ + self.CurrentSystem + """}),
                                                                                                     {"role": "user", "content":""" + self.CurrentSystem + """}]""",
                                                                           crazy=self.Current_crazy,
                                                                           version=self.Currentversion,
                                                                           Model=self.CurrentModel,
                                                                           WINDOWNAME='PROMPT Optimizer - System' + self.CurrentWindowName)

                                self.PromptCoaching = SystemQuestion.Basic_GPT_Query(System=SSW.PROMPTFIX_System,
                                                                            Line2_Role=SSW.PROMPTFIX_ROLE,
                                                                            Line3_Format=SSW.PROMPTFIX_Format,
                                                                            Background=SSW.ChatGPT_CodeRef,
                                                                            Line4_Task=SSW.PROMPTFIX_USER2 + """Note, You are providing feedback based on the Following 'NewSystem' and 'USER' values, provided in the following code with the full value being entered in the messages arg of the 'openai.ChatCompletion.create' function (see code for reference)     messages = [{"role": "system", "content": """ + self.CurrentSystem + """}),
                                                                             {"role": "user", "content":""" + self.CurrentSystem + """}]""",
                                                                            crazy=self.Current_crazy,
                                                                            WINDOWNAME='PROMPT Optimizer - Details' + self.CurrentWindowName)
                                print("self.PromptCoaching")
                                print(self.PromptCoaching)

                                self.CurrentWindowName = self.LastWindowName
                                try:
                                    current_time1 = datetime.datetime.now()
                                    current_time = current_time1.strftime('%m-%d-%Y_%H.%M.%S')

                                    cu.SaveCSV(SavePath=self.SavePath,
                                               Title=self.FileName + ' Prompt Coaching' + current_time,
                                               Text=self.PromptCoaching)
                                except:
                                    d = 1


                            except:
                                d = 1

                            # GPT_Mode.Basic_GPT_Query(self, System=SSW.PROMPTFIX_System, )

                # This can be final update because it will be somewhat tricky
                # Write code for what happens to pull values from User input and set Permanently (Will really only work for Role, System, Format*), will not work for task or background if I am entering text with the task then I cant really do this, For Background it makes virtually 0 sense.
                # Eventually there should be a change character/review characters mode.
                elif UserMode2 == 441:
                    # KeepGoing = True
                    print("self.promptB:")
                    print(self.promptB)

                elif UserMode2 == 2000:
                    self.Currentversion = self.TE.Get_version()
                    if self.Currentversion == 1:
                        self.LastVersion = self.Currentversion
                        self.Currentversion = 2

                    elif self.Currentversion == 2:
                        self.LastVersion = self.Currentversion
                        self.Currentversion = 1

                # #This is the mode for optimizing prompts
                # elif UserMode2 == 2002:
                #     #Get GPT To give System Prompt
                #     #Get GPT To give USER PROMPT
                #     if  version ==1:
                #         print("Error not currently set up to optimize for Version 1")
                #
                #     else:
                #         try:
                #             CurrentSystem = self.TE.Get_System()
                #             if CurrentSystem != '':
                #                 self.CurrentSystem = CurrentSystem
                #         except:
                #             c = 1
                #
                #
                #
                #         try:
                #             CurrentTask = self.TE.Get_Task()
                #             if CurrentTask != '':
                #                 self.CurrentTask = CurrentTask
                #         except:
                #             c = 1
                #         GPT_Mode.Basic_GPT_Query(self, System = SSW.PROMPTFIX_System )

                # (Eventually Make this for version 1 so its all variables you either go one by one or you can have them return)

                # Pull Up Original Prompt

                elif UserMode2 == 9:
                    try:
                        SPEAKTEXT = ''
                        # self.promptB = False
                        KeepGoing = False
                        try:
                            SPEAKTEXT = self.TE2.GetSpeakText()
                        except:
                            print("error 23234352")
                        # t = threading.Thread(target=cu.speak, args=(SPEAKTEXT,)).start()
                        t1 = Process(target=cu.speak, args=(SPEAKTEXT,))
                        t1.start()
                        t1.join()
                        t1.terminate()
                    except:

                        print("Error with Resetting to Original GPT Response Process")




                elif UserMode2 == 13 or UserMode2 == 14:

                    KeepGoing = False
                    if UserMode2 == 14:
                        # Make them into an array of all prior values so I can go back through time and pull them all in case I want to go back, also would be cool to have way to either go back or edit templates on the fly a little more (like overwrite data in a file)
                        MessageBelow = "*** Pulled Original Prompt Back Into Request Function (GPT) - "
                        self.LastSystem = self.CurrentSystem
                        self.LastRole = self.CurrentRole
                        self.LastFormat = self.CurrentFormat
                        self.LastTask = self.CurrentTask
                        self.LastBackground = self.CurrentBackground
                        self.LastBackground2 = self.CurrentBackground2
                        self.LastBackground3 = self.CurrentBackground3
                        self.LastCrazy
                        self.CurrentModel = self.LastModel
                        self.Currentversion = self.LastVersion

                        self.CurrentSystem = self.OriginalSystem
                        self.CurrentRole = self.OriginalRole
                        self.CurrentFormat = self.OriginalFormat
                        self.CurrentTask = self.OriginalTask
                        self.CurrentBackground = self.OriginalBackground
                        self.CurrentBackground2 = self.OriginalBackground2
                        self.CurrentBackground3 = self.OriginalBackground3
                        self.Current_crazy = self.Original_crazy
                        self.CurrentModel = self.OriginalModel
                        self.Currentversion = self.Originalversion



                    # print("self.promptB:")
                    # print(self.promptB)

                    # Pull Up Last Prompt
                    elif UserMode2 == 13:
                        KeepGoing = False
                        MessageBelow = "*** Pulled Last Prompt Back Into Request Function (GPT) - "
                        self.LastSystemz = self.CurrentSystem
                        self.LastRolez = self.CurrentRole
                        self.LastFormatz = self.CurrentFormat
                        self.LastTaskz = self.CurrentTask
                        self.LastBackgroundz = self.CurrentBackground
                        self.LastBackground2z = self.CurrentBackground2
                        self.LastBackground3z = self.CurrentBackground3
                        self.LastCrazyz = self.LastCrazy
                        self.CurrentModelz = self.LastModel
                        self.Currentversionz = self.LastVersion

                        self.CurrentSystem = self.LastSystem
                        self.CurrentRole = self.LastRole
                        self.CurrentFormat = self.LastFormat
                        self.CurrentTask = self.LastTask
                        self.CurrentBackground = self.LastBackground
                        self.CurrentBackground2 = self.LastBackground2
                        self.CurrentBackground3 = self.LastBackground3
                        self.Current_crazy = self.LastCrazy
                        self.CurrentModel = self.LastModel
                        self.Currentversion = self.LastVersion

                        self.LastSystem = self.LastSystemz
                        self.LastRole = self.LastRolez
                        self.LastFormat = self.LastFormatz
                        self.LastTask = self.LastTaskz
                        self.LastBackground = self.LastBackgroundz
                        self.LastBackground2 = self.LastBackground2z
                        self.LastBackground3 = self.LastBackground3z
                        self.LastCrazy = self.LastCrazyz
                        self.CurrentModel = self.CurrentModelz
                        self.Currentversion = self.Currentversionz

                    # GPT_Response = self.Last_Prompt
                    # print("self.promptB:")
                    # print(self.promptB)
                    #

                    self.Full_User_Prompt = """User Inputs to Chat GPT: 
                        1). System:  """ + self.CurrentSystem + up.LineBreak + """
                        2).Role: """ + self.CurrentRole + up.LineBreak + """
                        3). Format: """ + self.CurrentFormat + up.LineBreak + """
                        4).Task: """ + self.CurrentTask + up.LineBreak + """
                        Background (If Any Provided): """ + self.CurrentBackground + up.LineBreak + """
                        Additional Background: """ + self.CurrentBackground2 + self.CurrentBackground3 + up.LineBreak + """
                        Crazy:""" + str(
                        self.Current_crazy) + up.LineBreak + "Model: " + self.CurrentModel + up.LineBreak + "Version: " + str(
                        self.Currentversion)


                    self.UserPrompts += up.breakupOutput + MessageBelow  + self.Full_User_Prompt + up.breakupOutput
                    self.Full_Transcript += up.breakupOutput + MessageBelow + self.Full_User_Prompt + up.breakupOutput





            except:
                    d = 10

        #t.join()
    def GPT_UserInput_Confirm_Tool(self, GPT_Response, System, Role, Format, Task, Background, Background2, Background3,
                                   crazy=.5, UserConfirm=True, WINDOWNAME="USER CONFIRM CHAT GPT RESULTS", TryCount=0,
                                   version=2,UserMode= "UI",):

        query = ''
        try:
            UserResponseProvided = False
            self.EDIT = ''
            self.FULLPROMPTONLY = self.CurrentSystem + self.CurrentRole + self.CurrentFormat + self.CurrentTask + self.CurrentBackground + self.CurrentBackground2 + self.CurrentBackground3
            TryCount += 1
            WindowNAME1 ="USER CONFIRM CHAT GPT RESULTS " + self.CurrentWindowName + ' ' + str(
                                           TryCount) + ' '
            # self.TE = TextEdit.TextEdit(UserConfirm=True)
            # # query = self.TE.MakeWindow(Text=self.Current_GPTResponse, UserConfirm=True,
            # #                            WindowName=WindowNAME1, USERLASTEDIT=self.EDIT,
            # #                            Current_PROMTS_ALL=self.FULLPROMPTONLY, version=self.Currentversion)
            # t = threading.Thread(target=self.TE.MakeWindow,args=(self.Current_GPTResponse,True,WindowNAME1,self.EDIT, self.FULLPROMPTONLY, self.Currentversion))
            # t.start()


            WindowInfo = GPT_Mode.WindowSetUp(self,Type="GPT", GPTResponse=self.Current_GPTResponse)
            #self.TE.MakeWindow()
            #self.TE = TextEdit.CustomWindow11(self.WindowName, self.window_type, self.WindowSize, self.main_buttons,self.main_checkboxes,self.internal_frame)

            # self.TE = QApplication([])
            windows = []

            # for info in WindowInfo:
            #     self.TE = TextEdit.CustomWindow11(*info)
            #     windows.append( self.TE)

           #self.TE = TextEdit.CustomWindow11(self.WindowName, self.window_type, self.WindowSize, self.main_buttons,
           #                                   self.main_checkboxes, self.internal_frame)

            #
            # self.TE.exec_()
            # t = threading.Thread(target=self.TE.WindowShow)
            # t = threading.Thread(target=self.TE.CreateWindow,args=())

            self.TE = TextEdit.CustomWindow11()


            t = threading.Thread(target=self.TE.CreateWindow, args=(self.WindowName, self.window_type, self.WindowSize, self.main_buttons,
                                               self.main_checkboxes, self.internal_frame))

            t.start()

            # self.TE = TextEdit.CustomWindow11()

            # class MyThread(QThread):
            #     def __init__(self, TE, WindowName, window_type, WindowSize, main_buttons, main_checkboxes,
            #                  internal_frame):
            #         super().__init__()
            #         self.TE = TE
            #         self.WindowName = WindowName
            #         self.window_type = window_type
            #         self.WindowSize = WindowSize
            #         self.main_buttons = main_buttons
            #         self.main_checkboxes = main_checkboxes
            #         self.internal_frame = internal_frame
            #
            #     def run(self):
            #         self.TE.CreateWindow(self.WindowName, self.window_type, self.WindowSize, self.main_buttons,
            #                              self.main_checkboxes, self.internal_frame)
            #
            #
            #
            # t = MyThread(self.TE, self.WindowName, self.window_type, self.WindowSize, self.main_buttons,
            #              self.main_checkboxes, self.internal_frame)
            # t.start()


            KeepGoing = False
            EDIT = ''
            # self.promptB = False
            while KeepGoing == False:

                speak1 = self.Speak
                TryCount += 1

                if KeepGoing == False:

                    UserMode1 = -1
                    if self.UserMode == "UI":

                        try:
                            # self.TE = TextEdit.TextEdit(UserConfirm=True)

                            WINDOWNAME1 = "USER CONFIRM CHAT GPT RESULTS" + self.CurrentWindowName + ' ' + str(
                                                           TryCount) + ' '

                            if UserResponseProvided == True:
                                try:
                                    self.TE.UpdateGPTResponseWindow(self.Current_GPTResponse,self.FULLPROMPTONLY,self.EDIT)
                                    UserResponseProvided = False
                                except:
                                    try:
                                        t.join()



                                    except:
                                        dn = 100
                                    UserResponseProvided = False
                                    #self.TE = TextEdit.CustomWindow11()
                                    WindowInfo = GPT_Mode.WindowSetUp(self,Type="GPT", GPTResponse=self.Current_GPTResponse)
                                    t = threading.Thread(target=self.TE.CreateWindow, args=(self.WindowName, self.window_type, self.WindowSize, self.main_buttons,self.main_checkboxes,self.internal_frame))
                                    t.start()




                            while UserResponseProvided ==False:
                                UserResponseProvided = self.TE.GetUserResponseProvided()
                                # self.CloseWindow = self.TE.GetCloseWindow()
                                # if self.CloseWindow ==True:
                                #     self.TE.quit()

                            UserMode1 = -1
                            UserMode1 = self.TE.GetUserResponseMode()



                            # query = self.TE.GetUserText()
                            print("UserMode1:")
                            print(UserMode1)

                        except:
                            print("major error, could not update window")

                    else:
                        print("""
                                                       Do you want to 
                                                       1). Small Edit, Take the text and switch a few things
                                                       2). ReWrite With Edits (Big Edit)
                                                       3). Rewrite No Edits
        
                                                       """)
                        self.promptB = cu.ConfirmBOT(GPT_Response, speak1)
                        query = cu.getUserResponse()

                    if (( 'one' in query or 'small' in query or 'few' in query or 'mini') and self.UserMode != "UI") or UserMode1 == 1:
                        try:
                            TryCount += 1
                            # promptB2 = True
                            # self.promptB = False
                            KeepGoing = False
                            if self.UserMode == "UI":
                                self.EDIT = query
                            else:
                                self.EDIT = cu.editBotPrompt()

                            print("EDIT")
                            print(self.EDIT )

                            self.Last_GPTResult = self.Current_GPTResponse
                            self.CurrentTempBackground2 = self.CurrentBackground2 + self.CurrentBackground3
                            if self.EDIT != '':

                                GPT_Mode.SaveLastGPTResponse(self, self.Current_GPTResponse)
                                GPT_Mode.SaveLast_Prompt(self, self.CurrentSystem, self.CurrentRole, self.CurrentFormat,
                                                      self.CurrentTask, self.CurrentBackground, self.CurrentBackground2,
                                                      self.CurrentBackground3,
                                                      crazy=self.Current_crazy, Model=self.CurrentModel,
                                                      version=self.Currentversion)

                                self.Current_GPTResponse = cu.ASKGPT(crazy=self.Current_crazy,
                                                                     System="** YOUR FIRST RESPONSE WAS NOT CORRECT, FOLLOW THE SPECIFIC INSTRUCTIONS OF  THE USER EDITS PROVIDED TO YOU IN ORDER TO MAKE THE CORRECT ADJUSTMENTS to the Text. It is critical you follow my instructions" + self.CurrentSystem,
                                                                     Role=self.CurrentRole, Format=self.CurrentFormat,
                                                                     Task="""Rewrite the following text using the edits/Requirements provided and make it in the respective formate described. ReWrite Text: ###""" + self.Current_GPTResponse + "###",
                                                                     Background3="***YOUR FIRST ATTEMPT WAS A FAIL, IT IS CRITICAL THAT YOU Use the following USER EDITS/REQUIREMENTS when completing your task USER EDIT/REQUIREMENTS: ###: " + self.EDIT + "### ***",
                                                                     Background=self.CurrentBackground,
                                                                     Background2=self.CurrentTempBackground2,
                                                                     version=self.Currentversion, Model=self.CurrentModel)
                                self.GPT_Responses.append(self.Current_GPTResponse)
                                #GPT_Mode.SaveCurrentGPTResponse(self, self.Current_GPTResponse)

                                self.CurrentWindowName = WINDOWNAME + " - Small Edit"
                                self.Full_Story += up.breakupOutput + "****Small Edit****" + self.EDIT + up.breakupOutput + self.Current_GPTResponse
                                self.Full_Transcript += up.breakupOutput + "****Small Edit****" + self.EDIT + up.breakupOutput + self.Current_GPTResponse
                                print(
                                    up.breakupOutput + "***************Used Quick Edit Based on User Input***********************" + up.breakupOutput + "Edit: " + self.EDIT + up.breakupOutput + self.Current_GPTResponse + up.breakupOutput)

                            else:
                                WINDOWNAME += ' *** ERROR - No Text Provided, but you selected a User Input Option*** '

                        except:

                            print("Error with ReWriting with EDIT GPT Response Process")

                    elif (('rewrite' in query or 'with edits' in query or 'redo' in query or 'two' in query) and self.UserMode != "UI") or UserMode1 == 2:
                        KeepGoing = False
                        TryCount += 1

                        if self.UserMode == "UI":
                            self.EDIT = query
                        else:
                            self.EDIT = cu.editBotPrompt()
                        print("EDIT")
                        print(self.EDIT)

                        self.Last_GPTResult = self.Current_GPTResponse
                        if self.EDIT != '':
                            self.CurrentTempBackground2 = self.CurrentBackground2 + self.CurrentBackground3

                            GPT_Mode.SaveLastGPTResponse(self, GPT_Response=self.Current_GPTResponse)
                            GPT_Mode.SaveLast_Prompt(self, System=self.CurrentSystem, Role=self.CurrentRole,
                                                  Format=self.CurrentFormat, Task=self.CurrentTask,
                                                  Background=self.CurrentBackground, Background2=self.CurrentBackground2,
                                                  Background3=self.CurrentBackground3
                                                  , crazy=self.Current_crazy, version=self.Currentversion,
                                                  Model=self.CurrentModel)

                            self.Current_GPTResponse = cu.ASKGPT(crazy=self.Current_crazy,
                                                                 System="** YOU Already tried once and failed, YOU MUST FOLLOW THE USER EDIT/REQUIREMENT INSTRUCTIONS from the USER in order TO COMPLETE THE TASK you are being requested. It is critical you answer this question according to the USER Edit/Requirements/Feeback Provided." + self.CurrentSystem,
                                                                 Role=self.CurrentRole,
                                                                 Format=self.CurrentFormat,
                                                                 Task=self.CurrentTask + "***YOUR FIRST ATTEMPT WAS A FAIL and you are doing the task for the " + str(
                                                                     TryCount) + " Time, IT IS CRITICAL THAT YOU Follow the USER EDITS/Requirements in order to get the outcome/Response from you that the USER NEEDS TO MOVE FORWARD.  Use the following USER EDITS/REQUIREMENTS when completing your task.*** USER EDIT/REQUIREMENTS: ###: " + self.EDIT + "### ",
                                                                 Background=self.CurrentBackground,
                                                                 Background2=self.CurrentBackground2,
                                                                 Background3=self.CurrentBackground3,
                                                                 version=self.Currentversion, Model=self.CurrentModel)
                            self.GPT_Responses.append(self.Current_GPTResponse)
                            # GPT_Mode.SaveLastGPTResponse(self, self.Current_GPTResponse)

                            TryCount += 1
                            self.UserPrompts += up.breakupOutput + "****Rewrite with Edits***:" + self.EDIT + up.breakupOutput

                            self.Full_Story += up.breakupOutput + "****Rewrite with Edits***:" + self.EDIT + up.breakupOutput + self.Current_GPTResponse
                            self.Full_Transcript += up.breakupOutput + "****Rewrite with Edits***:" + self.EDIT + up.breakupOutput + self.Current_GPTResponse
                            self.CurrentWindowName = WINDOWNAME + " - ReWrite with Edit"
                            print(
                                up.breakupOutput + "***************Used Redo With Notes/Edits Based on User Input***********************" + up.breakupOutput + "Edit: " + self.EDIT + up.breakupOutput + self.Current_GPTResponse + up.breakupOutput)

                        else:
                            WINDOWNAME += ' *** ERROR - No Text Provided, but you selected a User Input Option*** '



                    elif (('full' in query or 'try new' in query or 'new' in query or 'three' in query) and self.UserMode != "UI") or UserMode1 == 3:
                        try:
                            TryCount += 1

                            GPT_Mode.SaveLastGPTResponse(self, GPT_Response=self.Current_GPTResponse)
                            GPT_Mode.SaveLast_Prompt(self, System=self.CurrentSystem, Role=self.CurrentRole,
                                                  Format=self.CurrentFormat, Task=self.CurrentTask,
                                                  Background=self.CurrentBackground, Background2=self.CurrentBackground2,
                                                  Background3=self.CurrentBackground3,
                                                  crazy=self.Current_crazy, version=self.Currentversion,
                                                  Model=self.CurrentModel)

                            self.Current_GPTResponse = cu.ASKGPT(crazy=self.Current_crazy,
                                                                 System="** YOUR FIRST ATTEMPT At Responding DID NOT SUCCEED, Take a slightly different approach to your last attempt, stick to the format provided to you and mix it up, be creative. " + self.CurrentSystem,
                                                                 Role=self.CurrentRole,
                                                                 Format=self.CurrentFormat,
                                                                 Task=self.CurrentTask, Background=self.CurrentBackground,
                                                                 Background2=self.CurrentBackground2,
                                                                 Background3=self.CurrentBackground3,
                                                                 version=self.Currentversion, Model=self.CurrentModel)

                            self.GPT_Responses.append(self.Current_GPTResponse)
                            print(
                                up.breakupOutput + "***************Used Redo ***********************" + up.breakupOutput + self.Current_GPTResponse + up.breakupOutput)

                            self.UserPrompts += up.breakupOutput + "****Rewrite***" + up.breakupOutput

                            WINDOWNAME = WINDOWNAME + " - ReWrite"
                            self.Full_Story += up.breakupOutput + "****Rewrite***" + up.breakupOutput + self.Current_GPTResponse
                            self.Full_Transcript += up.breakupOutput + "****Rewrite***" + up.breakupOutput + self.Current_GPTResponse
                        except:

                            print("Error with ReWriting GPT Response Process")


                    elif UserMode1 == 0:
                        self.Current_GPTResponse = self.TE.GetFinalGPTOutput()
                        KeepGoing = True
                        t.join()



                    # End All User Input, Run All The Way through
                    elif UserMode1 == 5:
                        self.Current_GPTResponse = self.TE.GetFinalGPTOutput()

                        self.UserConfirm = False
                        self.MainPromptUser = False
                        self.SmallPromptUser = False
                        KeepGoing = True
                        t.join()



                    # End User Input for Small Items
                    elif UserMode1 == 6:
                        self.Current_GPTResponse = self.TE.GetFinalGPTOutput()

                        KeepGoing = True
                        self.SmallPromptUser = False
                        UserConfirm = False
                        t.join()


                    # End User Input for Main Items - Skip to next part
                    elif UserMode1 == 7:
                        self.Current_GPTResponse = self.TE.GetFinalGPTOutput()

                        KeepGoing = True
                        self.MainPromptUser = False
                        self.SmallPromptUser = False
                        UserConfirm = False
                        t.join()


                    # Restores Asking User for confirmation (all prompts)
                    elif UserMode1 == 50:
                        self.Current_GPTResponse = self.TE.GetFinalGPTOutput()
                        t.join()
                        KeepGoing = True
                        self.MainPromptUser = True
                        self.SmallPromptUser = True
                        self.UserConfirm = True





                    # User Review Prompts
                    elif UserMode1 == 10:
                        try:
                            # print("self.promptB:")
                            # print(self.promptB)
                            GPT_Mode.GPT_Confirm_Prompts(self, TryCount=TryCount,
                                                      WINDOWNAME="CHAT GPT USER REVIEW PROMPTS - " + self.CurrentWindowName)
                            ReviewPrompts = True
                            KeepGoing = False
                            self.Full_Transcript += up.breakupOutput + "****REVIEW PROMPTS***" + up.breakupOutput + "BEFORE:" + self.Full_User_Prompt + up.LineBreak

                        except:

                            print("Error with Resetting to REVIEW GPT PROMPT Process (VIA WINDOW 1)")


                    # NOT DOING THIS NOW< FOR NOW I CAN HAVE IT SO I JUST PRESS REVIEW PROMPTS AND DO IT THERE IF I HAVE TO, IF ITS BOTHERSOME I CAN EVENTUALLY CODE THIS
                    # #Restore original Response & Original Prompt
                    # elif UserMode1 == 10:
                    #     self.promptB = False
                    #     print("self.promptB:")
                    #     print(self.promptB)
                    #     self.Reset_Prompts = True
                    #     KillSwitch -= 1
                    #
                    #     continue

                    #Speaks the Text from the UI
                    elif UserMode1 == 9:
                        try:
                            SPEAKTEXT = ''
                            # self.promptB = False
                            KeepGoing = False
                            try:
                                SPEAKTEXT = self.TE.GetSpeakText()
                            except:
                                print("error 23234352")
                            #t = threading.Thread(target=cu.speak, args=(SPEAKTEXT,)).start()
                            t3 = Process(target=cu.speak, args=(SPEAKTEXT,))
                            t3.start()
                            t3.join()
                            t3.terminate()
                        except:

                            print("Error with Resetting to Original GPT Response Process")


                    # Pull Up Original Response
                    elif UserMode1 == 11:
                       try:

                            # self.promptB = False
                            KeepGoing = False
                            self.Current_GPTResponse = self.Original_GPTResponse
                            # print("self.promptB:")
                            # print(self.promptB)
                            self.Full_Transcript += up.breakupOutput + "****Pulled Up Original GPT Response***" + up.breakupOutput + "Original GPT Response:" + self.Original_GPTResponse + up.LineBreak
                       except:

                           print("Error with Resetting to Original GPT Response Process")
                    # Pull Up Last GPT
                    elif UserMode1 == 12:
                        try:
                            # self.promptB = False
                            KeepGoing = False
                            self.Current_GPTResponse = self.Last_GPTResult
                            # print("self.promptB:")
                            # print(self.promptB)
                            self.Full_Transcript += up.breakupOutput + "****Pulled Up Prior GPT Response***" + up.breakupOutput + "Prior GPT Response:" + self.Original_GPTResponse + up.LineBreak
                        except:
                            print("Error with Resetting to Original GPT Response Process")
                    # Option to Make Art
                    elif UserMode1 == 8:
                        try:
                            self.MakeArtGPT = True
                            config = self.Art_Type_Config + StoryMode.artDetailsPrompt
                            GPT_Response1 = self.Current_GPTResponse[:3000]

                            x44 = SHAINE.Story()
                            Art_Role = self.Art_Style_For_Story
                            Art_Format = StoryMode.artDetailsFormat
                            t = threading.Thread(target=x44.GPTArt2, args=(
                            Art_Role, GPT_Response1, config, Art_Format, self.Current_crazy,)).start()
                            AP = x44.GPTArt2(self, Art_Role, User_Subject=GPT_Response1, ArtFormat=StoryMode.artDetailsFormat,
                                             prompt=config, UserConfirm=UserConfirm, )
                            ArtPrompt = self.Art_Style_For_Story + AP

                            print(ArtPrompt)
                            originalFilepath = GPT_Mode.makeArt(self, Prompt=ArtPrompt)
                            if self.Mode.upper() not in str(self.SavePath).upper():
                                PicNewPath1 = Path(PureWindowsPath(self.SavePath, self.Mode))
                                cu.Check_Folder_Exists(PicNewPath1)
                            else:
                                PicNewPath1 = SavePath
                            PicNewPath = Path(PureWindowsPath(PicNewPath1, self.FileName + '.png'))
                            shutil.copyfile(originalFilepath, PicNewPath)
                            self.Full_Transcript += up.breakupOutput + "****Made ART Based off Text***" + up.breakupOutput + "GPT Response:" + self.Last_GPTResult + up.LineBreak

                            SavePath = self.SavePath
                            SaveFile = self.FileName
                            print("self.promptB:")
                            print(self.promptB)
                            # self.promptB = True
                        except:
                            print("Error with MAKE ART Process")


                    # Selects the text from the user input
                    elif UserMode1 == 4:
                        try:
                            if self.UserMode == "UI":
                                try:
                                    self.EDIT = self.TE.GetUserText()
                                except:
                                    print("error")
                            else:
                                self.EDIT = cu.editBotPrompt()

                            if self.EDIT != '':
                                self.Current_GPTResponse =  self.EDIT
                                print(up.breakupOutput + "***************Input User  GPT Response Manually ***********************" + up.breakupOutput + self.Current_GPTResponse + up.breakupOutput)

                                self.Full_Transcript += up.breakupOutput + "***************Input User  GPT Response Manually ***********************" + up.breakupOutput + self.Current_GPTResponse + up.breakupOutput



                                WINDOWNAME = "PLEASE CONFIRM USERS TEXT BEING USED    -   " + self.CurrentWindowName
                                #self.promptB = False
                                KeepGoing = False
                            else:
                                self.CurrentWindowName = ' *** ERROR - No Text Provided, but you selected a User Input Option - TRY AGAIN*** ' + self.CurrentWindowName
                        except:
                            print("Error with User Input Process")

   #         t.join()
        except:
            print("Error with User Input Process")

        return KeepGoing



    def WindowSetUp(self,Type= "GPT", GPTResponse = '', UserEdits = '', System = '', Role= '', Task= '', Format= '', Background= '', Background2= '', Background3= '', Crazy= .5):

        #self.GPTResponse = "Default text 1"
        self.main_buttons1 = ["Continue", "Cancel", "ReGenerate", "ReGenerate with Edit", "ReWrite Edit" , "Review Prompts",	"SPEAK","ALL", "BIG", "MEDIUM", "SMALL"]
        self.main_buttons2 = ["Continue", "Cancel", "<", ">", "SAVE ALL", "OG","SPEAK"]


        self.FrameButtons_User = ["<", ">", "OG", "Save", "Generate", "Use User Text", "Speak", "Speak Input"]
        self.FrameButtons_GPT = ["<", ">", "OG", "Save", "Generate", "Regenerate with Edit", "Rewrite with User Edits", "Speak", "Speak Input"]
        self.FrameButtons2 = ["<", ">", "OG", "Save", "Speak", "Generate"]
        self.FrameButtons2.append("Optimize Prompt")
        CurrentTest = "Prompt Test1"

        self.WindowInfo1 = "Test1"
        self.WindowInfo2 = "Test2"


        if Type== "GPT":
            self.WindowName = "SHAINE"
            self.WindowSize = "large"
            self.internal_frame = ([("CHAT GPT", GPTResponse, self.FrameButtons_GPT, [], "gray"),("USER EDITS", UserEdits, self.FrameButtons_User, [], "lightgreen")])
            self.window_type = self.WindowInfo1
            self.main_buttons = self.main_buttons1
            self.main_checkboxes = ["ALL", "BIG", "MEDIUM", "SMALL"]
            self.window_info = [(self.WindowName,self.window_type , self.WindowSize,self.main_buttons,self.main_checkboxes, self.internal_frame)]

        else:
            self.WindowName = "PROMPTS REVIEW"
            self.WindowSize = "large"
            self.main_checkboxes = []
            self.window_type = self.WindowInfo1
            self.main_buttons = self.main_buttons2
            self.internal_frame =([("System", System, self.FrameButtons2, [], "lightyellow"),
                ("Role", Role, self.FrameButtons2, self.main_checkboxes, "lightpink"),
                ("Format", Format,  self.FrameButtons2, [], "green"),
                ("Task", Task, self.FrameButtons2, [], "lightgreen"),
                ("Background", Background, self.FrameButtons2, [], "lightblue"),
                ("Background2", Background2, self.FrameButtons2, [], "blue"),
                ("Background3", Background3, self.FrameButtons2, [], "purple"),("Crazy", Crazy, self.FrameButtons2, [], "yellow")])
            self.window_info = [(self.WindowName, self.window_type,self.WindowSize ,self.main_buttons,self.main_checkboxes,self.internal_frame)]

        # Create a separate thread to run the GUI
        #x = create_windows6(window_info=window_info)
        #gui_thread = threading.Thread(target=create_windows6, args=(window_info,))
        #gui_thread.start()

        return self.window_info


    def Get_SmallPromptUser(self):
        return self.SmallPromptUser

    def Get_UserConfirm(self):
        return self.UserConfirm

    def Get_MainPromptUser(self):
        return  self.MainPromptUser


    def Get_UserPrompts(self):
        return self.UserPrompts

    def Get_Transcript(self):
        return  self.Full_Transcript

    def Get_Story(self):
        return  self.Full_Story

    def Get_UserPromptsCount(self):
        return  self.UserPromptsCount
    # def Get_PROMPTS(self):
    #     return  self.Full_Transcript


    #
    # def Get_Role(self):
    #     return self.UserPromptRole
    #
    # def Get_Format(self):
    #     return self.UserPromptFormat
    #
    # def Get_Task(self):
    #     return self.UserPromptTask
    #
    # def Get_Background(self):
    #     return self.UserPromptBackground
    #
    # def Get_Background2(self):
    #     return self.UserPromptBackground2
    #
    # def Get_Background3(self):
    #     return self.UserPromptBackground3
    #
    # def Get_version(self):
    #     #TextEdit.GetPrompts(self)
    #     return self.UserPromptversion
    #
    #
    # def Get_Crazy(self):
    #     return self.UserPromptCrazy





    def GPTArt2(self,
                ArtRole="You are a skilled artist who is able to easily take text and come up with masterpieces to go along with the context/theme/mood of the text. You are a master artist and skilled communicator able to take a lot of details and come up with a succinct prompt for AI to make a work of are with. Use the Artistic Style described to your persona along with the text to come up with your response",
                User_Subject='Pick a random subject and artistic style/medium  go wild and make it exciting, beautiful and shocking',
                prompt="In 13 words or fewer describe what utensils you will use, colors, styles, specialties include the  art style the  theme and  mood | Based on the text you were given think of something abstract related to the painting, or paint a vivid scene, or paint one of the characters/multiple characters together as the text describes them, be creative, but keep your prompt under 313 characters total. Your response should be formatted as a short prompt for DALL-E (AI-Art generator) to create a work of art/photograph",
                ArtFormat=StoryMode.artDetailsFormat + ', <Short description of Work of art under 250 characters>',
                crazy=.5, sys_prompt=sms.ArtPrompt_Sys, Model="gpt-3.5-turbo", UserConfirm='False'):
        Full_User_Prompt = sys_prompt + prompt + User_Subject + ArtFormat
        if len(Full_User_Prompt) > 6000:
            Model = "gpt-3.5-turbo-16k-0613"
        elif len(Full_User_Prompt) < 6000:
            Model = "gpt-3.5-turbo"

        keepgoing = True
        GPTARTPROMPT = User_Subject
        while keepgoing == True:
            try:

                #     Art_Prompt1 = openai.ChatCompletion.create(
                # model=Model,
                # messages = [
                #                {"role": "system", "content": sys_prompt},
                #                {"role": "user", "content": prompt + User_Subject},
                #                {"role": "user", "content": ArtFormat}
                #            ], temperature = crazy
                #     )
                #
                #     GPTARTPROMPT = Art_Prompt1.choices[0].message.content
                ArtRole1 = "You are a skilled artist who is able to easily take text and come up with beautiful works of art of all artistic mediums and styles. Your masterpieces go along with the story perfectly matching the context/theme/mood of the text. You are a master artist and skilled communicator able to take a lot of details and come up with a succinct prompt for AI to make a work of are with. Use the Artistic Style described to your persona along with the text to come up with your response" + ArtRole
                SystemQuestion = GPT_Mode()
                GPTARTPROMPT = SystemQuestion.Basic_GPT_Query(Model=Model, Line1_System_Rule=sys_prompt, Line2_Role=ArtRole1,
                                                     Line3_Format=ArtFormat, Line4_Task="Task: ### " + prompt + "###",
                                                     Background=User_Subject, User_Confirm=UserConfirm, crazy=crazy)
                keepgoing = False

            except:
                print('GPT error waiting 13 seconds and trying again...')

                try:
                    time.sleep(13)
                except:
                    dn = 100

            return GPTARTPROMPT

