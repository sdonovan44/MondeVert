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



class AutomationSpecialists():
    def __init__(self):
        d = 1


class consultant():
    def __init__(self):
        d = 1




#the other bot reads the text and

class MasterDeveloper():
    def __init__(self):
        d = 1

#$This version should likely use a model that is better based on snip of code
#have it write code based on snip of code
#have it add comments to its own code after it writes it based on snip of code
#have it provide additional options if something does not work based on snip of code
#provide an explanation of what the code is doing and how to make it work based on snip of code
#provide troubleshooting tips based on snip of code
#Have different masteries per language and maybe even libraries if needed.
#some should have ability to code multiple languages
#ask developer
#have the moderator listening the whole time in a separate thread
#moderator should decide who the question goes to but maybe not idk
#moderator is key, he is basically my ability to control the podcast and get certain things done easily, He will have a specific voice I give him to talk to me with.
#Maybe I can eventually have him part of it like a cohost, but not yet.
#idea for a cohost like socrates or whoever I choose
#I can make my cohost whoever I choose on the fly, there are options to quick swap, use saved cohost or make new one
#I can similar to pull in guest, pull in experts (if not by default)
#have an option for *Normal SHAINE to pull info from GPT, in future using other tools would be amazing
#have ability to run all of my tools via this but not yet
#journal mode/therapy mode should become part of this (other than podcast mode maybe have journal/therapy mode priority)




#Make there be an option where I use characterai to make a new character and have them respond to me, look into importing this asap
#also look for other alternatives to chat gpt or learn how to combine multiple


#Under discussion there should be variables for who is in the discussion
#Pick who is leading the discussion
#Dialogue style
#Purpose/Goal/Task (maybe separate for type of task not sure though)
#have someone who judges if discussion is done/task accomplished
#have a time limit for how long conversation should go
#build a mode where user interacts, you should have a way for the AI to review the last text said (if the person just spoke they should wait for a response, if they get no response after 10 seconds be like or not... or fuck me right make it funny, but then maybe wait like 30 seconds and ask if they are done talking, it will end then and there is yes, otherwise )
#They should be waiting for long pause form user to generate a response, if multiple, again same bot cant speak twice unless no response given etc.
#context bot reads the message and summarrizes it, should keep everyones response tracked separate, also together, the summarry as well as actual transcript should be saved both together and separated by person speaking
#The stuff the USER says should be treated as if he is God Almighty, the creater said it as a commandment meaning if he says do something the AI must with no hesitation, also there should be a way to remove or add people to the conversation as needed
#it would be cool if what we discuss could trigger writing a movie or story etc without ending the conversation
#for scrum mode, maybe we can include the user and he can be the main person or the managing director that has final say. it could be a cool way to solve tasks for sure
#if you say something like I am done talking to [name] they should ask if you want them to leave which you then say yes (it does not need to be chat GPT you could maybe just look for the word and the name or something IDK.)
#if you say something like I want to bring in another character or person to discuss further, subject expert. Role play that you are x, based on blah blah
#Also have option to bring on random character that is going to be interviewed by me.
#


#for now open a window that does not close and is like an interactive menu for the discussion live, when the discussion ends there should be option to view info/text
#The window should be a dark themed chat where

class Discussion():
    def __init__(self,IDEA,Host,Moderator,Guests =[], Moderator_Mode = 'Load'):
        d = 1


#needs to be able to listen to user, the user is really where it kicks off, not always but in this case yes, maybe it should always be whoever is the host.
#if AI host they come up with what to say and goes from there
#Moderator in a separate thread reads what user says, the text is already displayed on the screen, it would be cool to do this for every few words so it is not too delayed.
#Moderator is looking for me to ask a question or say guest name then it will send a prompt that way
#at first have the amount of silence time pretty long, have ability to adjust by increments of .2 Sec or something like that
#have option to make it really long as well, also have option to make it reasonably short, or default
#if I say like "let me finsh or you interuppted me automatically adjust it up by .2 and then say sorry (whoever interuppted me, it should by default be Moderator voice
# but if the other person speaks make them say sorry it would be funny)
#use persona and key info from the user's role characteristics






















#Podcast Mode

#Step0 - Make your Idea (if shane is host load the bio and make the persona), early on I want to save the persona's so that I can grab the data again in the future and so that it is available for reference
#Step1 - Create Guest, either using topic I come up with, or random on the spot, that can be an option I choose from
#Step2 - Update all of Guest info
#Step3 - Prepare Topics of discussion share with me the host (or AI host if that ever happens, maybe start with AI with AI, or me and AI, I kinda like me and AI so I can guide it)
#Step4 - Prep Guest for topic etc/give background they are on my podcast. Eventually I should use AI to come up with a set of things to prep them for might make it more interesting, also I can feed in the intial idea as well.
#Step5 - Have moderator/SHAINE say introduction, Guest says hello (Monde Vert in partnership with Amini Amor presents SHAINE SHOW, where together Shane D and his virtual assistant SHAINE speak to AI and other guests about life and other things.
#Step6 - Run Discussion, have a separate tool listening to my responses so it knows when to end conversation or run specific tool (add guest, change something, add cohost etc. also have option to tweak the guest if its not working)
#Step7 - Save all the transcripts so they can be reviewd, try to record as well if microphone allows it, if not I need to record to document this as well.


