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


class SYSTEM():
    def __init__(self):
        d = 1


class Task():
    def __init__(self):
        d = 1


class Background():
    def __init__(self):
        d = 1


class Format():
    def __init__(self):
        d = 1



Format_Person = """
Name|Age|Sex|Occupation|Hometown|CurrentLocation|languages|PhysicalDescription|Personality|Wants|Needs|Secrets|Drive|Values  
                 Voice|QuickStoryTopics|quick Jokes or style of jokes|Family|Friends|FunFacts|Short Bio
"""

#task1 = createpersona
#task2 = create detailed bio, stories about his quick story topics at least 2-3 and store them. If you are out of stories kick off a separate thread to make another story based on discussion we have been having, when the time is right interject with it, maybe write the joke and then once its done and no one is talking you either start telling your story or


class Person():
    def __init__(self, Name, Age, Sex, Wants, Needs, Secrets, Drive, Occupation, Hometown, CurrentLocation, Personality, Bio, PhysicalDescription, Values,
                 Voice, SpeakVoice,QuickStories,Jokes,ElavatorPitch, Family, Friends,FunFact, Greetings, Language_Style, Speaking_Style):
        d = 1
        self.Name


class Role():
    def __init__(self):
        d = 1


class Writer():
    def __init__(self):
        d = 1

class USER():
    def __init__(self):
        d = 1





class IDEA():
    def __init__(self):
        d = 1

class Part():
    def __init__(self):
        d = 1

class Scene():
    def __init__(self):
        d = 1

class  Characters():
    def __init__(self):
        d = 1








class Goal():
    def __init__(self):
        d = 1


class Task():
    def __init__(self):
        d = 1


class Request():
    def __init__(self):
        d = 1


class Reseach():
    def __init__(self):
        d = 1

class Musician():
    def __init__(self):
        d = 1

class LogicBot():
    def __init__(self):
        d = 1


class Discussion():
    def __init__(self):
        d = 1


class Menu():
    def __init__(self):
        d = 1


class Mode():
    def __init__(self):
        d = 1



class PresetBasic():

    def __init__(self):
        d = 1
