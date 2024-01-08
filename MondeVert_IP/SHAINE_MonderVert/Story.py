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
from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu, ShakesBot as s, GPT_Mode as GPT
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


#OutputTypes = ["Play","Novel", "ScreenPlay","Song"]

class Story():
    def __init__(self, IDEA = '' ,UserConfirm = False, ConfirmInput = False, UserMode = 'UI',Mode = 'MVAA',Writer = '', UserInputs_Config = 'AI Only',OutputTypes = ["Play", "Novel", "ScreenPlay"],voice=4, Logic_AI = 0, language_settings=1,Chunk_Limit = 777,  SavePath =up.AI_AudioBook_Path,  Writer_Style = '',Artist = '', Artist_Style = '', Story_Type = 'ScreenPlay', Seasons = 1, Episodes = 3, Books = '', Acts = '', Scenes = '', Movies = '', Text_Output_Config = [''], IDEA_Source = 'AI', Output_Audio_Config = '' ):
        self.voice = voice
        self.language_settings = language_settings
        self.UserMode = UserMode
        self.ConfirmInput = ConfirmInput
        if  self.language_settings ==1:
            self.Translate = ['English']

        self.AssistantName = up.getAssistantName()
        self.UserName = up.getUserName()
        self.transcript_Final = ''
        self.API_Key = API_Key
        self.Show_Print = True
        self.Correction_Comment = ''
        self.AI_Corrected_Content = ''
        self.SilentMode = False
        self.transcript_Final = ''
        self.Outline_progression = ''
        self.Character_progression = ''
        self.Full_Transcript = ''
        self.Prior_Season = ''
        self.Prior_Episode = ''
        self.Prior_Scenes = ''
        self.Prior_Scenes_a = ''
        self.Prior_Scenes_p = ''
        self.Prior_Scenes_n = ''
        self.Prior_Scenes_s = ''
        self.Prior_Scene = ''
        self.Prior_Scene_a = ''
        self.Prior_Scene_p = ''
        self.Prior_Scene_n = ''
        self.Prior_Scene_s = ''

        self.data = ''
        self.AudioBook_Text = ''
        self.Episode_Outline = []
        self.Character_progression = ''
        self.Outline_progression = ''
        self.Episode_Outlines = ''
        self.Episode_Story_Song = ''
        self.OutputTypes = OutputTypes
        self.Chunk_Limit = Chunk_Limit
        self.current_time1 = datetime.datetime.now()
        self.current_time = self.current_time1.strftime('%m-%d-%Y_%H.%M')
        self.UserPrompts = ''
        self.Backgrounds = ''
        self.Full_Story = """"""
        self.UserConfirm = UserConfirm

        voice_set = self.voice
        xVoice = 1
        self.UserPromptsCount = 0
        self.FilePaths = []
        self.FilePaths_Email = []
        self.Art_Descriptions = []


        #This is definitely needed, the stuff above might not be needed
        self.Request_log = []
        openai.api_key = API_Key
        self.SavePath = Path(PureWindowsPath(SavePath, Mode))
        self.Mode = Mode

        self.Version = []
        self.Version2 = []
        self.Version3 = []
        self.Version4 = []
        self.Version5 = []
        self.Version6 = []
        self.Speak = False
        self.SaveTranscript = False
        self.Art_Type_Config = ''
        self.LiveNovel = ''
        self.LiveAudio = ''
        self.LiveSong = ''
        self.LiveScreenPlay = ''
        self.LivePlay = ''
        self.LiveMusical = ''

        self.MainPromptUser = self.UserConfirm
        self.SmallPromptUser = self.UserConfirm
        self.PartPromptUser = self.UserConfirm
        self.Art_Style_For_Story = "Pick a random style/medium based on the following text: "


        if "ART" in Mode.upper():
            #do nothing
            dn = 100


        else:
        #UserDrivenFields, if they are all blank then AI needs to generate the values
        #Concept of Series Length is established here
            self.numSeasons = Seasons
            self.numEpisode = Episodes
            self.numBooks = Books
            self.numActs = Acts
            self.numMovies = Movies
            self.numScenes = Scenes

            #this will drive if you use Seasons or Episodes
            self.Mode = Mode
            self.Story_Type = Story_Type

            #The following Fields are mostly config
            self.Text_Output_Config = Text_Output_Config
            if self.Text_Output_Config =='':
                self.Text_Output_Config = self.Story_Type
            self.UserInputs_Config =UserInputs_Config
            self.Output_Audio_Config = Output_Audio_Config
            if self.Output_Audio_Config == '':
                self.Output_Audio_Config = self.Story_Type[0]




            if Logic_AI == 0:
                crazy = round((randbelow(520000) + 170000) / 100000, 0)
                crazy = crazy / 10
                #print('Crazy Rating: ' + str(crazy))
                crazy += .2
                if crazy < .4:
                    crazy = .6
                if crazy > .9:
                    crazy = .7
            else:
                crazy = Logic_AI


            self.crazy =crazy

            #TE = TextEdit.TextEdit()
            self.TE = TextEdit.TextEdit( UserConfirm=True)




            if   'MUSIC'  in Mode.upper():
                self.systemPrompt = MW.system_TextDJ
            elif 'COMEDY'  in Mode.upper():
                self.systemPrompt = CW.system_TextComedy
            elif 'POEM' in Mode.upper():
                self.systemPrompt = PW.system_TextStory
            elif 'FAMIL'  in Mode.upper():
                self.systemPrompt = StoryMode.system_TextStory_Kids
            else:
                self.systemPrompt = StoryMode.system_TextStory




    #"gpt-4"
            if   'COOK' not in Mode.upper():
                #UserManipulates the story if they choose to fill these in otherwise we trigger the AI to create these values
                self.Artist = Artist
                self.Writer = Writer
                self.IDEA = IDEA
                self.IDEA_Source = IDEA_Source
                self.Writer_Style = Writer_Style
                self.Artist_Style = Artist_Style



                #sets up all of the prompts to simplify where I make the edits for my prompts
                Story.setPrompts(self)

                # Pre Story Elements are gathered for the story such as IDEA/Writer/Artist details
                if self.Writer == '':
                    self.Writer_Summary = Story.getWriter(self)

                elif 'EXACT' in self.UserInputs_Config.upper():
                    self.Writer_Summary = self.Writer
                elif 'SUMMARIZE' in self.UserInputs_Config.upper()  :
                    print("Working as expected")
                    self.Writer_Summary = Story.getWriter(self, Persona =  self.Writer)
                else :
                    print("Working as expected")
                    self.Writer_Summary = Story.getWriter(self, Persona =  self.Writer)




                if  self.Writer_Style == '':
                    self.Writer_Style_Summary =  Story.getWriter_Style(self)
                elif 'SUMMARIZE' in self.UserInputs_Config.upper():
                    self.Writer_Style_Summary = Story.getWriter_Style(self, Writer_Style=self.Writer_Style)
                elif 'EXACT' in self.UserInputs_Config.upper():
                    self.Writer_Style_Summary = self.Writer_Style
                else :
                    print("Working as expected")
                    self.Writer_Style_Summary = Story.Writer_Style(self, Writer_Style =  self.Writer_Style)

                self.IDEA_Role = self.IDEA_Role + self.Writer_Style_Summary

                #self.Speak = True
                if self.IDEA_Source == 'AI':
                    if self.IDEA =='':
                        self.IDEA_Final =  Story.getIDEA(self, Mode = 'AI')
                    else:
                        self.IDEA_Final = Story.getIDEA(self, Mode = 'AI2', IDEA = self.IDEA)
                elif self.UserInputs_Config == 'Summarize':
                    self.IDEA_Final =  Story.getIDEA(self, Mode = 'Summarize', IDEA = self.IDEA)
                elif self.UserInputs_Config == 'Exact':
                    self.IDEA_Final = self.IDEA
                else:
                    if self.IDEA =='':
                        self.IDEA_Final =  Story.getIDEA(self, Mode = 'AI')
                    else:
                        self.IDEA_Final = Story.getIDEA(self, Mode='Summarize', IDEA=self.IDEA)








            #This is potentially where I can make it a menu that does not always use the full 3 level story maker and instead goes only to the 2 level or also if I want to inject the prestuff I can do so and just run with refreshing the story

            #After Pre Story Elements are gathered we begin to make outlines for the story



            if 'MVAA2' in Mode.upper():



                Story.NewStoryMode(self)

                print('self.Writer_Summary')
                print(self.Writer_Summary)
                print('self.Writer_Style_Summary')
                print(self.Writer_Style_Summary)
                print('self.IDEA_Final')
                print(self.IDEA_Final)


            if 'MVAA_QUICK' in Mode.upper() or 'POEM' in Mode.upper() or 'FAMIL' in Mode.upper():



                Story.NewStoryMode2(self)
                Story.FinalOutputs(self)


                print('self.Writer_Summary')
                print(self.Writer_Summary)
                print('self.Writer_Style_Summary')
                print(self.Writer_Style_Summary)
                print('self.IDEA_Final')
                print(self.IDEA_Final)



            elif 'MUSIC'in Mode.upper() or 'COMEDY' in Mode.upper():


                if 'MUSIC'in Mode.upper():
                    RightKey = "Genre"
                    idea2_Format = """
                                Desired Format:
                                Musician Writing Style: {Short Response}
                                """

                    idea2_Task = """Use the Original IDEA you have created and the writing persona you have created to write a succinct (make it less than 30 words) summary of the Writing Style to be used in order to  make a unique song/story that still incorporates the key parts of the writer based on the IDEA provided. Show do not tell, use literary devices and create a unique personality to draw inspiration from"""

                    idea2 = Story.Basic_GPT_Query(self,
                                                   Line2_Role= MW.DJ_Role ,
                                                   Line3_Format=idea2_Format,
                                                   Background="""Use the following Idea Outline to write your song's outline. Idea  Outline:###""" + self.IDEA_Final + """###""",
                                                   Line4_Task=idea2_Task,
                                                   crazy=self.crazy, Big=True, User_Confirm=self.UserConfirm, Line1_System_Rule= self.systemPrompt, WINDOWNAME="IDEA 2 ?? Used for Story Role when Making Music")

                    self.IDEA_Role2 = MW.DJ_Role + " Role play that you are the following Persona to complete your task: " + idea2
                    #OUTLINETAG = "Song_Outline: "

                else:
                    RightKey = "Details"
                    self.IDEA_Role2 = CW.Comedy_Role
                    #OUTLINETAG = "Joke_Outline: "



                print("USing the following Persona for song: ")
                print(self.IDEA_Role2)

                self.Story_Role = self.IDEA_Role2

                self.Song_Outline = Story.getSongOutline(self)






                try:
                    Title = 'MondeVert Song ' + self.current_time
                    TrimCharR = self.Song_Outline.find(RightKey)
                    TrimCharL = self.Song_Outline.find("Title:")

                    Title = self.Song_Outline[TrimCharL:TrimCharR]



                except:
                    try:
                        Title = 'MondeVert Song ' + self.current_time
                        TrimCharR = self.Song_Outline.find("#")
                        TrimCharL = self.Song_Outline.find("Title:")

                        Title = self.Song_Outline[TrimCharL:TrimCharR]

                    except:


                        Title = 'MondeVert Song ' + self.current_time
                        try:
                            Text = self.Song_Lyrics[:200]
                            Title = Story.Quick_Title(self, Text=Text)

                        except:
                            Title = 'MondeVert Song ' + self.current_time


                Title = Title.replace("Title", "")
                self.Title = cu.CleanFileName(Title)
                NewSavePath = Path(PureWindowsPath(self.SavePath ,  self.Title + '  ' +  self.current_time))

                cu.Check_Folder_Exists(NewSavePath)

                self.Song_Lyrics = Story.getSongLyrics(self)



                if 'MUSIC' in Mode.upper():
                    self.DJInstructions = Story.DJMakeABeat(self)



                print(self.Song_Outline)
                print(self.Song_Lyrics)







                try:
                    cu.SaveCSV(Text=self.Writer_Style_Summary + self.Story_Role, SavePath=NewSavePath, Title=self.Title + ' Writer Style', AddTimeStamp=False)
                    cu.SaveCSV(Text=self.IDEA_Final, SavePath=NewSavePath, Title=self.Title + ' IDEA', AddTimeStamp=False)
                    cu.SaveCSV(Text=self.Song_Outline, SavePath=NewSavePath, Title = self.Title + ' Outline', AddTimeStamp= False)
                    cu.SaveCSV(Text=self.Song_Lyrics, SavePath=NewSavePath, Title = self.Title, AddTimeStamp= False)
                    cu.SaveCSV(Text=self.DJInstructions, SavePath=NewSavePath, Title=self.Title + " DJ  Instructions", AddTimeStamp=False)
                    print( up.breakupOutput + "Writer Style: " + self.Writer_Style_Summary + self.Story_Role + up.breakupOutput2)
                    print(up.breakupOutput + "IDEA: " + self.IDEA_Final + up.breakupOutput2)
                    print(up.breakupOutput + "Song_Outline" + self.Song_Outline + up.breakupOutput2)
                    print(up.breakupOutput + "Song_Lyrics: " + self.Song_Lyrics + up.breakupOutput2)
                    print(up.breakupOutput + "DJInstructions: " + self.DJInstructions + up.breakupOutput2)
                except:
                    print("Error Saving Files Recover Data Below")
                    print( up.breakupOutput + "Writer Style: " + self.Writer_Style_Summary + self.Story_Role + up.breakupOutput2)
                    print(up.breakupOutput + "IDEA: " + self.IDEA_Final + up.breakupOutput2)
                    print(up.breakupOutput + "Song_Outline: " + self.Song_Outline + up.breakupOutput2)
                    print(up.breakupOutput + "Song_Lyrics: " + self.Song_Lyrics + up.breakupOutput2)


            elif 'MVAA' in Mode.upper():

                if 'QUICK' not in Mode.upper():
                    Story.getMainOutlines(self, IDEA=self.IDEA_Final)
                    self.arttext = self.Outline_Main_Style
                    if self.Artist_Style == '':
                        self.Art_Style_For_Story = Story.getArtist_Style(self, arttext = self.arttext)
                    elif self.UserInputs_Config == 'Summarize':
                        self.Art_Style_For_Story = Story.getArtist_Style(self, arttext = self.arttext,Artist=self.Artist_Style)
                    elif self.UserInputs_Config == 'Exact':
                        self.Art_Style_For_Story = self.Artist_Style
                    else:
                        self.Art_Style_For_Story = Story.getArtist_Style(self, arttext=self.arttext, Artist=self.Artist_Style)




                    Story.FullSeries(self)
                    Story.getCharacters(self)

                    text = self.Outline_Main_Summary + self.Characters
                    # t = threading.Thread(target=Story.TheatricalPreview, args=(self,text)).start()



                    Story.SavePreFiles(self)
                    Story.TheatricalPreview(self, Text=text)
                    # Arg1 = 'self'
                    # t1 = threading.Thread(target=Story.conceptArt, args=(Arg1,)).start()
                    # threads.append(t1)
                    Story.FullSeason(self)
                    Story.FinalOutputs(self)

            elif 'COOK' in Mode.upper():
                Story.MakeRecipe(self)
            elif 'REWRITE' in Mode.upper():
                self.ReWrite = ''
                #Make a query that sends in text to ChatGPT to rewrite (use the common utility to split the text as per the number of characters that seem useful"
                Story.Split_Audio2Revise(self,Text=self.IDEA_Final)



                #Step 1 is break up the text
                #step 2 is rewrite each excerpt via Chat GPT
                #Step3 is to send it through the Translate tool, create art and audio for it
                #Step5 is save the different versions, but this might be automatic if done right



    def DJMakeABeat(self):

        Background_DJ1 = "Use the following Samples and Instrumental Details from the following Song_Outline for your response.   Song Outline: ###" + self.IDEA_Final + """###"""
        Background_DJ2 = "Use the following Lyrics as reference for your response.   LYRICS: ###" + self.Song_Lyrics + """###"""

        DJInstructions = Story.Basic_GPT_Query(self,
                                             Line2_Role=self.Story_Role,
                                             Line3_Format=MW.ExplainTheBeat_Format,
                                             Background=Background_DJ1, Background2 = Background_DJ2,
                                             Line4_Task=MW.ExplainTheBeat,
                                             crazy=self.crazy, Big=True, User_Confirm=self.UserConfirm,
                                             WINDOWNAME="DJ Make A Beat", Line1_System_Rule=self.systemPrompt)

        return DJInstructions

    def getSongOutline(self, Format = MW.Song_Outline_Format, Task = MW.Song_Outline_Task,makeArt = False):
        d = 100

        if "COMEDY" in self.Mode.upper():
            Format = CW.Joke_Outline_Format
            Task = CW.Joke_Outline_Task
            makeArt = False

        Song_Outline = Story.Basic_GPT_Query(self,
                                              Line2_Role=self.Story_Role,
                                              Line3_Format=Format,
                                              Background="""Use the following Idea Outline to write/create your outline. Idea  IDEA:###""" + self.IDEA_Final+ "###",
                                              Line4_Task=Task,
                                              crazy=self.crazy, Big=True, User_Confirm = self.UserConfirm, WINDOWNAME="SongOutline", Line1_System_Rule=self.systemPrompt, MakeArt=makeArt, SavePath=self.SavePath)

        return Song_Outline




    def getSongLyrics(self, Format = MW.Song_Format, Task = MW.Song_Task, makeArt = False):
        d = 100
        if "COMEDY" in self.Mode.upper():
            Format = CW.Joke_Format
            Task = CW.Joke_Task
            makeArt = True


        Song = Story.Basic_GPT_Query(self,
                                              Line2_Role=self.Story_Role,
                                              Line3_Format=Format,
                                              Background="""Use the following Outline to complete your task/provide your response Outline:###""" + self.Song_Outline,
                                              Line4_Task=Task,
                                              crazy=self.crazy, Big=True, User_Confirm = self.UserConfirm, WINDOWNAME="SongLyrics", Line1_System_Rule= MW.system_TextDJ, MakeArt=makeArt, SavePath=self.SavePath)
        return Song

    def NewStoryMode(self):

        self.Story_Role = 'You are a brilliant assistant to the user, Role Play as an award winning writer able to impersonate any genre or style/voice base your persona on the following Writing Style  Writing Style: ' + self.Writer_Style_Summary

        NewStory_Outline = Story.Basic_GPT_Query(self,
                                                    Line2_Role= self.Story_Role,
                                                    Line3_Format=SP.Story_Outline_Format,
                                                    Line4_Task=SP.Story_Outline_Task +  """Use the following  Text  as a source for your Outline   IDEA:###""" + self.IDEA_Final + "###",
                                                    crazy=self.crazy, Big=True, User_Confirm = self.MainPromptUser, WINDOWNAME="Story Outline", Line1_System_Rule= self.systemPrompt)


        Title = Story.Quick_Title(self,Text = NewStory_Outline)
        cu.SaveCSV(Text=NewStory_Outline,SavePath=self.SavePath, Title=Title+ '_New Outline')
        cu.SaveCSV(Text=self.IDEA_Final, SavePath=self.SavePath, Title=Title + '_New Idea')

        self.arttext = NewStory_Outline
        if self.Artist_Style == '':
            self.Art_Style_For_Story = Story.getArtist_Style(self, arttext=self.arttext)
        elif self.UserInputs_Config == 'Summarize':
            self.Art_Style_For_Story = Story.getArtist_Style(self, arttext=self.arttext, Artist=self.Artist_Style)
        elif self.UserInputs_Config == 'Exact':
            self.Art_Style_For_Story = self.Artist_Style
        else:
            self.Art_Style_For_Story = Story.getArtist_Style(self, arttext=self.arttext, Artist=self.Artist_Style)

        NewStory_AllScenes_Outline = Story.Basic_GPT_Query(self,
                                                    Line2_Role=self.Story_Role,
                                                    Line3_Format=SP.Story_AllScenes_Outline_Format,
                                                    Background=   """Use the following  Text  as a source for your Story (Expand on the ideas and give a full story based on the requirements provided)  Text:###""" + NewStory_Outline,
                                                    Line4_Task= SP.Story_AllScenes_Outline_Task,
                                                    crazy=self.crazy, Big=True, User_Confirm = self.MainPromptUser, WINDOWNAME="Short Story New", Line1_System_Rule= self.systemPrompt)



        cu.SaveCSV(Text=NewStory_AllScenes_Outline,SavePath=self.SavePath, Title=Title+ '_Full Story')



