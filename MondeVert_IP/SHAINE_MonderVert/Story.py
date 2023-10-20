import datetime
import sys
from pathlib import Path, PureWindowsPath
import platform
import pandas as pd
global Record
from  MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Wedding_Prompts as WeddingP
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Social_Media_SHAINE as sms
from secrets import randbelow
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Long_User_Prompts as lup, User_Prefs as up, \
    Stories_For_Audio_Files as SAF, StoryMode_Wizard as StoryMode, ReWrites as RW, StoryPrompts as SP
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



#OutputTypes = ["Play","Novel", "ScreenPlay","Song"]

class Story():
    def __init__(self, IDEA = '' ,Mode = 'MVAA',Writer = '', UserInputs_Config = 'AI Only',OutputTypes = ["Play","Novel", "ScreenPlay"],voice=4, Logic_AI = 0, language_settings=1,Chunk_Limit = 777,  SavePath =up.AI_AudioBook_Path,  Writer_Style = '',Artist = '', Artist_Style = '', Story_Type = 'ScreenPlay', Seasons = 1, Episodes = 3, Books = '', Acts = '', Scenes = '', Movies = '', Text_Output_Config = [''], IDEA_Source = 'AI', Output_Audio_Config = '' ):
        self.voice = voice
        self.language_settings = language_settings

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
        self.SavePath=up.AI_AudioBook_Path + up.System_Folder_Path_Fix + Mode
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




        elif 'MVAA' in Mode.upper():
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







    def NewStoryMode(self):

        self.Story_Role = 'You are a brillian assistant to the user, Role Play as an award winning writer able to impersonate any genre or style/voice base your persona on the following Writing Style  Writing Style: ' + self.Writer_Style_Summary

        NewStory_Outline = Story.Basic_GPT_Query(self,
                                                    Line2_Role= self.Story_Role,
                                                    Line3_Format=SP.Story_Outline_Format,
                                                    Line4_Task=SP.Story_Outline_Task +  """Use the following  Text  as a source for your Outline   IDEA:###""" + self.IDEA_Final,
                                                    crazy=self.crazy, Big=True)


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

        NewStory_AllScenes_Outline = Story.Basic_GPT_Query2(self,
                                                    Line2_Role=self.Story_Role,
                                                    Line3_Format=SP.Story_AllScenes_Outline_Format,
                                                    Line4_Task=   """Use the following  Text  as a source for your Story (Expand on the ideas and give a full story based on the requirements provided)  Text:###""" + NewStory_Outline,
                                                    Line5_Task= SP.Story_AllScenes_Outline_Task,
                                                    crazy=self.crazy, Big=True)



        cu.SaveCSV(Text=NewStory_AllScenes_Outline,SavePath=self.SavePath, Title=Title+ '_Full Story')




    def ReWrite(self, Text):
        self.Story_Role = 'Role Play as an award winning writer able to impersonate any genre or style/voice base your persona on the following Text  Text: '  + self.Writer_Style_Summary

        ReWrite = Story.Basic_GPT_Query(self,
                                                    Line2_Role=self.Story_Role,
                                                    Line3_Format=self.Rewrite_Format,
                                                    Line4_Task=self.Rewrite_Task + """Use the following  Text  as a source for your rewrite   Text:###""" + Text,
                                                    crazy=self.crazy,
                                                    Subject='')

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
        try:
            Preview = Story.Basic_GPT_Query(self,
                                                     Line2_Role=self.Story_Role,
                                                     Line3_Format=StoryMode.Theatrical_Format,
                                                     Line4_Task=StoryMode.Theatrical_Task + Text,

                                                      crazy=self.crazy)

            cu.SaveCSV(Text=Preview,SavePath=self.SavePath, Title=self.FileName+ '_Theatrical Preview')
            FileName=self.FileName + '_Theatrical Preview'
            #Voice = random.choices(SAF.Original_List_of_Voices_English[0])
            cu.SaveText2Audio(SavePath=self.SavePath, FileName=FileName,
                              Neural='Neural',
                              Mode='AUDIOBOOK', Chunk_Limit=self.Chunk_Limit, Artist_Persona=self.Art_Style_For_Story, Translate=self.Translate,
                              Text=Preview)

        except:
            print("Error trying to make theatrical preview")


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
                    PicNewPath1 = self.SavePath + up.System_Folder_Path_Fix + self.Mode
                    cu.Check_Folder_Exists(PicNewPath1)
                    PicNewPath = PicNewPath1 + up.System_Folder_Path_Fix + self.Title + '.png'

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
                                                          crazy=self.crazy)


        self.Outline_Main_Style = Story.Basic_GPT_Query(self,
                                                 Line2_Role='Take on the following writer persona:' + self.Writer_Style_Summary,
                                                 Line3_Format=self.Story_Style_Details_Format,
                                                 Line4_Task=self.Story_Style_Details_Task + self.Outline_Main,
                                                 Special='',
                                                  crazy=self.crazy)

        self.Story_Role = """You are a brilliant assistant who is Role Playing as an award winning writer able to impersonate any genre or style/voice. Make sure you completely respond to the requests I provie and if I tell you the 'Desired Format:' I expect it to be exact base your role playing persona on the following details""" + self.Outline_Main_Style

        self.Outline_Main_Summary = Story.Basic_GPT_Query(self,
                                                 Line2_Role= self.Story_Role,
                                                 Line3_Format=self.StoryDetails_Format,
                                                 Line4_Task=self.StoryDetails_Task +  self.Outline_Main + IDEA,
                                                 Special='',
                                                  crazy=self.crazy)



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
        self.SavePath = self.SavePath + up.System_Folder_Path_Fix + Title1
        cu.Check_Folder_Exists(self.SavePath)
        cu.Check_Folder_Exists(self.SavePath + '\\Outlines')
        FileName_Char_Main = Title1 + '_Main Characters_'
        FileName_Char_Minor = Title1 + '_Minor Characters_'
        # Call Character art prompt


        print('self.Mode')
        print(self.Mode)

        if 'REWRITE' in self.Mode.upper():

            Text2Add = 'Writer: ' + self.Writer_Summary + up.breakupOutput + 'Writer Style: ' + self.Writer_Style_Summary + up.breakupOutput + 'ReWrite: ' + self.ReWrite + up.breakupOutput + 'Original IDEA: ' + self.IDEA + up.breakupOutput + 'Final IDEA: ' + self.IDEA_Final
            FileName_Details_Pre = self.FileName + ' PreProduction'
            cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=self.SavePath + '\\Outlines')

        else:
            Text2Add = 'Story Outline: ' + self.Outline_Main + up.breakupOutput + 'Story Details: ' + self.Outline_Main_Summary + up.breakupOutput2 + 'Story Details(fine): ' + self.Outline_Main_Style + up.breakupOutput2 + 'All Seasons Outline: ' + self.Outline_ALL_Seasons + up.breakupOutput + 'Characters: ' + self.Characters + up.breakupOutput2 + up.breakupOutput + 'Writer Persona: ' + self.Writer_Summary + up.breakupOutput2 + up.breakupOutput + 'Writer Persona Summary: ' + self.Writer_Style_Summary + up.breakupOutput2 + up.breakupOutput + 'Artist Persona: ' + self.Art_Style_For_Story + up.breakupOutput2 + up.breakupOutput + 'Original IDEA: ' + self.IDEA + up.breakupOutput + 'Final IDEA: ' + self.IDEA_Final
            FileName_Details_Pre = self.FileName + ' PreProduction'
            cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=self.SavePath + '\\Outlines')




    def Character_Summary(self, Outline, Season = 0, Episode = 0,Scene = 0):
        x = 100

        Characterst = self.Characters
        if len(Characterst) > 4000:
            Characterst = Characterst[:4000]

        CharactersTrim = Story.Basic_GPT_Query(self,
                                                   Line2_Role=self.Story_Role,
                                                   Line3_Format=StoryMode.Characters_Format_Fine,
                                                   Line4_Task=StoryMode.Characters_Task_Fine + """ Text:###""" + Outline[:2000] + """### based on the prior Text, Pick specific characters from the following list of characters (you can introduce your own characters if needed, but keep the main characters involved): """ + Characterst,
                                                   crazy=self.crazy,
                                                   Subject='', Big=True)

        if Episode == 0 and Scene == 0:
            text1 = 'Characters Used for Season ' + str(Season)
        elif Scene == 0:
            text1 = 'Characters Used for  Season ' + str(Season) + ' Episode ' + str(Episode)
        else:
            text1 = 'Characters Used for of Season ' + str(Season) + ' Episode ' + str(Episode) + ' Scene ' + str(
                Scene)

        self.Character_progression += up.breakupOutput2 + text1 + ': ' + CharactersTrim

        return CharactersTrim


    def Character_Update(self, Outline, Season = 0, Episode = 0,Scene = 0):
        x = 100
        try:
            Characters1 = Story.Basic_GPT_Query(self,Line2_Role=self.Story_Role,
                                                    Line3_Format=StoryMode.Characters_Update_Format,
                                                    Line4_Task=StoryMode.Characters_Update_Task + """  Text:###""" + Outline[:3000] + """### Update the following characters based on the prior text: """ + self.Characters,
                                                    crazy=self.crazy,
                                                    Subject='')

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
                    self.Character_progression += up.breakupOutput2 + + text1  + ': ' + self.Characters
            except:
                print("Could not update the Characters")
        except:
            print("Could not update the Characters")



    def SummarizeText(self, Text):
        c = 1
        Summarized_text = Story.Basic_GPT_Query(self, Line2_Role=self.Story_Role,
                                                   Line3_Format=self.Story_Summarize_Format,
                                                   Line4_Task=self.Story_Summarize_Task + """ Use the following text for the source of information Text:###""" + Text ,
                                                   crazy=self.crazy,
                                                   Subject='')


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


                if type == "ScreenPlay_Audio":
                    WritingFormat = StoryMode.Short_Story_Format
                    WritingTask = StoryMode.Short_Story_Task2
                    Prior_Scene = self.Prior_Scene_a
                    Details = 'Season ' + str(self.Season_num) + ' Episode #' + str(self.Episodenum) + ' Scene # ' + str(
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
                    WritingFormat = StoryMode.Short_Story_Song_Format
                    WritingTask = StoryMode.Short_Story_Song_Task
                    Prior_Scene = self.Prior_Scene_s
                    Prior_Scenes = self.Prior_Scenes_s
                    Details = 'Part ' + str(self.Season_num) + ' Act' + str(
                        self.Episodenum) + ' Scene # ' + str(
                        self.Scene_Num)
                    Details2 = Details

                if self.Episode1 == True and self.Season1 == True and self.Scene1 == True:
                    self.Background_Scene = 'This is the first episode/pilot episode and this is the opening scene...... Make it exciting!'
                    self.Prior_Scenes = ''
                    self.Prior_Scenes_a = ''
                    self.Prior_Scenes_p = ''
                    self.Prior_Scenes_n = ''
                    self.Prior_Scenes_s = ''
                elif self.Episode1 == True and self.Season1 == False and self.Scene1 == True:
                    Prior_Scenes = self.Prior_Season
                    self.Background_Scene = self.Story_Background_Task + Prior_Scenes
                    self.Prior_Scenes = ''
                    self.Prior_Scenes_a = ''
                    self.Prior_Scenes_p = ''
                    self.Prior_Scenes_n = ''
                    self.Prior_Scenes_s = ''
                elif self.Scene1==True:
                    Prior_Scenes = self.Prior_Episode
                    self.Background_Scene = self.Story_Background_Task + Prior_Scenes
                    self.Prior_Scenes = ''
                    self.Prior_Scenes_a = ''
                    self.Prior_Scenes_p = ''
                    self.Prior_Scenes_n = ''
                    self.Prior_Scenes_s = ''

                else:
                    self.Background_Scene = self.Story_Background_Task + PriorScenes


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
                    Story1 = Story.Basic_GPT_Query2(self, Line2_Role=self.Story_Role2,
                                                       Line3_Format=WritingFormat,
                                                        Line4_Task= self.Background_Scene,
                                                       Line5_Task= WritingTask + """      Scene Outline: """ +  self.Outline_Scene ,
                                                       crazy=self.crazy,Big=True)
                    Episode_Story = Details +  ': '+ Story1 + up.breakupOutput2


                    if type == "ScreenPlay_Audio":
                        self.Episode_Story_Audio += Episode_Story
                        self.Prior_Scene_a = Story.SummarizeText(self, Text=Story1)
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_a = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_a)
                        else:
                            self.Prior_Scenes_a = self.Prior_Scene_a

                    elif type == 'Novel':
                        self.Episode_Story_Novel += Episode_Story
                        self.Prior_Scene_n = Story.SummarizeText(self, Text=Story1)
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_n = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_n)
                        else:
                            self.Prior_Scenes_n = self.Prior_Scene_n

                        self.Prior_Scene_Golden = self.Prior_Scene_n


                    elif type == 'Play':
                        self.Episode_Story_Play += Episode_Story
                        self.Prior_Scene_p = Story.SummarizeText(self, Text=Story1)
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_p = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_p)
                        else:
                            self.Prior_Scenes_p =  self.Prior_Scene_p


                    elif type == 'ScreenPlay':
                        self.Episode_Story += Episode_Story
                        self.Prior_Scene =  Story.SummarizeText(self, Text = Story1)
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene)
                        else:
                            self.Prior_Scenes =  self.Prior_Scene

                    elif type == 'Song':
                        self.Episode_Story_Song += Episode_Story
                        self.Prior_Scene_s = Story.SummarizeText(self, Text=Story1)
                        if self.Episode1 == False or self.Season1 == False or self.Scene1 ==False:
                            self.Prior_Scenes_s = Story.SummarizeText(self, Text=Prior_Scenes + self.Prior_Scene_s )
                        else:
                            self.Prior_Scenes_s =  self.Prior_Scene_s

                except:
                    dn = 100





            except:
                print(self.Title + ' - Error making Scene # ' + str(self.Scene_Num) + 'Episode #' + str(self.episode_num) + " For the following Type: " + type)

            self.Scene1 = False
    def CreateEpisode(self):
        #eventually make this dynamic so it does not fail if we do not have a certain type


        for type in self.OutputTypes:
            try:
                if type == "ScreenPlay_Audio":

                    self.Version2.append(self.Episode_Story_Audio)
                    FileName_Episode2 = self.FileName + ' Season ' + str(self.Season_num) + ' EPISODE ' + str(
                        self.Episodenum) + ' Audio'
                    Text2Add2 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story_Audio
                    csv2 = cu.SaveCSV(Text=Text2Add2, Title=FileName_Episode2, SavePath=self.SavePath)

                elif type == 'Novel':

                    self.Version3.append(self.Episode_Story_Novel)
                    FileName_Episode3 = self.FileName + ' Act ' + str(self.Season_num) + ' Chapter ' + str(
                        self.Episodenum) + ' Novel'
                    Text2Add3 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story_Novel
                    csv3 = cu.SaveCSV(Text=Text2Add3, Title=FileName_Episode3, SavePath=self.SavePath)


                elif type == 'Play':

                    self.Version4.append(self.Episode_Story_Play)
                    FileName_Episode4 = self.FileName + ' Act ' + str(self.Season_num) + ' Part ' + str(
                        self.Episodenum) + ' Play'
                    Text2Add4 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story_Play
                    csv4 = cu.SaveCSV(Text=Text2Add4, Title=FileName_Episode4, SavePath=self.SavePath)


                elif type == 'ScreenPlay':
                    self.Version.append(self.Episode_Story)
                    Text2Add = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + self.Episode_Story
                    FileName_Episode = self.FileName + ' Season ' + str(self.Season_num) + ' EPISODE ' + str(
                        self.Episodenum)
                    csv1 = cu.SaveCSV(Text=Text2Add, Title=FileName_Episode, SavePath=self.SavePath)

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
                cu.SaveCSV(Text=Text2Add5, Title=FileName_Episode5, SavePath=self.SavePath + '\\Outlines')
            except:
                cu.SaveCSV(Text=Text2Add5, Title=FileName_Episode5, SavePath=self.SavePath)