#Notes about Discussion tool
# After the first greeting from guest it should wait for me to speak, note it should keep track of last speaker so there is no double talking. Build in a safe word to end things abrubtly so I can get out and save everything if needed
# Do not let double talk, if it keeps cutting me off I should have something that is a code word for when to stop listening, use global/self variable
#Then its off, before sending anything to Chat GPT, it should first analyze what I say for quick words that supercede going to chat gpt so I am not abusing him, guest should have filler stuff that moderator can pull from to kill time, especially if I say something like I am thinking or something.
# #If I say hold on that can be code word for wait 10 seconds to go start listening again. Also if I say codeword and then pause then it can stop until I say go/continue or something like that
#Basically at first I should have it save after every thing
#for context I will keep the entire conversation broken up by what I said and what he said, also a mix of both clearly marked with who says what. the last 5 things will be presented to the chatbot
#anything beyond the 5 things every time it goes beyond the 5th thing said, chat gpt will summarrize that, then using that and prior full summary it will add context
#Ultimately you get the following: Full Conversation saved in one string, Full conversation saved response by response (both),#Summary of every 6 blocks or whenever the total background is more than x characters ,
# Character/person specific responses
#******MAKE AN OPTION for them to review what they said previously about x, it will show them what they said previously, then they will say a short elaboration on the topic, while saying the quick story they are going to create the other story and once that is ready and first story has been spoken outloud
#they will then finish the thought, For this task keep what the user/host asks for what they elaborate on, the first part is reintroduction to what they said and a little more info
####Maybe do the same thing for a specific part of the conversation or something, we can use mod to confirm what part and then they can intervene (the more important part is the review x, because it might help me get them to give me insights that I need that they are not giving me)





    #Podcast is where I build the discussion, discussion is a small piece of a bigger inner working at play

#Note in the future it will start with main menu of SHAINE, part of the main menu, I will have choice of using default prompt for idea or provide one on the fly or if I want to let the AI come up with one.
#I am for now going to hand-feed in the prompt so it will not be fully how I want it but its a good start
class Podcast(self,IDEA,Host,Moderator,Guests =[], Moderator_Mode = 'Load'):
    def __init__(self):
        d = 1
        self.IDEA = IDEA
        self.Host = Host
        self.Moderator =Moderator
        self.Guests = Guests
        self.Moderator_Mode =Moderator_Mode




    def MakeIdea(self):
        x = 1



    def CreateGuest(self):
        x = 1


    def UpdateGuestInfo(self):
        x= 1

    def PrepareTopics(self):
        x = 1


    def PrepareGuest(self):
        x = 1

    def ModeratorIntroduction(self ):
        x = 1

    #Moderator has either a prefilled intro, or he comes up with one on the fly and speaks it out lout, it would be interesting to have music to play as an intro and maybe make this random based on character but I do not know if this is even possible yet.....
    #after SHAINE/moderator says his thing, guest has his own first words and then we run the run discussion tool do all of this under the podcast function I think
    def GuestIntroduction(self):
        x = 1

    #this is where I start the actual function known as discussion, it will need certain parameters and to be written of course
    def RunDiscussion(self, Topic, Guests, Host, Moderator, Requirements,  ):
        x = 1
        #this is maybe pretty basic where it just calls the function, maybe I do not even need it as part of this class and just do it separatley idk yet





#This is where I kick off the podcast and run through all of the functions above
    def RunPodcast(self):
        x = 1

        Podcast.MakeIdea(self)

        Podcast.CreateGuest(self)

        if 'LOAD' is in self.Moderator_Mode.upper() :
            Mod = Podcast.LoadModerator()
        else:
            Mod = Podcast.CreateModerator()

        Podcast.UpdateGuestInfo(self)

        Podcast.PrepareTopics(self)

        Podcast.PrepareGuest(self)

        Podcast.ModeratorIntroduction(self)

        Podcast.GuestIntroduction(self)

        Podcast.RunDiscussion(self, Moderator = Mod)

        #create function where we have myself say goodbye and maybe the mod gives a quick wrap up,
        # there should definitely be a last quip from the guest
        Podcast.SignOff


    def LoadModerator(self):
        d = 1

    def CreateModerator(self):
        x = 1








class Moderator():
    def __init__(self):
        d = 1






class ScrumTeam():
    def __init__(self):
        d = 1


class ScrumMaster():
    def __init__(self):
        d = 1


class ProductOwner():
    def __init__(self):
        d = 1

class Team_Lead():
    def __init__(self):
        d = 1


class QA():
    def __init__(self):
        d = 1

class BA():
    def __init__(self):
        d = 1


class Researcher:
    def __init__(self):
        d = 1

class BusinessTeamLead:
    def __init__(self):
        d = 1


class ManagingDirector():
    def __init__(self):
        d = 1