#this is where you add code to go scene by scene and update characters etc.

    def NewStoryMode2(self, DelimiterCheck='@SCENE', ReplaceKey='@@SCENE',  upperWord='Scene', Delimiter='@@'):

        self.Episode1 = True
        self.Season1 = True
        self.Scene1 = True

        AllScenes_Outline_Task = SP.Story_AllScenes_Outline_Task
        AllScenes_Outline_Format = SP.Story_AllScenes_Outline_Format
        Outline_Expand_Task = SP.Story_Outline_Expand_Task
        Outline_Expand_Format = SP.Story_Outline_Expand_Format
        Outline_Task = SP.Story_Outline_Task
        Outline_Format = SP.Story_Outline_Format
        AllScenes_Char_Summary_Task = SP.Story_AllScenes_Char_Summary_Task
        AllScenes_Char_Summary_Format = SP.Story_AllScenes_Char_Summary_Format
        Style_Details_Format = self.Story_Style_Details_Format
        Style_Details_Task2 = self.Story_Style_Details_Task2



        if 'POEM' in self.Mode.upper():
            AllScenes_Outline_Task = PW.Story_AllScenes_Outline_Task
            AllScenes_Outline_Format = PW.Story_AllScenes_Outline_Format
            Outline_Expand_Task = PW.Story_Outline_Expand_Task
            Outline_Expand_Format = PW.Story_Outline_Expand_Format
            Outline_Task = PW.Story_Outline_Task
            Outline_Format = PW.Story_Outline_Format
            AllScenes_Char_Summary_Task = PW.Story_AllScenes_Char_Summary_Task
            AllScenes_Char_Summary_Format = PW.Story_AllScenes_Char_Summary_Format
            Style_Details_Format = PW.Story_Episode_Writing_Style_Task
            Style_Details_Task2 = PW.Story_Episode_Writing_Style_Format

            self.Story_Scene_Outline_Format = PW.Poem_Outline_Format
            self.Story_Scene_Outline_Task = PW.Poem_Outline_Task
            DelimiterCheck = '@POEM'
            ReplaceKey = '@@POEM'
            upperWord = 'Poem'


        ##Note this is where you change the prompts for it to be Poetry prompts or other for you to use here


        self.Story_Role = 'You are a brilliant assistant to the user, Role Play as an award winning writer/Director/Playwrite able to impersonate any genre or style/voice base your persona on the following Writing Style  Writing Style: ' + self.Writer_Style_Summary

        self.StoryRoleAdd = Story.Basic_GPT_Query(self,Line2_Role=self.Story_Role, Line3_Format=Style_Details_Format,Line4_Task=Style_Details_Task2
                                                  ,Background ="""Use the following Writing Style for your response Writing Style:### """ + self.Writer_Style_Summary ,
                                                               crazy=self.crazy,
                                                               Subject='', User_Confirm=self.SmallPromptUser,
                                                               WINDOWNAME='Story Writing Style  ' , Line1_System_Rule= self.systemPrompt)

        self.Outline_ALL_Seasons = self.IDEA_Final
        self.Story_Role = 'You are a brilliant assistant to the user, Role Play as an award winning writer able to impersonate any genre or style/voice base your persona on the following Writing Style  Writing Style: ' + self.StoryRoleAdd
        Story.getCharacters(self)




        self.Characters2 = self.Characters



        if len(self.Characters2) > 6500 or 'POEM' in self.Mode.upper() :
            self.Characters2 = Story.Basic_GPT_Query(self,
                                                     Line2_Role=self.Story_Role,
                                                     Line3_Format=AllScenes_Char_Summary_Format,
                                                     Background= """Use the following  Text  as background for your response    Characters: ###""" + self.Characters +  """###""",
                                                     Line4_Task=AllScenes_Char_Summary_Task,
                                                     crazy=self.crazy, Big=True, User_Confirm=self.UserConfirm,
                                                     WINDOWNAME="Characters Summary (Too long of a character list)", Line1_System_Rule= self.systemPrompt)





        NewStory_Outline = Story.Basic_GPT_Query(self,
                                                 Line2_Role=self.Story_Role,
                                                 Line3_Format=Outline_Format,
                                                 Background= """Use the following  Text  as background for your Outline   IDEA:###""" + self.IDEA_Final + """### Characters: ###""" + self.Characters2 +  """###""",
                                                 Line4_Task=Outline_Task,
                                                 crazy=self.crazy, Big=True, User_Confirm=self.MainPromptUser,
                                                 WINDOWNAME="Story Outline", Line1_System_Rule= self.systemPrompt)

        try:
            self.NewStory_Outline = NewStory_Outline
            TrimCharR = NewStory_Outline.find("@Part") + 1
            TrimCharL = NewStory_Outline.find("Title")

            Title = NewStory_Outline[TrimCharL:TrimCharR]



        except:
            Title = ''
            try:
                Text = NewStory_Outline
                Title = Story.Basic_GPT_Query(self,
                                                 Line2_Role=self.Story_Role,
                                                 Line3_Format=" short 4 word or less abstract title",
                                                 Line4_Task=  """Use the following  Text  to come up with a short/abstract title for your story, your response should be the title only based on the following text Text:###""" + Text + """###""",
                                                 crazy=self.crazy, Big=True, User_Confirm=self.MainPromptUser,
                                                 WINDOWNAME="Get Title", Line1_System_Rule= self.systemPrompt)

            except:
                Title = 'New Story ' + self.current_time

        Title = Title.replace("The Title:", "")
        Title = Title.replace("Title:", "")
        Title = Title.replace("The Title", "")
        Title = Title.replace("Title", "")

        TitleOO = Title

        if len(Title) > 90:
            Title = Title[:44]

        Title1 = cu.CleanFileName(Title)
        Title1 = Title1.strip()
        self.FileName = Title1
        Title = Title1
        self.SavePath = Path(PureWindowsPath(self.SavePath, Title1))
        cu.Check_Folder_Exists(self.SavePath)
        self.SavePath_Outlines = Path(PureWindowsPath(self.SavePath, 'Outlines'))
        cu.Check_Folder_Exists(self.SavePath_Outlines)
        self.SaveTranscript = True


        cu.SaveCSV(Text=NewStory_Outline, SavePath=self.SavePath_Outlines, Title=self.FileName + '_New Outline')
        cu.SaveCSV(Text=self.IDEA_Final, SavePath=self.SavePath_Outlines, Title=self.FileName + '_New Idea')

        self.arttext = NewStory_Outline
        if self.Artist_Style == '':
            self.Art_Style_For_Story = Story.getArtist_Style(self, arttext=self.arttext)
        elif self.UserInputs_Config == 'Summarize':
            self.Art_Style_For_Story = Story.getArtist_Style(self, arttext=self.arttext, Artist=self.Artist_Style)
        elif self.UserInputs_Config == 'Exact':
            self.Art_Style_For_Story = self.Artist_Style
        else:
            self.Art_Style_For_Story = Story.getArtist_Style(self, arttext=self.arttext, Artist=self.Artist_Style)
        self.Season_num = 1


        self.Episode_by_Episode = Story.cutBy(self, Text=NewStory_Outline, upperWord='Part', Delimiter='@@',
                                              DelimiterCheck='@PART', ReplaceKey='@@PART')



        print("len(self.Episode_by_Episode):")
        print(str(len(self.Episode_by_Episode)))
        countPart = len(self.Episode_by_Episode)
        print("CountParts")
        print(str(countPart))
        for x1 in range(1,countPart):
            self.Episodenum = x1
            self.Episode_Story = ''
            self.Episode_Story_Audio = ''
            self.Episode_Story_Novel = ''
            self.Episode_Story_Play = ''
            self.Episode_Story_Song = ''

            self.Prior_Episode_Summary = ''


            try:
                NewStory_Outline1 = self.Episode_by_Episode[x1]

            except:
                d=100


            #note this is where it updates characters based on the current part of the story
            try:
                Story.Character_Update(self, Outline=NewStory_Outline1,Episode=x1, Characters_Update_Task=StoryMode.Characters_Update_Task2)
            except:
                d = 100


            self.Characters2 = self.Characters



            PartNumFix = ''

            if x1 == 1:
                PartNumFix = """DO NOT RESOLVE THE STORY/DO NOT WRITE THE CONCLUSION/RESOLUTION, Leave the story open ended: This is Part 1 (Beginning - Introduction & Exposition) out of 3 parts. This is the first part so make it exciting while laying the groundwork for the entire story, introduce characters and make the story come to life, do not write a conclusion, in fact the rising action should only just be starting for main plot, you can have arc plots get further along, and set up a red herring to make the story not obvious  Have some arc plots resolve but make sure the main plot is not resolved in this section of Scenes. introduce most of the characters and set up a plot twist or something else for the later 2 parts, make sure you set up another TWO THIRDS of the story. Introduce characters and Exposition with rising action/conflict development.  Again, Do not wrap up the entire story in this part,  You should end this part of the story with the major plot starting to get towards the rising action, in the first part establish the plots/arc plots for the second part to resolve the arc plots and build the conflict for the main plot in season 2, The first few scenes should be interesting and draw us in and then provide most of the background for the story in this part."""
            elif x1 == 2 and countPart > 2 :
                PartNumFix = "DO NOT RESOLVE THE STORY/DO NOT WRITE THE CONCLUSION/RESOLUTION for the story, follow the outline provided you need to start where Part 1 left off and end in a spot that transitions smoothly into part 3,  Leave story open ended:  this is part 2 (Middle - Rising Action & conflict building up to the climax but not quite kicking the climax off yet, leave the final scene on a cliff hanger going into the next section)  out of 3 parts, start to finish building the rising action and reach the climax, you can reveal the major plot twists in part 2, build up the story for the final Climax, you should not go into detail of the climax, but rather explain the build up and set up the story to lead into part 3 with the climax rearing to go. , that is up to you, definitely have all characters introduced and set up the third part. Do not wrap up the entire story leave room for falling action and resolution in part 3"
            elif x1 == 3 or countPart == 3:
                PartNumFix = "this is the final part of the STORY (End - Climax & Falling Action & Resolution/Conclusion) , This should be the most exciting part right off the bat using the prior details continue where the plot is and start to complete the story.  wrap up the plot and other arc plots and make the story interesting and entertaining, build off the prior details and also use the outline provided for guidance. Your next set of scenes should start where the prior part ended and your Story should end according to the outline you have been provided saying how to end this part of the story. "

            elif x1 == 4:
                PartNumFix = "this is the final part of the STORY (End - Climax & Falling Action & Resolution/Conclusion) , This should be the most exciting part right off the bat using the prior details continue where the plot is and start to complete the story.  wrap up the plot and other arc plots and make the story interesting and entertaining, build off the prior details and also use the outline provided for guidance. Your next set of scenes should start where the prior part ended and your Story should end according to the outline you have been provided saying how to end this part of the story. Note: This is more or less an error because you were supposed to write only 3 parts. For this part, focus on the climax of the story and come up with an alternate way of portraying the climax and how the events can unfold. Come up with a small Arc plot that can be related to something earlier in the story, you must resolve it. Also you can  create an origin story for the villain/antagonist in the story, you can also create origin stories for any of the characters you would like, make it fun and try to provide a new perspective to the story that can be explored further, maybe even come up with a scene from way in the past that sets the stage for the final scenes/final climax. Was there a prior friendship ruinded, did someone murder their family member in the past etc. Make sure it fits the tone and context of the story. If you are not given enough context or information about the outline you are supposed to work with, try to use the information provided about the characters to at least write an alternate storyline for them, you can also right dream sequences that are redherrings of the final scenes/climax, or you can write a scene that is from a random person's perspective, be creative these will end up being cool additional storylines that can be used in unique ways to make the story different. Try your best to make the story in the same world/universe as the original story it will be more interesting if they cross over in terms of characters, story elements, settings, etc. "



            #PartNumFix = "DO NOT RESOLVE THE STORY"

            Background = PartNumFix + ''



            if x1 > 1:
                self.Episode1 = False
                Background = PartNumFix + " Use the following information for reference, do not repeat the information, but build off it and use it as a reference to the prior details of the story you are writing. Your response should update how the storyline ends and how the storyline starts based on the prior information, also update the details of the storyline so that it has no plot holes and continues the story from the prior part . this is the summary of the prior part, do not break continuity or ruin the themes/storylines being set up. (DO NOT BE REPETETIVE, KEEP CONTINUITY AND ADAPT THE OUTLINE BASED ON PRIOR ACTIONS/EVENTS FROM THE STORY)" + self.Prior_Episode


            if "FAMIL" in self.Mode.upper() or "CHILDREN" in self.Mode.upper() or "KID" in self.Mode.upper():
                Background = ""
                Story.getCharacters(self, Text = """STORY: ### """ + NewStory_Outline1 + """###   CHaracters to Recycle/Use as Reference, Add New Characters to make the story fresh. Bad guys should be new and the conflict should be new so mix it up. Take some of the minor characters and make them major characters now, have a main character be a minor character. Characters: ###""" + self.Characters2 + "###")
                self.Characters2 = self.Characters


            NewStory_Outline2 = Story.Basic_GPT_Query(self,
                                                     Line2_Role=self.Story_Role,
                                                     Line3_Format=Outline_Expand_Format,
                                                     Background= Background +  """Use the following  Text  as a source for your Outline/response   IDEA/Outline:###""" + NewStory_Outline1 + """### Characters: ###""" + self.Characters2 + """###""",
                                                     Line4_Task=Outline_Expand_Task,
                                                     crazy=self.crazy, Big=True, User_Confirm=self.UserConfirm,
                                                     WINDOWNAME="Story Outline (NewStory_Outline2)", Line1_System_Rule=self.systemPrompt)





            NewStory_AllScenes_Outline = Story.Basic_GPT_Query(self,
                                                                Line2_Role=self.Story_Role,
                                                                Line3_Format=AllScenes_Outline_Format,
                                                                Background=  """. Use the following  Text  as a source/Outline for your Story (Expand on the ideas and give the details for the part of your story provided in the following text)  Text:###""" + NewStory_Outline2 + "###" ,
                                                                Line4_Task=AllScenes_Outline_Task,
                                                                crazy=self.crazy, Big=True,
                                                                User_Confirm=self.UserConfirm,
                                                                WINDOWNAME="Short Story New - Part " + str(x1), Line1_System_Rule= self.systemPrompt )

            #Outline_ALL_Episodes =
            self.NewStory_AllScenes_Outline = NewStory_AllScenes_Outline

            self.Outline_Episodes_Details = self.Writer_Style_Summary

            cu.SaveCSV(Text=NewStory_AllScenes_Outline, SavePath=self.SavePath_Outlines, Title=self.FileName + '_All Scenes Part ' + str(x1))

            self.Story_Role2 =  """You are a brilliant assistant who is Role Playing as an award winning writer able to impersonate any genre or style/voice. Make sure you completely respond to the requests I provide and if I tell you the 'Desired Format:' I expect it to be exact based on your role playing persona on the following details""" + self.Outline_Episodes_Details


            self.Scene_by_Scene = Story.cutBy(self, Text= NewStory_AllScenes_Outline , upperWord=upperWord, Delimiter=Delimiter,
                                              DelimiterCheck=DelimiterCheck, ReplaceKey=ReplaceKey)

            self.SceneCounts = len(self.Scene_by_Scene)
            Story.FullScene(self)
            Story.CreateEpisode(self)






    # this is where you add code to go scene by scene and update characters etc.

    def ReWrite(self, Text):
        self.Story_Role = 'Role Play as an award winning writer able to impersonate any genre or style/voice base your persona on the following Text  Text: '  + self.Writer_Style_Summary

        ReWrite = Story.Basic_GPT_Query(self,
                                                    Line2_Role=self.Story_Role,
                                                    Line3_Format=self.Rewrite_Format,
                                                    Line4_Task=self.Rewrite_Task + """Use the following  Text  as a source for your rewrite   Text:###""" + Text,
                                                    crazy=self.crazy,
                                                    Subject='', User_Confirm = self.UserConfirm , WINDOWNAME="ReWrite ", Line1_System_Rule= self.systemPrompt)

        return ReWrite



        #Next Steps
        #First and foremost find out why its not outputting anything - its stopping before it makes the Episode Specific Info
        #Create art in another thread for the original outlines
        #Trim the fat
        #make it work better
        #remove redundancies
        #clean up formats so they run smoother
        #Make sure the prior info is being passed in correctly
        #make it more dynamic so it does not need to be hard coded for all types if I only run a subset of outputs


        # print(self.Writer_Summary)
        # print(up.breakupOutput2)
        # print(self.Writer_Style_Summary)
        # print(up.breakupOutput2)
        # print(self.IDEA)
        # print(up.breakupOutput2)
        # print(self.IDEA_Final)
        # print(up.breakupOutput2)
        # print(self.Outline_Main)
        # print(up.breakupOutput2)
        # print(self.Outline_Main_Summary)
        # print(up.breakupOutput2)
        # print(self.Outline_Main_Style)
        # print(up.breakupOutput2)
        # print(self.Series_Length)
        # print(up.breakupOutput2)
        # print(self.Characters)
        # print(self.Art_Style_For_Story)
        # print(self.Outline_ALL_Seasons)

        #Set up so you can feed in a specific outline



        #Take an idea and make a blog post
        #take an idea and make a series of post/research topic
        #take a complex idea and make a unique study guide
        #take a long text and rewrite it, maybe make it so it can take any size text and make the adjustments (feed in 3000 characters in or less at a time, break it up by paragraphs.punctuation)



    def TheatricalPreview(self, Text):
        d = 100
        Preview = ''
        # try:
        #     Preview = Story.Basic_GPT_Query(self,
        #                                              Line2_Role=self.Story_Role,
        #                                              Line3_Format=StoryMode.Theatrical_Format,
        #                                              Line4_Task=StoryMode.Theatrical_Task + Text,
        #
        #                                               crazy=self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME="Theatrical")
        #
        #     cu.SaveCSV(Text=Preview,SavePath=self.SavePath, Title=self.FileName+ '_Theatrical Preview')
        #     FileName=self.FileName + '_Theatrical Preview'
        #     #Voice = random.choices(SAF.Original_List_of_Voices_English[0])
        #     cu.SaveText2Audio(SavePath=self.SavePath, FileName=FileName,
        #                       Neural='Neural',
        #                       Mode='AUDIOBOOK', Chunk_Limit=self.Chunk_Limit, Artist_Persona=self.Art_Style_For_Story, Translate=self.Translate,
        #                       Text=Preview)
        #
        # except:
        #     print("Error trying to make theatrical preview")


        return Preview
    def conceptArt(self):
        try:
            self.Characters_List = Story.cutBy(self, Text=self.Characters, upperWord='Name', Delimiter='@@',
                                              DelimiterCheck='@NAME', ReplaceKey='@@NAME')

            for x in self.Characters_List:
                if x != '':
                    ArtPrompt = Story.GPTArt2(self, ArtFormat=self.Art_Style_For_Story, User_Subject=x, prompt = "Use the following styles as a guide to create a unique piece of art based on the following text. Text: " )
                    print(ArtPrompt)
                    originalFilepath = Story.makeArt(self, Prompt=ArtPrompt)
                    PicNewPath1 = Path(PureWindowsPath(self.SavePath , self.Mode))
                    cu.Check_Folder_Exists(PicNewPath1)
                    PicNewPath = Path(PureWindowsPath( PicNewPath1 ,self.Title + '.png'))

                    shutil.copyfile(originalFilepath, PicNewPath)

        except:
            print('Error making concept art')

    def getMainOutlines(self, IDEA = ''):
        self.Series_Length ="For Reference Episode_Constraints:  {Seasons:{" + str(self.numSeasons) + """}    Episodes:{""" + str(self.numEpisode) + """}}"""
        self.Outline_Main_AddOn_Pre = self.Outline_Main_AddOn_Pre +  self.Series_Length

        self.Outline_Main = Story.Basic_GPT_Query(self,
                                                          Line2_Role='Take on the following writer persona:' + self.Writer_Style_Summary,
                                                          Line3_Format=self.Story_Outline_Main_Format,
                                                          Line4_Task=self.Outline_Main_AddOn_Pre  + self.Story_Outline_Main_Task + IDEA,
                                                          Special='',
                                                          crazy=self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME="Outline Main", Line1_System_Rule= self.systemPrompt)


        self.Outline_Main_Style = Story.Basic_GPT_Query(self,
                                                 Line2_Role='Take on the following writer persona:' + self.Writer_Style_Summary,
                                                 Line3_Format=self.Story_Style_Details_Format,
                                                 Line4_Task=self.Story_Style_Details_Task + self.Outline_Main,
                                                 Special='',
                                                  crazy=self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME="Outline Main Style", Line1_System_Rule= self.systemPrompt)

        self.Story_Role = """You are a brilliant assistant who is Role Playing as an award winning writer able to impersonate any genre or style/voice. Make sure you completely respond to the requests I provie and if I tell you the 'Desired Format:' I expect it to be exact base your role playing persona on the following details""" + self.Outline_Main_Style

        self.Outline_Main_Summary = Story.Basic_GPT_Query(self,
                                                 Line2_Role= self.Story_Role,
                                                 Line3_Format=self.StoryDetails_Format,
                                                 Line4_Task=self.StoryDetails_Task +  self.Outline_Main + IDEA,
                                                 Special='',
                                                  crazy=self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME="Outline Main Summary", Line1_System_Rule= self.systemPrompt)



        # self.Series_Length = Story.Basic_GPT_Query(self,
        #                                          Line2_Role='Take on the following writer persona:' + self.Writer_Style_Summary,
        #                                          Line3_Format=self.Story_length_Details_Format,
        #                                          Line4_Task=self.Story_length_Details_Task + self.Outline_Main,
        #                                          Special='',
        #                                           crazy=self.crazy)

        self.Outline_progression += up.breakupOutput2 + 'IDEA Summary: ' + self.IDEA_Final
        self.Outline_progression += up.breakupOutput2 + 'Outline - Main - Most High Level: ' + self.Outline_Main
        self.Outline_progression += up.breakupOutput2 + 'Outline - Main - StoryLine Summary: ' + self.Outline_Main_Summary
        self.Outline_progression += up.breakupOutput2 + 'Outline - Main - Style Details: ' + self.Outline_Main_Style





    def cutBy(self, Text, Delimiter, DelimiterCheck, ReplaceKey,upperWord):
        x = 100
        Text_List = ['']
        uWord = upperWord.upper()
        Text = Text.replace(upperWord, uWord)


        if DelimiterCheck in Text:
            Text = Text.replace(DelimiterCheck, ReplaceKey)
            Text2 = Text.split(Delimiter)

        else:

            Text = Text.replace(uWord, ReplaceKey)
            Text2 = Text.split(Delimiter)


        for s in Text2:
            if uWord in s.upper():
                Text_List.append(s)

        return Text_List


    def SavePreFiles(self):
        data = ''
        AudioBook_Text = ''


        Text = self.Outline_Main
        if 'REWRITE' in self.Mode.upper():
            Text = self.IDEA_Final

        try:

            TrimCharR = self.Outline_Main.find("#Episode") + 1
            TrimCharL = self.Outline_Main.find("Title:")

            Title = self.Outline_Main[TrimCharL:TrimCharR]



        except:
            Title = ''
            try:
                Text = self.Outline_Main
                Title = Story.Quick_Title(self, Text=Text)

            except:
                Title = ''


        if Title == '':
            try:
                Title = Story.Quick_Title(self, Text=Text)

            except:
                Title = 'MondeVert_SHAINE_Confidential_AudioBook'

        Title = Title.replace("The Title:", "")
        Title = Title.replace("Title:", "")
        Title = Title.replace("The Title", "")
        Title = Title.replace("Title", "")

        TitleOO = Title


        if len(Title) > 90:
            Title = Title[:44]

        Title1 = cu.CleanFileName(Title)
        Title1 = Title1.strip()
        self.FileName = Title1
        self.SavePath = Path(PureWindowsPath(self.SavePath , Title1))
        cu.Check_Folder_Exists(self.SavePath)
        cu.Check_Folder_Exists(Path(PureWindowsPath(self.SavePath  ,'Outlines')))

        self.SaveTranscript = True
        FileName_Char_Main = Title1 + '_Main Characters_'
        FileName_Char_Minor = Title1 + '_Minor Characters_'
        # Call Character art prompt


        print('self.Mode')
        print(self.Mode)

        if 'REWRITE' in self.Mode.upper():

            Text2Add = 'Writer: ' + self.Writer_Summary + up.breakupOutput + 'Writer Style: ' + self.Writer_Style_Summary + up.breakupOutput + 'ReWrite: ' + self.ReWrite + up.breakupOutput + 'Original IDEA: ' + self.IDEA + up.breakupOutput + 'Final IDEA: ' + self.IDEA_Final
            FileName_Details_Pre = self.FileName + ' PreProduction'
            cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=Path(PureWindowsPath(self.SavePath , 'Outlines')))

        else:
            Text2Add = 'Story Outline: ' + self.Outline_Main + up.breakupOutput + 'Story Details: ' + self.Outline_Main_Summary + up.breakupOutput2 + 'Story Details(fine): ' + self.Outline_Main_Style + up.breakupOutput2 + 'All Seasons Outline: ' + self.Outline_ALL_Seasons + up.breakupOutput + 'Characters: ' + self.Characters + up.breakupOutput2 + up.breakupOutput + 'Writer Persona: ' + self.Writer_Summary + up.breakupOutput2 + up.breakupOutput + 'Writer Persona Summary: ' + self.Writer_Style_Summary + up.breakupOutput2 + up.breakupOutput + 'Artist Persona: ' + self.Art_Style_For_Story + up.breakupOutput2 + up.breakupOutput + 'Original IDEA: ' + self.IDEA + up.breakupOutput + 'Final IDEA: ' + self.IDEA_Final
            FileName_Details_Pre = self.FileName + ' PreProduction'
            cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=Path(PureWindowsPath(self.SavePath ,'Outlines')))




    def Character_Summary(self, Outline, Season = 0, Episode = 0,Scene = 0, windowname = "Character Summary"):
        x = 100

        Characterst = self.Characters
        # if len(Characterst) > 4000:
        #     Characterst = Characterst[:4000]

        CharactersTrim = Story.Basic_GPT_Query(self,
                                                   Line2_Role=self.Story_Role,
                                                   Line3_Format=StoryMode.Characters_Format_Fine,
                                               Background="""based on the Reference Text to be provided, Pick specific characters from the following list of characters that coorespond with the outline you were provided  (you can introduce your own characters if needed, but keep the main characters involved) CHARACTERS: """ + Characterst,
                                                   Line4_Task=StoryMode.Characters_Task_Fine + """ Reference Text:###""" + Outline[:4000] + """###""",
                                                   crazy=self.crazy,
                                                   Subject='', Big=True, User_Confirm =  self.SmallPromptUser , WINDOWNAME=windowname, Line1_System_Rule= self.systemPrompt)

        if Episode == 0 and Scene == 0:
            text1 = 'Characters Used for Season ' + str(Season)
        elif Scene == 0:
            text1 = 'Characters Used for  Season ' + str(Season) + ' Episode ' + str(Episode)
        else:
            text1 = 'Characters Used for of Season ' + str(Season) + ' Episode ' + str(Episode) + ' Scene ' + str(
                Scene)

        self.Character_progression += up.breakupOutput2 + text1 + ': ' + CharactersTrim

        return CharactersTrim


    def Character_Update(self, Outline, Season = 0, Episode = 0,Scene = 0, Characters_Update_Format  = StoryMode.Characters_Update_Format,Characters_Update_Task  = StoryMode.Characters_Update_Task ):
        x = 100
        try:
            Characters1 = Story.Basic_GPT_Query(self,Line2_Role=self.Story_Role,
                                                    Line3_Format=Characters_Update_Format,
                                                    Background= """" Update the following character descriptions based on the reference text to be provided.  Characters ###: """ + self.Characters+ "###",
                                                    Line4_Task=Characters_Update_Task+ """Use the following Text as background for your Response  Reference Text:###""" + Outline[:4000] + "###",
                                                    crazy=self.crazy,
                                                    Subject='', User_Confirm = self.MainPromptUser, WINDOWNAME="Character Update - Season: " + str(Season) +"Episode: " +  str(Episode) +"Scene: "+ str(Scene), Line1_System_Rule= self.systemPrompt)

            try:
                CheckSize = len(self.Characters) * .44

                if len(Characters1) > CheckSize:
                    self.Characters = Characters1

                    if Episode ==0 and Scene ==0:
                        text1 = 'Characters Updated as of Season ' + str(Season)
                    elif Scene ==0:
                        text1 = 'Characters Updated as of Season '  + str(Season) + ' Episode ' + str(Episode)
                    else:
                        text1 = 'Characters Updated as of Season ' + str(Season) + ' Episode ' + str(Episode) +  ' Scene ' + str(Scene)
                    self.Character_progression += up.breakupOutput2 +  text1  + ': ' + self.Characters
            except:
                print("Could not update the Characters")
        except:
            print("Could not update the Characters")



    def SummarizeText(self, Text, windowname = "Summarize"):
        c = 1
        Summarized_text = Story.Basic_GPT_Query(self, Line2_Role=self.Story_Role,
                                                   Line3_Format=self.Story_Summarize_Format,
                                                   Line4_Task=self.Story_Summarize_Task + """ Use the following text for the source of information Text:###""" + Text ,
                                                   crazy=self.crazy,
                                                   Subject='', User_Confirm =  self.SmallPromptUser, WINDOWNAME = windowname, Line1_System_Rule= self.systemPrompt)


        return Summarized_text

    def WriteStory(self):
        x = 1
        Story1 = ''
        Story2 = ''
        Story4 = ''
        Story5 = ''
        Story3 = ''
        PriorScene = ''

        PriorScenes = ''
        for type in self.OutputTypes:
            # try:
            #     current_time1 = datetime.datetime.now()
            #     current_time = self.current_time1.strftime('%m-%d-%Y_%H.%M')
            #     a = current_time
            #     b = self.current_time
            #
            #     c = a - b
            #
            #     minutes = c.total_seconds() / 60
            #     print('Total difference in minutes: ', minutes)
            #
            #     # returns the difference of the time of the day
            #     minutes = c.seconds / 60
            #     if minutes > 250:
            #         continue
            #         sys.exit()
            #     if minutes > 251:
            #         sys.exit()
            #
            # except:
            #     dn = 100

            try:



                # SceneDetailinfo = "Season " + str(self.Season_num) + ' Episode ' + str(
                #         self.Episodenum) + ' Scene ' + str(self.Scene_Num)

                if type == "Poem":
                    # WritingFormat = StoryMode.Short_Story_Format
                    # WritingTask = StoryMode.Short_Story_Task2

                    WritingFormat = StoryMode.Short_Story_Task_Poem
                    WritingTask = StoryMode.Short_Story_Format_Poem

                    Prior_Scene = self.Prior_Scene_a
                    Prior_Scenes = self.Prior_Scenes
                    # Details = 'Season ' + str(self.Season_num) + ' Episode #' + str(self.Episodenum) + ' Scene # ' + str(
                    #     self.Scene_Num)
                    Details = 'Season ' + str(self.Season_num) + ' Part #' + str(
                        self.Episodenum) + ' Poem # ' + str(
                        self.Scene_Num)
                    Prior_Scenes = self.Prior_Scenes_a
                elif type == 'Novel':
                    WritingFormat = StoryMode.Short_Story_Format_Novel_Chapter
                    WritingTask = StoryMode.Short_Story_Task_Novel_Chapter
                    Prior_Scene = self.Prior_Scene_n

                    Details = 'Book ' + str(self.Season_num) + ' Act ' + str(
                        self.Episodenum) + ' Chapter # ' + str(
                        self.Scene_Num)
                    Prior_Scenes = self.Prior_Scenes_n
                    Details2 = 'Book ' + str(self.Season_num) + ' Act' + str(self.Episodenum)
                elif type == 'Play':
                    WritingFormat = StoryMode.Short_Story_Format_Play_Scene
                    WritingTask = StoryMode.Short_Story_Task_Play_Scene
                    Prior_Scene = self.Prior_Scene_p

                    Details = 'Part ' + str(self.Season_num) + ' Act' + str(
                        self.Episodenum) + ' Scene # ' + str(
                        self.Scene_Num)
                    Prior_Scenes = self.Prior_Scenes_p
                    Details2 = Details
                elif type == 'ScreenPlay':
                    WritingFormat = StoryMode.Short_Story_Format_Screenplay_Scene
                    WritingTask = StoryMode.Short_Story_Task2
                    Prior_Scene = self.Prior_Scene
                    Prior_Scenes = self.Prior_Scenes
                    Details = 'Season ' + str(self.Season_num) + ' Episode #' + str(self.Episodenum) + ' Scene # ' + str(
                        self.Scene_Num)
                    Details2 = 'Season ' + str(self.Season_num) + ' Episode #' + str(self.Episodenum)
                elif type == 'Song':
                    WritingFormat = StoryMode.Short_Story_Format_PlayMusical_Scene
                    WritingTask = StoryMode.Short_Story_Task_PlayMusical_Scene
                    Prior_Scene = self.Prior_Scene_s
                    Prior_Scenes = self.Prior_Scenes_s
                    Details = 'Part ' + str(self.Season_num) + ' Act' + str(
                        self.Episodenum) + ' Scene # ' + str(
                        self.Scene_Num)
                    Details2 = Details

                if self.Episode1 == True and self.Season1 == True and self.Scene1 == True:
                    self.Background_Scene = 'this is the opening scene...... Make it exciting!'
                    self.Prior_Scenes = ''
                    self.Prior_Scenes_a = ''
                    self.Prior_Scenes_p = ''
                    self.Prior_Scenes_n = ''
                    self.Prior_Scenes_s = ''
                elif self.Episode1 == True and self.Season1 == False and self.Scene1 == True:
                    self.Background_Scene = 'Make sure the Outline you make for this scene makes sense given the past events in the story if the original outline provided is not 100% logical make the neccesary adjustments to make the story you outline make sense and not completely random. ' + self.Story_Background_Task + " Prior Season (Do Not Repeat, but potentially build off this): ###" + self.Prior_Season + "###"

                    # self.Background_Scene = self.Story_Background_Task + self.Prior_Season
                    self.Prior_Scenes = ''
                    self.Prior_Scenes_a = ''
                    self.Prior_Scenes_p = ''
                    self.Prior_Scenes_n = ''
                    self.Prior_Scenes_s = ''
                elif self.Scene1==True:

                    # self.Background_Scene = self.Story_Background_Task + self.Prior_Episode
                    self.Background_Scene = 'Make sure the Outline you make for this scene makes sense given the past events in the story if the original outline provided is not 100% logical make the neccesary adjustments to make the story you outline make sense and not completely random. ' + self.Story_Background_Task + " Prior Episode (Do Not Repeat, but potentially build off this): ### " + self.Prior_Episode + "###"

                    self.Prior_Scenes = ''
                    self.Prior_Scenes_a = ''
                    self.Prior_Scenes_p = ''
                    self.Prior_Scenes_n = ''
                    self.Prior_Scenes_s = ''

                else:
                    # self.Background_Scene = self.Story_Background_Task + PriorScenes

                    self.Background_Scene = 'Make sure the Outline you make for this scene makes sense given the past events in the story if the original outline provided is not 100% logical make the neccesary adjustments to make the story you outline make sense and not completely random. ' + self.Story_Background_Task  + " Prior Scene (Do Not Repeat, but potentially build off this) Prior Scene: ###" + Prior_Scenes + "###"


                try:
                    self.Outline_progression += "Prior Scene Details as of  " + str(self.Season_num) + ' Episode ' + str(
                        self.Episodenum) + ' Scene ' + str(self.Scene_Num) +  " Type " + type + ": " + Prior_Scene


                    self.Backgrounds += Details + self.Background_Scene
                except:
                    dn=100

                # "Play", "Novel", "ScreenPlay", "Song"
                try:
                    Episode_Story = self.FileName  + ' - Error making Scene # ' + str(self.Scene_Num) + 'Episode #' + str(self.episode_num) + " For the following Type: " + type
                except:
                    Episode_Story = 'Major error'

                try:
                    Story1 = Story.Basic_GPT_Query(self, Line2_Role=self.Story_Role2,
                                                       Line3_Format=WritingFormat,
                                                        Background= self.Background_Scene,
                                                       Line4_Task= WritingTask + """      Scene Outline: """ +  self.Outline_Scene ,
                                                       crazy=self.crazy,Big=True, User_Confirm = self.MainPromptUser, WINDOWNAME= "Writing Story - " + type + "   "+ Details, Line1_System_Rule= self.systemPrompt)
                    Episode_Story = Details +  ': '+ Story1 + up.breakupOutput2

                    try:
                        Savepath1 = Path(PureWindowsPath(self.SavePath ,'Outlines' ))
                        cu.Check_Folder_Exists(Savepath1)
                        cu.SaveCSV(Text=Episode_Story, SavePath=Savepath1,
                               Title=self.FileName +' Live - '+ Details + self.current_time)
                    except:
                        print("Error Saving File")

                    if type == "Poem":
                        self.Episode_Story_Audio += Episode_Story

                        self.LiveAudio += Episode_Story

                        try:
                            cu.SaveCSV(Text=self.LiveAudio, SavePath=self.SavePath,
                                       Title=self.FileName + ' Live Poem Book  ' + self.current_time)

                        except:
                            print("Error Saving File")

                        self.Prior_Scene_a = Story.SummarizeText(self, Text=Story1)
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_a = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_a)
                        else:
                            self.Prior_Scenes_a = self.Prior_Scene_a

                    elif type == 'Novel':
                        self.Episode_Story_Novel += Episode_Story
                        self.LiveNovel += Episode_Story

                        try:
                            cu.SaveCSV(Text=self.LiveNovel, SavePath=self.SavePath,
                                       Title=self.FileName + ' Live Novel  ' + self.current_time)

                        except:
                            print("Error Saving File")

                        self.Prior_Scene_n = Story.SummarizeText(self, Text=Story1, windowname = "Summarize Previous Scene - Novel (self.Prior_Scene_n)" + Details)
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_n = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_n, windowname = "Summarize Previous Scenes - Novel (self.Prior_Scenes_n)" + Details)
                        else:
                            self.Prior_Scenes_n = self.Prior_Scene_n

                        self.Prior_Scene_Golden = self.Prior_Scene_n
                        if "ScreenPlay" not in self.OutputTypes :
                            self.Prior_Scene = self.Prior_Scene_n
                            self.Prior_Scenes = self.Prior_Scenes_n

                    elif type == 'Play':
                        self.Episode_Story_Play += Episode_Story
                        self.LivePlay += Episode_Story
                        try:
                            cu.SaveCSV(Text=self.LivePlay, SavePath=self.SavePath,
                                       Title=self.FileName + ' Live Play   ' + self.current_time)

                        except:
                            print("Error Saving File")

                        self.Prior_Scene_p = Story.SummarizeText(self, Text=Story1, windowname = "Summarize Previous Scene - Play (self.Prior_Scene_p) " + Details )
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_p = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_p, windowname = "Summarize Previous Scenes - Play (self.Prior_Scenes_p)" + Details)
                        else:
                            self.Prior_Scenes_p =  "Note The Following Details have already happened for reference only: " + self.Prior_Scene_p

                        if "ScreenPlay" not in self.OutputTypes and "Novel" not in self.OutputTypes :
                            self.Prior_Scene = self.Prior_Scene_p
                            self.Prior_Scenes = self.Prior_Scenes_p


                    elif type == 'ScreenPlay':
                        self.Episode_Story += Episode_Story
                        self.LiveScreenPlay += Episode_Story
                        try:
                            cu.SaveCSV(Text=self.LiveScreenPlay, SavePath=self.SavePath,
                                       Title=self.FileName + ' Live ScreenPlay   ' + self.current_time)

                        except:
                            print("Error Saving File")


                        self.Prior_Scene =  Story.SummarizeText(self, Text = Story1, windowname= 'self.Prior_Scene Summarize')
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene, windowname= 'self.Prior_Scenes Summarize')
                        else:
                            self.Prior_Scenes =  self.Prior_Scene

                    elif type == 'Song':
                        self.Episode_Story_Song += Episode_Story
                        self.LiveMusical += Episode_Story
                        try:
                            cu.SaveCSV(Text=self.LiveMusical, SavePath=self.SavePath,
                                       Title=self.FileName + ' Live Musical    ' + self.current_time)

                        except:
                            print("Error Saving File")

                        self.Prior_Scene_s = Story.SummarizeText(self, Text=Story1, windowname= 'self.Prior_Scene_s Summarize')
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_s = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_s, windowname= 'self.Prior_Scenes_s' )
                        else:
                            self.Prior_Scenes_s =  self.Prior_Scene_s

                except:
                    dn = 100


                try:
                    cu.SaveCSV(Text=self.Prior_Scene, SavePath=Savepath1,
                               Title=self.FileName + ' Live Prior Scene '+ Details + '  '+ self.current_time)

                except:
                    print("Error Saving File")


                try:
                    cu.SaveCSV(Text=self.Prior_Scenes, SavePath=Savepath1,
                               Title=self.FileName + ' Live Prior Scenes '+ Details + '    ' +  self.current_time)
                except:
                    print("Error Saving File")



            except:
                print(self.Title + ' - Error making Scene # ' + str(self.Scene_Num) + 'Episode #' + str(self.episode_num) + " For the following Type: " + type)

            self.Scene1 = False
    def CreateEpisode(self):
        #eventually make this dynamic so it does not fail if we do not have a certain type


        for type in self.OutputTypes:
            try:
                if type == "Poem":

                    self.Version2.append(self.Episode_Story_Audio)
                    FileName_Episode2 = self.FileName + ' Season ' + str(self.Season_num) + ' Part ' + str(
                        self.Episodenum) + ' Poem'
                    Text2Add2 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story_Audio
                    csv2 = cu.SaveCSV(Text=Text2Add2, Title=FileName_Episode2, SavePath=self.SavePath)

                elif type == 'Novel':

                    self.Version3.append(self.Episode_Story_Novel)
                    FileName_Episode3 = self.FileName + ' Act ' + str(self.Season_num) + ' Chapter ' + str(
                        self.Episodenum) + ' Novel'
                    Text2Add3 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story_Novel
                    csv3 = cu.SaveCSV(Text=Text2Add3, Title=FileName_Episode3, SavePath=self.SavePath)
                    PriorEpisodeText = self.Episode_Story_Novel
                    if "ScreenPlay" not in self.OutputTypes :
                        PriorEpisodeText = self.Episode_Story_Novel

                elif type == 'Play':

                    self.Version4.append(self.Episode_Story_Play)
                    FileName_Episode4 = self.FileName + ' Act ' + str(self.Season_num) + ' Part ' + str(
                        self.Episodenum) + ' Play'
                    Text2Add4 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story_Play
                    csv4 = cu.SaveCSV(Text=Text2Add4, Title=FileName_Episode4, SavePath=self.SavePath)
                    if "ScreenPlay" not in self.OutputTypes and  "Novel" not in self.OutputTypes:
                        PriorEpisodeText = self.Episode_Story_Play

                elif type == 'ScreenPlay':
                    self.Version.append(self.Episode_Story)
                    Text2Add = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story
                    FileName_Episode = self.FileName + ' Season ' + str(self.Season_num) + ' EPISODE ' + str(
                        self.Episodenum)
                    csv1 = cu.SaveCSV(Text=Text2Add, Title=FileName_Episode, SavePath=self.SavePath)
                    PriorEpisodeText = self.Episode_Story

                elif type == 'Song':
                    self.Version6.append(self.Episode_Story_Song)
                    FileName_Episode6 = self.FileName + ' Season ' + str(self.Season_num) + ' EPISODE ' + str(
                        self.Episodenum) + ' Song'
                    Text2Add6 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story_Song
                    csv4 = cu.SaveCSV(Text=Text2Add6, Title=FileName_Episode6, SavePath=self.SavePath)

            except:
                'Error Saving Episode File'

        try:
            Text2Add5 = 'Outline_Scene(s): ' + self.Episode_Construction + up.breakupOutput
            FileName_Episode5 = self.FileName + ' Season ' + str(self.Season_num) + ' Episode ' + str(self.Episodenum) + ' Outline '
            try:
                cu.SaveCSV(Text=Text2Add5, Title=FileName_Episode5, SavePath=Path(PureWindowsPath(self.SavePath , 'Outlines')))
            except:
                cu.SaveCSV(Text=Text2Add5, Title=FileName_Episode5, SavePath=self.SavePath)


