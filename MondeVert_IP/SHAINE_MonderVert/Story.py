import datetime
import sys

import pandas as pd
global Record
from  MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Wedding_Prompts as WeddingP
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Social_Media_SHAINE as sms
from secrets import randbelow
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Long_User_Prompts as lup, User_Prefs as up, \
    Stories_For_Audio_Files as SAF, StoryMode_Wizard as StoryMode
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





class Story():
    def __init__(self, voice=4, language_settings=1, Mode = 'Story', SavePath =up.SavePath, Writer = '',  Writer_Style = '',Artist = '', Artist_Style = '', Story_Type = 'ScreenPlay', Seasons = '', Episodes = '', Books = '', Acts = '', Scenes = '', Movies = '', Text_Output_Config = [''], UserInputs_Config = 'AI Only', IDEA_Source = 'AI', Output_Audio_Config = ''):
        self.voice = voice
        self.language_settings = language_settings
        self.AssistantName = up.getAssistantName()
        self.UserName = up.getUserName()
        self.transcript_Final = ''
        self.API_Key = API_Key
        self.Show_Print = True
        self.Correction_Comment = ''
        self.AI_Corrected_Content = ''
        self.SilentMode = False





        self.current_time1 = datetime.datetime.now()
        self.current_time = self.current_time1.strftime('%m-%d-%Y_%H.%M')
        self.UserPrompts = ''

        voice_set = self.voice
        xVoice = 1
        self.UserPromptsCount = 0
        self.FilePaths = []
        self.FilePaths_Email = []
        self.Art_Descriptions = []


        #This is definitely needed, the stuff above might not be needed
        self.Request_log = []
        openai.api_key = API_Key
        self.SavePath = SavePath



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




        #UserManipulates the story if they choose to fill these in otherwise we trigger the AI to create these values
        self.Artist = Artist
        if self.Artist == '':
            Story.getArtist()
        elif self.UserInputs_Config == 'Summarize':
            Story.summarizeArtist()

        self.Artist_Style = Artist_Style
        if self.Artist_Style == '':
            #if this is blank we do not want to use it yet, once you have some text you can create this
            dn = 100
            #Story.getArtist_Style(self)
        elif self.UserInputs_Config == 'Summarize':
            Story.summarizeArtist_Style()

        self.Writer = Writer
        if self.Writer == '':
            Story.getWriter(self)
        elif self.UserInputs_Config == 'Summarize':
            Story.summarizeWriter(self)

        self.Writer_Style = Writer_Style
        if self.Writer_Style == '':
            Story.getWriter_Style(self)
        elif self.UserInputs_Config == 'Summarize':
            Story.summarizeWriter_Style(self)

        self.IDEA_Source = IDEA_Source
        if self.IDEA_Source == 'AI':
            Story.getIDEA(self)
        elif self.IDEA_Source == 'AI':
            Story.getIDEA(self)
        # elif self.UserInputs_Config == 'Summarize':
        #     Story.summarizeIDEA_Source()


                    #First --> Confirm Which Chat GPT to use for long user prompts
                    #Next update other parameters etc.
                    #Set up basic shells of each utility/Function
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


    def getArtist(self):
        x = 1

    def Artist_Style(self):
        x = 1

    def  getWriter(self):
        x = 1


    def getWriter_Style(self):
        x = 1

    def summarizeArtist(self):
        x = 1

    def summarizeArtist_Style(self):
        x = 1

    def summarizeWriter(self):
        x = 1

    def summarizeWriter_Style(self):
        x = 1

        #the following start blank,but the user is able to input their own values here



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