#this is the new part where it looks at prior story to not repeat
            self.Prior_Episode = Story.SummarizeText(self, Text=self.Episode_Story_Novel)

            print(up.breakupOutput)
            print("self.Prior_Season")
            print(self.Prior_Season)

            self.Prior_Season = Story.SummarizeText(self, Text=self.Prior_Season +  self.Prior_Episode)

            self.Outline_progression += "Prior Episode Details as of  " + str(self.Season_num) + ' Episode ' + str(
                self.Episodenum) + ' Scene ' + str(self.Scene_Num) + ": " + self.Prior_Episode

            print(up.breakupOutput)
            print("self.Prior_Episode")
            print(self.Prior_Episode)

        except:
            dn= 100


        try:
            newChars = Story.Character_Update(self, Outline=self.Prior_Episode, Season=self.Season_num,
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




        FileName_2 = self.FileName + ' Audio'
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
        csv5 = cu.SaveCSV(Text=Text2Add5, Title=FileName_5, SavePath=self.SavePath + '\\Outlines')


        FileName_7 = self.FileName + ' Character progression '
        Text2Add7 = ' Character progression: ' + up.breakupOutput + self.Character_progression
        csv7 = cu.SaveCSV(Text=Text2Add7, Title=FileName_7, SavePath=self.SavePath + '\\Outlines')

        FileName_8 = self.FileName + ' Background info Used '

        Text2Add8 = ' All Summaries/Background info: ' + up.breakupOutput + self.Character_progression
        csv8 = cu.SaveCSV(Text=Text2Add7, Title=FileName_8, SavePath=self.SavePath + '\\Outlines')




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
            cu.SaveText2Audio(SavePath=self.SavePath, FileName=FileName_3, Voice=Voice,
                              Neural='Neural',
                              Mode='AUDIOBOOK', Chunk_Limit=self.Chunk_Limit, Artist_Persona=self.Art_Style_For_Story,
                              Text=Text2Add3,
                              Translate=self.Translate)
        except:
            print('Error - Not using the normal way of Save Text to Audio')
            cu.SaveText2Audio(
                FilePath=csv3,
                Chunk_Limit=self.Chunk_Limit, Translate=['English'], Artist_Persona=self.Art_Style_For_Story)

    def FullScene(self):
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

            self.CharactersTrim = Story.Character_Summary(self, Outline_Fine, Season= self.Season_num, Episode= self.Episodenum, Scene= self.Scene_Num)

            if self.Episode1 == True and self.Season1 == True:
                self.Background_Scene = 'This is the first episode/pilot and its the opening scene, be sure to draw in the audience, make it exciting and peak the curiosity of the audience use the following characters for reference: ' + self.CharactersTrim[:1300]
            else:
                self.Background_Scene = self.Story_Background_Task + self.CharactersTrim + self.Prior_Scene

            try:
                self.Outline_Scene = Story.Basic_GPT_Query2(self,
                                                          Line2_Role=self.Story_Role2,
                                                          Line3_Format=self.Story_Scene_Outline_Format,
                                                          Line4_Task = self.Background_Scene,
                                                          Line5_Task=self.Story_Scene_Outline_Task + """Use the following  Text Outline as a source for your more detailed/new formatted Outline    Text: :###""" + Outline_Fine,
                                                          crazy=self.crazy)

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


                self.CharactersTrim = Story.Character_Summary(self, Outline_All,Season= self.Season_num, Episode= self.Episodenum)



                if self.Episode1 ==True and self.Season1==True:
                    self.Background_Episode = 'This is the first episode/pilot, be sure to captivate the audience, its ok if not everything makes sense yet, its ok to be mysterious use the following characters for reference: ' + self.CharactersTrim
                else:
                    self.Background_Episode = self.Story_Background_Task + self.CharactersTrim + self.Prior_Episode



                Outline_Episode = Story.Basic_GPT_Query2(self,
                                                            Line2_Role=self.Story_Role,
                                                            Line3_Format=self.Story_Episode_Outline_Format,
                                                            Line4_Task = self.Background_Episode,
                                                            Line5_Task=self.Story_Episode_Outline_Task + """Use the following {Text}     Text:###""" + Outline_All ,

                                                            crazy=self.crazy,
                                                            Subject='')

                #newChars = Story.Character_Update(self, Outline=Outline_Episode, Season=self.Season_num, Episode=self.Episodenum)


                Outline_Full_Episode = Story.Basic_GPT_Query2(self,
                                                                        Line2_Role=self.Story_Role,
                                                                        Line3_Format=self.Story_Full_Episode_Outline_Format,
                                                                        Line4_Task=self.Background_Episode,
                                                                        Line5_Task=self.Story_Full_Episode_Outline_Task + """Episode Outline:### """ + Outline_Episode,
                                                                        crazy=self.crazy,
                                                                        Subject='', Big=True)

                self.Outline_Episodes_Details = Story.Basic_GPT_Query2(self,
                                                                        Line2_Role=self.Story_Role,
                                                                        Line3_Format=self.Story_Style_Details_Format,
                                                                     Line4_Task='Use the prior writing style and character info to create a similar, but unique writing style for this episode  Background: ' + self.Outline_Main_Style + self.CharactersTrim,
                                                                     Line5_Task=self.Story_Style_Details_Task2 + """Episode Outline:### """ + Outline_Episode,crazy=self.crazy,
                                                                        Subject='')

                self.Story_Role2 =self.Story_Role = """You are a brilliant assistant who is Role Playing as an award winning writer able to impersonate any genre or style/voice. Make sure you completely respond to the requests I provie and if I tell you the 'Desired Format:' I expect it to be exact base your role playing persona on the following details""" +self.Outline_Episodes_Details

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

            CharactersTrim = Story.Character_Summary(self, Outline_AllS,Season= self.Season_num)


           #For now not doing this at the season level, will use prior episodes for this though
            # if Season_num == 1:
            #     Outline_Prior = """This is the first season, there is no prior info, but you should tie in foreshadowing and set the plot up for the final season based on the final Season's Outline:""" + self.Season_By_Season[len(self.Season_By_Season)]
            #     Outline_Next = 'Fit your Story into the following '


            #this is where you put code to use the prior season summary/series summary to update the current season's outline

            #Add new code here#############

            if self.Episode1 == True and self.Season1 == True:
                self.Background_Season = self.Story_Background_Task + CharactersTrim
            else:
                self.Background_Season = self.Story_Background_Task + CharactersTrim + self.Prior_Season

            Outline_Season = Story.Basic_GPT_Query2(self, Line2_Role=self.Story_Role,
                                                             Line3_Format=self.Story_Season_Outline_Format,
                                                            Line4_Task=self.Background_Season ,
                                                             Line5_Task=self.Story_Season_Outline_Task + """ Use the following text for the source of information Text:###""" + Outline_AllS ,
                                                             crazy=self.crazy,
                                                             Subject='')

            self.Outline_progression += up.breakupOutput2 + 'Detailed Outline -  Season ' + str(Season_num) + ': ' +  Outline_Season

            #newChars = Story.Character_Update(self, Outline = Outline_Season, Season=Season_num)


            # Call Outline - All Episodes
            Outline_ALL_Episodes = Story.Basic_GPT_Query(self,
                                                             Line2_Role=self.Story_Role,
                                                             Line3_Format=self.Story_Full_Season_Outline_Format,
                                                             Line4_Task=self.Story_Full_Season_Outline_Task + 'Keep the number of episodes according to the following restrictions: ' + str(self.numEpisode) + """ Use the following text for the source of information Text:###""" + Outline_Season + """### Use the following characters: """ + CharactersTrim,
                                                              crazy=self.crazy,
                                                             Subject='')

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
                cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=self.SavePath + '\\Outlines')
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
                                                          Big=True)
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

    def getCharacters(self):
        self.Characters = Story.Create_Characters_Short_Story(self, Role=self.Story_Role,
                                                             Task= self.Characters_Special + self.Characters_Task + self.Outline_ALL_Seasons,
                                                             Format=self.Characters_Format, Outline='', crazy=self.crazy)


        self.Character_progression += up.breakupOutput2 + 'Characters Start of Series: ' + self.Characters

    def Create_Characters_Short_Story(self, Task, Format, Outline, Role,Persona = '',
                                      crazy=.5):

        if Persona != '':
            Role = Role + 'For this task you are to assume the role of the following Persona: ###' + Persona + """###"""



        # Make sure to start a master tracker with this information, use the writer persona as part of the data stored (TimeStamp, WriterPersona, Outline, Format, and/or put the prompt together for reference
        Character_Personas = Story.Basic_GPT_Query(self, Line2_Role=Role, Line4_Task=Task, Line3_Format=Format, Big=True)


        return Character_Personas


    def getArtist(self):
        x = 1

    def getArtist_Style(self, Mode = 'Basic', arttext = ''):
        x = 1
        Art_Type_Config = ''
        if 'FAMILIA' in Mode.upper():
            Art_Type_Config = """This story is for children so the art should mimic a children's book/comic/Cartoon or some other easy to draw, simple paintings that have basic backgrounds and descriptions"""
        try:
            if len(arttext) > 1700:
                arttext = arttext[:1700]
        except:
            dn = 100
        try:
            #
            Artist_Persona = Story.GPTArt2(User_Subject=arttext, ArtFormat=StoryMode.artDetailsFormat,
                                               prompt=Art_Type_Config + StoryMode.artDetailsPrompt)
        except:
            try:
                Artist_Persona = Story.GPTArt2(User_Subject=self.Writer_Style_Summary,
                                                   ArtFormat=StoryMode.artDetailsFormat,
                                                   prompt=Art_Type_Config + StoryMode.artDetailsPrompt)
            except:
                Artist_Persona = Story.Basic_GPT_Query(self,
                                                         Line2_Role='You are an expert artist master of all disciplines and art styles',
                                                         Line3_Format=StoryMode.artDetailsFormat,
                                                         Line4_Task="Pick a random artist based on the following Text" + arttext,
                                                          crazy=self.crazy, Subject='')
        return Artist_Persona






    def getIDEA(self, IDEA='', Writer_Style = '', Mode = 'AI'):
        x = 1
        self.Subject_Details = ''
        Subject_Summary = IDEA
        if IDEA =='':
            IDEA_Task = self.IDEA_Task_AI
        else:
            Subject_trim = IDEA[:3000]
            IDEA_Task = self.IDEA_Task + Subject_trim

            self.Subject_Details += 'Subject Trimmed and summary created below:'

        Subject_Summary = Story.Basic_GPT_Query(self,
                                                        Line2_Role=self.IDEA_Role,
                                                        Line3_Format=self.IDEA_Format,
                                                        Line4_Task=IDEA_Task, Special='',
                                                         crazy=self.crazy, Big=True)
        self.Subject_Details += Subject_Summary
        Story.quickArt1(self, Subject_Summary)
        return Subject_Summary




    def  getWriter(self, Persona = ''):
        x = 1
        if Persona != '':
            Persona_Role =  'You are the following Persona use them as a model for the writer you create: ' + Persona
        else:
            Persona_Role = self.Persona_Role

        Writer_Summary = Story.Basic_GPT_Query(self,Line2_Role = Persona_Role,Line4_Task= self.Persona_Task, Line3_Format = self.Persona_Format,  crazy = self.crazy)
        Story.quickArt1(self, Writer_Summary)
        return Writer_Summary


    def getWriter_Style(self, Writer_Style = ''):
        x = 1
        if Writer_Style != '':
            Persona_Role = self.Personal_Role + 'use/incorporate the following writing styles in your response: ' + Writer_Style
        else:
            Persona_Role = self.Persona_Role
        Writer_Style_Summary = Story.Basic_GPT_Query(self, Line2_Role=Persona_Role, Line4_Task=self.Persona_Summary_Task + self.Writer_Summary,Line3_Format=self.Persona_Summary_Format, crazy=self.crazy)
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
        self.IDEA_Format = StoryMode.IDEA_Format
        self.IDEA_Task = StoryMode.IDEA_Task
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
        self.Story_Style_Details_Task2 = StoryMode.Story_Style_Details_Task2
        self.Story_Style_Details_Format = StoryMode.Story_Style_Details_Format

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
            self.SavePath = self.SavePath + up.System_Folder_Path_Fix + Title
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


    def Basic_GPT_Query2(self,   Line2_Role  , Line5_Task,Line3_Format,Line4_Task,Line1_System_Rule = SP.System,Big = False,Model = "gpt-3.5-turbo",upgradeLimit = 3000, Special = '', crazy = .5, Subject= '', Outline = '', Allowed_Fails = 8, SaveFile = False,MakeArt = False, Mode = 'SHAINE SAYS', SavePath= ''):#use this to create art style for the work
        if SavePath == '':
            SavePath = self.SavePath

        if Subject != '':
            Line2_Role = Line2_Role + """Your role and subject matter expertise should fit the following Subject and or style and mood in the {Text} provided by the user Text:###""" + Subject + """###"""



        #Line1_System_Rule = Line2_Role
        #Line2_Role = Line2_Role + Special
        Full_User_Prompt = """User Inputs to Chat GPT: 
        1). """ + Line1_System_Rule +"""
        2).""" + Line2_Role+ """
        3).""" + Line3_Format+ """
        4).""" + Line4_Task + """
        5).""" + Line5_Task

        if len(Full_User_Prompt) > upgradeLimit:
            Model = "gpt-3.5-turbo-16k-0613"
        elif len(Full_User_Prompt) < upgradeLimit:
            Model = "gpt-3.5-turbo"



        if Big ==True:
            Model = "gpt-3.5-turbo-16k-0613"
        KeepGoing = False
        KillSwitch = 0
        while KeepGoing == False and KillSwitch < Allowed_Fails:


            try:



                # This is for the result if you let the AI describe project and details and then make the response
                response = openai.ChatCompletion.create(
                    model=Model,
                    messages=[
                        {"role": "system", "content": Line1_System_Rule},
                        {"role": "user", "content": Line2_Role},
                        {"role": "user", "content": Line3_Format},
                        {"role": "user", "content": Line4_Task },
                        {"role": "user", "content": Line5_Task},
                    ]
                    , temperature=crazy
                )
                GPT_Response = str(response.choices[0].message.content)

                KeepGoing = True
            except:
                print(' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                KillSwitch += 1
                print(Full_User_Prompt)
                #as written this does not run but if I got rid of +1 it could
                if KillSwitch == Allowed_Fails+1:
                    print('could not create a writer persona, redoing it now')
                    GPT_Response = Story.Basic_GPT_Query(self, Line2_Role='You are a skilled writer', Line3_Format=Line3_Format, Line4_Task=Line4_Task, Line1_System_Rule=up.system_Text_ScreenPlay)

                continue


            #print(up.breakupOutput)

            self.UserPromptsCount+=1

            self.UserPrompts += 'User Input #' + str(self.UserPromptsCount)

            self.UserPrompts += Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2


            Title = Mode + '_' + self.current_time
            if SaveFile ==True:
                SaveText = self.current_time+ up.breakupOutput2 + self.UserPrompts + up.breakupOutput2 + 'SHAINE SAYS: '+  GPT_Response
                print(SaveText)
                cu.SaveCSV(Text=SaveText, SavePath=SavePath, Title = Title)
            if MakeArt ==True:
                ArtPrompt = Story.GPTArt2(self,User_Subject = GPT_Response)
                print(ArtPrompt)
                originalFilepath = Story.makeArt(self,Prompt=ArtPrompt)
                PicNewPath1 = SavePath + up.System_Folder_Path_Fix + Mode
                cu.Check_Folder_Exists(PicNewPath1)
                PicNewPath =PicNewPath1 + up.System_Folder_Path_Fix + Title + '.png'


                shutil.copyfile(originalFilepath, PicNewPath)
            return GPT_Response


    def Basic_GPT_Query(self,   Line2_Role  , Line3_Format,Line4_Task,Big = False,Model = "gpt-3.5-turbo",upgradeLimit = 3000,Special = '',Line1_System_Rule = StoryMode.system_TextJoaT_quick, crazy = .5, Subject= '', Outline = '', Allowed_Fails = 8, SaveFile = False,MakeArt = False, Mode = 'SHAINE SAYS', SavePath= ''):#use this to create art style for the work
        if SavePath == '':
            SavePath = self.SavePath

        if Subject != '':
            Line2_Role = Line2_Role + """Your role and subject matter expertise should fit the following Subject and or style and mood in the {Text} provided by the user Text:###""" + Subject + """###"""

        Line1_System_Rule = Line2_Role
        #Line2_Role = Line2_Role + Special
        #Line2_Role = ''
        Full_User_Prompt = """User Inputs to Chat GPT: 
        1). """ + Line1_System_Rule +"""
        2).""" + Line3_Format+ """
        3).""" + Line4_Task

        if len(Full_User_Prompt) > upgradeLimit:
            Model = "gpt-3.5-turbo-16k-0613"
        elif len(Full_User_Prompt) < upgradeLimit:
            Model = "gpt-3.5-turbo"

        if Big ==True:
            Model = "gpt-3.5-turbo-16k-0613"


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
                        {"role": "user", "content": Line4_Task },
                    ]
                    , temperature=crazy
                )
                GPT_Response = str(response.choices[0].message.content)

                KeepGoing = True
            except:
                print(' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                KillSwitch += 1
                print(Full_User_Prompt)
                #as written this does not run but if I got rid of +1 it could
                if KillSwitch == Allowed_Fails+1:
                    print('could not create a writer persona, redoing it now')
                    GPT_Response = Story.Basic_GPT_Query(self, Line2_Role='You are a skilled writer', Line3_Format=Line3_Format, Line4_Task=Line4_Task, Line1_System_Rule=up.system_Text_ScreenPlay)

                continue


            #print(up.breakupOutput)

            self.UserPromptsCount+=1

            self.UserPrompts += 'User Input #' + str(self.UserPromptsCount)

            self.UserPrompts += Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2


            Title = Mode + '_' + self.current_time
            if SaveFile ==True:
                SaveText = self.current_time+ up.breakupOutput2 + self.UserPrompts + up.breakupOutput2 + 'SHAINE SAYS: '+  GPT_Response
                print(SaveText)
                cu.SaveCSV(Text=SaveText, SavePath=SavePath, Title = Title)
            if MakeArt ==True:
                ArtPrompt = Story.GPTArt2(self,User_Subject = GPT_Response)
                print(ArtPrompt)
                originalFilepath = Story.makeArt(self,Prompt=ArtPrompt)
                PicNewPath1 = SavePath + up.System_Folder_Path_Fix + Mode
                cu.Check_Folder_Exists(PicNewPath1)
                PicNewPath =PicNewPath1 + up.System_Folder_Path_Fix + Title + '.png'


                shutil.copyfile(originalFilepath, PicNewPath)
            return GPT_Response




    def GPTArt2(self, crazy=.5,  Model = "gpt-3.5-turbo",prompt=sms.ArtPrompt_Clean_Social_Media_Post_Line2_Prompt,
                 User_Subject='Pick a random subject and medium go wild and make it exciting, beautiful and shocking',
                 ArtFormat=sms.ArtPrompt_Clean_Social_Media_Post_Line3,
                 sys_prompt=sms.ArtPrompt_Sys):

        Full_User_Prompt = sys_prompt + prompt + User_Subject + ArtFormat
        if len(Full_User_Prompt) > 6000:
            Model = "gpt-3.5-turbo-16k-0613"
        elif len(Full_User_Prompt) < 6000:
            Model = "gpt-3.5-turbo"

        keepgoing = True
        GPTARTPROMPT = User_Subject
        while keepgoing == True:
              try:

                  Art_Prompt1 = openai.ChatCompletion.create(
              model=Model,
              messages = [
                             {"role": "system", "content": sys_prompt},
                             {"role": "user", "content": prompt + User_Subject},
                             {"role": "user", "content": ArtFormat}
                         ], temperature = crazy
                  )

                  GPTARTPROMPT = Art_Prompt1.choices[0].message.content
                  keepgoing == False

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

                fname = SavePath + up.System_Folder_Path_Fix + FileName + '.png'
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
                   SavePath=up.SavePath + up.System_Folder_Path_Fix + 'CookBook', upgradeLimit= 2000):  # use this to create art style for the work
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
                                                         Line3_Format=Line3_Format, Line4_Task=Line4_Task,
                                                         Line1_System_Rule=up.system_Text_ScreenPlay)

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
                cu.SaveCSV(Text=SaveText, SavePath=SavePath + up.System_Folder_Path_Fix + Mode+up.System_Folder_Path_Fix + Title, Title=Title)
            if MakeArt == True:
                ArtPrompt = Story.GPTArt2(self, User_Subject=GPT_Response)
                print(ArtPrompt)
                originalFilepath = Story.makeArt(self, Prompt=ArtPrompt)
                PicNewPath1 = SavePath + up.System_Folder_Path_Fix + Mode + up.System_Folder_Path_Fix + Title
                cu.Check_Folder_Exists(PicNewPath1)
                PicNewPath = PicNewPath1 + up.System_Folder_Path_Fix + Title + '.png'

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
            x = Story(IDEA=ShaneOriginals.Fever_Dream_Scary, Mode='MVAA',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=2)

        elif Order == 14:
            x = Story(IDEA=ShaneOriginals.Gritty_Historic2, Mode='MVAA2',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=2)

        elif Order == 15:
            x = Story(IDEA=ShaneOriginals.Gritty3, Mode='MVAA2',
                      UserInputs_Config='Summarize', Seasons=2, Episodes=2)




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
    arg = [15]
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