#this is the new part where it looks at prior story to not repeat
            self.Prior_Episode = Story.SummarizeText(self, Text=PriorEpisodeText, windowname="Summarize -  Prior Episode (self.Prior_Episode)" + str(self.Season_num) + ' EPISODE ' + str(
                        self.Episodenum))

            print(up.breakupOutput)
            print("self.Prior_Episode")

            if self.Prior_Episode == None:
                self.Prior_Episode = ' '
            print(self.Prior_Episode)





            self.Outline_progression += "Prior Episode Details as of  " + str(self.Season_num) + ' Episode ' + str(
                self.Episodenum) + ' Scene ' + str(self.Scene_Num) + ": " + self.Prior_Episode



        except:
            dn= 100


        try:
            Story.Character_Update(self, Outline=self.Prior_Episode, Season=self.Season_num,
                                              Episode=self.Episodenum)
        except:
            d= 100


    def FinalOutputs(self):
        Audio_Script = ''
        ScreenPlay = ''
        Novel = ''
        Play = ''
        Song = ''

        Voice = random.choices(SAF.Original_List_of_Voices_English[0])

        Voice_Audio = Voice

        Voice_Novel = Voice

        Voice_Play = Voice

        # print('translate Langauge:')
        # print(Translate)





        FileName_1 = self.FileName + ' ScreenPlay '

        RunLen = len(self.Version)
        for x in range(0, RunLen):
            ScreenPlay += self.Version[x]
        Text2Add = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + ScreenPlay
        csv1 = cu.SaveCSV(Text=Text2Add, Title=FileName_1, SavePath=self.SavePath)




        FileName_2 = self.FileName + ' Poem'
        RunLen = len(self.Version2)
        for x in range(0, RunLen):
            Audio_Script += self.Version2[x]
        Text2Add2 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Audio_Script
        csv2 = cu.SaveCSV(Text=Text2Add2, Title=FileName_2, SavePath=self.SavePath)




        FileName_3 = self.FileName + ' Novel'
        RunLen = len(self.Version3)
        for x in range(0, RunLen):
            Novel += self.Version3[x]
        Text2Add3 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Novel
        csv3 = cu.SaveCSV(Text=Text2Add3, Title=FileName_3, SavePath=self.SavePath)

        FileName_4 = self.FileName + ' Play'
        RunLen = len(self.Version4)
        for x in range(0, RunLen):
            Play += self.Version4[x]
        Text2Add4 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Play
        csv4 = cu.SaveCSV(Text=Text2Add4, Title=FileName_4, SavePath=self.SavePath)



        FileName_6 = self.FileName + ' Song '
        RunLen = len(self.Version6)
        for x in range(0, RunLen):
            Song += self.Version6[x]
        Text2Add6 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Song
        csv6 = cu.SaveCSV(Text=Text2Add6, Title=FileName_6, SavePath=self.SavePath)





        FileName_5 = self.FileName + ' Outlines '
        RunLen = len(self.Episode_Outline)
        for x in range(0, RunLen):
            self.Episode_Outlines += self.Episode_Outline[x]
        Text2Add5 = "Outline Details: " + up.breakupOutput + self.Outline_progression
        csv5 = cu.SaveCSV(Text=Text2Add5, Title=FileName_5, SavePath=Path(PureWindowsPath(self.SavePath, 'Outlines')))


        FileName_7 = self.FileName + ' Character progression '
        Text2Add7 = ' Character progression: ' + up.breakupOutput + self.Character_progression
        csv7 = cu.SaveCSV(Text=Text2Add7, Title=FileName_7, SavePath=Path(PureWindowsPath(self.SavePath , 'Outlines')))

        FileName_8 = self.FileName + ' Background info Used '

        Text2Add8 = ' All Summaries/Background info: ' + up.breakupOutput + self.Character_progression
        csv8 = cu.SaveCSV(Text=Text2Add7, Title=FileName_8, SavePath=Path(PureWindowsPath(self.SavePath , 'Outlines')))




        #
        # try:
        #
        #     cu.SaveText2Audio(SavePath=self.SavePath, FileName=FileName_4, Voice=Voice,
        #                       Neural='Neural',
        #                       Mode='AUDIOBOOK', Chunk_Limit=1444, Artist_Persona=self.Art_Style_For_Story,
        #                       Text=Text2Add4,
        #                       Translate=self.Translate)
        # except:
        #     print('Error - Not using the normal way of Save Text to Audio')
        #     cu.SaveText2Audio(
        #         FilePath=csv4,
        #         Chunk_Limit=1444, Translate=['English'], Artist_Persona=self.Art_Style_For_Story)
        #


        try:
            # cu.SaveText2Audio(SavePath=SavePath, FileName=FileName_Episode3, Voice=Voice_Novel,
            #                   Neural='Neural',
            #                   Mode='AUDIOBOOK', Chunk_Limit=Chunk_Limit, Artist_Persona=Art_Style_For_Story,
            #                   Text=Text2Add3,
            #                   Translate=Translate)
            #
            #
            #
            # #Do Not Do Yet
            # cu.SaveText2Audio(SavePath=self.SavePath, FileName=FileName_3, Voice=Voice,
            #                   Neural='Neural',
            #                   Mode='AUDIOBOOK', Chunk_Limit=self.Chunk_Limit, Artist_Persona=self.Art_Style_For_Story,
            #                   Text=Text2Add3,
            #                   Translate=self.Translate)

            d = 99
        except:
            print('Error - Not using the normal way of Save Text to Audio')
            cu.SaveText2Audio(
                FilePath=csv3,
                Chunk_Limit=self.Chunk_Limit, Translate=['English'], Artist_Persona=self.Art_Style_For_Story)

    def FullScene(self ):
        x = 1

        Scene_Range = self.SceneCounts
        # print("Number of scenes: ")
        # print (Scene_Range)
        self.Episode_Construction = ''
        for y in range(1, Scene_Range):

            Scene_Num = y
            self.Scene_Num = Scene_Num
            self.Story1 = ''
            self.Story2 = ''
            self.Story4 = ''
            self.Story5 = ''
            self.Story3 = ''

            try:
                if len(self.Scene_by_Scene) >= Scene_Num:
                    Outline_Fine = self.Scene_by_Scene[Scene_Num]
            except:
                print('Review something is up with the way you are error checking here - Full Episode')
                #continue

            self.CharactersTrim = Story.Character_Summary(self, Outline_Fine, Season= self.Season_num, Episode= self.Episodenum, Scene= self.Scene_Num, windowname= 'Characters - Full Scene')

            if self.Episode1 == True and self.Season1 == True and self.Scene_Num == 1:
                self.Background_Scene = 'This is the opening scene, be sure to draw in the audience, make it exciting and peak the curiosity of the audience use the following characters for reference: ' + self.CharactersTrim
            else:
                self.Background_Scene = 'Make sure the Outline you make for this scene makes sense given the past events in the story if the original outline provided is not 100% logical make the neccesary adjustments to make the story you outline make sense and not completely random/illogical. ' + self.Story_Background_Task +  " Prior Scenes (Do Not Repeat, but potentially build off this): " + self.Prior_Scenes + "###" + 'Characters: ###' + self.CharactersTrim +  '###'

            #
            # try:
            #     self.UpdatedOutlineScene = Story.Basic_GPT_Query(self,
            #                                               Line2_Role=self.Story_Role2,
            #                                               Line3_Format=self.Story_Scene_Outline_Format,
            #                                               Background = self.Background_Scene,
            #                                               Line4_Task=self.Story_Scene_Outline_Task + """Use the following  Text Outline as a source for your more detailed/new formatted Outline    Text: :###""" + Outline_Fine,
            #                                               crazy=self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME= "Outline Story (Scene) Revision "  +   str(self.Season_num) + ' Episode ' + str(self.Episodenum) +  ' Scene ' + str(self.Scene_Num) + ": ")
            #
            #




            try:
                self.Outline_Scene = Story.Basic_GPT_Query(self,
                                                          Line2_Role=self.Story_Role2,
                                                          Line3_Format=self.Story_Scene_Outline_Format,
                                                           Background= self.Background_Scene,
                                                          Line4_Task=self.Story_Scene_Outline_Task + """Use the following  Text Outline as a source for your more detailed/new formatted Outline    Text: :###""" + Outline_Fine,
                                                          crazy=self.crazy, User_Confirm = self.MainPromptUser, WINDOWNAME= "Outline Story"  +   str(self.Season_num) + ' Episode ' + str(self.Episodenum) +  ' Scene ' + str(self.Scene_Num) + ": " , Line1_System_Rule= self.systemPrompt)

            except:
                self.Outline_Scene = Outline_Fine

            #newChars = Story.Character_Update(self, Outline=self.Outline_Scene, Season=self.Season_num, Episode=self.Episodenum, Scene = self.SceneNum)
            self.Episode_Construction += up.breakupOutput2 + 'Scene Specific Outline' + self.Outline_Scene
            self.Outline_progression += "Outline " +   str(self.Season_num) + ' Episode ' + str(self.Episodenum) +  ' Scene ' + str(self.Scene_Num) + ": " + self.Outline_Scene


            try:
                Story.WriteStory(self)
            except:
                print('Error Making Scene')

    def FullEpisode(self):
        x = 1
        print('self.EpisodeCounts')
        print(self.EpisodeCounts)

        epnum = self.EpisodeCounts
        for episode_num2 in range(1,epnum ):
            self.Episode_Story = ''
            self.Episode_Story_Audio = ''
            self.Episode_Story_Novel = ''
            self.Episode_Story_Play = ''
            self.Episode_Story_Song = ''
            self.Episodenum = episode_num2
            self.Prior_Episode_Summary = ''
            # print(episode_num2)
            # print(len(Outline_ALL_Episode_list) )

            try:
                if len( self.Episode_by_Episode) >= episode_num2:
                    #print(self.Episode_by_Episode[episode_num2])
                    Outline_All =  self.Episode_by_Episode[episode_num2]
            except:
                print('Review something is up with the way you are error checking here - Full Episode')
                #continue


            try:
                self.Outline_progression += up.breakupOutput2 + 'High Level Outline -  Season ' + str(self.Season_num) + ' Episode ' + str(episode_num2)+ ': ' + Outline_All


                self.CharactersTrim = Story.Character_Summary(self, Outline_All,Season= self.Season_num, Episode= self.Episodenum, windowname= 'Characters - Full Episode')



                if self.Episode1 ==True and self.Season1==True:
                    self.Background_Episode = 'This is the first episode/pilot, be sure to captivate the audience, its ok if not everything makes sense yet, its ok to be mysterious. You should make sure your story fits the number of seasons/episodes provided in the outline. use the following characters for reference: ' + self.CharactersTrim
                else:
                    self.Background_Episode = self.Story_Background_Task  + 'Characters: ###' + self.CharactersTrim + "### Prior Season: " + self.Prior_Episode + "###"



                Outline_Episode = Story.Basic_GPT_Query(self,
                                                            Line2_Role=self.Story_Role,
                                                            Line3_Format=self.Story_Episode_Outline_Format,
                                                            Background = self.Background_Episode,
                                                            Line4_Task=self.Story_Episode_Outline_Task + """Use the following {Text}     Text:###""" + Outline_All ,

                                                            crazy=self.crazy,
                                                            Subject='', User_Confirm = self.UserConfirm, WINDOWNAME= 'High level Outline -  Season ' + str(self.Season_num) + ' Episode ' + str(episode_num2), Line1_System_Rule= self.systemPrompt)

                #newChars = Story.Character_Update(self, Outline=Outline_Episode, Season=self.Season_num, Episode=self.Episodenum)


                Outline_Full_Episode = Story.Basic_GPT_Query(self,
                                                                        Line2_Role=self.Story_Role,
                                                                        Line3_Format=self.Story_Full_Episode_Outline_Format,
                                                                        Background=self.Background_Episode,
                                                                        Line4_Task=self.Story_Full_Episode_Outline_Task + """Episode Outline:### """ + Outline_Episode,
                                                                        crazy=self.crazy,
                                                                        Subject='', Big=True, User_Confirm = self.UserConfirm, WINDOWNAME= 'Detailed Outline -  Season ' + str(self.Season_num) + ' Episode ' + str(episode_num2), Line1_System_Rule= self.systemPrompt)

                self.Outline_Episodes_Details = Story.Basic_GPT_Query(self,
                                                                        Line2_Role=self.Story_Role,
                                                                        Line3_Format=self.Story_Style_Details_Format,
                                                                     Background='Use the prior writing style and character info to create a similar, but unique background/context for this episode  Background: ' + self.Outline_Main_Style + self.CharactersTrim,
                                                                     Line4_Task=self.Story_Style_Details_Task2 + """Episode Outline:### """ + Outline_Episode,crazy=self.crazy,
                                                                        Subject='', User_Confirm = self.UserConfirm, WINDOWNAME= 'Episode Writing Style  ' + str(self.Season_num) + ' Episode ' + str(episode_num2), Line1_System_Rule= self.systemPrompt)

                self.Story_Role2 =self.Story_Role = """You are a brilliant assistant who is Role Playing as an award winning writer able to impersonate any genre or style/voice. Make sure you completely respond to the requests I provide and if I tell you the 'Desired Format:' I expect it to be exact based on your role playing persona on the following details""" +self.Outline_Episodes_Details

                self.Outline_progression += up.breakupOutput2 + 'High level Outline -  Season ' + str(self.Season_num) + ' Episode ' + str(episode_num2) + ': ' + Outline_Episode
                self.Outline_progression += up.breakupOutput2 + 'Detailed Outline -  Season ' + str(self.Season_num) + ' Episode ' + str(episode_num2) + ': ' + Outline_Full_Episode
                self.Outline_progression += up.breakupOutput2 + 'Episode Writing Style  ' + str(self.Season_num) + ' Episode ' + str(episode_num2) + ': ' + self.Outline_Episodes_Details

                self.Episode_Outline.append(Outline_Full_Episode)
                self.Scene_by_Scene = Story.cutBy(self, Text=Outline_Full_Episode, upperWord='Scene', Delimiter='@@',
                                                DelimiterCheck='@SCENE', ReplaceKey='@@SCENE')

                self.SceneCounts = len(self.Scene_by_Scene)
                Story.FullScene(self)
                Story.CreateEpisode(self)

            except:
                print('Error Making episode')

            self.Episode1 = False


    def FullSeason(self):


        self.Season1 = True

        Season_num1 = self.SeasonCounts
        for x in range(1,Season_num1):
            self.Episode1 = True
            self.Scene1 = True
            self.Season_num = x
            Season_num = x


            if x > 1 :
                self.Prior_Season = Story.SummarizeText(self, Text=self.Prior_Season + self.Prior_Episode,windowname="Summarize = Prior Season" + str(self.Season_num) )
                print(up.breakupOutput)
                print("self.Prior_Season")
                print(self.Prior_Season)

            try:
                if len (self.Season_By_Season) >= Season_num:
                    Outline_AllS = self.Season_By_Season[Season_num]
            except:
                continue

            self.Outline_progression += up.breakupOutput2 + 'High Level Outline - Season ' + str(Season_num) + ': ' + Outline_AllS

            # print(up.breakupOutput2)
            # print('Outline_AllS')
            # print(Outline_AllS)
            # print(up.breakupOutput2)

            CharactersTrim = Story.Character_Summary(self, Outline_AllS,Season= self.Season_num, windowname= 'Characters - Full Season')


           #For now not doing this at the season level, will use prior episodes for this though
            # if Season_num == 1:
            #     Outline_Prior = """This is the first season, there is no prior info, but you should tie in foreshadowing and set the plot up for the final season based on the final Season's Outline:""" + self.Season_By_Season[len(self.Season_By_Season)]
            #     Outline_Next = 'Fit your Story into the following '


            #this is where you put code to use the prior season summary/series summary to update the current season's outline

            #Add new code here#############

            if self.Episode1 == True and self.Season1 == True:
                self.Background_Season = "use the following characters along with the outline provided to come up with your response. Characters:  " + CharactersTrim
            else:
                self.Background_Season = "Using the events that have happened make the story make sense logically and when you make this season's outline make it follow the story based on background information, use the original outline as a guide but do not ruin the story by being bound by the outline, make the best story possible." + self.Story_Background_Task +'Characters: ###' + CharactersTrim +"### Prior Season: " +self.Prior_Season + "###"

            Outline_Season = Story.Basic_GPT_Query(self, Line2_Role=self.Story_Role,
                                                             Line3_Format=self.Story_Season_Outline_Format,
                                                            Background=self.Background_Season ,
                                                             Line4_Task=self.Story_Season_Outline_Task + """ Use the following text for the source of information Text:###""" + Outline_AllS ,
                                                             crazy=self.crazy,
                                                             Subject='', User_Confirm = self.UserConfirm, WINDOWNAME='Detailed Outline -  Season ' + str(Season_num), Line1_System_Rule= self.systemPrompt)

            self.Outline_progression += up.breakupOutput2 + 'Detailed Outline -  Season ' + str(Season_num) + ': ' +  Outline_Season

            #newChars = Story.Character_Update(self, Outline = Outline_Season, Season=Season_num)


            # Call Outline - All Episodes
            Outline_ALL_Episodes = Story.Basic_GPT_Query(self,
                                                             Line2_Role=self.Story_Role,
                                                             Line3_Format=self.Story_Full_Season_Outline_Format,
                                                             Line4_Task=self.Story_Full_Season_Outline_Task + 'Keep the number of episodes according to the following restrictions: ' + str(self.numEpisode) + """ Use the following text for the source of information Text:###""" + Outline_Season + """### Use the following characters: """ + CharactersTrim,
                                                              crazy=self.crazy,
                                                             Subject='', User_Confirm = self.UserConfirm, WINDOWNAME='Outline - All Episodes - High Level Episodes Outlines (Full Season ' + str(Season_num) + '):', Line1_System_Rule= self.systemPrompt)

            self.Outline_progression += up.breakupOutput2 + 'Outline - All Episodes - High Level Episodes Outlines (Full Season ' + str(Season_num) + '):'+ Outline_ALL_Episodes

            self.Episode_by_Episode = Story.cutBy(self, Text=Outline_ALL_Episodes, upperWord='Episode', Delimiter='@@',
                                                DelimiterCheck='@EPISODE', ReplaceKey='@@EPISODE')

            self.EpisodeCounts = len(self.Episode_by_Episode)


            # print(up.breakupOutput2)
            # print('Episode_by_Episode')
            # print(self.Episode_by_Episode)
            # print(up.breakupOutput2)

            try:
                Writer_Art_Details =   'Writer_Persona: ' + self.Writer_Summary + 'Writer_Persona_Summary: ' + self.Writer_Style_Summary + 'Art_Style_For_Story: '+self.Art_Style_For_Story
                Text2Add = Writer_Art_Details +  up.breakupOutput2 + self.Outline_progression + up.breakupOutput2 + 'Character progression Details: ' +  self.Character_progression
                FileName_Details_Pre = self.FileName + ' Season ' + str(Season_num) + ' Outlines'
                cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=Path(PureWindowsPath(self.SavePath, 'Outlines')))
            except:
                print('Did not save preproduction file #2')

            Story.FullEpisode(self)

        self.Season1 = False

        #Next steps is to use the prior season to shape the story of the next season (also try to tie it into the next season), do this for episode and scene specific outlines
        #Use the Season by Season text to create a season specific outline, for each season trigger the next level of outlines
        #Update characters along the way so you have the most up to date info and new characters get introduced



    def FullSeries(self):
        self.Prior_Season = ''
        self.Prior_Episode = ''
        self.Prior_Scenes = ''
        self.Prior_Scenes_a = ''
        self.Prior_Scenes_p = ''
        self.Prior_Scenes_n = ''
        self.Prior_Scenes_s = ''
        self.Prior_Scene = ''
        self.Prior_Scene_a = ''
        self.Prior_Scene_p = ''
        self.Prior_Scene_n = ''
        self.Prior_Scene_s = ''
        x = 1
        Outline_ALL_Seasons_list = ['']
        # Call Outline - All Episodes
        print("self.numSeasons")
        print(str(self.numSeasons))

        # Line4_Task='Use the following Outline as additional background for your task: ' + self.IDEA_Final,
        self.Outline_ALL_Seasons = Story.Basic_GPT_Query(self,
                                                         Line2_Role=self.Story_Role,
                                                         Line3_Format=self.Story_Full_Series_Outline_Format,
                                                         Line4_Task=self.Story_Full_Series_Outline_Task + """Use the following High level {Main Outline} as a source for the creating the season by season specific outline you are working on  Outline for each Season in the Series   (It is imperative create descriptions/outlines for    """ +  str(self.numSeasons) + """ @Seasons ) Story Details:"""  + self.Outline_Main_Summary,
                                                          crazy=self.crazy,
                                                          Big=True, User_Confirm = self.UserConfirm, WINDOWNAME= 'Outline - All Seasons - High Level Full Series Outlines: ' , Line1_System_Rule= self.systemPrompt)
        self.Outline_progression += up.breakupOutput2 + 'Outline - All Seasons - High Level Full Series Outlines: ' + self.Outline_ALL_Seasons

        self.Season_By_Season = Story.cutBy(self, Text=self.Outline_ALL_Seasons, upperWord='Season', Delimiter='@@',
                                            DelimiterCheck='@SEASON', ReplaceKey='@@SEASON')



        self.SeasonCounts = len(self.Season_By_Season)







                    #Updated Prompts to be used
                    #Connect all of the features
                    #Run Tests!!!!!!


                    #Other parameters to add
                        #Crazy, Chunk Limit, Make song???

         #Steps

        #1 Set all of the UserInput/AI Input Fields
        #2 Combine Idea and Writer Style to make Writing Style if not already provided (Note if Writing Style is provided we need to reformat it so that it is properly formatted)
                #(have different Prompt for exact vs summarize), exact only reformats, summarize enhances beyond the user's exact input

        #3 Using Idea + Story Type + writing style --> Create Main Characters + Separately create minor characters
            #We should pop in a step here to set the Artist Style so we have it based on the current data we have selected
            #In order to be able to use this, we should maybe make a summary of the characters so we can reference it in a more useful way (not sure this may be too much extra work)


        #4 Using writing style + Idea +  Character Summary--> Full Story Outline
        #5 Update Character Summary  using the Full Story Outline (Make the prompt to have how they start vs what their final description/next major development is like

        #6  using Writing Style + Full Story Outline + updated/condensed Character Summary --> All Seasons Outline (@Season1, @Season2, @Season3)
        #7 Update Character Summary  using the All Seasons Outline
        #8  Using Writing Style +  All Seasons Outline  + updated/condensed Character Summary + Prior @Season's Summary (only if Season# > 1) + Next @Season High Level summary (for last season, have a running list of season by season what has happened high level and then adjust story according to this)
                # --> Full Season Outline (Blow Up for 1 of the @Season Outlines)


            #9 Update Character Summary  using the Full Season Outline (maybe we do not want to do this, not sure)



        #10 Writing Style + Full Season Outline + Character Summary --> All Episodes Outline

            #11 Update Character Summary  using the All Episodes Outline (maybe we do not want to do this, not sure)

        #12 Writing Style + All Episode Outline + Character Summary  + (prior Episode summary) + (Next Episode Orinal @Outline)--> Full Episode Outline

            #13 Update Character Summary  using the Full Episode Outline (maybe we do not want to do this, not sure)

        #14 Writing Style + Full Episode Outline + Character Summary --> All Scenes Outline
        #15 Update Character Summary  using the All Scenes Outline (maybe we do not want to do this, not sure)
        #16 Writing Style + All Episode Outline + Character Summary +  (prior Scene summary) + (Next Scene Orinal @Outline)--> Full Scene Outline
        #17 Update Character Summary  using the Full Scene Outline (maybe we do not want to do this, not sure) - Instead create summary for the specific scene to use based on the Full scene's outline (do this for other areas I flagged like this)
        #18 Using Writing Style + Full Scene Outline + Character Summary --> Scene Text (Final)




        #19 Summarize the Scene Text so it can be referenced by next scene
            #19b Update Character Summary  using the Scene SUMMARY

        #20 Aggregate all scenes + also Scene Summarys --> 1. Episode Text 2. Episode Summary
        #21 Aggregate all Episodes + also Episode Summarys --> 1. Season Text 2. Season Summary

        #22 Save Text files (episode by episode), eventually make 1 file for the entire thing (for Audio recording)
        #23 Create Audio Recording
        #End?

    def getCharacters(self, Text = ''):
        if Text == '':
            Text = self.Outline_ALL_Seasons


        self.Characters = Story.Create_Characters_Short_Story(self, Role=self.Story_Role,
                                                             Task= self.Characters_Special + self.Characters_Task + Text,
                                                             Format=self.Characters_Format, Outline='', crazy=self.crazy)


        self.Character_progression += up.breakupOutput2 + 'Characters Start of Series: ' + self.Characters

    def Create_Characters_Short_Story(self, Task, Format, Outline, Role,Persona = '',
                                      crazy=.5):

        if Persona != '':
            Role = Role + 'For this task you are to assume the role of the following Persona: ###' + Persona + """###"""



        # Make sure to start a master tracker with this information, use the writer persona as part of the data stored (TimeStamp, WriterPersona, Outline, Format, and/or put the prompt together for reference
        Character_Personas = Story.Basic_GPT_Query(self, Line2_Role=Role, Line4_Task=Task, Line3_Format=Format, Big=True, User_Confirm=self.UserConfirm, WINDOWNAME='Create Characters Short Story', Line1_System_Rule= self.systemPrompt)


        return Character_Personas


    def getArtist(self):
        x = 1

    def getArtist_Style(self, Mode = 'Basic', arttext = ''):
        x = 1
        self.Art_Type_Config = ''
        if 'FAMILIA' in Mode.upper():
            self.Art_Type_Config = """This story is for children so the art should mimic a children's book/comic/Cartoon or some other easy to draw, simple paintings that have basic backgrounds and descriptions"""
        try:
            if len(arttext) > 1700:
                arttext = arttext[:1700]
        except:
            dn = 100
        try:
            #
            Artist_Persona = Story.GPTArt2(User_Subject=arttext, ArtFormat=StoryMode.artDetailsFormat,
                                               prompt=self.Art_Type_Config + StoryMode.artDetailsPrompt)
        except:
            try:
                Artist_Persona = Story.GPTArt2(User_Subject=self.Writer_Style_Summary,
                                                   ArtFormat=StoryMode.artDetailsFormat,
                                                   prompt=self.Art_Type_Config + StoryMode.artDetailsPrompt)
            except:
                Artist_Persona = Story.Basic_GPT_Query(self,
                                                         Line2_Role='You are an expert artist master of all disciplines and art styles',
                                                         Line3_Format=StoryMode.artDetailsFormat,
                                                         Line4_Task="Pick a random artist based on the following Text" + arttext,
                                                          crazy=self.crazy, Subject='', User_Confirm = self.UserConfirm, WINDOWNAME='Artist Persona For Art', Line1_System_Rule= self.systemPrompt)
        return Artist_Persona






    def getIDEA(self, IDEA='', Writer_Style = '', Mode = 'AI'):
        x = 1
        self.Subject_Details = ''
        if "MUSIC" in self.Mode.upper():
            if IDEA == '':
                self.IDEA_Task_AI = "Come up with an idea for a Song based on your persona"
            else:
                #self.IDEA_Format = """there needs to be enough details for a full Song to be written, use the details provided and add to it to make it uniquely your own."""
                self.IDEA_Format = MW.Song_Outline_Format_IDEA
                self.IDEA_Task = "You are to use the information given to you to come up with an idea for a song, it can be a story or a general message, do not make it too long but try to make the topics relateable and witty and complex. make the audience think a little but also make the song entertaining"
        elif "COMEDY" in self.Mode.upper():
            if IDEA == '':
                self.IDEA_Task_AI ="Come up with an idea for a Joke or Funny Idea/Comparison/thought/Scenario/Story based on your persona, make it funny and unique."

            self.IDEA_Format = CW.Joke_IDEA_Format
            self.IDEA_Task = CW.Joke_IDEA_Task

        elif "POEM" in self.Mode.upper():
            if IDEA == '':
                self.IDEA_Task_AI ="Ccreate your own detailed outline for a book of poems (with 1 or more intricate stories witin the poetry ideas. You should also make it clear the topics you want to cover, the ideas/beliefs/lessons you want to get accross and how you want your poems to be unique and match your writing persona along with the details provided to you) with plenty of details and characters enough characters, plots and arc plots that can be converted into a full feature length film or a novel/Play. Be detailed and make the poems interesting and poetically make it like a story that is not totally connected but has overlapping events/parts/perspectives/ideas, try to have multiple storylines that intertwine.  Use profanity.swears. bad words like fuck shit bitch, dick, boobs, tits, sex, drugs etc. "

            self.IDEA_Format = PW.IDEA_Format
            self.IDEA_Task = PW.IDEA_Task



        if "FAMIL" in self.Mode.upper() or "CHILDREN" in self.Mode.upper() or "KID" in self.Mode.upper():
            IDEA_ADULT = ''
        else:
            self.IDEA_Task = self.IDEA_Task + SP.IDEA_ADULT


        Subject_Summary = IDEA

        if IDEA == '':
            IDEA_Task = self.IDEA_Task_AI

        else:
            Subject_trim = IDEA[:8000]
            IDEA_Task = self.IDEA_Task + Subject_trim
            self.Subject_Details += 'Subject Trimmed and summary created below:'






        Subject_Summary = Story.Basic_GPT_Query(self,
                                                        Line2_Role=self.IDEA_Role,
                                                        Line3_Format=self.IDEA_Format,
                                                        Line4_Task=IDEA_Task, Special='',
                                                         crazy=self.crazy, Big=True, User_Confirm = self.UserConfirm, WINDOWNAME='IDEA/Subject Summary - Get IDEA', Line1_System_Rule= self.systemPrompt)
        self.Subject_Details += Subject_Summary
        Story.quickArt1(self, Subject_Summary)
        return Subject_Summary




    def  getWriter(self, Persona = ''):
        x = 1
        if Persona != '':
            Persona_Role =  'You are the following Persona use them as a model for the writer you create: ' + Persona
        else:
            Persona_Role = self.Persona_Role

        Writer_Summary = Story.Basic_GPT_Query(self,Line2_Role = Persona_Role,Line4_Task= self.Persona_Task, Line3_Format = self.Persona_Format,  crazy = self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME='Get Writer info',  Line1_System_Rule= self.systemPrompt)
        Story.quickArt1(self, Writer_Summary)
        return Writer_Summary


    def getWriter_Style(self, Writer_Style = ''):
        x = 1
        self.Persona_Role = "You are a brilliant assistant for the user, You are a gifted writer and have a high EQ, despite this you are relateable and understand how to entertain people. you excel at writing lyrics, stories and are a master at any task you are requested"
        # if Writer_Style != '':
        #     Persona_Role =  Persona_Role + 'use/incorporate the following writing styles in your response: ' + Writer_Style
        #


        if  'SONG' not in self.Mode:

            Writer_Style_Summary = Story.Basic_GPT_Query(self, Line2_Role=self.Persona_Role, Line4_Task=self.Persona_Summary_Task + self.Writer_Summary,Line3_Format=self.Persona_Summary_Format, crazy=self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME='Get Writer Style', Line1_System_Rule= self.systemPrompt)
        else:
            Writer_Style_Summary = Story.Basic_GPT_Query(self, Line2_Role=self.Persona_Role,
                                                     Line4_Task= lup.Music_Persona_Task + self.Writer_Summary,
                                                     Line3_Format=lup.Music_Persona_Format, crazy=self.crazy, User_Confirm = self.UserConfirm, WINDOWNAME='Get Song Writer Style', Line1_System_Rule= self.systemPrompt)

        Story.quickArt1(self, Writer_Style_Summary)

        return Writer_Style_Summary




    def quickArt1(self, Text = ''):
        if Text != '':
            try:
                ArtPrompt = Story.GPTArt2(self, User_Subject=Text, prompt='Pick a completely random artist or photographer| art style| theme| mood |and a short prompt for DALL-E (AI-Art generator) to create a work of art/photograph', ArtFormat=self.Art_Persona_Format + ', <Short description of Work of art under 250 characters>')
                try:
                    ArtPath = Story.makeArt(self, Prompt=ArtPrompt)
                    self.PersonaArtPath = ArtPath
                except:
                    dn = 100
            except:
                dn = 100

            try:
                cu.add2Master_Persona(
                    Text=str(self.current_time + '  ' + Text + ' Art File location: ' + ArtPath))

            except:
                dn = 100





    def setPrompts(self):
        self.Persona_Role =StoryMode.Persona_Role
        self.Persona_Task = StoryMode.Persona_Task
        self.Persona_Format = StoryMode.Persona_Format
        self.Persona_Summary_Role =StoryMode.Persona_Summary_Role
        self.Persona_Summary_Task = StoryMode.Persona_Summary_Task
        self.Persona_Summary_Format = StoryMode.Persona_Summary_Format

        self.Outline_Main_AddOn_Pre = StoryMode.Short_Story_Config + StoryMode.Shane_Test_User_Input

        self.Art_Persona_Role =StoryMode.ArtRole
        self.Art_Persona_Task = StoryMode.artDetailsPrompt
        self.Art_Persona_Format = StoryMode.artDetailsFormat

        self.IDEA_Role = StoryMode.IDEA_Role
        self.IDEA_Format = SP.IDEA_Format
        self.IDEA_Task = SP.IDEA_Task

        # if "MUSIC" in self.Mode.upper():
        #     self.IDEA_Format = """Provide enough details for the IDEA to be summarized into a masterpiece lyrically, this should have all info needed to write a song based on the writing persona and/or the original idea provided."""
        #     self.IDEA_Task = """Summarize and expand on the IDEA provided to you and provide enough details to make a lyrical masterpeice (Do not write the song yet, provide details so the lyrics can be written later on with all key details and enough information for AI to use as a base for a song. Use details that are provided and pull from the writing persona to make it original and relateable"""

        self.IDEA_Task_AI = StoryMode.IDEA_Task_AI

        self.Characters_Task = StoryMode.Characters_Task
        self.Characters_Special = StoryMode.Characters_Special
        self.Characters_Role = StoryMode.Characters_Role
        self.Characters_Format = StoryMode.Characters_Format

        self.Story_Outline_Main_Task = StoryMode.Story_Outline_Main_Task
        self.Story_Outline_Main_Format = StoryMode.Story_Outline_Main_Format


        self.StoryDetails_Task = StoryMode.StoryDetails_Task
        self.StoryDetails_Format = StoryMode.StoryDetails_Format

        self.Story_Style_Details_Task = StoryMode.Story_Style_Details_Task
        self.Story_Style_Details_Task2 = StoryMode.Story_Episode_Writing_Style_Task
        self.Story_Style_Details_Format = StoryMode.Story_Episode_Writing_Style_Format

        self.Story_length_Details_Task = StoryMode.Story_length_Details_Task
        self.Story_length_Details_Format = StoryMode.Story_length_Details_Format

        self.Story_Full_Series_Outline_Task = StoryMode.Story_Full_Series_Outline_Task
        self.Story_Full_Series_Outline_Format = StoryMode.Story_Full_Series_Outline_Format

        self.Story_Background_Task = StoryMode.Story_Background_Task

        self.Story_Summarize_Format = StoryMode.Story_Summarize_Format
        self.Story_Summarize_Task = StoryMode.Story_Summarize_Task


        self.Story_Season_Outline_Task = StoryMode.Story_Season_Outline_Task
        self.Story_Season_Outline_Format = StoryMode.Story_Season_Outline_Format

        self.Story_Full_Season_Outline_Task = StoryMode.Story_Full_Season_Outline_Task
        self.Story_Full_Season_Outline_Format = StoryMode.Story_Full_Season_Outline_Format

        self.Story_Episode_Outline_Task = StoryMode.Story_Episode_Outline_Task
        self.Story_Episode_Outline_Format = StoryMode.Story_Episode_Outline_Format

        self.Story_Full_Episode_Outline_Task = StoryMode.Story_Full_Episode_Outline_Task
        self.Story_Full_Episode_Outline_Format = StoryMode.Story_Full_Episode_Outline_Format

        self.Story_Scene_Outline_Format = StoryMode.Story_Scene_Outline_Format
        self.Story_Scene_Outline_Task = StoryMode.Story_Scene_Outline_Task

        self.Story_Episode_Writing_Style_Format = StoryMode.Story_Episode_Writing_Style_Format
        self.Story_Episode_Writing_Style_Task = StoryMode.Story_Episode_Writing_Style_Task

        self.Rewrite_Task = StoryMode.Rewrite_Task
        self.Rewrite_Format = StoryMode.Rewrite_Format




    def Quick_Title(self, Text,Model = "gpt-3.5-turbo", Line1_System_Rule = up.system_TextJoaT_quick, crazy = .5):
        KeepGoing = False
        KillSwitch = 0



        try:

            TrimCharR = Text.find("}") + 1
            TrimCharL = Text.find("Title:")

            Title = Text[TrimCharL:TrimCharR]

            Title = Title.replace("Title", "")

        except:
            Title = ''
            try:
                if len(Text)> 6000:
                    Model= "gpt-3.5-turbo-16k-0613"
                elif len(Text)< 6000:
                    Model = "gpt-3.5-turbo"
                while KeepGoing == False and KillSwitch < 8:
                    try:

                        Line1_System_Rule = Line1_System_Rule
                        Line2_Task_Text = """Text: ###""" + Text + "###"
                        Line3_Format_Text = StoryMode.Title_Format
                        response = openai.ChatCompletion.create(
                            model=Model,
                            messages=[
                                {"role": "system", "content": Line1_System_Rule},
                                {"role": "user", "content": Line3_Format_Text},
                                {"role": "user", "content": Line2_Task_Text}
                            ]
                            , temperature=crazy
                        )
                        Title = response.choices[0].message.content
                        Title = Title.replace("The Title:", "")
                        Title = Title.replace("Title:", "")
                        Title = Title.replace("The Title", "")
                        Title = Title.replace("Title", "")
                        KeepGoing = True
                    except:
                        print(' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                        KillSwitch += 1
                        if KillSwitch == 9:
                            print('could not create a writer persona, redoing it now')
                            Title = 'Unknown title - Too many errors'
                            Title = Title.replace("The Title:", "")
                            Title = Title.replace("Title:", "")
                            Title = Title.replace("The Title", "")
                            Title = Title.replace("Title", "")
                        continue


            except:
                dn = 100
                Title = 'MondeVert Story '


        try:
            if len(Title) > 90:
                Title = Title[:44]

            Title = cu.CleanFileName(Title)
            Title = Title.strip()
            self.FileName = Title
            self.SavePath = Path(PureWindowsPath(self.SavePath, Title))
            cu.Check_Folder_Exists(self.SavePath)
        except:
            dn = 100

        return Title










    def saveTranscript(self):
        cu.saveTranscript(self.transcript_Final, self.current_time)

    def Add2Transcript(self, text2Add):
        self.transcript_Final += text2Add + ' \n'



    def speak(self, audio, Add2T=True, voice=''):
        if voice == '':
            voice = self.voice

        if Add2T == True:
            Story.Add2Transcript(self, self.AssistantName + ': ' + audio)
        engine = pyttsx3.init()
        # getter method(gets the current value
        # of engine property)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice].id)
        # Method for the speaking of the assistant
        if self.SilentMode == False:
            engine.say(audio + "")
            # Blocks while processing all the currently
            # queued commands
            engine.runAndWait()
        else:
            print('Silent Mode Activated: ' + audio)

    #
    # def Basic_GPT_Query2(self,   Line2_Role  , Line5_Task,Line3_Format,Line4_Task,Line1_System_Rule = SP.System,Big = False,Model = "gpt-3.5-turbo",upgradeLimit = 3000, Special = '', crazy = .5, Subject= '', Outline = '', Allowed_Fails = 8, SaveFile = False,MakeArt = False, Mode = 'SHAINE SAYS', SavePath= '',  User_Confirm = True, WINDOWNAME = "SHAINE Advanced - "):#use this to create art style for the work
    #     if SavePath == '':
    #         SavePath = self.SavePath
    #
    #     if Subject != '':
    #         Line2_Role = Line2_Role + """Your role and subject matter expertise should fit the following Subject and or style and mood in the {Text} provided by the user Text:###""" + Subject + """###"""
    #
    #
    #
    #     #Line1_System_Rule = Line2_Role
    #     #Line2_Role = Line2_Role + Special
    #     Full_User_Prompt = """User Inputs to Chat GPT:
    #     1). """ + Line1_System_Rule +"""
    #     2).""" + Line2_Role+ """
    #     3).""" + Line3_Format+ """
    #     4).""" + Line4_Task + """
    #     5).""" + Line5_Task
    #
    #     if len(Full_User_Prompt) > upgradeLimit:
    #         Model = "gpt-3.5-turbo-16k-0613"
    #     elif len(Full_User_Prompt) < upgradeLimit:
    #         Model = "gpt-3.5-turbo"
    #
    #
    #     TryCount = 0
    #     if Big ==True:
    #         Model = "gpt-3.5-turbo-16k-0613"
    #     KeepGoing = False
    #     KillSwitch = 0
    #     while KeepGoing == False and KillSwitch < Allowed_Fails:
    #
    #
    #         try:
    #
    #
    #
    #             # This is for the result if you let the AI describe project and details and then make the response
    #             response = openai.ChatCompletion.create(
    #                 model=Model,
    #                 messages=[
    #                     {"role": "system", "content": Line1_System_Rule},
    #                     {"role": "user", "content": Line2_Role},
    #                     {"role": "user", "content": Line3_Format},
    #                     {"role": "user", "content": Line4_Task },
    #                     {"role": "user", "content": Line5_Task},
    #                 ]
    #                 , temperature=crazy
    #             )
    #             GPT_Response = str(response.choices[0].message.content)
    #
    #             self.UserPromptsCount += 1
    #
    #             self.UserPrompts += 'User Input #' + str(self.UserPromptsCount)
    #
    #             self.UserPrompts += Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2
    #             self.Full_Transcript += 'User Input #' + str(self.UserPromptsCount) + Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2
    #             self.Full_Story += up.breakupOutput + "****Original GPT Response****" + GPT_Response
    #             self.Full_Transcript += up.breakupOutput + "****Original GPT Response****" + up.breakupOutput + GPT_Response
    #
    #             if User_Confirm == True:
    #                 self.promptB = False
    #                 while self.promptB == False:
    #
    #                     speak1 = self.Speak
    #
    #                     TryCount += 1
    #                     if self.promptB == False:
    #                         print("""
    #                         Do you want to
    #                         1). Small Edit, Take the text and switch a few things
    #                         2). ReWrite With Edits (Big Edit)
    #                         3). Rewrite No Edits
    #
    #                         """)
    #
    #                         print(self.UserMode)
    #                         UserMode1 = -1
    #                         if self.UserMode == "UI":
    #                             # try:
    #                             #     example = self.TE.MakeWindow(self.UserPrompts)
    #                             # except:
    #                             #     print("error with example window")
    #
    #                             query = self.TE.MakeWindow(GPT_Response, UserConfirm=True, WindowName = WINDOWNAME + str(TryCount))
    #                             UserMode1 = -1
    #                             UserMode1 = self.TE.GetUserResponseMode()
    #                             print("UserMode1:")
    #                             print(UserMode1)
    #
    #                         else:
    #                             query = cu.getUserResponse()
    #                             self.promptB = cu.ConfirmBOT(GPT_Response, speak1)
    #
    #                         if (( 'one' in query or 'small' in query or 'few' in query or 'mini') and self.UserMode != "UI") or UserMode1 == 1:
    #                             self.promptB = False
    #                             promptB2 = True
    #                             if self.UserMode == "UI":
    #                                 EDIT = query
    #                             else:
    #                                 EDIT = cu.editBotPrompt()
    #                             response = openai.ChatCompletion.create(
    #                                 model=Model,
    #                                 messages=[
    #                                     {"role": "system", "content": Line1_System_Rule},
    #                                     {"role": "user", "content": Line2_Role},
    #                                     {"role": "user", "content": Line3_Format},
    #                                     {"role": "user",
    #                                      "content": "Use the following guidance when completing your task: " + EDIT},
    #                                     {"role": "user",
    #                                      "content": """Rewrite the following text using the edits provided and make it in the respective formate described.  Text: """ + GPT_Response},
    #                                 ]
    #                                 , temperature=crazy
    #                             )
    #                             GPT_Response = str(response.choices[0].message.content)
    #
    #                             self.Full_Story += up.breakupOutput + "****Small Edit****" + EDIT + up.breakupOutput + GPT_Response
    #                             self.Full_Transcript +=  up.breakupOutput + "****Small Edit****" + EDIT + up.breakupOutput + GPT_Response
    #
    #
    #                             WINDOWNAME = WINDOWNAME + " - Small Edit"
    #
    #
    #                         elif (('rewrite' in query or 'with edits' in query or 'redo' in query or 'two' in query) and self.UserMode != "UI") or UserMode1 == 2:
    #
    #                             self.promptB = False
    #                             if self.UserMode == "UI":
    #                                 EDIT = query
    #                             else:
    #                                 EDIT = cu.editBotPrompt()
    #                             response = openai.ChatCompletion.create(
    #                                 model=Model,
    #                                 messages=[
    #                                     {"role": "system", "content": Line1_System_Rule},
    #                                     {"role": "user", "content": Line2_Role},
    #                                     {"role": "user", "content": Line3_Format},
    #                                     {"role": "user",
    #                                      "content": "Use the following guidance when completing your task: " + EDIT},
    #                                     {"role": "user", "content": Line4_Task},
    #                                     {"role": "user", "content": Line5_Task},
    #                                 ]
    #                                 , temperature=crazy
    #                             )
    #                             GPT_Response = str(response.choices[0].message.content)
    #
    #                             self.UserPrompts += up.breakupOutput + "****Rewrite with Edits***:" + EDIT +  up.breakupOutput
    #                             self.Full_Transcript += up.breakupOutput + "****Rewrite with Edits***:" + EDIT +  up.breakupOutput
    #                             self.Full_Story += up.breakupOutput +  "****Rewrite with Edits***:" + EDIT + up.breakupOutput + GPT_Response
    #                             self.Full_Transcript += up.breakupOutput +  "****Rewrite with Edits***:" + EDIT + up.breakupOutput + GPT_Response
    #                             WINDOWNAME = WINDOWNAME + " - ReWrite with Edit"
    #
    #                             WINDOWNAME = WINDOWNAME + " - ReWrite With Edit"
    #
    #                         elif (('full' in query or 'try new' in query or 'new' in query or 'three' in query) and self.UserMode != "UI") or UserMode1 == 3:
    #                             promptB2 = False
    #                             self.promptB = False
    #                             response = openai.ChatCompletion.create(
    #                                 model=Model,
    #                                 messages=[
    #                                     {"role": "system", "content": Line1_System_Rule},
    #                                     {"role": "user", "content": Line2_Role},
    #                                     {"role": "user", "content": Line3_Format},
    #                                     {"role": "user", "content": Line4_Task},
    #                                     {"role": "user", "content": Line5_Task},
    #                                 ]
    #                                 , temperature=crazy
    #                             )
    #                             GPT_Response = str(response.choices[0].message.content)
    #                             self.UserPrompts += up.breakupOutput + "****Rewrite***:" +   up.breakupOutput
    #                             self.Full_Transcript += up.breakupOutput + "****Rewrite***:" +   up.breakupOutput
    #                             self.Full_Story += up.breakupOutput +  "****Rewrite***:"  + up.breakupOutput + GPT_Response
    #                             self.Full_Transcript += up.breakupOutput +  "****Rewrite***:"  + up.breakupOutput + GPT_Response
    #                             WINDOWNAME = WINDOWNAME + " - Full ReWrite"
    #
    #                         elif UserMode1 == 0:
    #                             self.promptB = True
    #                             print("self.promptB:")
    #                             print(self.promptB)
    #
    #
    #
    #                         elif UserMode1 == 4:
    #                             if self.UserMode == "UI":
    #                                 EDIT = query
    #                             else:
    #                                 EDIT = cu.editBotPrompt()
    #                             self.promptB = True
    #                             GPT_Response = EDIT
    #                             WINDOWNAME = WINDOWNAME + " - Used User Text"
    #
    #
    #                         print("Used the following Text  for Response??: " + str(
    #                         UserMode1) + up.breakupOutput + GPT_Response)
    #
    #
    #
    #
    #                     else:
    #                         self.Full_Story +=  up.breakupOutput +"Used the following Text  for Response: " + GPT_Response
    #                         print(
    #                             "Used the following Text  for Response: " + str(UserMode1) + up.breakupOutput + GPT_Response)
    #
    #                         self.Full_Story += up.breakupOutput
    #                         KeepGoing = True
    #             else:
    #                 KeepGoing = True
    #
    #
    #         except:
    #             print(' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
    #             KillSwitch += 1
    #             print(Full_User_Prompt)
    #             #as written this does not run but if I got rid of +1 it could
    #             if KillSwitch == Allowed_Fails+1:
    #                 print('could not create a writer persona, redoing it now')
    #                 GPT_Response = Story.Basic_GPT_Query(self, Line2_Role='You are a skilled writer', Line3_Format=Line3_Format, Line4_Task=Line4_Task, Line1_System_Rule=up.system_Text_ScreenPlay)
    #
    #             continue
    #
    #
    #         #print(up.breakupOutput)
    #
    #         if self.SaveTranscript == True:
    #             try:
    #                 cu.SaveCSV(Text=WINDOWNAME + self.Full_Story, SavePath=self.SavePath,
    #                            Title=self.FileName + ' All Responses Transcript (no Prompts)')
    #                 cu.SaveCSV(Text=WINDOWNAME + self.Full_Transcript, SavePath=self.SavePath,
    #                            Title=self.FileName + ' All Responses and prompts')
    #
    #             except:
    #                 print("could not save files")
    #
    #         Title = Mode + '_' + self.current_time
    #         if SaveFile ==True:
    #             SaveText = self.current_time+ up.breakupOutput2 + self.UserPrompts + up.breakupOutput2 + 'SHAINE SAYS: '+  GPT_Response
    #             print(SaveText)
    #             cu.SaveCSV(Text=SaveText, SavePath=SavePath, Title = Title)
    #         if MakeArt ==True:
    #             ArtPrompt = Story.GPTArt2(self,User_Subject = GPT_Response)
    #             print(ArtPrompt)
    #             originalFilepath = Story.makeArt(self,Prompt=ArtPrompt)
    #             PicNewPath1 = Path(PureWindowsPath(SavePath, Mode))
    #             cu.Check_Folder_Exists(PicNewPath1)
    #             PicNewPath =Path(PureWindowsPath(PicNewPath1,Title + '.png'))
    #
    #
    #             shutil.copyfile(originalFilepath, PicNewPath)
    #         return GPT_Response

    def Basic_GPT_Query2(self, Line2_Role, Line3_Format, Line4_Task, Big=False, Background='', Background2='',
                         Background3='', Model="gpt-3.5-turbo", upgradeLimit=3000, Special='',
                         Line1_System_Rule=SP.System, crazy=.5, Subject='', Outline='', Allowed_Fails=8, SaveFile=False,
                         MakeArt=False, Mode='SHAINE SAYS', SavePath='', User_Confirm=False,
                         WINDOWNAME="SHAINE Basic - ", ReviewPrompts=False, version=1,
                         Retry=True):  # use this to create art style for the work


        CHATGPT = GPT.GPT_Mode()
        GPTResponse = CHATGPT.Basic_GPT_Query()



    def Basic_GPT_Query2(self,   Line2_Role  , Line3_Format,Line4_Task,Big = False,Background = '',Background2 = '', Background3 = '',Model = "gpt-3.5-turbo",upgradeLimit = 3000,Special = '',Line1_System_Rule = SP.System, crazy = .5, Subject= '', Outline = '', Allowed_Fails = 8, SaveFile = False,MakeArt = False, Mode = 'SHAINE SAYS', SavePath= '', User_Confirm = False, WINDOWNAME = "SHAINE Basic - ", ReviewPrompts = False,  version = 1, Retry= True):#use this to create art style for the work
        self.PermanentSetPrompt = False
        ReviewPrompts_Original = ReviewPrompts

        if SavePath == '':
            SavePath = self.SavePath

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
        self.FULLPROMPTONLY = self.CurrentSystem + self.CurrentRole + self.CurrentFormat + self.CurrentTask +self.CurrentBackground  + self.CurrentBackground2 + self.CurrentBackground3




        TryCount = 0
        KeepGoing = False
        KillSwitch = 0
        while KeepGoing == False and KillSwitch < Allowed_Fails:
            TryCount+=1
            try:

                if ReviewPrompts ==True or ReviewPrompts_Original ==True:
                    Story.GPT_Confirm_Prompts(self,  System=self.CurrentSystem,Role=self.CurrentRole, Format=self.CurrentFormat, Task=self.CurrentTask, Background=self.CurrentBackground, Background2=self.CurrentBackground2, Background3=self.CurrentBackground3, User_Confirm = User_Confirm, crazy=self.Current_crazy, TryCount=TryCount, WINDOWNAME="CONFIRM CHAT GPT PROMPTS - " + self.CurrentWindowName, version=self.Currentversion, Model=self.CurrentModel)


                if TryCount > 1:
                    Story.SaveLastGPTResponse( self,GPT_Response=self.Current_GPTResponse)
                    Story.SaveLast_Prompt(self, System=self.CurrentSystem,Role=self.CurrentRole, Format=self.CurrentFormat, Task=self.CurrentTask,Background=self.CurrentBackground, Background2=self.CurrentBackground2,Background3=self.CurrentBackground3,crazy=self.Current_crazy,version = self.Currentversion, Model=self.CurrentModel)

                self.Full_User_Prompt = """User Inputs to Chat GPT: 
                1). """ + self.CurrentSystem + """
                2).""" + self.CurrentRole + """
                3).""" + self.CurrentFormat + """
                4).""" + self.CurrentTask + """
                Background (If Any Provided): """ + self.CurrentBackground + """
                Additional Background: """ + self.CurrentBackground2 +self.CurrentBackground3

                if version == 2:
                    self.NewSystem = cu.Version2GPTSetUp(Format=self.CurrentFormat, System=self.CurrentSystem, Role=self.CurrentRole,
                                                    Background=self.CurrentBackground, Background3=self.CurrentBackground3,
                                                    Background2=self.CurrentBackground2)
                    self.Full_User_Prompt = """User Inputs to Chat GPT: 
                    System: """ + self.NewSystem + """
                    USER: """ + self.CurrentTask

                if len(self.Full_User_Prompt) > upgradeLimit:
                    Model = "gpt-3.5-turbo-16k-0613"
                elif len(self.Full_User_Prompt) < upgradeLimit:
                    Model = "gpt-3.5-turbo"

                if Big == True:
                    Model = "gpt-3.5-turbo-16k-0613"


                self.Current_GPTResponse = cu.ASKGPT(System=self.CurrentSystem,Role=self.CurrentRole, Format=self.CurrentFormat, Task=self.CurrentTask, Background=self.CurrentBackground, Background2=self.CurrentBackground2, Background3=self.CurrentBackground3,  crazy=self.Current_crazy, Model=Model, version=self.Currentversion)
               # Story.SaveOriginalGPTResponse(self, GPT_Response=self.Current_GPTResponse)

                if TryCount == 1:
                    self.Original_GPTResponse = self.Current_GPTResponse



                self.UserPromptsCount += 1

                self.UserPrompts += 'User Input #' + str(self.UserPromptsCount)

                self.UserPrompts += self.Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2
                self.Full_Transcript += 'User Input #' + str(self.UserPromptsCount) + self.Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2
                self.Full_Story += up.breakupOutput + "****Original GPT Response****" + self.Current_GPTResponse
                self.Full_Transcript += up.breakupOutput + "****Original GPT Response****"  + up.breakupOutput + self.Current_GPTResponse


                if User_Confirm == True:
                    KeepGoing = Story.GPT_UserInput_Confirm_Tool(self, GPT_Response=self.Current_GPTResponse, System=self.CurrentSystem,Role=self.CurrentRole, Format=self.CurrentFormat, Task=self.CurrentTask, Background=self.CurrentBackground, Background2=self.CurrentBackground2, Background3=self.CurrentBackground3, crazy=self.Current_crazy, TryCount=TryCount, UserConfirm=User_Confirm, version = self.Currentversion, WINDOWNAME=self.CurrentWindowName)


                else:
                    self.Full_Story += "Final Text used for Response: " + up.LineBreak + self.Current_GPTResponse + up.LineBreak + up.breakupOutput2
                    print("Used the following Text  for Response: " +  + up.LineBreak +self.Current_GPTResponse)
                    KeepGoing = True




            except:
                print(' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                KillSwitch += 1
                print(self.Full_User_Prompt)
                #ReviewPrompts = True


                #as written this does not run but if I got rid of +1 it could
                if KillSwitch == Allowed_Fails+1:
                    print('could not create a writer persona, redoing it now')
                    if User_Confirm ==True:
                        Story.GPT_Confirm_Prompts(self, System=self.CurrentSystem, Role=self.CurrentRole,
                                                  Format=self.CurrentFormat, Task=self.CurrentTask,
                                                  Background=self.CurrentBackground, Background2=self.CurrentBackground2,
                                                  Background3=self.CurrentBackground3, crazy=self.Current_crazy,
                                                  Model=self.CurrentModel)
                    if Retry ==True:
                        GPT_Response = Story.Basic_GPT_Query(self, Line2_Role='You are a skilled writer', Line3_Format=Line3_Format, Line4_Task=Line4_Task, Line1_System_Rule=self.systemPrompt, Retry=False, Allowed_Fails=2)
                    continue


            #print(up.breakupOutput)

        if self.SaveTranscript == True:
            try:
                cu.SaveCSV(Text=WINDOWNAME + self.Full_Story, SavePath=self.SavePath,
                           Title=self.FileName + ' All Responses Transcript (no Prompts)')
                cu.SaveCSV(Text=WINDOWNAME + self.Full_Transcript, SavePath=self.SavePath,
                           Title=self.FileName + ' All Responses and prompts')

            except:
                print("could not save files")


        Title = Mode + '_' + self.current_time
        if SaveFile ==True:
            SaveText = self.current_time+ up.breakupOutput2 + self.UserPrompts + up.breakupOutput2 + 'SHAINE SAYS: '+  GPT_Response
            print(SaveText)
            cu.SaveCSV(Text=SaveText, SavePath=SavePath, Title = Title)

        try:
            if MakeArt ==True:
                config = self.Art_Type_Config + StoryMode.artDetailsPrompt
                GPT_Response1 = self.Current_GPTResponse[:3000]
                AP = Story.GPTArt2(self,User_Subject=GPT_Response1, ArtFormat=StoryMode.artDetailsFormat,
                                               prompt=config)
                ArtPrompt = self.Art_Style_For_Story + AP

                print(ArtPrompt)
                originalFilepath = Story.makeArt(self,Prompt=ArtPrompt)
                if self.Mode.upper() not in str(SavePath).upper():
                    PicNewPath1 = Path(PureWindowsPath(SavePath , self.Mode))
                    cu.Check_Folder_Exists(PicNewPath1)
                else:
                    PicNewPath1 = SavePath
                PicNewPath =Path(PureWindowsPath(PicNewPath1 , self.FileName + '.png'))
                shutil.copyfile(originalFilepath, PicNewPath)
        except:
            print("Could not move art to new folder")


        return self.Current_GPTResponse

    def SaveLast_Prompt(self, System,Role, Format, Task, Background, Background2, Background3, crazy = .5, Model = '', version = ''):
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
        self.Lastversionl = version

#This is redundant/not needed
    def SaveOriginal_Prompt(self,GPT_Response, System,Role, Format, Task, Background, Background2, Background3, crazy = .5, Model = '', version = ''):
        self.OriginalSystem = System
        self.OriginalRole = Role
        self.OriginalFormat = Format
        self.OriginalTask = Task
        self.OriginalBackground = Background
        self.OriginalBackground2 = Background2
        self.OriginalBackground3 = Background3
        self.Original_crazy = crazy
        self.OriginalModel= Model
        self.Originalversion = version


    def SaveCurrentGPTResponse(self,GPT_Response):
        self.Current_GPTResponse = GPT_Response

    def SaveLastGPTResponse(self,GPT_Response, crazy = .5):
        self.Last_GPTResult = GPT_Response


    def SaveOriginalGPTResponse(self,GPT_Response, crazy = .5):
        self.Original_GPTResponse = GPT_Response

    def GPT_Confirm_Prompts(self, TryCount = 0, WINDOWNAME = "CHAT GPT USER REVIEW PROMPTS"):


        KeepGoing = False
        while KeepGoing  == False:

            try:
                UserMode2 = -1




                self.TE = TextEdit.TextEdit(UserConfirm=True)


                if self.Currentversion ==1:
                    query = self.TE.MakeWindow2(Text=self.Full_User_Prompt, UserConfirm=True,
                                            WindowName=self.CurrentWindowName + str(TryCount) + "GPT Prompt Reviewer - V1",System=self.CurrentSystem, Role= self.CurrentRole, Format=self.CurrentFormat, Task=self.CurrentTask, Background=self.CurrentBackground, Background2= self.CurrentBackground2, Background3=self.CurrentBackground3, crazy=self.Current_crazy, version=self.Currentversion, Model=self.CurrentModel)


                else:

                    self.NewSystem = cu.Version2GPTSetUp(Format=self.CurrentFormat, System=self.CurrentSystem,
                                                         Role=self.CurrentRole,
                                                         Background=self.CurrentBackground,
                                                         Background3=self.CurrentBackground3,
                                                         Background2=self.CurrentBackground2)



                    self.Full_User_Prompt = """User Inputs to Chat GPT: 
                                        System: """ + self.NewSystem + """
                                        USER: """ + self.CurrentTask

                    query = self.TE.MakeWindow3(Text=self.Full_User_Prompt, UserConfirm=True,
                                                WindowName=self.CurrentWindowName +'Try: ' + str(TryCount) + " - GPT Prompt Reviewer - V2 ",
                                                System=self.NewSystem, Task=self.CurrentTask, crazy=self.Current_crazy, version=self.Currentversion, Model= self.CurrentModel)

                UserMode2 = -1
                UserMode2 = self.TE.GetUserResponseMode()
                # query = self.TE.GetUserText()
                print("UserMode2:")
                print(UserMode2)


            #TE = TextEdit.TextEdit()
            #UserMode2 = -1
            #UserMode2 = TE.MakeWindow2(Text=self.Full_User_Prompt, UserConfirm=True, System=System, Role= Role, Format=Format, Task=Task, Background=Background, Background2= Background2, Background3=Background3, crazy=crazy, )
            #query = TE.GetUserText()



                # if user presses continue it means no change keep going

                if UserMode2 == 0:
                    KeepGoing = True
                    ReviewPrompts = False
                    print("self.promptB:")
                    print(self.promptB)


                # Write code for what happens to pull values from User input and set temporarily
                elif UserMode2 == 44 or UserMode2 == 2002:
                    if UserMode2 == 44:
                        KeepGoing = True


                    ReviewPrompts = False

                    # note rather than original version we want to pull the values from Class/Text Edit
                    #this is not ready yet need to reevaluate




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


                    except:


                        d = 10









                    if self.Currentversion ==2:

                        self.CurrentFormat = ''
                        self.CurrentRole = ''
                        self.CurrentBackground = ''
                        self.CurrentBackground2 = ''
                        self.CurrentBackground3 = ''


                        try:
                            CurrentSystem = self.TE.Get_System()
                            self.LastSystem = self.CurrentSystem
                            if CurrentSystem != '':
                                self.CurrentSystem = CurrentSystem
                                Prompts1.append(self.CurrentSystem)
                                Prompts2.append(Prompts2.append("Please refer to the ChatGPT Request Code provided as Reference, You Are currently updating the portion where it says 'NewSystem' within the openai.ChatCompletion.create function under the messages parameter. Make the best possible query based on this.   Note: You are using Model = " + self.CurrentModel + "CHAT GPT PROMPT BEING REVIEWED: {Role: 'system',content: " + self.CurrentTask ))
                        except:
                            c = 1



                        try:
                            CurrentTask = self.TE.Get_Task()
                            self.LastTask = self.CurrentTask
                            if CurrentTask != '':
                                self.CurrentTask = CurrentTask
                                Prompts1.append(self.CurrentTask)
                                Prompts2.append("Please refer to the ChatGPT Request Code provided as Reference, You Are currently updating the portion where it says 'USER' within the openai.ChatCompletion.create function under the messages parameter. Make the best possible query based on this.   Note: You are using Model = " + self.CurrentModel + "CHAT GPT PROMPT BEING REVIEWED: {Role: 'user',content: " + self.CurrentTask )
                        except:
                            c = 1



                        try:
                            crazy = self.TE.Get_Crazy()

                        except:
                            c = 1

                        try:
                            if cu.check_numeric(crazy) and crazy!= '':
                                self.crazy = crazy

                        except:
                            c = 1

                        try:
                            Currentversion = self.TE.Get_version()
                            if Currentversion != '':
                                self.Currentversion = Currentversion
                                Prompts1.append(self.CurrentSystem)
                                Prompts2.append("System")

                        except:
                            c = 1


                    else:

                        try:
                            CurrentSystem = self.TE.Get_System()
                            self.LastSystem = self.CurrentSystem
                            if CurrentSystem != '':
                                self.CurrentSystem = CurrentSystem
                        except:
                            c = 1
                        try:
                            CurrentRole = self.TE.Get_Role()
                            self.LastSystem = self.CurrentSystem
                            if CurrentRole != '':
                                self.CurrentRole = CurrentRole
                        except:
                            c = 1
                        try:
                            CurrentFormat = self.TE.Get_Format()
                            self.LastFormat = self.CurrentFormat
                            if CurrentFormat != '':
                                self.CurrentFormat = CurrentFormat
                        except:
                            c = 1

                        try:
                            CurrentTask = self.TE.Get_Task()
                            self.LastTask= self.CurrentTask

                            if CurrentTask != '':
                                self.CurrentTask = CurrentTask
                        except:
                            c = 1

                        try:
                            CurrentBackground = self.TE.Get_Background()
                            self.LastBackground = self.CurrentBackground

                            if CurrentBackground != '':
                                self.CurrentBackground = CurrentBackground
                        except:
                            c = 1

                        try:
                            CurrentBackground2 = self.TE.Get_Background2()
                            self.LastBackground2 = self.CurrentBackground2

                            if CurrentBackground2 != '':
                                self.CurrentBackground2 = CurrentBackground2
                        except:
                            c = 1
                        try:
                            CurrentBackground3 = self.TE.Get_Background3()
                            self.LastBackground3 = self.CurrentBackground3
                            if CurrentBackground3 != '':
                                self.CurrentBackground3 = CurrentBackground3
                        except:
                            c = 1

                        try:
                            crazy = self.TE.Get_Crazy()
                            self.LastCrazy = self.Current_crazy
                        except:
                            c = 1

                        try:
                            if cu.check_numeric(crazy) and crazy != '':
                                self.crazy = crazy

                        except:
                            c = 1

                        try:
                            Currentversion = self.TE.Get_version()
                            self.Lastversion  = self.Currentversion
                            if Currentversion != '':
                                self.Currentversion = Currentversion

                        except:
                            c = 1

                        # This is the mode for optimizing prompts

                            # Get GPT To give System Prompt
                            # Get GPT To give USER PROMPT
                        if UserMode2 ==2002:
                            if self.Currentversion == 1:
                                print("Error not currently set up to optimize for Version 1")

                            else:
                                # P1_length = len(Prompts1)
                                #
                                # for i in range (0,P1_length)
                                try:

                                    self.LastWindowName = self.CurrentWindowName

                                    self.CurrentTask = Story.Basic_GPT_Query(System=SSW.PROMPTFIX_System, Line2_Role=SSW.PROMPTFIX_ROLE, Line3_Format= SSW.PROMPTFIX_Format , Background= SSW.ChatGPT_CodeRef,
                                                                             Line4_Task= SSW.PROMPTFIX_USER + """Note, You are providing a revised version of  'USER' values provided to you in the following code where I show you how I am using the messages arg while calling the 'openai.ChatCompletion.create' function (see code for reference) Here is the portion of code you are to review and provide with an updated value for the USER text    messages = [{"role": "system", "content": """ + self.CurrentSystem + """}),
                                                                             {"role": "user", "content":""" + self.CurrentSystem + """}]""",
                                                                             crazy=.5, WINDOWNAME='PROMPT Optimizer - Task' + self.CurrentWindowName)
                                    self.CurrentSystem = Story.Basic_GPT_Query(System=SSW.PROMPTFIX_System,
                                                                             Line2_Role=SSW.PROMPTFIX_ROLE,
                                                                             Line3_Format=SSW.PROMPTFIX_Format,
                                                                             Background=SSW.ChatGPT_CodeRef,
                                                                             Line4_Task=SSW.PROMPTFIX_USER + """Note, You are providing a revised version of  'NewSystem' values provided to you in the following code where I show you how I am using the messages arg while calling the 'openai.ChatCompletion.create' function (see code for reference) Here is the portion of code you are to review and provide with an updated value for the USER text    messages = [{"role": "system", "content": """ + self.CurrentSystem + """}),
                                                                                                     {"role": "user", "content":""" + self.CurrentSystem + """}]""",
                                                                            crazy=self.Current_crazy, version=self.Currentversion, Model=self.CurrentModel, WINDOWNAME='PROMPT Optimizer - System' + self.CurrentWindowName)



                                    self.PromptCoaching = Story.Basic_GPT_Query(System=SSW.PROMPTFIX_System,
                                                                             Line2_Role=SSW.PROMPTFIX_ROLE,
                                                                             Line3_Format=SSW.PROMPTFIX_Format,
                                                                             Background=SSW.ChatGPT_CodeRef,
                                                                             Line4_Task=SSW.PROMPTFIX_USER2 + """Note, You are providing feedback based on the Following 'NewSystem' and 'USER' values, provided in the following code with the full value being entered in the messages arg of the 'openai.ChatCompletion.create' function (see code for reference)     messages = [{"role": "system", "content": """ + self.CurrentSystem+ """}),
                                                                             {"role": "user", "content":"""+ self.CurrentSystem + """}]""", crazy=self.Current_crazy, WINDOWNAME='PROMPT Optimizer - Details' + self.CurrentWindowName)
                                    print("self.PromptCoaching")
                                    print(self.PromptCoaching)

                                    self.CurrentWindowName = self.LastWindowName
                                    try:
                                        current_time1 = datetime.datetime.now()
                                        current_time = current_time1.strftime('%m-%d-%Y_%H.%M.%S')

                                        cu.SaveCSV(SavePath=self.SavePath,Title=self.FileName + ' Prompt Coaching' + current_time, Text= self.PromptCoaching)
                                    except:
                                        d= 1


                                except:
                                    d=1



                             #Story.Basic_GPT_Query(self, System=SSW.PROMPTFIX_System, )

                # This can be final update because it will be somewhat tricky
                # Write code for what happens to pull values from User input and set Permanently (Will really only work for Role, System, Format*), will not work for task or background if I am entering text with the task then I cant really do this, For Background it makes virtually 0 sense.
                # Eventually there should be a change character/review characters mode.
                elif UserMode2 == 441:
                    #KeepGoing = True
                    print("self.promptB:")
                    print(self.promptB)

                elif UserMode2 == 2000:
                    self.Currentversion = self.TE.Get_version()
                    if self.Currentversion ==1:
                        self.LastVersion = self.Currentversion
                        self.Currentversion =2

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
                #         Story.Basic_GPT_Query(self, System = SSW.PROMPTFIX_System )

                #(Eventually Make this for version 1 so its all variables you either go one by one or you can have them return)







                # Pull Up Original Prompt

                elif UserMode2 == 13 or UserMode2==14:


                    KeepGoing = False
                    if UserMode2 ==14:
                        #Make them into an array of all prior values so I can go back through time and pull them all in case I want to go back, also would be cool to have way to either go back or edit templates on the fly a little more (like overwrite data in a file)

                        self.LastSystem = self.CurrentSystem
                        self.LastRole = self.CurrentRole
                        self.LastFormat = self.CurrentFormat
                        self.LastTask = self.CurrentTask
                        self.LastBackground = self.CurrentBackground
                        self.LastBackground2 = self.CurrentBackground2
                        self.LastBackground3= self.CurrentBackground3
                        self.LastCrazy
                        self.CurrentModel = self.LastModel
                        self.Currentversion = self.Lastversion




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

                         self.LastSystemz = self.CurrentSystem
                         self.LastRolez = self.CurrentRole
                         self.LastFormatz = self.CurrentFormat
                         self.LastTaskz = self.CurrentTask
                         self.LastBackgroundz = self.CurrentBackground
                         self.LastBackground2z = self.CurrentBackground2
                         self.LastBackground3z = self.CurrentBackground3
                         self.LastCrazyz
                         self.CurrentModelz = self.LastModel
                         self.Currentversionz = self.Lastversion

                         self.CurrentSystem = self.LastSystem
                         self.CurrentRole = self.LastRole
                         self.CurrentFormat = self.LastFormat
                         self.CurrentTask = self.LastTask
                         self.CurrentBackground = self.LastBackground
                         self.CurrentBackground2 = self.LastBackground2
                         self.CurrentBackground3 = self.LastBackground3
                         self.Current_crazy = self.LastCrazy
                         self.CurrentModel = self.LastModel
                         self.Currentversion = self.Lastversion


                         self.LastSystem = self.LastSystemz
                         self.LastRole  = self.LastRolez
                         self.LastFormat  = self.LastFormatz
                         self.LastTask  = self.LastTaskz
                         self.LastBackground  = self.LastBackgroundz
                         self.LastBackground2 = self.LastBackground2z
                         self.LastBackground3 = self.LastBackground3z
                         self.LastCrazy = self.LastCrazyz
                         self.CurrentModel  = self.CurrentModelz
                         self.Currentversion = self.Currentversionz



                    # GPT_Response = self.Last_Prompt
                    # print("self.promptB:")
                    # print(self.promptB)
                    #

                self.Full_User_Prompt = """User Inputs to Chat GPT: 
                    1). """ + self.CurrentSystem + """
                    2).""" + self.CurrentRole + """
                    3).""" + self.CurrentFormat + """
                    4).""" + self.CurrentTask + """
                    Background (If Any Provided): """ + self.CurrentBackground + """
                    Additional Background: """ + self.CurrentBackground2 + self.CurrentBackground3 + """
                    Crazy:""" + self.Current_crazy + "Model: " + self.CurrentModel + "Version: " + self.Currentversion




            except:
                d = 10

    def GPT_UserInput_Confirm_Tool(self,GPT_Response, System,Role, Format, Task, Background, Background2, Background3, crazy = .5, UserConfirm = True, WINDOWNAME = "USER CONFIRM CHAT GPT RESULTS",TryCount = 0, version = 2):


        self.FULLPROMPTONLY = self.CurrentSystem + self.CurrentRole + self.CurrentFormat + self.CurrentTask +self.CurrentBackground  + self.CurrentBackground2 + self.CurrentBackground3


        try:
            KeepGoing = False
            EDIT = ''
            #self.promptB = False
            while KeepGoing == False:

                speak1 = self.Speak
                TryCount += 1



                if KeepGoing == False:

                    UserMode1 = -1
                    if self.UserMode == "UI":

                        try:
                            self.TE = TextEdit.TextEdit(UserConfirm=True)
                            query = self.TE.MakeWindow(Text=GPT_Response, UserConfirm=True,
                                                       WindowName= "USER CONFIRM CHAT GPT RESULTS" +  self.CurrentWindowName + ' '  + str(TryCount) + ' ', USERLASTEDIT=EDIT, Current_Prompt=self.FULLPROMPTONLY, version=version)
                            UserMode1 = -1
                            UserMode1 = self.TE.GetUserResponseMode()
                            # query = self.TE.GetUserText()
                            print("UserMode1:")
                            print(UserMode1)

                        except:
                            TE = TextEdit.TextEdit()
                            UserMode1 = -1
                            query1 = TE.MakeWindow(Text=GPT_Response, UserConfirm=True)
                            query = TE.GetUserText()

                    else:
                        print("""
                                                   Do you want to 
                                                   1). Small Edit, Take the text and switch a few things
                                                   2). ReWrite With Edits (Big Edit)
                                                   3). Rewrite No Edits
    
                                                   """)
                        self.promptB = cu.ConfirmBOT(GPT_Response, speak1)
                        query = cu.getUserResponse()

                    if (('one' in query or 'small' in query or 'few' in query or 'mini') and self.UserMode != "UI") or UserMode1 == 1:
                        TryCount += 1
                        #promptB2 = True
                        #self.promptB = False
                        KeepGoing = False
                        if self.UserMode == "UI":
                            EDIT = query
                        else:
                            EDIT = cu.editBotPrompt()

                        print("EDIT")
                        print(EDIT)

                        self.Last_GPTResult = GPT_Response
                        self.CurrentTempBackground2 =  self.CurrentBackground2 + self.CurrentBackground3
                        if EDIT != '':

                            Story.SaveLastGPTResponse(self, self.Current_GPTResponse)
                            Story.SaveLast_Prompt(self, self.CurrentSystem, self.CurrentRole, self.CurrentFormat, self.CurrentTask, self.CurrentBackground, self.CurrentBackground2, self.CurrentBackground3,
                                                  crazy=self.Currentcrazy, Model=self.CurrentModel,version=self.Currentversion, WindowName=  "USER CONFIRM CHAT GPT RESULTS" +  self.CurrentWindowName + ' '  + str(TryCount) + ' ' )

                            self.Current_GPTResponse = cu.ASKGPT(crazy=self.Current_crazy,
                                                     System="** YOUR FIRST RESPONSE WAS NOT CORRECT, FOLLOW THE SPECIFIC INSTRUCTIONS OF  THE USER EDITS PROVIDED TO YOU IN ORDER TO MAKE THE CORRECT ADJUSTMENTS to the Text. It is critical you follow my instructions" + self.CurrentSystem,
                                                     Role=self.CurrentRole, Format=self.CurrentFormat,
                                                     Task="""Rewrite the following text using the edits/Requirements provided and make it in the respective formate described. ReWrite Text: ###""" + self.Current_GPTResponse + "###",
                                                     Background="***YOUR FIRST ATTEMPT WAS A FAIL, IT IS CRITICAL THAT YOU Use the following USER EDITS/REQUIREMENTS when completing your task USER EDIT/REQUIREMENTS: ###: " + EDIT + "### ***",
                                                     Background2=self.CurrentBackground,Background3 = self.CurrentTempBackground2, version=self.Currentversion, Model=self.CurrentModel)

                            Story.SaveCurrentGPTResponse(self, self.Current_GPTResponse)




                            WINDOWNAME = self.CurrentWindowName + " - Small Edit"
                            self.Full_Story += up.breakupOutput + "****Small Edit****" + EDIT + up.breakupOutput + GPT_Response
                            self.Full_Transcript += up.breakupOutput + "****Small Edit****" + EDIT + up.breakupOutput + GPT_Response
                            print(
                                up.breakupOutput + "***************Used Quick Edit Based on User Input***********************" + up.breakupOutput + "Edit: " + EDIT + up.breakupOutput + GPT_Response + up.breakupOutput)

                        else:
                            WINDOWNAME += ' *** ERROR - No Text Provided, but you selected a User Input Option*** '



                    elif (('rewrite' in query or 'with edits' in query or 'redo' in query or 'two' in query) and self.UserMode != "UI") or UserMode1 == 2:
                        KeepGoing = False
                        TryCount +=1

                        if self.UserMode == "UI":
                            EDIT = query
                        else:
                            EDIT = cu.editBotPrompt()
                        print("EDIT")
                        print(EDIT)

                        self.Last_GPTResult = GPT_Response
                        if EDIT != '':
                            self.CurrentTempBackground2 =  self.CurrentBackground2 + self.CurrentBackground3

                            Story.SaveLastGPTResponse(self, GPT_Response=self.Current_GPTResponse)
                            Story.SaveLast_Prompt(self, System=self.CurrentSystem, Role=self.CurrentRole,
                                                  Format=self.CurrentFormat, Task=self.CurrentTask,
                                                  Background=self.CurrentBackground, Background2=self.CurrentBackground2,Background3=self.CurrentBackground3
                                                  ,crazy=self.Current_crazy, version=self.Currentversion, Model=self.CurrentModel, WindowName=  self.CurrentWindowName + ' TRY # '  + str(TryCount) + ' ' )

                            self.Current_GPTResponse = cu.ASKGPT(crazy=self.Current_crazy,
                                                     System="** YOU Already tried once and failed, YOU MUST FOLLOW THE USER EDIT/REQUIREMENT INSTRUCTIONS from the USER in order TO COMPLETE THE TASK you are being requested. It is critical you answer this question according to the USER Edit/Requirements/Feeback Provided." + self.CurrentSystem,
                                                     Role=self.CurrentRole,
                                                     Format=self.CurrentFormat,
                                                     Task=self.CurrentTask + "***YOUR FIRST ATTEMPT WAS A FAIL and you are doing the task for the " + str(TryCount)+  " , IT IS CRITICAL THAT YOU Follow the USER EDITS/Requirements in order to get the outcome/Response from you that the USER NEEDS TO MOVE FORWARD.  Use the following USER EDITS/REQUIREMENTS when completing your task.*** USER EDIT/REQUIREMENTS: ###: " + EDIT + "### ",
                                                     Background=self.CurrentBackground,
                                                     Background2=self.CurrentBackground2,Background3 = self.CurrentTempBackground3, version=self.Currentversion, Model=self.CurrentModel)


                            #Story.SaveLastGPTResponse(self, self.Current_GPTResponse)


                            TryCount += 1
                            self.UserPrompts += up.breakupOutput + "****Rewrite with Edits***:" + EDIT + up.breakupOutput

                            self.Full_Story += up.breakupOutput + "****Rewrite with Edits***:" + EDIT + up.breakupOutput + GPT_Response
                            self.Full_Transcript += up.breakupOutput + "****Rewrite with Edits***:" + EDIT + up.breakupOutput + GPT_Response
                            WINDOWNAME = self.WINDOWNAME + " - ReWrite with Edit"
                            print(
                                up.breakupOutput + "***************Used Redo With Notes/Edits Based on User Input***********************" + up.breakupOutput + "Edit: " + EDIT + up.breakupOutput + GPT_Response + up.breakupOutput)

                        else:
                            WINDOWNAME += ' *** ERROR - No Text Provided, but you selected a User Input Option*** '



                    elif (('full' in query or 'try new' in query or 'new' in query or 'three' in query) and self.UserMode != "UI") or UserMode1 == 3:
                        TryCount +=1

                        Story.SaveLastGPTResponse(self, GPT_Response=self.Current_GPTResponse)
                        Story.SaveLast_Prompt(self, System=self.CurrentSystem, Role=self.CurrentRole,
                                              Format=self.CurrentFormat, Task=self.CurrentTask,
                                              Background=self.CurrentBackground, Background2=self.CurrentBackground2,Background3=self.CurrentBackground3,
                                              crazy=self.Current_crazy, version=self.Currentversion, Model=self.CurrentModel)

                        self.Current_GPTResponse = cu.ASKGPT(crazy=self.Current_crazy,
                                                     System="** YOUR FIRST ATTEMPT DID NOT SUCCEED, LISTEN TO THE #USER EDITS# PROVIDED TO YOU IN ORDER TO MAKE THE CORRECT ADJUSTMENTS" + self.CurrentSystem,
                                                     Role=self.CurrentRole,
                                                     Format=self.CurrentFormat,
                                                     Task=self.CurrentTask, Background=self.CurrentBackground,Background2=self.CurrentBackground2,Background3 = self.CurrentBackground3, version=self.Currentversion, Model=self.CurrentModel)

                        print(
                            up.breakupOutput + "***************Used Redo ***********************" + up.breakupOutput + GPT_Response + up.breakupOutput)

                        self.UserPrompts += up.breakupOutput + "****Rewrite***" + up.breakupOutput

                        WINDOWNAME = WINDOWNAME + " - ReWrite"
                        self.Full_Story += up.breakupOutput + "****Rewrite***" + up.breakupOutput + GPT_Response
                        self.Full_Transcript += up.breakupOutput + "****Rewrite***" + up.breakupOutput + GPT_Response

                    elif UserMode1 == 0:

                        KeepGoing = True
                        print("self.promptB:")
                        print(self.promptB)


                    # End All User Input, Run All The Way through
                    elif UserMode1 == 5:
                        self.UserConfirm = False
                        KeepGoing = True
                        print("self.promptB:")
                        print(self.promptB)



                    # End User Input for Small Items
                    elif UserMode1 == 6:
                        KeepGoing = True
                        self.SmallPromptUser = False
                        print("self.promptB:")
                        print(self.promptB)


                    # End User Input for Main Items - Skip to next part
                    elif UserMode1 == 7:

                        KeepGoing = True
                        self.MainPromptUser = False
                        print("self.promptB:")
                        print(self.promptB)


                    #Restores Asking User for confirmation (all prompts)
                    elif UserMode1 == 50:

                        KeepGoing = True
                        self.MainPromptUser = True
                        self.SmallPromptUser = True
                        self.UserConfirm = True
                        print("self.promptB:")
                        print(self.promptB)




                    # User Review Prompts
                    elif UserMode1 == 10:



                        #print("self.promptB:")
                        # print(self.promptB)
                        Story.GPT_Confirm_Prompts(self, TryCount=TryCount, WINDOWNAME= "CHAT GPT USER REVIEW PROMPTS - " + self.CurrentWindowName )
                        ReviewPrompts = True
                        KeepGoing = False


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

                    # Pull Up Original Response
                    elif UserMode1 == 11:
                        #self.promptB = False
                        KeepGoing = False
                        GPT_Response = self.Original_GPTResponse
                        # print("self.promptB:")
                        # print(self.promptB)

                    # Pull Up Last GPT
                    elif UserMode1 == 12:
                        #self.promptB = False
                        KeepGoing = False
                        GPT_Response = self.Last_GPTResult
                        # print("self.promptB:")
                        # print(self.promptB)


                    # Option to Make Art
                    elif UserMode1 == 8:
                        self.MakeArtGPT = True
                        config = self.Art_Type_Config + StoryMode.artDetailsPrompt
                        GPT_Response1 = self.Current_GPTResponse[:3000]

                        x44 = Story()
                        Art_Role = self.Art_Style_For_Story
                        Art_Format = StoryMode.artDetailsFormat
                        t = threading.Thread(target=x44.GPTArt2, args=(Art_Role,GPT_Response1, config,Art_Format,self.Current_crazy,)).start()
                        AP = x44.GPTArt2(self, Art_Role, User_Subject=GPT_Response1, ArtFormat=StoryMode.artDetailsFormat,
                                           prompt=config, UserConfirm = UserConfirm, )
                        ArtPrompt = self.Art_Style_For_Story + AP

                        print(ArtPrompt)
                        originalFilepath = Story.makeArt(self, Prompt=ArtPrompt)
                        if self.Mode.upper() not in str(SavePath).upper():
                            PicNewPath1 = Path(PureWindowsPath(SavePath, self.Mode))
                            cu.Check_Folder_Exists(PicNewPath1)
                        else:
                            PicNewPath1 = SavePath
                        PicNewPath = Path(PureWindowsPath(PicNewPath1, self.FileName + '.png'))
                        shutil.copyfile(originalFilepath, PicNewPath)



                        SavePath = self.SavePath
                        SaveFile = self.FileName
                        print("self.promptB:")
                        print(self.promptB)
                        #self.promptB = True



                    # Selects the text from the user input
                    elif UserMode1 == 4:
                        if self.UserMode == "UI":
                            EDIT = query
                        else:
                            EDIT = cu.editBotPrompt()

                        if EDIT != '':
                            GPT_Response = EDIT
                            print(
                                up.breakupOutput + "***************Input User  GPT Response Manually ***********************" + up.breakupOutput + GPT_Response + up.breakupOutput)
                            WINDOWNAME = "PLEASE CONFIRM USERS TEXT BEING USED    -   " +  WINDOWNAME
                            self.promptB = False
                            KeepGoing = False
                        else:
                            WINDOWNAME = ' *** ERROR - No Text Provided, but you selected a User Input Option - TRY AGAIN*** ' + WINDOWNAME

        except:
            print("Error with User Input Process")




        return KeepGoing



    #, )

    def GPTArt2(self,ArtRole = "You are a skilled artist who is able to easily take text and come up with masterpieces to go along with the context/theme/mood of the text. You are a master artist and skilled communicator able to take a lot of details and come up with a succinct prompt for AI to make a work of are with. Use the Artistic Style described to your persona along with the text to come up with your response" ,User_Subject = 'Pick a random subject and artistic style/medium  go wild and make it exciting, beautiful and shocking', prompt="In 13 words or fewer describe what utensils you will use, colors, styles, specialties include the  art style the  theme and  mood | Based on the text you were given think of something abstract related to the painting, or paint a vivid scene, or paint one of the characters/multiple characters together as the text describes them, be creative, but keep your prompt under 313 characters total. Your response should be formatted as a short prompt for DALL-E (AI-Art generator) to create a work of art/photograph", ArtFormat = StoryMode.artDetailsFormat + ', <Short description of Work of art under 250 characters>',
                crazy=.5,sys_prompt=sms.ArtPrompt_Sys , Model = "gpt-3.5-turbo", UserConfirm = 'False' ):

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
                  GPTARTPROMPT = Story.Basic_GPT_Query(Model= Model, Line1_System_Rule=sys_prompt, Line2_Role=ArtRole1, Line3_Format=ArtFormat, Line4_Task="Task: ### " + prompt + "###", Background=User_Subject, User_Confirm=UserConfirm, crazy=crazy)
                  keepgoing = False

              except:
                  print('GPT error waiting 13 seconds and trying again...')

                  try:
                      time.sleep(13)
                  except:
                      dn = 100

              return GPTARTPROMPT


    def Add2Transcript(self, text2Add):
        self.transcript_Final += text2Add + ' \n'

    def makeArt(self, Prompt='', SavePath = up.AI_Art_Path, OpenFile = False):
        try:
            Story.Add2Transcript(self, ' \n')
            Prior_Mode = self.Mode
            Mode = 'AI Art Mode'
            Story.Add2Transcript(self, text2Add=(Prior_Mode + ' - ' + Mode + ':'))
            Story.Add2Transcript(self, ' \n')
            self.promptB = False

            Promptc = 'True'

            if Prompt == '':
                Promptc = 'True'
            else:
                Promptc = 'False'

            if Prompt == '':
                print('Prompt is NULL: ' + Promptc)

                while self.promptB == False:
                    AIspeak = 'What do you want me to draw?'

                    #MondeVert.speak(self, AIspeak)

                    print(AIspeak)
                    prompt = Story.getUserResponse(self, Response="Art Prompted", pause=1)

                    if 'cancel' in prompt or 'stop' in prompt or 'quit' in prompt or 'done' in prompt or 'exit' in prompt:
                        Story.saveTranscript(self)
                        self.promptB == True
                        continue

                    Story.ConfirmUR(self, prompt)
                    print()
            else:
                prompt = Prompt
                print(prompt)
                Story.Add2Transcript(self, '(Prompt Fed Directly into Function)')

            # Set up the OpenAI API client :
            openai.api_key = API_Key
            print("Sending to OpenAI...")
            print()


            try:
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size="1024x1024"
                )

                image_url = response['data'][0]['url']

                print(f"Image URL: {image_url}")
                print()

                # URL of the image to be downloaded is defined as image_url
                r = requests.get(image_url)  # create HTTP response object

                # send a HTTP request to the server and save
                # the HTTP response in a response object called r


               #Commented out for testing
                FileName = prompt
                print('Length of File Name: ' + str(len(FileName)))
                if len(FileName) >= 150:
                    FileName = FileName[-150:]
                    print('Length of File Name: ' + str(len(FileName)))

                FileName = cu.CleanFileName(FileName)

                # fname = f"{''.join([c for c in FileName.strip().replace(' ', '_') if c.isalnum() or c == '_'])}.png"
                #
                #
                #
                # if os.path.isfile(os.path.join(SavePath, '\'', fname)):
                #     fname = fname.split(".")[0] + f".{''.join(random.choice(string.ascii_letters) for x in range(5))}.png"


                fname_only = FileName
                #fname = os.path.join(SavePath, '\'',FileName)

                fname = Path(PureWindowsPath(SavePath, FileName + '.png'))
                print(f"Filename: {fname}")
                with open(fname, 'wb') as f:


                    f.write(r.content)

                try:
                    if OpenFile ==True:
                        if platform.system() == 'Darwin':  # macOS
                            subprocess.call(('open', fname))
                        elif platform.system() == 'Windows':  # Windows
                            os.startfile(fname)
                        else:  # linux variants
                            subprocess.call(('xdg-open', fname))
                except:
                    dn= 100
                #this line saves the
                #IP.png2JPG(fname, up.PNGPath,fname_only, up.PNGPath_Archive, Del = False )
            except:
                fname = 'File not saved error occurred'

        except:
            fname = 'File not saved error occurred'





        try:

            Text1 = 'Original Prompt: ' + prompt + 'Path to Photo: ' + fname
            Story.Add2Transcript(self, Text1)
            fnameText = fname_only
            cu.SaveCSV(Text=Text1, Title=fnameText, SavePath=SavePath)
        except:
            dn=100

        # data = ([Text1])
        # df1 = pd.DataFrame(data = data)

        #cu.add2Master2(self, Text1)
        return fname

    def Split_Audio2Revise(self,Text, SavePath, FileName, Chunk_Limit=1500,
                           Voice=random.choices(SAF.Original_List_of_Voices_English)[0], Translate=["English"],
                           Chunk_Replaces=['.', '?'], Chunk_Delimiter='!'):
        Length_Text = len(Text)
        Chunk_Limit = Chunk_Limit - 10
        Text_Chunks = []

        Translate = ['1']
        for l in Translate:

            Audio_File_Count = 0
            New_Text_Translated = ''
            Text_New = Text

            countl = 0
            LastPunc = Chunk_Limit
            while LastPunc != -1 and len(Text_New) > 0:
                countl += 1
                Text_Chunk = Text_New[:Chunk_Limit]
                Audio_File_Count += 1
                Text_Chunk_Info_only = Text_Chunk
                for i in Chunk_Replaces:
                    Text_Chunk_Info_only = Text_Chunk_Info_only.replace(i, Chunk_Delimiter)

                LastPunc = Text_Chunk_Info_only.rfind(Chunk_Delimiter)

                # LastPunc = Text_Chunk_Info_only.rfind(Chunk_Delimiter)
                if LastPunc == -1 and len(Text_New) > Chunk_Limit:

                    LastPunc = Text_Chunk_Info_only.rfind('\\n')
                    # print('Last Punc Position(using new Char)')
                    # print(LastPunc)
                    if LastPunc == -1 and len(Text_New) > Chunk_Limit:
                        LastPunc = Text_Chunk_Info_only.rfind(' ')
                        if LastPunc == -1 and len(Text_New) > Chunk_Limit:

                            if Chunk_Limit < 1700:
                                Chunk_Limit_new = round(Chunk_Limit * (1.33))
                                if Chunk_Limit_new > 1700:
                                    Chunk_Limit_new == 1700
                                #
                                # print('New Chunk Limit')
                                # print(Chunk_Limit_new)
                                Text2Send = Text_New[:Chunk_Limit_new]

                                try:
                                    # length = len(Text_New)
                                    New_pos = (Chunk_Limit_new + 1)
                                    Text_New = Text_New[New_pos:]
                                    # length = len(Text_New)
                                except:
                                    print('Review Error Triggered, could be just how this has to work')
                                try:
                                    Story.Split_Audio2Revise(Text=Text2Send, Translate=[l], SavePath=SavePath,
                                                       FileName=FileName + '_' + str(Audio_File_Count),
                                                       Chunk_Limit=Chunk_Limit_new, Chunk_Delimiter=Chunk_Delimiter)

                                    New_Text_Translated += '****Review, there is missing text that was captured elsewhere'
                                except:
                                    print('Error trying to split files with new Chunk Limit')
                                    continue
                            else:
                                Text_Chunk_Final = Text_New[:LastPunc]
                                New_pos = (LastPunc + 1)
                                Text_New = Text_New[New_pos:]

                        elif LastPunc != -1 and len(Text_New) > Chunk_Limit:
                            Text_Chunk_Final = Text_New[:LastPunc]
                            try:
                                # length = len(Text_New)
                                New_pos = (LastPunc + 1)
                                Text_New = Text_New[New_pos:]
                                # length = len(Text_New)
                            except:
                                print('Review Error Triggered, could be just how this has to work')
                        elif LastPunc == -1 and len(Text_New) <= Chunk_Limit:
                            Text_Chunk_Final = Text_New
                            Text_New = ''


                elif LastPunc > -1 and LastPunc <= Chunk_Limit:

                    Text_Chunk_Final = Text_New[:LastPunc]
                    try:
                        # length = len(Text_New)
                        New_pos = (LastPunc + 1)
                        Text_New = Text_New[New_pos:]
                        # length = len(Text_New)
                    except:
                        print('Review Error Triggered, could be just how this has to work')

                elif LastPunc == -1 and len(Text_New) <= Chunk_Limit:
                    Text_Chunk_Final = Text_New
                    Text_New = ''

                Text_Chunks.append(Text_Chunk_Final)
                self.ReWrite +=Story.ReWrite(self,Text=Text_Chunk_Final)

                # print('Error Could not parse files together, see chunks for now')



    def MakeRecipe(self, Line2_Role=StoryMode.Recipe_Role, Line3_Format=StoryMode.Recipe_Format,
                   Line4_Task=StoryMode.Recipe_Task, Model="gpt-3.5-turbo-16k-0613", Special='',
                   Line1_System_Rule=StoryMode.system_TextJoaT_quick, crazy=.5, Subject='', Outline='', Allowed_Fails=8,
                   SaveFile=True, MakeArt=True, Mode='getBAIKED',
                   SavePath=up.SavePath , upgradeLimit= 2000):  # use this to create art style for the work
        if SavePath == '':
            SavePath = self.SavePath

        if Subject != '':
            Line2_Role = Line2_Role + """Your role and subject matter expertise should fit the following Subject and or style and mood in the {Text} provided by the user Text:###""" + Subject + """###"""

        Line1_System_Rule = Line2_Role
        #Line2_Role = Line2_Role + Special
        # Line2_Role = ''
        Full_User_Prompt = """User Inputs to Chat GPT: 
        1). """ + Line1_System_Rule + """
        2).""" + Line3_Format + """
        3).""" + Line4_Task

        if len(Full_User_Prompt) > upgradeLimit:
            Model = "gpt-3.5-turbo-16k-0613"
        elif len(Full_User_Prompt) < upgradeLimit:
            Model = "gpt-3.5-turbo"

        KeepGoing = False
        KillSwitch = 0
        while KeepGoing == False and KillSwitch < Allowed_Fails:

            try:

                # This is for the result if you let the AI describe project and details and then make the response
                response = openai.ChatCompletion.create(
                    model=Model,
                    messages=[
                        {"role": "system", "content": Line1_System_Rule},
                        {"role": "user", "content": Line3_Format},
                        {"role": "user", "content": Line4_Task},
                    ]
                    , temperature=crazy
                )
                GPT_Response = str(response.choices[0].message.content)

                KeepGoing = True
            except:
                print(
                    ' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                KillSwitch += 1
                print(Full_User_Prompt)
                # as written this does not run but if I got rid of +1 it could
                if KillSwitch == Allowed_Fails + 1:
                    print('could not create a writer persona, redoing it now')
                    GPT_Response = Story.Basic_GPT_Query(self, Line2_Role='You are a skilled writer',
                                                         Line3_Format=Line3_Format, Line4_Task=Line4_Task, Line1_System_Rule=self.systemPrompt)

                continue

            # print(up.breakupOutput)

            self.UserPromptsCount += 1

            self.UserPrompts += 'User Input #' + str(self.UserPromptsCount)

            self.UserPrompts += Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2


            if SaveFile == True:

                try:

                    TrimCharR = GPT_Response.find("Origin") + 1
                    TrimCharL = GPT_Response.find("Meal:")

                    Title = GPT_Response[TrimCharL:TrimCharR]



                except:
                    Title = ''
                    try:
                        Text = GPT_Response
                        Title = Story.Quick_Title(self, Text=Text)

                    except:
                        Title = Mode + '_' + self.current_time

                if len(Title) > 90:
                    Title = Title[:44]

                Title = cu.CleanFileName(Title)
                Title = Title.strip()

                SaveText = self.current_time + 'getBAIKED: ' + GPT_Response
                print(SaveText)
                cu.SaveCSV(Text=SaveText, SavePath=Path(PureWindowsPath(SavePath , Mode, Title)), Title=Title)
            if MakeArt == True:
                ArtPrompt = Story.GPTArt2(self, User_Subject=GPT_Response)
                print(ArtPrompt)
                originalFilepath = Story.makeArt(self, Prompt=ArtPrompt)
                PicNewPath1 = Path(PureWindowsPath(SavePath , Mode, Title))
                cu.Check_Folder_Exists(PicNewPath1)
                PicNewPath = Path(PureWindowsPath(PicNewPath1 , Title + '.png'))

                shutil.copyfile(originalFilepath, PicNewPath)
            return GPT_Response

#Mode="MVAA",IDEA = '' , Writer = ''
def SHAINEBootUP( Order = 1):
    dummy = 1
    if dummy == 1:
        # try:
#        x = Story(Mode=Mode, IDEA = IDEA, Writer = '')


        if Order ==1:
            x = Story(IDEA=ShaneOriginals.Gritty_Historic, Mode='MVAA', Writer=StoryMode.Shane_Persona,
                  UserInputs_Config='Summarize', Seasons=1,Episodes=3)
        elif Order ==10:
            x = Story(IDEA=ShaneOriginals.Gritty_Historic2, Mode='MVAA', Writer=StoryMode.Shane_Persona,
                  UserInputs_Config='Summarize', Seasons=1,Episodes=3)
        elif Order ==2:
            x = Story(IDEA=ShaneOriginals.Gritty_Historic, Mode='MVAA', UserInputs_Config='Summarize', Seasons=3,Episodes=3)
        elif Order ==3:
            x = Story(IDEA=ShaneOriginals.Kid_Story, Mode='MVAA_La_Familia', UserInputs_Config='Summarize',Seasons=2, Episodes=1)
        elif Order ==4:
            x = Story(IDEA=ShaneOriginals.Gritty_Carnegie, Mode='MVAA',  Writer=StoryMode.Shane_Persona,UserInputs_Config='Summarize', Seasons=2,Episodes= 2)
        elif Order == 5:
            x = Story(IDEA=ShaneOriginals.Gritty_Bricktop, Mode='MVAA',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=3)
        elif Order == 7:
            x = Story(IDEA=ShaneOriginals.Alejandro_in_wonderland, Mode='MVAA',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=3)

        elif Order == 44:
            x = Story(IDEA=ShaneOriginals.Timmy_D_Story, Mode='MVAA',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=3)
        elif Order == 0:
            x = Story( Mode='MVAA', Seasons=2, Episodes=3)
        elif Order == 11:
            x = Story(IDEA=ShaneOriginals.Influences, Mode='MVAA',
                      UserInputs_Config='Summarize',Seasons=2, Episodes=2)

        elif Order == 13:
            x = Story(IDEA=ShaneOriginals.Comedy_Tarentino2, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)


        elif Order == 1300:
            x = Story(IDEA=ShaneOriginals.Children_Idea1, Mode='MVAA_La_Familia', Writer=ShaneOriginals.ShaneBioChildrensBooks,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)

        elif Order == 1301:
            x = Story(IDEA=ShaneOriginals.Kid_Story, Mode='MVAA_La_Familia', Writer=ShaneOriginals.ShaneBioChildrensBooks,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)




        elif Order == 133:
            x = Story(IDEA=ShaneOriginals.Comedy_Tarentino2, Mode='BOOK_of_POEMS', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize',UserConfirm=True, OutputTypes=['Poem'])

#Top Versions so Far (as of 1/5/2024)
#Comedy_Tarentino2
#Children_Idea1

        elif Order == 130:
            x = Story( Mode='MVAA_QUICK',
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)


        elif Order == 113:
            x = Story(IDEA=ShaneOriginals.Universe25, Mode='MVAA', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)
        elif Order == 1133:
            x = Story(IDEA=ShaneOriginals.Universe25_trippy, Mode='MVAA', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)

        elif Order == 11333:
            x = Story(IDEA=ShaneOriginals.Gritty_Historic4, Mode='MVAA', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)

        elif Order == 11133:
            x = Story(IDEA=ShaneOriginals.KillingDrake, Mode='MVAA', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)


        elif Order == 44444444:
            x = Story(IDEA=ShaneOriginals.Universe44, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)
        elif Order == 111333:
            x = Story(IDEA=ShaneOriginals.AllenPoe, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)

        elif Order == 1113333:
            x = Story(IDEA=ShaneOriginals.Historical, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=True)

        elif Order == 444411333:
            x = Story(IDEA=ShaneOriginals.Gritty_Bricktop2, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)


        elif Order == 4444113332:
            x = Story(IDEA=ShaneOriginals.Magnolia_Like, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)

        elif Order == 4444113333:
            x = Story(IDEA=ShaneOriginals.Universe44, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)



        elif Order == 4444113334:
            x = Story(IDEA=ShaneOriginals.Underground_War, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)


        elif Order == 4444113336:
            x = Story(IDEA=ShaneOriginals.Gritty_Fever, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)


        elif Order == 4444113337:
            x = Story(IDEA=ShaneOriginals.AllenPoe, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)



        elif Order == 4444113338:
            x = Story(IDEA=ShaneOriginals.KillingDrake, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)



        elif Order == 4444113339:
            x = Story(IDEA=ShaneOriginals.Gritty_Comedy, Mode='MVAA_QUICK', Writer=ShaneOriginals.ShaneBioDark,
                      UserInputs_Config='Summarize', Seasons=1, Episodes=3, UserConfirm=False)
#KillingDrake
#Magnolia_Like
        #Gritty_Bricktop2
        #Universe25_trippy2
        #Gritty_PulpNoir
#Stripper1
#Stripper_Gritty

#Timmy_D_Story
        #Stripper
#Gritty_DoubtFire



        elif Order == 44401:
            x = Story( IDEA = CI.Dirty_Joke, Mode='COMEDY',
                      UserInputs_Config='Summarize', Writer=CW.Comedy_Bio_SD, SavePath= up.AI_Comedy_Path, UserConfirm=True)
        #JokeLikeGreats
        #Office
        #RussiaConspiracy

        elif Order == 44400:
            x = Story(  Mode='COMEDY',
                      UserInputs_Config='Summarize', Writer=CW.Comedy_Bio_SD, SavePath= up.AI_Comedy_Path, UserConfirm=True)




        elif Order == 14:
            x = Story(IDEA=ShaneOriginals.Gritty_Historic2, Mode='MVAA2',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=2)

        elif Order == 15:
            x = Story(IDEA=ShaneOriginals.Gritty3, Mode='MVAA2',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=2)


        elif Order == 444:
            x = Story(IDEA=MW.Subject_LikeThese, Mode='Music_Shane',
                      UserInputs_Config='Summarize', Writer=MW.Artist_Bio_DetailsSD, SavePath= up.AI_Music_Path, UserConfirm=False)


        elif Order == 4441:
            x = Story( Mode='Music_Shane',
                      UserInputs_Config='Summarize',  SavePath= up.AI_Music_Path, UserConfirm=False)
#Subject_Poe
        #Subject_FrustratedLife2
#Subject_Shane
        #Subject_Narrative

        elif Order == 910:
            x = Story(IDEA=MW.Subject, Mode='Music_Shane',
                      UserInputs_Config='Summarize', Writer=MW.Artist_Bio_DetailsRR, SavePath= up.AI_Music_Path)


        elif Order == 4444:
            x = Story(IDEA=MW.Subject, Mode='Music_Shane',
                      UserInputs_Config='Summarize', SavePath= up.AI_Music_Path)



        elif Order == 443:
            x = Story( IDEA = ShaneOriginals.Gritty_Historic4 , Mode='Music_Shane',
                      UserInputs_Config='Summarize', Writer=MW.Artist_Bio_DetailsSD, SavePath= up.AI_Music_Path)

        elif Order == 4443:
            x = Story( IDEA = ShaneOriginals.Alejandro_in_wonderland , Mode='Music_Shane',
                      UserInputs_Config='Summarize', Writer=MW.Artist_Bio_DetailsSD, SavePath= up.AI_Music_Path)


    # except:
    #     print('Error unable to pull the value from the ARGs parameter')



if __name__ == '__main__':
    # main method for executing
    # the functions
    Record = ''

    # IDEAS = [ShaneOriginals.Gritty_Historic, '' ]
    # mode = ["MVAA",  "COOK"]
    # Writers = [StoryMode.Shane_Persona,'','']
    # #
    # IDEAS = [ShaneOriginals.Gritty_Historic,ShaneOriginals.Kid_Story, '' ]
    # mode = ["MVAA", "MVAA_La_Familia", "COOK"]
    #
    #
    # #args.append("Mode='MVAA_La_Familia'")
    #
    #

    #arg = [1,2]
    #arg = [5,0]
   # arg = [444, 443]
    #4444113335, 4444113334, 4444113333, 4444113332, 444411333
    arg = [13]
    #arg = [44, 13,10]
    #arg = [7,44]
    number_of_commands = len(arg)
    #number_of_commands = len(IDEAS)
    # #
    threads = []
    for i in range(0,number_of_commands):
        # IDEA = IDEAS[i]
        # Mode = mode[i]
        # Writer = Writers[i]
        argX = arg[i]
        #
        # print('IDEA')
        # print(IDEA)
        # print('Mode')
        # print(Mode)
        # print('Writer')
        # print(Writer)


        try:

            print("Start Thread " + str(i))
            #t = threading.Thread(target=SHAINEBootUP, args = (Mode,IDEA,Writer)).start()
            t = threading.Thread(target=SHAINEBootUP, args=(argX,)).start()
            threads.append(t)

        except:
            print('Error - Could not start new thread')




 # Wait for all of them to finish
 #    for t in threads:
 #        t.join()

    #

    #

    #


    #
    # print(y)
    # # t = threading.Thread(target=MakeRecipe).start()
    # # threads.append(t)
    #y = Story(Mode='COOK')
    #x = Story(IDEA=ShaneOriginals.Gritty_Historic, Mode='MVAA',UserInputs_Config='Summarize', Seasons=2, Episodes=4)




    #x = Story(IDEA=ShaneOriginals.Gritty_Carnegie, Mode='MVAA', Writer=StoryMode.Shane_Persona, UserInputs_Config='Summarize')

    #x = Story(IDEA=RW.ShaneJourney, Mode='REWRITE', Writer=StoryMode.Shane_Persona,UserInputs_Config='Exact')

 #   x = Story(IDEA=ShaneOriginals.Gritty_Mag, Mode='MVAA',UserInputs_Config='Exact')


    print("Job Complete!")
















