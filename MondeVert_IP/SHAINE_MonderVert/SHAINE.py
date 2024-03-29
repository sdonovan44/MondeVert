import datetime
import sys

import pandas as pd
from pathlib import Path, PureWindowsPath
global Record
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Wedding_Prompts as WeddingP
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Social_Media_SHAINE as sms
from secrets import randbelow
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Long_User_Prompts as lup, User_Prefs as up, \
    Stories_For_Audio_Files as SAF, StoryMode_Wizard as StoryMode
from threading import Event
from gingerit.gingerit import GingerIt
import numpy
import time
import re

# from MondeVert_IP.SHAINE_MonderVert.Testing_Files import AWS_Speech_Test  as AWS
# from exceptions import PendingDeprecationWarning
Record = ''
# import urllib2
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
import MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS.StoryOutlines as ShaneOriginals

# from email_config import gmail_pass, user, host, port


URL = "..."  # noqa
API_KEY = "..."


# make a transcript class that takes down all of my requests and saves to a text file
# have specific command for the assistant to save in a certain folder (always add date & time to the file
# create things like to do lists
# ideas
# stories and dialogue
# the key is being able to store it properly and sytemically access as well
# every program I create should be executeable through the assistant


# Urgent to do
# Make it a class
# have transcribe and also proofread (later) add method where in the middle of dictating you can add titles so it gets properly makred eventually
# bullets etc. parenthesis
# Have it so every pause puts a new line in between so its easy to pull out pauses etc.
# Most important is to have a mode where it callse poembot and reads the lines to me.
# .... also I would like for it to be a mini drama where I get multiple voices and characters that read
# the output etc eventually learn how to animate/make a nice script.
# create a series so eventually we might have a way to feed in characters to poem bot so its not just random like it is now lol

# 12/18/2022 get the assistant able to open the respective web browsers
# set up mouse so it has shortcuts
# be able to run on both mac and also the pc
# import the site view bot
# update the youtube bot so it hides ips properly and also so it loops through videos to not draw attention
#    (make it so it starts off slow then has pockets of 100 here and there big days occasionally and find out how to make it work properly
# have assistant able to run those on command (buy wifi adapter so I can have it running whenever & get new monitor for that too


# Update transcribe commands (Review file so far,#Have a separate function to make the title (different than subject)
##Also I should be able to mark the file as important based on results (add tag)
# Make a program that goes through and corrects the script into a new tab (puts subject as start of the word blocks (with other data in parenthesis for tagging)
# Also make it so that the poems do not overwrite but get concatenated together
# Make a theatre method that uses multithreading to do stuff
# overall threads should allow this to run faster
# Make it so I can update all meta data and also add more metadata
# Goal, mark as header (prior or next maybe)


# def MultiThread2(Args):
#     command_array = Args
#     number_of_commands = len(command_array)
#     def run_the_command(index):
#         exec (command_array[index])
#
#     threads = []
#     for i in range(number_of_commands):
#         try:
#             t = threading.Thread(target=run_the_command, args=(i,))
#             t.start()
#             threads.append(t)
#
#         except:
#             print('Error unable to pull the value from the ARGs parameter')
#


class MondeVert():
    def __init__(self, voice=4, language_settings=1):
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
        self.SavePath = up.SavePath
        self.Mode = 'SHAINE booted up'
        self.current_time1 = datetime.datetime.now()
        self.current_time = self.current_time1.strftime('%m-%d-%Y_%H.%M')
        self.UserPrompts = ''
        global xVoice
        global voice_set
        voice_set = self.voice
        xVoice = 1
        self.UserPromptsCount = 0
        self.FilePaths = []
        self.FilePaths_Email = []
        self.Art_Descriptions = []
        self.Request_log = []
        openai.api_key = API_Key

    def Open_Web(url):
        url = url
        webbrowser.open_new_tab(url)

    def speak(self, audio, Add2T=True, voice=''):
        if voice == '':
            voice = self.voice

        if Add2T == True:
            MondeVert.Add2Transcript(self, self.AssistantName + ': ' + audio)
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

    def speakSweet(self, audio, Add2T=True):
        if Add2T == True:
            MondeVert.Add2Transcript(self, self.AssistantName + ': ' + audio)
        engine = pyttsx3.init()
        # getter method(gets the current value
        # of engine property)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[4].id)
        # Method for the speaking of the assistant
        if self.SilentMode == False:
            engine.say(audio + "")
            # Blocks while processing all the currently
            # queued commands
            engine.runAndWait()
        else:
            print('Silent Mode Activated: ' + audio)

        # def RandomCharacters

    def testvoices(self):
        # import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        index = 0
        for voice in voices:
            print(f'index-> {index} -- {voice.name}')
            engine.setProperty('voice', voices[index].id)
            engine.say("Shane do you like this voice more than the last one you busy little bee turkish" + "")

            index += 1
        engine.runAndWait()

    def Setvoices(self, Quick=False):

        if Quick == False:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            index = 0
            indexCount = 0
            # load_dotenv()
            # Set up the OpenAI API client :
            openai.api_key = API_Key

            prompt = 'Write a short paragraph (less than 44 words) that uses different pronunciations and complex words while being warm and welcoming to a person named Shane'
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2500,
                n=1,
                stop=None,
                temperature=0.5,
            )
            speak1 = 'Do you want to set this voice as active?'

            # Print the generated text
            message = completions.choices[0].text
            print(message)
            MondeVert.Add2Transcript(self, text2Add=message)
            set1 = False

            for voice in voices:
                indexCount += 1

            while set1 == False:
                if index <= indexCount:
                    print(f'index-> {index} -- {voices[index].name}')
                    engine.setProperty('voice', voices[index].id)
                    engine.say(message)
                    # MondeVert.speak(self, speak1)
                    Query = MondeVert.getUserResponse(self)

                    if "yes" in Query or "set" in Query or ("make" in Query and "active" in Query) or (
                            "set" in Query and "active" in Query):
                        self.voice = index
                        voice_set = self.voice
                        xVoice = index
                        # MondeVert.speak(self, 'Voice Set')
                        set1 = True

                    index += 1
                    engine.runAndWait()
                else:
                    MondeVert.Setvoices(self, Quick=True)

        else:
            self.voice = int(input('What Voice do you want to make active?'))
            # MondeVert.speak(self, 'Voice Set')

        ####################################################################################################################################################################################
        ## Below are more utlities that help me to do repetitive tasks quicker
        ####################################################################################################################################################################################

    def createDF(self):
        test = [('', '', '', '', '', '', '', '', '', '', '', '', '', '', '')]
        self.transcript = pd.DataFrame(test, columns=['Entry #', 'Date', 'Subject', 'Type/Marker', 'Priority',
                                                      'Original_Text', 'Edited_Text', 'AI_Corrected_Text',
                                                      'AI_Correction_Comment', 'Note', 'AI_Content',
                                                      'AI_Correction_Content', 'File_Name', 'Added to text File',
                                                      'Completed/Added to blog'])

    def adddata2DF(self):

        row = (self.entry - 1)
        self.transcript.loc[row] = [str(self.entry), self.current_time, self.subject, self.Type, self.Significance,
                                    self.query1,
                                    self.new_Query, self.AI_Corrected_Text, self.Correction_Comment, self.Notes,
                                    self.Words, self.AI_Corrected_Content, self.FileName, self.Added2TextFile,
                                    self.Completed]

    def ActivateSilentMode(self):
        self.SilentMode = True

    def ActivateLoudMode(self):
        self.SilentMode = False

    def saveTranscript(self):
        cu.saveTranscript(self.transcript_Final, self.current_time)

    def Add2Transcript(self, text2Add):
        self.transcript_Final += text2Add + ' \n'

        # MondeVert.speak(self,'Error Saving')
        # print ('Error Saving')

    # 2 options for better transcribe tool 1). Make my own where it transcribes the whole thing (this is probably best), I can have a multithread to print or output either way the live text so I can see what I am saying and it will make a rough correction on the fly.
    # Have the ability to kick off certain processes like sending emails, scheduling meetings. Post instagram (auto or manual (basic or advance), Have the ability to run the entire tool by voice activation, further you can decide if its fully on the fly by talking to AI or if you want to direct it to certain inputs and pick a file for another. Outline mode, explain mode etc.)
    # if we can run everything, keep recording and outputting the Text to speech I think we are in a sweet spot for the actual AI. There should be a noice supression piece eventually to remove ambient noise.
    # you should be able to train model so it recognize your voice over other sounds (this tech exists 100% see siri alexa teams somehow etc.)
    # Ask walt about how to get better sounding voice models for text to speech?? Look up model how to train your voice to be used

    def cleanText(self, text, SHAINE_Clean=False):
        # result = ''
        parser = GingerIt()
        try:
            if int(len(text)) <= 4999:
                # print(len(text))
                result = pd.DataFrame(parser.parse(text))

                # result.drop_duplicates()
            else:
                result = pd.DataFrame('', '', '')
                self.Notes = 'Text is Large so may need to review the parts that may have been cut by mistake'
                for i in range(0, (len(text) // 5000) + 1):
                    texttemp = text[0 + (5000 * i):4999 + (5000 * i)]
                    if len(texttemp) > 0:
                        result11 = pd.DataFrame(parser.parse(text))
                        result1 = [result1 + texttemp]
                result = pd.DataFrame(result1, columns='result')

            if len(result.loc[0, 'result']) > 0:
                # print(result.loc[:,'result'].values)
                rr = str(result.loc[0, 'result'])
                self.Correction_Comment += 'Corrections Made.'
            else:
                rr = text
                self.Correction_Comment += 'No Corrections Needed.'



        except:
            print('Text was not properly cleaned by GingerIT: ' + text)
            # print(text)
            rr = text
            self.Correction_Comment += 'No Corrections Needed (Caused an error and did not return anything).'

        # print('Sending Text to SHAINE to clean it up ' + text)
        # if(SHAINE_Clean ==True):
        #     try:
        #         if int(len(text)) <= 4999:
        #             # print(len(text))
        #             result = pd.DataFrame(parser.parse(text))
        #             # result.drop_duplicates()
        #         else:
        #             result = pd.DataFrame('', '', '')
        #             self.Notes = 'Text is Large so may need to review the parts that may have been cut by mistake'
        #             for i in range(0, (len(text) // 5000) + 1):
        #                 texttemp = text[0 + (5000 * i):4999 + (5000 * i)]
        #                 if len(texttemp) > 0:
        #                     print("Current SubSet of Text being cleaned by SHAINE: " + texttemp)
        #                     #This is where I use
        #                     #result11 = pd.DataFrame(parser.parse(text))
        #                     result1 = [result1 + texttemp]
        #             result = pd.DataFrame(result1, columns='result')
        #     except:
        #
        #         return rr

        return rr

    def makeQuickPoem(self):
        x = s.PoemBot(1, 1, 1, 1, 40, 3)
        x.ReloadModel("model.h5")
        x.setupdata()
        self.Words = x.shakesbot_DA_Make_Script(size=300)
        # self.Words[0:100]
        print(self.Words)
        self.Words = MondeVert.cleanText(self, self.Words)
        MondeVert.speakSweet(self, self.Words)

    def StartThread(self):
        trd1 = threading.Thread(target=MondeVert.Make_Script2(self))
        self.w[i] = trd1.start()
        x = MondeVert.Make_Script2(self)
        print(x)

        self.threads.append(trd1)

    def Make_Script(self):
        size = 1
        self.threads = []
        self.w = numpy.empty(size, dtype=str)
        for self.i in range(0, size):
            MondeVert.StartThread(self)
            print(self.w[i])
            # globals()[f"trd{i}"] = threading.Thread(target=MondeVert.Make_Script2(self))
            # w[i] = globals()[f"trd{i}"].start()

        for x in self.threads:
            x.join()

        for ii in range(0, size):
            self.Words += str(self.w[ii])

        self.AI_Corrected_Content = MondeVert.cleanText(self, self.Words)

    def Make_Script2(self):
        pb = s.PoemBot(1, 1, 1, 1, 40, 3)
        pb.ReloadModel('model.h5')
        pb.setupdata()
        w1 = pb.shakesbot_DA_Make_Script()
        MondeVert.speakSweet(self, w1)
        # print (w1)
        return w1

    def generateGreek(self):
        w2 = self.pb.generateGreek() + ' \n' + ' \n'
        return w2

    def ChatGPTDA(self, temp=0.5, MakeArt=False, Prompt='', UseArtPrompt=False, ConfirmBot=True):
        MondeVert.Add2Transcript(self, ' \n')
        Prior_Mode = self.Mode
        self.Mode = 'Chat GPT Mode'
        self.message = ''
        MondeVert.Add2Transcript(self, text2Add=(Prior_Mode + ' - ' + self.Mode + ':'))
        MondeVert.Add2Transcript(self, ' \n')
        prompt = ''
        self.promptB = False
        # Import the OpenAI library
        # Set up the OpenAI API client :
        openai.api_key = API_Key
        # Record the audio
        # MondeVert.speak(self, " Chat GPT is running!", voice=4)

        if UseArtPrompt == True:
            MakeArtPrompt = "Provide me with a prompt to share with artificial inteligence that will create a unique and visually pleasing work of art. "
        else:
            MakeArtPrompt = ''

        if Prompt == '':
            sStop1 = False
        else:
            sStop1 = True

        sStop = False
        # check if the reply contains 'yes'
        while sStop == False:
            # Record the audio

            MondeVert.Add2Transcript(self, MakeArtPrompt)

            # engine.runAndWait()
            if sStop1 == True:
                prompt = MakeArtPrompt + Prompt
                print(prompt)
            else:
                prompt = MakeArtPrompt + MondeVert.getUserResponse(self, pause=1.44)
                if ('STOP' in prompt.upper() and (
                        'LISTEN' in prompt.upper())) or 'QUIT' == prompt.upper() or ' QUIT ' == prompt.upper() or (
                        'END' in prompt.upper() and ('CONVERSA' in prompt.upper())):
                    sStop = True
                    # print ('Its supposed to quit here')
                    continue

            # Generate text
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2444,
                n=1,
                stop=None,
                temperature=temp,
            )
            self.message = completions.choices[0].text
            print(self.message)

            if MakeArt == False and (
                    'MAKE' in prompt.upper() or 'ART' in prompt.upper()) and 'PROMPT' in prompt.upper() and sStop1 == False:
                MondeVert.ConfirmBOT(self, self.message)
                if self.promptB == True:
                    MondeVert.makeArt(self, self.message)
                    continue
                else:
                    continue

            if MakeArt == True or sStop1 == True:
                if ConfirmBot == True:
                    MondeVert.ConfirmBOT(self, self.message)
                else:
                    MondeVert.speakSweet(self, self.message)
                    self.promptB = True

                if self.promptB == True:
                    sStop = True
                    continue
                else:

                    continue
            else:
                MondeVert.speakSweet(self, self.message)

        return self.message

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Above is code I did not write, below is code that allows user to update values of respective values
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    def getfilename(self):
        self.FileName = MondeVert.getdata(self, 'FileName')

    def getsubject(self):
        self.subject = MondeVert.getdata(self, 'subject')

    def getDictation_Type(self):
        self.Dictation_Type = MondeVert.getdata(self, 'Type')

    def getSignificance(self):
        self.Significance = MondeVert.getdata(self, 'Significance')

    def getNote(self):
        self.Notes += '|' + MondeVert.getdata(self, 'Notes')

    def getdata(self, Field):

        # MondeVert.speak(self, 'what is the ' + Field)
        print('Please confirm the ' + Field)
        s = True
        Query = ''
        while (s == True):
            Query = MondeVert.getUserResponse(self)
            Query2 = ''
            WaitforResponse = False
            while (WaitforResponse == False):
                # MondeVert.speak(self, Query + ' Is that correct?')
                Query2 = MondeVert.getUserResponse(self)
                if "yes" in Query2 or "correct" in Query2 or "ya" in Query2 or "yeah" in Query2:
                    # MondeVert.speak(self, 'Thanks for confirming the ' + Field)
                    s = False
                    WaitforResponse = True
                    continue
                if "no" in Query2 or "wrong" in Query2 or "not it" in Query2 or "nope" in Query2:
                    # MondeVert.speak(self, 'ok  please say the ' + Field + ' you want to set')
                    print('ok  please say the ' + Field + ' you want to set')
                    WaitforResponse = True
                    continue
                else:
                    # MondeVert.speak(self, 'Lets try that again what is the ' + Field)
                    Event().wait(1)
                    continue
        return Query

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################ below is code that allow me to confirm with the user the inputs are correct
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    def takeCommand(self):
        Query = MondeVert.getUserResponse(self, Response="Action Requested")
        return Query

    def ConfirmBOT(self, message):
        # MondeVert.speak(self, 'Chat GPT responded with: ' + message + ' do you want to use this prompt?', voice=4)
        query = MondeVert.getUserResponse(self)

        if 'yes' in query or 'correct' in query or 'yeah' in query or 'submit' in query:
            self.promptB = True

        if 'edit' in query or 'change' in query and ('prompt' in query or 'words' in query):
            MondeVert.editBotPrompt(self, message)

    def transcribe_Build_Query(self, pause=3.13):
        Query = MondeVert.getUserResponse(self)
        return Query

    def transcribe_Build_Query_Pause(self):
        Speak1 = 'What Tool do you want to use?'
        Print1 = 'Options: ChatGPT (ChatBot), Transcribe Mode , Make To Do List, Change Subject, Edit, Poem, Stop Recording --> Build others here'
        # MondeVert.speak(self, Speak1)
        print(Print1)
        Query = MondeVert.getUserResponse(self, Response="Tool Selected")
        return Query

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ##########################                below is ChatGPT                  ##############################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

    def makeArt(self, Prompt='', SavePath=up.AI_Art_Path, OpenFile=False):
        try:
            MondeVert.Add2Transcript(self, ' \n')
            Prior_Mode = self.Mode
            self.Mode = 'AI Art Mode'
            MondeVert.Add2Transcript(self, text2Add=(Prior_Mode + ' - ' + self.Mode + ':'))
            MondeVert.Add2Transcript(self, ' \n')
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

                    # MondeVert.speak(self, AIspeak)

                    print(AIspeak)
                    prompt = MondeVert.getUserResponse(self, Response="Art Prompted", pause=1)

                    if 'cancel' in prompt or 'stop' in prompt or 'quit' in prompt or 'done' in prompt or 'exit' in prompt:
                        MondeVert.saveTranscript(self)
                        self.promptB == True
                        continue

                    MondeVert.ConfirmUR(self, prompt)
                    print()
            else:
                prompt = Prompt
                print(prompt)
                MondeVert.Add2Transcript(self, '(Prompt Fed Directly into Function)')

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

                # Commented out for testing
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
                # fname = os.path.join(SavePath, '\'',FileName)

                fname = SavePath + up.System_Folder_Path_Fix + FileName + '.png'
                print(f"Filename: {fname}")
                with open(fname, 'wb') as f:

                    f.write(r.content)

                try:
                    if OpenFile == True:
                        if platform.system() == 'Darwin':  # macOS
                            subprocess.call(('open', fname))
                        elif platform.system() == 'Windows':  # Windows
                            os.startfile(fname)
                        else:  # linux variants
                            subprocess.call(('xdg-open', fname))
                except:
                    dn = 100
                # this line saves the
                # IP.png2JPG(fname, up.PNGPath,fname_only, up.PNGPath_Archive, Del = False )
            except:
                fname = 'File not saved error occurred'

        except:
            fname = 'File not saved error occurred'

        try:

            Text1 = 'Original Prompt: ' + prompt + 'Path to Photo: ' + fname
            MondeVert.Add2Transcript(self, Text1)
            fnameText = fname_only
            cu.SaveCSV(Text=Text1, Title=fnameText, SavePath=SavePath)
        except:
            dn = 100

        # data = ([Text1])
        # df1 = pd.DataFrame(data = data)

        # cu.add2Master2(self, Text1)
        return fname

    # Define a function that sends a message to ChatGPT
    def chat_query(self, prompt):
        model_engine = "text-davinci-003"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=2048,
            n=1,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return message

    # Define a function that handles the conversation
    def conversation_handler(self, prompt):
        # Send the prompt to ChatGPT
        load_dotenv()
        # Set up the OpenAI API client :
        openai.api_key = API_Key
        response = MondeVert.chat_query(prompt)
        print(f"MondeVert: {response}")

        # End the conversation if ChatGPT says goodbye
        if "goodbye" in response.lower():
            return

        # Otherwise, get user input and continue the conversation
        prompt = input("User: ")
        MondeVert.conversation_handler(prompt)

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Long Code where I give Digital Assistant commands##    (user menus)
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

    def RunChatGPT(self):
        # this will look very diff in the future The digital assistant will pass in certain key words to run different functions, but really this should exist without digital assist this is auxilary to anything I run it will be way easier to maintain
        dn = 1

    # Provide me with a copy of the short bio you come up with and then using that I want you to role play you are the respective artist and write a short 1 page story about something that would happen in the life of the respective artist you described. It can be about any topic but it should feel authentic to the life of the person you described."}
    def Make_a_Song(self, Mode='Random Song', SavePath=up.SavePath):
        ArtPaths = []
        openai.api_key = API_Key
        SavePath = SavePath + up.System_Folder_Path_Fix + Mode
        crazy = round((randbelow(520000) + 170000) / 100000, 0)
        crazy = crazy / 10
        print(crazy)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_Text},
                {"role": "user", "content": up.ArtistBio_SongArtist}
            ], temperature=crazy
        )

        Artist_Bio = response.choices[0].message.content

        Song1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_Text},
                {"role": "user", "content": up.RolePlay_SongArtist + Artist_Bio},
                {"role": "user", "content": up.Song_Prompt_SongArtists},
                {"role": "user", "content": up.Title_SongArtists},
                {"role": "user", "content": up.Samples_SongArtists},
                {"role": "user", "content": up.Tune_SongArtists}

            ]
            , temperature=crazy
        )
        Song = Song1.choices[0].message.content

        Art_Prompt1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_Text},
                {"role": "user", "content": up.RolePlay_SongArtist + Artist_Bio},
                {"role": "user", "content": up.ArtPrompt_SongArtist}
            ], temperature=crazy
        )

        Art_Prompt = Art_Prompt1.choices[0].message.content

        print(Artist_Bio)
        # MondeVert.speak(self, Artist_Bio)
        print(Song)
        # MondeVert.speak(self, Song)
        print(Art_Prompt)
        # MondeVert.speak(self, Art_Prompt)

        # Art2 = MondeVert.ChatGPTDA(self, temp=crazy, MakeArt=True, Prompt=(Art_Prompt),ConfirmBot=False)
        try:
            ArtPath2 = MondeVert.makeArt(self, Art_Prompt)
            ArtPaths.append(ArtPath2)

        except:
            ArtPath2 = ''

        Title = MondeVert.ChatGPTDA(self, temp=crazy, MakeArt=True, Prompt=(up.Song_Title_Prompt + Song),
                                    ConfirmBot=False)
        prompt = "Artist info:" + Artist_Bio + "Work of Art Inspiration:" + Art_Prompt + "Song:" + Song
        Prompts_Used = [
            up.system_Text + up.RolePlay_SongArtist + "AI Created a Persona shown as the Artist Bio Above" + up.Song_prompt + up.ArtPrompt_SongArtist]
        ArtistPoetInfo = 'Lyrics Written By: ' + up.Song_Writer + '      (' + 'Artwork by: ' + up.AI_ArtistName + ')'
        cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title,
                            SavePath=SavePath, Mode='Song Lyrics' + Mode)

    def add2log(self, Log_Add):
        Log_Add = lup.NewLine
        self.Request_log.append(Log_Add)

        Log_Add2 = up.breakupOutput
        self.Request_log.append(Log_Add2)
        Log_Add3 = lup.NewLine
        self.Request_log.append(Log_Add3)

    def Make_a_poem(self, Chunk_Limit=700, USERTITLE='', Poet_Bio_Details='', Make_Persona=True, Artist_Persona='',
                    Poet_Persona='', Line1_System=up.system_TextJoaT, Line2_Role=lup.Poem_Role,
                    Line3_Format=lup.Poem_Format, Line4_Task=lup.Poem_Task,
                    Line3_Format_outline=lup.Poem_Outline_Format, Line4_Task_outline=lup.Poem_Outline_Task,
                    SavePath=up.AI_Poetry_Path, Mode='Poem', crazy=.5, Persona_Role=lup.Poet_Persona_Role,
                    Persona_Task=lup.Poet_Persona_Task, Persona_Format=lup.Poet_Persona_Format,
                    Persona_Special=lup.Poet_Persona_Special, Revise_Task=lup.Poem_Revise_Task,
                    Revise_Format=lup.Poem_Revise_Format, Translate=SAF.Translation_Languages_Testing):
        # test
        dn = 100
        crazy = round((randbelow(520000) + 170000) / 100000, 0)
        crazy = crazy / 10
        print(crazy)

        aPrompt = sms.ArtPrompt_Clean_Social_Media_Post_Line2_Prompt
        if 'Picture_Book' in Mode:
            aPrompt = lup.PicturebookArt

        crazy += .2
        if crazy < .4:
            crazy = .6
        if crazy > .9:
            crazy = .7

        ArtPaths = []
        openai.api_key = API_Key
        # SavePath = up.AI_Music_Path
        cu.Check_Folder_Exists(SavePath)

        Outline = '*Did not create'
        Poem = '*Did not create'
        Bitter_critic = '*Did not create'
        Revised_Poem = '*Did not create'

        if Mode not in SavePath:
            SavePath = SavePath + up.System_Folder_Path_Fix + Mode
        cu.Check_Folder_Exists(SavePath)

        if Poet_Bio_Details == '' or Make_Persona == True:
            try:
                Poet_Bio_Details = MondeVert.Writer_Persona_Short_Story(self, Role=Persona_Role,
                                                                        Task=Persona_Task,
                                                                        Format=Persona_Format,
                                                                        Special=Persona_Special,
                                                                        Subject=Poet_Bio_Details, crazy=.5)
            except:
                if Poet_Bio_Details != '':
                    Poet_Bio_Details = Poet_Bio_Details
                else:
                    Poet_Bio_Details = ''

        # make outline

        if Mode != 'StudyGuide':
            Outline = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role + str(Poet_Bio_Details),
                                                Line3_Format=Line3_Format_outline, Line4_Task=Line4_Task_outline)
        else:
            Outline = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role, Line3_Format=Line3_Format_outline,
                                                Line4_Task=Line4_Task_outline)

        if Outline == '':
            MondeVert.add2log(self, Log_Add='Outline: Error when trying to make Outline')

            if Poet_Bio_Details == '':
                Outline = MondeVert.Basic_GPT_Query(self,
                                                    Line4_Task='Come up with an outline to help a user complete the following task: ' + Line4_Task)
            else:
                Outline = Poet_Bio_Details
        else:
            MondeVert.add2log(self, Log_Add='Outline: ' + Outline)

        # make poem

        if Mode != 'StudyGuide':
            Poem = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role + str(Poet_Bio_Details),
                                             Line3_Format=Line3_Format, Line4_Task=Line4_Task + Outline)
        else:
            Poem = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role, Line3_Format=Line3_Format,
                                             Line4_Task=Line4_Task + Outline)
        # Edit poem
        if Poem != '*Did not create':

            MondeVert.add2log(self, Log_Add='Original_Text: ' + Poem)
            Revised_Poem = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role + Poet_Bio_Details,
                                                     Line3_Format=Revise_Format, Line4_Task=Revise_Task + Poem)

        else:
            MondeVert.add2log(self, Log_Add='Original_Text: Error when trying to make Poem')

            Revised_Poem = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role + Poet_Bio_Details,
                                                     Line3_Format=Line3_Format,
                                                     Line4_Task=Line4_Task + Outline)

        if Revised_Poem == '*Did not create':
            Revised_Poem = 'No Revision done, this work was too perfect'
            MondeVert.add2log(self, Log_Add='Revised_Text: Error when trying to make Revised_Poem')

        else:
            MondeVert.add2log(self, Log_Add='Revised_Text: ' + Revised_Poem)

        try:
            if len(Revised_Poem) > 150:
                Lyrics = Revised_Poem
            elif Mode == 'StudyGuide':
                Lyrics = Outline
            else:
                Lyrics = Poem

            Lyrics1 = Lyrics
        except:
            Lyrics = Poem

        try:
            Title = MondeVert.Quick_Title(self,
                                          Text='Make an abstract and concise title that draws in the reader for the following text: ' + Lyrics)

            Title = Title.replace("The Title:", "")
            Title = Title.replace("Title:", "")
            Title = Title.replace("The Title", "")
            Title = Title.replace("Title", "")

        except:
            Title = Mode + '_' + self.current_time
        dn = 100

        # Create new subfolder etc for this filepath
        if len(Title) > 90:
            Title = Title[:44]

        Title1 = cu.CleanFileName(Title)
        USERTITLE = cu.CleanFileName(USERTITLE)

        Title1 = str(Title1)
        # if len(Title1) > 44:
        #     Title1 = Title1[0:44]

        if USERTITLE == '':
            folder = Title1
        else:
            folder = USERTITLE
            if len(SavePath + up.System_Folder_Path_Fix + folder) > 200:
                if len(folder) > 40:
                    folder = folder[0:40]
        MondeVert.add2log(self, Log_Add='Title: ' + Title)

        # Title1 = Title1 + self.current_time
        SavePath = SavePath + up.System_Folder_Path_Fix + folder
        FullFilePath = SavePath + up.System_Folder_Path_Fix + Title1
        SavePath_Details = SavePath + up.System_Folder_Path_Fix + 'SHAINE - Details'
        SavePath_Pics = SavePath + r'\SHAINE - Art'

        cu.Check_Folder_Exists(SavePath)
        cu.Check_Folder_Exists(SavePath_Details)
        cu.Check_Folder_Exists(SavePath_Pics)
        MondeVert.add2log(self, Log_Add='SavePath Created: ' + SavePath)
        MondeVert.add2log(self, Log_Add='SavePath Created: ' + SavePath_Details)
        MondeVert.add2log(self, Log_Add='SavePath Created: ' + SavePath_Pics)

        originalFilepath = self.PersonaArtPath
        PicNewPath = SavePath_Pics + up.System_Folder_Path_Fix + Title1 + '_Persona Pic.png'

        try:
            shutil.copyfile(originalFilepath, PicNewPath)
            MondeVert.add2log(self, Log_Add='New Art Created: ' + PicNewPath)
        except:
            MondeVert.add2log(self, Log_Add='Art not moved properly check the following path: ' + originalFilepath)
            dn = 100
        # Run Bitter Critic
        Bitter_Critic = MondeVert.Basic_GPT_Query(self, Line2_Role=up.Test_Role_Critic,
                                                  Line3_Format=up.Test_Format_Critic,
                                                  Line4_Task=up.Test_Task_Critic + Lyrics,
                                                  Special=up.Test_Special_Critic)

        if Bitter_Critic == '':
            Bitter_Critic = 'No Critique done, this work was too amateur'
            MondeVert.add2log(self, Log_Add='Bitter Critic: No Critique done, this work was too amateur')
        else:
            MondeVert.add2log(self, Log_Add='Bitter Critic: ' + Bitter_Critic)
        # make artist person

        try:
            Art_Details = ''
            if len(Outline) > 1313:
                Outline1 = Outline[:1313]
            else:
                Outline1 = Outline

            try:
                Art_persona = MondeVert.Artist_Persona_Short_Story(self, Writer_persona=Outline1)
                try:
                    # Art_Details = MondeVert.summarize_art_style_for_short_story(writer_persona=Poet_Bio_Details,
                    #                                                         outline=Lyrics,Artist_Persona=Art_persona, Format=lup.artDetailsFormat)  # , Format='Make a concise summary of an art style and artist to make a work of art like. Also provide the colors used, themes, moods, and tones.')

                    Art_Details = MondeVert.GPTArt2(self, User_Subject=Art_persona, ArtFormat=lup.artDetailsFormat,
                                                    prompt=lup.artDetailsPrompt)

                    originalFilepath = self.PersonaArtPath2
                    PicNewPath = SavePath_Pics + '_' + Title1 + '_Artist Pic.png'
                    try:
                        shutil.copyfile(originalFilepath, PicNewPath)
                    except:
                        dn = 100

                except:
                    Dn = 100



            except:
                dn = 100
        except:
            dn = 100

        print(Art_Details)

        if Art_Details == '':
            try:

                Art_Details = MondeVert.GPTArt2(self, User_Subject=Outline1, ArtFormat=lup.artDetailsFormat,
                                                prompt=lup.artDetailsPrompt)
            except:
                try:
                    Art_Details = MondeVert.GPTArt2(self, User_Subject=Poet_Bio_Details, ArtFormat=lup.artDetailsFormat,
                                                    prompt=lup.artDetailsPrompt)
                except:
                    if Art_Details == '':
                        Art_Details = 'Where the wild things are, fun and colorful'
                    dn = 100

        print(Art_Details)
        # summarize art style
        # Save Files including word document
        # Make art specific for the poem
        # make audio for Italian, Spanish, French, English

        print(up.breakupOutput2)

        # MondeVert.speak(self, "DJ MondeVert Work complete yo")
        try:
            data_final = """Poet_Bio: """ + Poet_Bio_Details + (up.breakupOutput2) + """Poem Details: """ + Outline + (
                up.breakupOutput2) + """Title: """ + Title + (
                             up.breakupOutput2) + """Poem: """ + Poem + (
                             up.breakupOutput2) + """Poem 2.0: """ + Revised_Poem + (
                             up.breakupOutput2) + """Bitter Critic: """ + Bitter_Critic

        except:
            data_final = """Poem: """ + Poem + """Poem 2.0: """ + Revised_Poem
        print(data_final)

        try:
            data_final = data_final + Poet_Bio_Details + Artist_Persona + Art_persona + Art_Details
        except:
            dn = 100
        # MondeVert.speak(self, "Saving the files round 1")
        # print(data)

        # data = [(self.current_time + '_' + data_final)]

        Text = str("Create Date: " + self.current_time + '_Results: ' + data_final)

        # print(data)
        try:
            # df1 = pd.DataFrame(data)
            # print(df1)
            # print(Title2)

            ReplaceStrings = [",0", " 0,", "Title:"]
            for r in ReplaceStrings:
                Lyrics = Lyrics.replace(r, "")

            filename = cu.SaveCSV(Title=Title1 + '_PreProduction', SavePath=SavePath_Details, Text=Text)
            MondeVert.add2log(self, Log_Add='Txt File Created: ' + filename)
            try:
                filename2 = cu.SaveCSV(Title=Title1, SavePath=SavePath, Text=Lyrics, AddTimeStamp=False)
                MondeVert.add2log(self, Log_Add='Txt File Created: ' + filename)
            except:
                dn = 100
        except:
            print('Review Error File did not save ')

        # try:
        if 1 == 1:
            newline = """\n"""
            newline2 = """\\n"""
            audioname = cu.SaveText2Audio(Text=Lyrics, Translate=Translate, SavePath=SavePath,
                                          FileName=Title1, Chunk_Replaces=['.', ')', ':', '?', newline, newline2],
                                          Chunk_Limit=Chunk_Limit,
                                          Artist_Persona=Art_Details, aPrompt=aPrompt)

        # except:
        #     test = 100
        #     print('Audio File not created')

        try:

            cu.send_email_no_attachment_gmail(body=Lyrics)
            cu.send_email_no_attachment_outlook(body=Lyrics)

            cu.send_email_w_attachment_outlook(body=Lyrics, filename=[PicNewPath])
            cu.send_email_w_attachment_gmail(body=Lyrics, filename=[PicNewPath], fType='png')


        except:
            print('email not send, its possible file was not created')

        if Art_Details == '':
            Art_Details = 'Be Creative and make a beautiful work of art related to the respective text'
        Art_Prompt = MondeVert.GPTArt2(self, prompt="Make a work of art describing the following subject:",
                                       User_Subject=Line2_Role + Poet_Bio_Details, ArtFormat=Art_Details)
        print("Work of Art Inspiration:" + Art_Prompt)

        try:
            ArtPath2 = MondeVert.makeArt(self, Art_Prompt)
            ArtPaths.append(ArtPath2)
            originalFilepath = ArtPath2
            PicNewPath = SavePath_Pics + up.System_Folder_Path_Fix + Title1 + '_Project Pic.png'
            try:
                shutil.copyfile(originalFilepath, PicNewPath)
            except:
                dn = 100

        except:
            ArtPath2 = ''

        # MondeVert.speak(self, "Saving the files round 2")
        prompt = data_final + "Work of Art Inspiration:" + str(
            Art_Prompt) + 'Artist Info: ' + Art_Details + up.breakupOutput2 + Artist_Persona
        Prompts_Used = [str(self.UserPromptsCount) + ' User Inputs: ' + self.UserPrompts]
        ArtistPoetInfo = 'Lyrics Written By: Shane Donovan   (' + 'Artwork by: ' + up.AI_ArtistName + ')'
        cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title1 + '_Final',
                            SavePath=SavePath_Details, Mode=Mode)

    def Make_a_SongRR(self, Artist_Bio_Details=up.Artist_Bio_DetailsSD, Song_Subject=up.Song_Subject_SD,
                      SavePath=up.AI_Music_Path, System=up.system_Text, Role=up.RolePlay_SongArtist,
                      Background=up.ArtistBio_SongArtist, Task=up.Song_Prompt_SongArtists,
                      Special=up.Samples_SongArtists, Format='', Mode='Random Song', USERTITLE=''):
        ArtPaths = []
        openai.api_key = API_Key
        # SavePath = up.AI_Music_Path
        cu.Check_Folder_Exists(SavePath)
        SavePath = SavePath + up.System_Folder_Path_Fix + Mode
        cu.Check_Folder_Exists(SavePath)

        crazy = round((randbelow(520000) + 170000) / 100000, 0)
        crazy = crazy / 10
        print(crazy)

        crazy += .2
        if crazy < .4:
            crazy = .6
        if crazy > .9:
            crazy = .7

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextRR},
                {"role": "user", "content": up.ArtistBio_SongArtistRR + Artist_Bio_Details}
            ], temperature=crazy
        )

        Artist_Bio = response.choices[0].message.content

        # print('Artist_Bio: ' + Artist_Bio)
        print(up.breakupOutput2)

        Song1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextRR},
                {"role": "user", "content": up.RolePlay_SongArtistRR + Artist_Bio},
                {"role": "user", "content": up.Song_Prompt_SongArtistsRR + Song_Subject},
                {"role": "user", "content": up.Song_Format_Prompt + up.SongFormat},
                # {"role": "user", "content": up.Title_SongArtistsRR},
                # {"role": "user", "content": up.Samples_SongArtistsRR},
                # {"role": "user", "content": up.Tune_SongArtistsRR}

            ]
            , temperature=crazy
        )
        Song = Song1.choices[0].message.content

        # Create original details
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextRR},
                {"role": "user", "content": up.RolePlay_SongArtistRR + Artist_Bio},
                {"role": "user", "content": up.Title_SongArtistsRR + Song}

            ], temperature=crazy
        )

        Title = response.choices[0].message.content

        Title = Title.replace("The Title:", "")
        Title = Title.replace("Title:", "")
        Title = Title.replace("The Title", "")
        Title = Title.replace("Title", "")
        # Create new subfolder etc for this filepath
        Title1 = cu.CleanFileName(Title)
        USERTITLE = cu.CleanFileName(USERTITLE)

        Title1 = str(Title1)
        # if len(Title1) > 44:
        #     Title1 = Title1[0:44]

        if USERTITLE == '':
            folder = Title1
        else:
            folder = USERTITLE

            if len(SavePath + up.System_Folder_Path_Fix + folder) > 200:
                if len(folder) > 40:
                    folder = folder[0:40]

        Title1 = Title1 + self.current_time
        SavePath = SavePath + up.System_Folder_Path_Fix + folder
        Title2 = SavePath + up.System_Folder_Path_Fix + Title1

        cu.Check_Folder_Exists(SavePath)

        # Create original details
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextRR},
                {"role": "user", "content": up.RolePlay_SongArtistRR + Artist_Bio},
                {"role": "user", "content": up.Samples_SongArtistsRR2 + Song}

            ], temperature=crazy
        )

        Samples2 = response.choices[0].message.content

        # Create original details
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextRR},
                {"role": "user", "content": up.RolePlay_SongArtistRR + Artist_Bio},
                {"role": "user", "content": up.ReWrite_Song + Song}

            ], temperature=crazy
        )

        ReWrite = response.choices[0].message.content

        # Create original details
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextDJ},
                {"role": "user", "content": up.RolePlay_SongArtistRR + Artist_Bio},
                {"role": "user", "content": Samples2},
                {"role": "user", "content": up.ExplainTheBeat + ReWrite}

            ], temperature=crazy
        )

        DJMondeVert = response.choices[0].message.content

        print(up.breakupOutput2)

        # MondeVert.speak(self, "DJ MondeVert Work complete yo")
        data_final = """Artist_Bio: """ + Artist_Bio + ": " + (
            up.breakupOutput2) + """ Potential Samples: """ + Samples2 + (up.breakupOutput2) + """Title: """ + Title + (
                         up.breakupOutput2) + """Song: """ + Song + (up.breakupOutput2) + """Song 2.0: """ + ReWrite + (
                         up.breakupOutput2) + """DJMondeVert: """ + DJMondeVert

        print(data_final)

        # MondeVert.speak(self, "Saving the files round 1")
        # print(data)

        # data = [(self.current_time + '_' + data_final)]
        Text = str("Create Date: " + self.current_time + '_Results: ' + data_final)
        # print(data)
        try:
            # df1 = pd.DataFrame(data)
            # print(df1)
            # print(Title2)

            filename = cu.SaveCSV(Title=Title1, SavePath=SavePath, Text=Text)

            # MondeVert.SaveText(self,df1,'MondeVert Assistant', 'Full Transcript')

        except:
            print('Review Error File did not save ')

        try:

            cu.send_email_no_attachment_gmail(body=Song)
            cu.send_email_no_attachment_outlook(body=Song)

            cu.send_email_w_attachment_outlook(body=Song, filename=[filename])
            cu.send_email_w_attachment_gmail(body=Song, filename=[filename], fType='txt')

        except:
            print('email not send, its possible file was not created')
            cu.send_email_no_attachment_outlook(body=Song)

        # MondeVert.speak(self, "Making the art, painting yo picture")
        Art_Prompt1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextRR},
                {"role": "user", "content": up.RolePlay_SongArtistRR + Artist_Bio},
                {"role": "user", "content": up.ArtPrompt_SongArtistRR}
            ], temperature=crazy
        )

        Art_Prompt = Art_Prompt1.choices[0].message.content
        print("Work of Art Inspiration:" + Art_Prompt)

        # print(Artist_Bio)
        # MondeVert.speak(self,Artist_Bio)
        # print(Song)
        # MondeVert.speak(self, Song)
        # print(Art_Prompt)
        # MondeVert.speak(self, Art_Prompt)

        # Art2 = MondeVert.ChatGPTDA(self, temp=crazy, MakeArt=True, Prompt=(Art_Prompt),ConfirmBot=False)
        try:
            ArtPath2 = MondeVert.makeArt(self, Art_Prompt)
            ArtPaths.append(ArtPath2)

        except:
            ArtPath2 = ''

        # MondeVert.speak(self, "Saving the files round 2")
        prompt = data_final + "Work of Art Inspiration:" + str(Art_Prompt)
        Prompts_Used = [str(self.UserPromptsCount) + ' User Inputs: ' + self.UserPrompts]
        ArtistPoetInfo = 'Lyrics Written By: ' + up.Song_Writer + '      (' + 'Artwork by: ' + up.AI_ArtistName + ')'
        cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title,
                            SavePath=SavePath, Mode='Song Lyrics' + Mode)

    def Make_a_Song_2(self, Make_Persona=False, Artist_Bio_Details='', Song_Subject=up.Song_Subject,
                      SavePath=up.AI_Music_Path, System=up.system_TextRR, Role=lup.Song_Role,
                      Outline_Task=up.ArtistBio_SongArtistRR, Task=up.Song_Prompt_SongArtists,
                      Special=up.Samples_SongArtists, Format=lup.Song_Format, Mode='Random Song', USERTITLE='',
                      Chunk_Limit=1333, Translate=SAF.Translation_Languages_Testing4,
                      Line3_Format_outline=lup.Song_Outline_Format, Line4_Task_Outline=lup.Song_Outline_Task):

        # Note if the bio is not passed in it makes a random persona up

        ArtPaths = []
        openai.api_key = API_Key
        # SavePath = up.AI_Music_Path
        cu.Check_Folder_Exists(SavePath)

        Outline = '*Did not create'
        Song = '*Did not create'
        Bitter_critic = '*Did not create'
        ReWrite = '*Did not create'
        DJMondeVert = '*Did not create'

        if Mode not in str(SavePath):
            SavePath = Path(PureWindowsPath(SavePath , Mode))
        cu.Check_Folder_Exists(SavePath)

        if Artist_Bio_Details == '' or Make_Persona == True:
            try:
                Artist_Bio_Details = MondeVert.Writer_Persona_Short_Story(self, Role=lup.Music_Persona_Role,
                                                                          Task=lup.Music_Persona_Task,
                                                                          Format=lup.Music_Persona_Format,
                                                                          Special=lup.Music_Persona_Special,
                                                                          Subject=Artist_Bio_Details, crazy=.5)
            except:
                if Artist_Bio_Details != '':
                    Artist_Bio_Details = Artist_Bio_Details
                else:
                    Artist_Bio_Details = 'You are a bold new artist make a song that will be a hit and make you a star, be catchy and use expert music theory to make your masterpiece'

        Artist_Bio = Artist_Bio_Details

        crazy = round((randbelow(520000) + 170000) / 100000, 0)
        crazy = crazy / 10
        print(crazy)

        crazy += .2
        if crazy < .4:
            crazy = .6
        if crazy > .9:
            crazy = .7

        Outline = cu.Basic_GPT_Query(Line2_Role=Role + Artist_Bio_Details, Line3_Format=Line3_Format_outline,
                                     Line4_Task=Line4_Task_Outline, crazy=crazy)

        try:
            Song = cu.Basic_GPT_Query(Line2_Role=Role + Artist_Bio_Details, Line3_Format=Format,
                                      Line4_Task=Task + Outline)
        except:
            dn = 100

        try:
            # Create original details
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": System},
                    {"role": "user", "content": Role + Artist_Bio},
                    {"role": "user", "content": up.Samples_SongArtistsRR2 + Song}

                ], temperature=crazy
            )

            Samples2 = response.choices[0].message.content
        except:
            dn = 100

        try:
            # Create original details
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": System},
                    {"role": "user", "content": Role + Artist_Bio},
                    {"role": "user", "content": up.ReWrite_Song + Song}

                ], temperature=crazy
            )

            ReWrite = response.choices[0].message.content
            Song_trim = ReWrite[:1600]
        except:
            dn = 100

        # Create original details
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": up.system_TextDJ},
                    {"role": "user", "content": Role + Artist_Bio_Details},
                    {"role": "user", "content": Samples2},
                    {"role": "user", "content": up.ExplainTheBeat + Song_trim}

                ], temperature=crazy
            )

            DJMondeVert = response.choices[0].message.content
        except:
            dn = 100
        print(up.breakupOutput2)

        # Run Bitter Critic

        try:
            if len(ReWrite) > 300:
                Lyrics = ReWrite
            else:
                Lyrics = Song

            Lyrics1 = Lyrics
        except:
            Lyrics = Song

        try:
            Title = MondeVert.Quick_Title(self,
                                          Text='Make an abstract and concise title that draws in the audience for the following lyrics/song: ' + Lyrics)

            Title = Title.replace("The Title:", "")
            Title = Title.replace("Title:", "")
            Title = Title.replace("The Title", "")
            Title = Title.replace("Title", "")

        except:
            Title = Mode + '_' + self.current_time

            # Create new subfolder etc for this filepath
        Title1 = cu.CleanFileName(Title)
        USERTITLE = cu.CleanFileName(USERTITLE)

        Title1 = str(Title1)
        # if len(Title1) > 44:
        #     Title1 = Title1[0:44]

        if USERTITLE == '':
            folder = Title1
        else:
            folder = USERTITLE

            if len(SavePath + up.System_Folder_Path_Fix + folder) > 200:
                if len(folder) > 40:
                    folder = folder[0:40]

        SavePath = Path(PureWindowsPath(SavePath , folder))
        FullFilePath = Path(PureWindowsPath(SavePath , Title1))
        SavePath_Details = Path(PureWindowsPath(SavePath  , 'SHAINE - Details'))
        SavePath_Pics = Path(PureWindowsPath(SavePath , r'\SHAINE - Art'))

        cu.Check_Folder_Exists(SavePath)
        cu.Check_Folder_Exists(SavePath_Details)
        cu.Check_Folder_Exists(SavePath_Pics)

        originalFilepath = self.PersonaArtPath
        PicNewPath = Path(PureWindowsPath(SavePath_Pics , Title1 + '_Persona Pic.png'))
        try:
            shutil.copyfile(originalFilepath, PicNewPath)
        except:
            dn = 100

        Bitter_Critic = ''

        try:
            Bitter_Critic = MondeVert.Basic_GPT_Query(self, Line2_Role=up.Test_Role_Critic,
                                                      Line3_Format=up.Test_Format_Critic,
                                                      Line4_Task=up.Test_Task_Critic + Lyrics,
                                                      Special=up.Test_Special_Critic)
        except:
            dn = 100
        if Bitter_Critic == '':
            Bitter_Critic = 'No Critique done, this work was too amateur'

        # MondeVert.speak(self, "DJ MondeVert Work complete yo")
        try:
            data_final = """Artist_Bio: """ + Artist_Bio_Details + """Song Details: """ + Outline + ": " + (
                up.breakupOutput2) + """ Potential Samples: """ + Samples2 + (
                             up.breakupOutput2) + """Title: """ + Title + (up.breakupOutput2) + """Song: """ + Song + (
                             up.breakupOutput2) + """Song 2.0: """ + ReWrite + (
                             up.breakupOutput2) + """DJMondeVert: """ + DJMondeVert + """Bitter Critic: """ + Bitter_Critic
        except:
            data_final = """Title: """ + Title + """                                Song: """ + Song + """                         Song 2.0: """ + ReWrite
        print(data_final)

        # MondeVert.speak(self, "Saving the files round 1")
        # print(data)

        # data = [(self.current_time + '_' + data_final)]
        Text = str("Create Date: " + self.current_time + '_Results: ' + data_final)

        # print(data)
        try:
            # df1 = pd.DataFrame(data)
            # print(df1)
            # print(Title2)

            filename = cu.SaveCSV(Title=Title1 + '_PreProduction', SavePath=SavePath_Details, Text=Text)
            try:
                filename2 = cu.SaveCSV(Title=Title1, SavePath=SavePath, Text=Lyrics, AddTimeStamp=False)

            except:
                dn = 100
        except:
            print('Review Error File did not save ')

        try:
            try:
                Art_persona = MondeVert.Artist_Persona_Short_Story(Writer_persona=Artist_Bio_Details)
                try:
                    Art_Details = MondeVert.summarize_art_style_for_short_story(writer_persona=Artist_Bio_Details,
                                                                                outline=Lyrics,
                                                                                Artist_Persona=Art_persona)  # , Format='Make a concise summary of an art style and artist to make a work of art like. Also provide the colors used, themes, moods, and tones.')
                except:
                    Dn = 100

                originalFilepath = self.PersonaArtPath2
                PicNewPath = SavePath_Pics + '_' + Title1 + '_Artist Pic.png'
                try:
                    shutil.copyfile(originalFilepath, PicNewPath)
                except:
                    dn = 100

            except:
                Art_Details = Artist_Bio_Details
                dn = 100

            newline = """\n"""
            newline2 = """\\n"""
            # audioname = cu.SaveText2Audio(Text=Lyrics, Translate=Translate, SavePath=SavePath,
            #                               FileName=Title1, Chunk_Replaces=['.', ')', ':', '?', newline, newline2],
            #                               Chunk_Limit=Chunk_Limit,
            #                               Artist_Persona=Art_Details)
            test = 100
        except:
            dn = 100

            # MondeVert.SaveText(self,df1,'MondeVert Assistant', 'Full Transcript')

        try:
            cu.send_email_no_attachment_gmail(body=Lyrics)
            cu.send_email_no_attachment_outlook(body=Lyrics)

            cu.send_email_w_attachment_outlook(body=Lyrics, filename=[PicNewPath])
            cu.send_email_w_attachment_gmail(body=Lyrics, filename=[PicNewPath], fType='png')

        except:
            print('email not send, its possible file was not created')

        Art_Prompt = MondeVert.GPTArt2(self, prompt=up.ArtPrompt_SongArtistRR, User_Subject=Role + Artist_Bio)
        print("Work of Art Inspiration:" + Art_Prompt)

        # print(Artist_Bio)
        # MondeVert.speak(self,Artist_Bio)
        # print(Song)
        # MondeVert.speak(self, Song)
        # print(Art_Prompt)
        # MondeVert.speak(self, Art_Prompt)

        # Art2 = MondeVert.ChatGPTDA(self, temp=crazy, MakeArt=True, Prompt=(Art_Prompt),ConfirmBot=False)
        try:
            ArtPath2 = MondeVert.makeArt(self, Art_Prompt)
            ArtPaths.append(ArtPath2)

        except:
            ArtPath2 = ''

        # MondeVert.speak(self, "Saving the files round 2")
        prompt = data_final + "Work of Art Inspiration:" + str(Art_Prompt)
        Prompts_Used = [str(self.UserPromptsCount) + ' User Inputs: ' + self.UserPrompts]
        ArtistPoetInfo = 'Lyrics Written By: Shane Donovan   (' + 'Artwork by: ' + up.AI_ArtistName + ')'
        cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title1,
                            SavePath=SavePath, Mode='Song Lyrics' + Mode)
        return Title

    def MondeVert_SHAINE_WeddingVows(self, FileName='Wedding Vows', RandomCouple=False, SavePath=up.AI_Wedding,
                                     Line1=up.system_TextJoaT, Line2=WeddingP.Wedding_Vows_Line2_role,
                                     Line3=WeddingP.Wedding_Vows_Line3_Format, Line4=WeddingP.Wedding_Vows_Line4_Task,
                                     Mode='Wedding Vows', Couple=''):
        RandomCouple = True
        if RandomCouple == True:
            Couple = MondeVert.Basic_GPT_Query(self, Line2_Role=WeddingP.Wedding_Persona_Line2_role,
                                               Line3_Format=WeddingP.Wedding_Persona_Line3_Format,
                                               Line4_Task=WeddingP.Wedding_Persona_Line4_Task)
        # Vows = MondeVert.Basic_GPT_Query(self,Line2_Role=WeddingP.Wedding_Vows_Line2_role, Line3_Format=WeddingP.Wedding_Vows_Line3_Format,Line4_Task=WeddingP.Wedding_Vows_Line4_Task + Couple + " ###")

        print(Couple)
        # print(Vows)
        try:
            if Couple == '':
                Couple = ' '
            # if Vows == '':
            #     Vows = ' '
            Text2Add = Couple  # + Vows
            # FileName = FileName + '_' + self.current_time
            cu.SaveCSV(Text=Text2Add, FileName=FileName, SavePath=SavePath)
            cu.SaveText2Audio(Text=Text2Add, FileName=FileName, SavePath=SavePath)
        except:

            print('Error asking GPT')

    def Manual_Audio_File(self, Source_FilePath, SavePath=up.AI_AudioBook_Path, Text_override='',
                          Voice=random.choices(SAF.Original_List_of_Voices_English)[0], FileName='SHAINE Testing',
                          Chunk_Limit=1500):
        # I can likely use this for all of the ChatGPT conversations
        # Text  = pd.read_csv(FilePath)
        print(Source_FilePath)

        Voice_fix = cu.CleanFileName(Voice)
        if Text_override == '':
            with open(Source_FilePath) as f:
                Text = f.read()

        else:
            Text = Text_override

        ItalianVoice = random.choices(SAF.Italian_Voices)[0]

        ItalianVoice = cu.CleanFileName(ItalianVoice)

        FilePathnew = Source_FilePath[:-4] + '.mp3'
        FilePathnew2 = Source_FilePath[:-4] + ItalianVoice + '_Italian.mp3'
        FilePathnew3 = Source_FilePath[:-4] + Voice_fix + '_Italian.mp3'
        FileName2 = FileName + '_Italian'

        LastPunc = Source_FilePath.rfind("\\")
        SavePath_Italian_Text = Source_FilePath[:LastPunc]
        Italian_FileName = Source_FilePath[(LastPunc + 1):-4] + '_Italian'

        print('SavePath_Italian_Text')

        print(SavePath_Italian_Text)

        print('Italian_FileName')
        print(Italian_FileName)
        if len(Text) < Chunk_Limit:
            try:

                # print(Text)
                Text_Italian = MondeVert.Translate_english2Italian(self, Text=Text)
            except:
                print('Error with italian GPT remake')
            try:
                # print(Text_Italian)
                Italian = cu.SaveCSV(Text=Text_Italian, SavePath=SavePath_Italian_Text, Title=Italian_FileName)
                print('Italian File' + Italian)
            except:
                print('Error with Saving Italian GPT remake')

            try:
                if len(Text_Italian) > 0:
                    NewTempPath = cu.SaveText2Audio(Text=Text_Italian, SavePath=SavePath, FilePath=FilePathnew2,
                                                    Voice=ItalianVoice, FileName=FileName2, Translate=['Italian'])
                    # NewTempPath2 = cu.SaveText2Audio(Text=Text_Italian, SavePath=SavePath, FilePath=FilePathnew3,
                    # Voice=Voice_fix, FileName=FileName2)
            except:
                print('Error with italian remake')

        # print(NewTempPath)
        try:
            # shutil.copy(NewTempPath, FilePathnew2)
            print('Audio File Saved in the following location: ' + FilePathnew2)
            print('Audio File created with Voice: ' + str(ItalianVoice))
            # shutil.copy(NewTempPath2, FilePathnew3)
            print('Audio File Saved in the following location: ' + FilePathnew3)
            print('Audio File created with Voice: ' + str(Voice_fix))
        except:
            print('Did not translate to italian')

        FilePathnew = Source_FilePath[:-4] + '_' + Voice_fix + '.mp3'
        NewTempPath = cu.SaveText2Audio(Text, SavePath=SavePath, FilePath=FilePathnew, Voice=Voice_fix,
                                        FileName=FileName, Translate=['English'])
        print(NewTempPath)
        try:
            # shutil.move(NewTempPath,FilePathnew)
            print('Audio File Saved in the following location: ' + FilePathnew)
            print('Audio File created with Voice: ' + str(Voice_fix))
        except:
            print(NewTempPath)

    def Basic_GPT_Query(self, Line2_Role, Line3_Format, Line4_Task, Big=False, Special='',
                        Line1_System_Rule=up.system_TextJoaT_quick, crazy=.5, Subject='', Outline='', Allowed_Fails=8,
                        SaveFile=False, MakeArt=False, Mode='SHAINE SAYS',
                        SavePath=''):  # use this to create art style for the work
        if SavePath == '':
            SavePath = self.SavePath

        if Subject != '':
            Line2_Role = Line2_Role + """Your role and subject matter expertise should fit the following Subject and or style and mood in the {Text} provided by the user Text:###""" + Subject + """###"""

        Line1_System_Rule = Line1_System_Rule + Line2_Role
        Line2_Role = Line2_Role + Special
        Full_User_Prompt = """User Inputs to Chat GPT: 
        1). """ + Line1_System_Rule + """
        2).""" + Line2_Role + """
        3).""" + Line3_Format + """
        4).""" + Line4_Task

        KeepGoing = False
        KillSwitch = 0
        while KeepGoing == False and KillSwitch < Allowed_Fails:

            if Big == True:
                Model = "gpt-3.5-turbo-16k-0613"
            else:
                Model = "gpt-3.5-turbo"
            try:

                # This is for the result if you let the AI describe project and details and then make the response
                response = openai.ChatCompletion.create(
                    model=Model,
                    messages=[
                        {"role": "system", "content": Line1_System_Rule},
                        {"role": "user", "content": Line2_Role},
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
                    GPT_Response = MondeVert.Basic_GPT_Query(self, Line2_Role='You are a skilled writer',
                                                             Line3_Format=Line3_Format, Line4_Task=Line4_Task,
                                                             Line1_System_Rule=up.system_Text_ScreenPlay)

                continue

            # print(up.breakupOutput)

            self.UserPromptsCount += 1

            self.UserPrompts += 'User Input #' + str(self.UserPromptsCount)

            self.UserPrompts += Full_User_Prompt + up.breakupOutput2 + up.breakupOutput2

            Title = Mode + '_' + self.current_time
            if SaveFile == True:
                SaveText = self.current_time + up.breakupOutput2 + self.UserPrompts + up.breakupOutput2 + 'SHAINE SAYS: ' + GPT_Response
                print(SaveText)
                cu.SaveCSV(Text=SaveText, SavePath=SavePath, Title=Title)
            if MakeArt == True:
                ArtPrompt = MondeVert.GPTArt2(self, User_Subject=GPT_Response)
                print(ArtPrompt)
                originalFilepath = MondeVert.makeArt(self, Prompt=ArtPrompt)
                PicNewPath1 = Path(PureWindowsPath(SavePath, Mode))
                cu.Check_Folder_Exists(PicNewPath1)
                PicNewPath =  Path(PureWindowsPath(PicNewPath1,  Title + '.png'))

                shutil.copyfile(originalFilepath, PicNewPath)
            return GPT_Response

    def summarize_art_style_for_short_story(self, Role, Task, Artist_Persona, outline, writer_persona,
                                            Format=lup.Art_Summary_short_story_format, crazy=.5,
                                            System=up.system_TextJoaT_quick):
        Line2_Role = Role
        Line3_Format = Format
        Line4_Task = """Using the following {Artist_Persona},{outline}, complete the respective formatted response""" + """
        Artist Persona:""" + str(Artist_Persona) + """###
        outline:  """ + str(outline)

        Art_Style_details = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role, Line4_Task=Line4_Task,
                                                      Line3_Format=Line3_Format)
        # print(up.breakupOutput2)
        return Art_Style_details

    # use this to create characters art
    # ned to run the prompt one first then this one (same goes for by scene too, this will just create the art ultimately
    def Create_Art_from_String_to_list(self, Art_Prompt, SavePath, FileName, Art_Style_details, Key_Word, Key_Char=':',
                                       Delimiter='|', crazy=.5):
        dummy = 1
        ArtPaths = []
        if dummy == 1:
            try:
                Art_PromptCharo = Art_Prompt
            except:
                print('Error Trying to make original Painting')
                Art_PromptCharo = Art_Prompt

            Art_PromptCharoo = Art_PromptCharo
            # ArtPrompt_Mondevert = + Result
            # ArtPrompt_Mondevert = ArtFormatAdvance + Result

            try:
                if Delimiter in Art_PromptCharo:
                    Art_PromptCharo = Art_PromptCharo.split(Delimiter)
                else:
                    Art_PromptCharo = Art_PromptCharo.replace(Key_Word + Key_Char, Delimiter)
                    Art_PromptCharo = Art_PromptCharo.replace(Key_Word, Delimiter)

                if Delimiter in Art_PromptCharo:
                    Art_PromptCharo = Art_PromptCharo.split(Delimiter)
                else:
                    Art_PromptCharo = Art_PromptCharo.replace(Key_Char, Delimiter)
                    Art_PromptCharo = Art_PromptCharo.split(Delimiter)

                # Test_Skel1 = Result.replace("Page:", "#")
                # Test_Skel1 = Test_Skel1.replace("Page", "#")

            # print('Art_PromptCharo')
            # print(Art_PromptCharo)

            except:
                print('Could not properly split out the string for multiple illustrations')

            # before sending as art I should do one more clean up of the language/prompt to make it best

            KillSwitch = 0
            KeepGoing = False
            while KeepGoing == False and KillSwitch < 6:
                try:
                    Art_PromptCharoo + 'Revised Prompts: '
                    Characters = []
                    x = len(Art_PromptCharo)
                    for c in range(0, x):
                        # print(c)
                        # Do the change here before setting the value or keep both
                        Characters.append(Art_PromptCharo[c])
                        Clean_Prompt_User_GPT_Input = MondeVert.Basic_GPT_Query(self,
                                                                                Line2_Role=lup.Clean_Role_after_Delimit + c,
                                                                                Line3_Format=lup.Clean_Format_after_Delimit,
                                                                                Line4_Task=lup.Clean_Task_after_Delimit,
                                                                                Special='Use the following Text for the styles to embody/artist persona to embody###  ' + Art_Style_details + c + '###',
                                                                                Line1_System_Rule=up.system_Text_Art,
                                                                                crazy=.5, Subject='')
                        Characters.append(Art_PromptCharo[Clean_Prompt_User_GPT_Input])

                        Art_PromptCharoo += Clean_Prompt_User_GPT_Input

                    # print('Characters')
                    # print(Characters)

                    for c in Characters:
                        print(' ')
                        print('-------------------------------------------')
                        print('-------------------------------------------')
                        print("Character: " + c)
                        print('-------------------------------------------')
                        # print("Character Art1: " + up.Character_Art1 + c)
                        ArtPath2 = MondeVert.makeArt(self, Art_PromptCharo + c)
                        ArtPaths.append(ArtPath2)
                        # print(ArtPath2)


                except:
                    print('Error Trying to create multiple paintings')
                    KillSwitch += 1
                KeepGoing = True

        return ArtPaths  # after its returned I append this to the folder with all relevant data

    # Make sure to start a master tracker with this information, use the writer persona as part of the data stored (TimeStamp, WriterPersona, Outline, Format, and/or put the prompt together for reference

    # use this to create characters
    def Create_Characters_Short_Story(self, Task, Special, Format, Outline, Persona, Role=lup.Short_Story_Role,
                                      crazy=.5):

        if Persona == '':
            MondeVert.Writer_Persona_Short_Story(self, Role=Role)

        Role = Role + 'For this task you are to assume the role of the following Persona: ###' + Persona + """###"""
        # Make sure to start a master tracker with this information, use the writer persona as part of the data stored (TimeStamp, WriterPersona, Outline, Format, and/or put the prompt together for reference
        Character_Personas = MondeVert.Basic_GPT_Query(self, Line2_Role=Role, Line4_Task=Task, Line3_Format=Format,
                                                       Special=Special)

        # make Character Art prompts for later
        Character_Art_Prompts_Main = MondeVert.Make_Art_prompts(self, Line2_Role=lup.Persona_artist_Role,
                                                                Line3_Format=lup.Character_Art_Format_Main,
                                                                Line4_Task=lup.Character_Art_Task_Main, Special='',
                                                                Line1_System_Rule=up.system_Text_Art,
                                                                Art_Style_details='Imitate a random artist and/or art style pick a random subject',
                                                                crazy=.5,
                                                                Subject=Character_Personas)

        Character_Art_Prompts_Minor = MondeVert.Make_Art_prompts(self, Line2_Role=lup.Persona_artist_Role,
                                                                 Line3_Format=lup.Character_Art_Format_Main,
                                                                 Line4_Task=lup.Character_Art_Task_Main, Special='',
                                                                 Line1_System_Rule=up.system_Text_Art,
                                                                 Art_Style_details='Imitate a random artist and/or art style pick a random subject',
                                                                 crazy=.5,
                                                                 Subject=Character_Personas)

        self.Character_Art_Prompts_Main = Character_Art_Prompts_Main
        self.Character_Art_Prompts_Minor = Character_Art_Prompts_Minor

        return Character_Personas

    def Writer_Persona_Short_Story(self, Role=lup.Persona_Role, Task=lup.Persona_Background,
                                   Format=lup.Persona_Format2, Special=lup.Persona_Special,
                                   Subject='', crazy=.5):

        ArtPath = 'No Art Made'
        if Subject != '':
            Role = Role + """Your role/persona and subject matter expertise should fit the following Subject and or style and mood in the {Text} provided by the user Text:###""" + Subject + """###"""

        Writer_Persona = MondeVert.Basic_GPT_Query(self, Line2_Role=Role, Line4_Task=Task, Line3_Format=Format,
                                                   Special=Special, crazy=crazy)
        # Save a csv of this info in ssavepath
        # Add to Master tracker of artists and writer personas
        try:
            ArtPrompt = MondeVert.GPTArt2(self, User_Subject=Writer_Persona)
            try:
                ArtPath = MondeVert.makeArt(self, Prompt=ArtPrompt)
                self.PersonaArtPath = ArtPath
            except:
                dn = 100
        except:
            dn = 100

        try:
            cu.add2Master_Persona(
                Text=str(self.current_time + '  ' + Writer_Persona + ' Art File location: ' + ArtPath))

        except:
            dn = 100

        return Writer_Persona

    def Artist_Persona_Short_Story(self, Role=lup.Persona_artist_Role, Task=lup.Persona_artist_Background,
                                   Format=lup.Persona_artist_Format, Special=lup.Persona_artist_Special,
                                   Writer_persona='', crazy=.5):
        ArtPath = 'No Art File Created'
        if Writer_persona != '':
            Special = Special + """You should fit the style and mood provided by the following Outline:###""" + Writer_persona + """###"""

            Artist_Persona = MondeVert.Basic_GPT_Query(self, Line2_Role=Role, Line4_Task=Task, Line3_Format=Format,
                                                       Special=Special, crazy=crazy)
            if Artist_Persona == '':
                Artist_Persona = 'Same artist that works for the simpsons, make it in simpson style art'

            try:
                ArtPrompt = MondeVert.GPTArt2(self, User_Subject=Artist_Persona)
                try:
                    ArtPath = MondeVert.makeArt(self, Prompt=ArtPrompt)
                    self.PersonaArtPath2 = ArtPath
                except:
                    dn = 100
            except:
                dn = 100

            try:
                cu.add2Master_Persona(
                    Text=str(self.current_time + '  ' + Artist_Persona + ' Art File location: ' + ArtPath))
            except:
                dn = 100

            # print(up.breakupOutput)
            return Artist_Persona

    def Make_Art_prompts(self, Line2_Role=lup.Persona_artist_Role, Line3_Format=lup.Persona_artist_Format,
                         Line4_Task=lup.Persona_artist_Task, Special='', Line1_System_Rule=up.system_Text_Art,
                         Art_Style_details='Imitate a random artist and/or art style pick a random subject', crazy=.5,
                         Subject='Choose a random artist and style and make an interesting prompt up'):
        Art_Prompt_With_Delimiter = MondeVert.Basic_GPT_Query(self, Line2_Role=Line2_Role + Art_Style_details,
                                                              Line3_Format=Line3_Format, Line4_Task=Line4_Task,
                                                              Special='', Line1_System_Rule=Line1_System_Rule,
                                                              crazy=crazy, Subject='')
        return Art_Prompt_With_Delimiter

    # run this once for characters then do it for the scenes --> for characters need the respective info (see other functions)
    # --> for scenes try to set it up too
    # --> also set up random info
    # lastly dont forget to make audio file

    def Quick_Title(self, Text, Line1_System_Rule=up.system_TextJoaT_quick, crazy=.5):
        KeepGoing = False
        KillSwitch = 0
        while KeepGoing == False and KillSwitch < 8:
            try:

                Line1_System_Rule = Line1_System_Rule
                Line2_Task_Text = """Text: ###""" + Text + "###"
                Line3_Format_Text = StoryMode.Title_Format
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
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
                print(
                    ' Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                KillSwitch += 1
                if KillSwitch == 9:
                    print('could not create a writer persona, redoing it now')
                    Title = 'Unknown title - Too many errors'
                    Title = Title.replace("The Title:", "")
                    Title = Title.replace("Title:", "")
                    Title = Title.replace("The Title", "")
                    Title = Title.replace("Title", "")
                continue
        return Title

    def Translate(self, Line1=SAF.Translate_Sys, Origin_Language='English', Language_Final='Italian',
                  Text='Sorry no text was sent but translate this instead, Monde Vert apologizes for the inconvenience',
                  Line2=SAF.Translate_Line2, Line3=SAF.Translate_Line3, Line4=SAF.Translate_Line4,
                  SavePath=up.AI_AudioBook_Path, File_Name='Italian Translation'):

        SAF.Pick_Voice(Language=Language_Final)

        Line4 = Line4 + Text + "] From [" + Origin_Language + "] to [" + Language_Final + "] "  # + Line4

        File_Name = File_Name + '_' + Origin_Language + ' to ' + Language_Final + '_Translation'
        Translated_Text = MondeVert.Basic_GPT_Query(self, Line1_System_Rule=Line1, Line2_Role=Line2, Line3_Format=Line3,
                                                    Line4_Task=Line4)
        return Translated_Text

    def Translate_english2Italian(self, Line1=up.Translate_Sys, Language='Italian',
                                  Text='Sorry no text was sent but translate this instead, Monde Vert apologizes for the inconvenience',
                                  Line2=up.Translate_PictureBook_Line2, Line3=up.Translate_PictureBook_Line3,
                                  Line4=up.Translate_PictureBook_Line4, SavePath=up.AI_Childrens_AudioBook_Path,
                                  File_Name='Italian Translation'):

        Line4 = Line4 + Text + "] From [English] to [" + Language + "] "  # + Line4

        File_Name = File_Name + '_Italian Translation'
        Italian_Text = MondeVert.Basic_GPT_Query(self, Line1_System_Rule=Line1, Line2_Role=Line2, Line3_Format=Line3,
                                                 Line4_Task=Line4)
        return Italian_Text

    # make it so it has threads to speed things up (this is intensive), for now make sure you can run multiple seasons, allow it to go scene by scene, and also add how episode starts/ends and how season starts and ends
    # def MondeVert_Audio_Video_Story(self, Persona='', Subject='', Translate=SAF.Translation_Languages_Testing,
    #                                 Role='', Background='', Task='', Special='', Title='SHAINE Project Fail Safe',
    #                                 Mode='Audio_Video_Story', Episodes=3, Seasons=2, Logic_AI=0, Format='',
    #                                 SavePath=up.AI_AudioBook_Path, Persona_Role=lup.Persona_Role,
    #                                 Persona_Task=lup.Persona_Background, Persona_Special=lup.Persona_Special,
    #                                 Persona_Format=lup.Persona_Format2,
    #                                 Persona_summary_Role=lup.Persona_Summary_For_Role_Play_Line2_Role,
    #                                 Persona_summary_Task=lup.Persona_Summary_For_Role_Play_Line4_Task,
    #                                 Persona_summary_Format=lup.Persona_Summary_For_Role_Play_Line3_Format,
    #                                 Persona_artist_Role=lup.Persona_artist_Role,
    #                                 Persona_artist_Task=lup.Persona_artist_Background,
    #                                 Persona_artist_Format=lup.Persona_artist_Format,
    #                                 Persona_artist_Special=lup.Persona_artist_Special,
    #                                 Outline1_Format=lup.Short_Story_Outline_Format,
    #                                 Outline1_Task=lup.Short_Story_Outline_Task, System=up.system_TextJoaT_quick,
    #                                 Outline_Main_AddOn_Pre=lup.Short_Story_Config + lup.Shane_Test_User_Input ,
    #                                 Season_Outline_Format=lup.Short_Story_Season_Outline_Format,
    #
    #                                 Season_Outline_Task=lup.Short_Story_Season_Outline_Task,
    #                                 Season_By_Season_Outline_Format=lup.Short_Story_SeasonBySeason_Outline_Format,
    #                                 Season_By_Season_Outline_Task=lup.Short_Story_SeasonBySeason_Outline_Task,
    #                                 Pilot_Short_story_fix1=lup.Pilot_Short_story_fix,
    #                                 Episode_by_Episode_Outline_Format=lup.Short_Story_Episode_Outline_Format,
    #                                 Episode_by_Episode_Outline_Task=lup.Short_Story_Episode_Outline_Task,
    #
    #                                 Episode_by_Episode_Format=lup.Short_Story_Format,
    #                                 Episode_by_Episode_Task=lup.Short_Story_Task2
    #                                 ):
    #
    #     Translate = ['English']
    #
    #     Episode_Count = Episodes
    #     ArtPaths = []
    #     openai.api_key = API_Key
    #     Art_PromptCharoo = ''
    #     Art_PromptCharo = ''
    #     Art_PromptForDALLE = ''
    #     Episode = []
    #     Episode2 = []
    #     Episode3 = []
    #     Episode4 = []
    #
    #     # ******************************************************************
    #     Episode_Outlines = ''
    #
    #     Outline_Main = 'N/A not ready to test this yet'
    #     Outline_All_Episodes = 'N/A not ready to test this yet'
    #     ScreenPlay = 'N/A not ready to test this yet'
    #     Outline_Episode_Specific = ''
    #     Title = 'N/A not ready to test this yet'
    #     Project_Description = 'N/A not ready to test this yet'
    #     Result = 'N/A not ready to test this yet'
    #     Result_AI = 'N/A not ready to test this yet'
    #     AIPrompt = 'N/A not ready to test this yet'
    #     Writer_Persona = 'N/A not ready to test this yet'
    #     Artist_Persona = 'N/A not ready to test this yet'
    #     Art_Prompts = 'N/A not ready to test this yet'
    #     Writer_Persona_Summary = ''
    #     Episode_Outline = []
    #
    #     Titleo = Title
    #
    #     if Logic_AI == 0:
    #         crazy = round((randbelow(520000) + 170000) / 100000, 0)
    #         crazy = crazy / 10
    #         print('Crazy Rating: ' + str(crazy))
    #         crazy += .2
    #         if crazy < .4:
    #             crazy = .6
    #         if crazy > .9:
    #             crazy = .7
    #     else:
    #         crazy = Logic_AI
    #
    #     SavePath
    #
    #     Format0 = up.Test_Format0
    #     KillSwitch = 0
    #
    #     Format_f = Format
    #     if Mode == 'skit':
    #         Format_f = Format0
    #
    #     if Title != '':
    #         Background = Title + Background
    #
    #     tempFormat = Format
    #     if Mode == 'PictureBook':
    #         Format = up.Test_Format_PictureBook_outline
    #
    #     if Persona != '':
    #         Persona_Role = 'You are the following Persona use them as a model for your response: ' + Persona
    #
    #     # Call Writer persona function
    #     Writer_Persona = MondeVert.Writer_Persona_Short_Story(self, Role=Persona_Role, Task=Persona_Task,
    #                                                           Format=Persona_Format, Special=Persona_Special,
    #                                                           Subject=Subject[:1313], crazy=crazy)
    #
    #     if Writer_Persona == '':
    #         Writer_Persona = Subject[:1313]
    #
    #     Writer_Persona_Summary = MondeVert.Basic_GPT_Query(self, Line2_Role=Persona_summary_Role,
    #                                                        Line4_Task=Persona_summary_Task + Writer_Persona,
    #                                                        Line3_Format=Persona_summary_Format, Special='',
    #                                                        Subject='', crazy=crazy)
    #
    #     if Writer_Persona_Summary == '':
    #         Writer_Persona_Summary = MondeVert.Basic_GPT_Query(self,
    #                                                            Line4_Task="Summarize the following Writer Persona: " + Writer_Persona,
    #                                                            Line3_Format=Persona_summary_Format, Special='',
    #                                                            Subject='', crazy=crazy)
    #
    #     cu.add2Master_Persona(Text=Writer_Persona)
    #     cu.add2Master_Persona(Text=Writer_Persona_Summary)
    #
    #     if Writer_Persona_Summary == '':
    #         Writer_Persona_Summary = Writer_Persona[:1800]
    #
    #
    #     Artist_Persona = MondeVert.Artist_Persona_Short_Story(self, Role=Persona_artist_Role,
    #                                                           Task=Persona_artist_Task,
    #                                                           Format=Persona_artist_Format,
    #                                                           Special=Persona_artist_Special,
    #                                                           Writer_persona=Writer_Persona, crazy=crazy)
    #
    #     Art_Details = MondeVert.GPTArt2(self, User_Subject=Artist_Persona, ArtFormat=lup.artDetailsFormat,
    #                                     prompt=lup.artDetailsPrompt)
    #
    #     # Call outline - Main function
    #
    #     if Subject == '':
    #         Outline_Main = MondeVert.Basic_GPT_Query(self,
    #                                                  Line2_Role='Take on the following writer persona:' + Writer_Persona,
    #                                                  Line3_Format=Outline1_Format,
    #                                                  Line4_Task=Outline_Main_AddOn_Pre + Outline1_Task, Special='',
    #                                                  Line1_System_Rule=System, crazy=crazy, Subject='')
    #     else:
    #         if Writer_Persona_Summary != '':
    #             Writer_Persona = Writer_Persona_Summary
    #         Outline1_Task = "Use the following outline to create your own outline, be sure to use the correct format for your outline"
    #         Outline0_Task = "Use the following outline to create your own outline, be sure to use the correct format for your outline"
    #         if len(Subject) > 1717:
    #             Subject_trim = Subject[:2700]
    #             Subject_Summary = MondeVert.Basic_GPT_Query(self,
    #                                                         Line2_Role='You are a master editor and writer',
    #                                                         Line3_Format='Trim redundant words and make it concise so it is less than 1900 characters and still has the main components of the story',
    #                                                         Line4_Task=Outline0_Task + Subject_trim, Special='',
    #                                                         Line1_System_Rule=System, crazy=crazy)
    #         Outline_Main = MondeVert.Basic_GPT_Query(self,
    #                                                  Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
    #                                                  Line3_Format=Outline1_Format,
    #                                                  Line4_Task=Outline_Main_AddOn_Pre + Outline1_Task + Subject_Summary,
    #                                                  Special='',
    #                                                  Line1_System_Rule=System, crazy=crazy)
    #     print('Writer Persona: ' + Writer_Persona)
    #     print('Writer Persona_Summary: ' + Writer_Persona_Summary)
    #     print('Artist Persona: ' + Artist_Persona)
    #     print(Outline_Main)
    #
    #     print('Created Writer Persona')
    #     print('Created Artist Persona')
    #     print('Created Main Outline')
    #
    #     # print(up.breakupOutput)
    #     # print('User_Input_Outline_Main: ' + User_Input_Outline_Main)
    #     # print(up.breakupOutput)
    #     # Call Art Theme Function
    #
    #     Art_Style_For_Story = MondeVert.summarize_art_style_for_short_story(self,Role,   Artist_Persona = Artist_Persona, outline = Outline_Main,Task = lup.artDetailsPrompt, Format = lup.artDetailsFormat, crazy = crazy, writer_persona = Writer_Persona_Summary )
    #     print('Created Artist style summary (see below)')
    #     print(Art_Style_For_Story)
    #
    #     # Call Character function
    #     Characters = MondeVert.Create_Characters_Short_Story(self, Role=lup.Characters_Role,
    #                                                          Task=lup.Characters_Task + Outline_Main,
    #                                                          Special=lup.Characters_Special,
    #                                                          Format=lup.Characters_Format, Outline='',
    #                                                          Persona=Writer_Persona_Summary, crazy=crazy)
    #     if Characters == '':
    #         Characters = MondeVert.Create_Characters_Short_Story(self, Role=lup.Characters_Role,
    #                                                              Task=lup.Characters_Task,
    #                                                              Special=lup.Characters_Special,
    #                                                              Format=lup.Characters_Format, Outline=Outline_Main,
    #                                                              Persona=Writer_Persona_Summary, crazy=crazy)
    #
    #     # Add this back once its working correctly
    #     # cu.Chop4Art(Text = Characters, Artist_Persona=Art_Details, Chunk_Limit=333, SavePath=SavePath, FileName=Title + '_Characters_v1')
    #     # cu.Chop4Art(Text=self.Character_Art_Prompts_Main + self.Character_Art_Prompts_Main, Artist_Persona=Art_Details, Chunk_Limit=333, SavePath=SavePath, FileName=Title + '_Characters_v2')
    #
    #     # print(up.breakupOutput)
    #     # print('User_Input_Character: ' +  User_Input_Character)
    #     # print(up.breakupOutput)
    #
    #     print('Created Character Personas')
    #     CharactersTrim = Characters[:444]
    #     Outline_ALL_Seasons_list = ['']
    #     # Call Outline - All Episodes
    #     Outline_ALL_Seasons = MondeVert.Basic_GPT_Query(self,
    #                                                      Line2_Role='Role Play as the following persona:' + Writer_Persona_Summary,
    #                                                      Line3_Format=Season_By_Season_Outline_Format,
    #                                                      Line4_Task=Season_By_Season_Outline_Task + """Use the following High level {Main Outline} as a source for the creating the season by season specific outline you are working on  Outline for each of the Seasons in the Series:###""" + Outline_Main +  """### Use the following main characters: """ + CharactersTrim,
    #                                                      Special='', Line1_System_Rule=System, crazy=crazy,
    #                                                      Subject='')
    #
    #     if "@" in Outline_ALL_Seasons:
    #         Outline_ALL_Seasons_split = Outline_ALL_Seasons.split("@")
    #     else:
    #         Outline_ALL_Seasons_split = Outline_ALL_Seasons.replace("Season", "@Season")
    #         Outline_ALL_Seasons_split = Outline_ALL_Seasons.replace("SEASON", "@SEASON")
    #         Outline_ALL_Seasons_split = Outline_ALL_Seasons.split("@")
    #
    #     for s in Outline_ALL_Seasons_split:
    #         if "SEASON" in s.upper():
    #             Outline_ALL_Seasons_list.append(s)
    #
    #     data = ''
    #     AudioBook_Text = ''
    #     SeasonCounts = Seasons + 1
    #     try:
    #         Title = MondeVert.Quick_Title(self, Outline_Main)
    #     except:
    #         Title = 'MondeVert_SHAINE_Confidential_AudioBook'
    #
    #     Title = Title.replace("The Title:", "")
    #     Title = Title.replace("Title:", "")
    #     Title = Title.replace("The Title", "")
    #     Title = Title.replace("Title", "")
    #     Title1 = cu.CleanFileName(Title)
    #     FileName = Title1
    #     SavePath = SavePath + up.System_Folder_Path_Fix + Title1
    #     cu.Check_Folder_Exists(SavePath)
    #     FileName_Char_Main = Title1 + '_Main Characters_'
    #     FileName_Char_Minor = Title1 + '_Minor Characters_'
    #     # Call Character art prompt
    #
    #     Text2Add = 'Story Outline: ' + up.breakupOutput + Outline_Main + up.breakupOutput2 + 'All Seasons Outline: ' + Outline_ALL_Seasons + up.breakupOutput + 'Characters: ' + up.breakupOutput + Characters + up.breakupOutput2 + up.breakupOutput + 'Writer Persona: ' + up.breakupOutput + Writer_Persona + up.breakupOutput2 + up.breakupOutput + 'Writer Persona Summary: ' + up.breakupOutput + Writer_Persona_Summary + up.breakupOutput2 + up.breakupOutput + 'Artist Persona: ' + up.breakupOutput + Artist_Persona + up.breakupOutput2 + up.breakupOutput + 'Character Description - Main: ' + up.breakupOutput + self.Character_Art_Prompts_Main + up.breakupOutput2 + up.breakupOutput + 'Character Description - Minor: ' + up.breakupOutput + self.Character_Art_Prompts_Minor
    #     FileName_Details_Pre = FileName + ' PreProduction'
    #     cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=SavePath)
    #
    #     for x in range(1,SeasonCounts):
    #         Season_num = x
    #
    #         try:
    #             if len (Outline_ALL_Seasons_list) >= Season_num:
    #                 Outline_AllS = Outline_ALL_Seasons_list[Season_num]
    #         except:
    #             continue
    #         print('Outline Season # ' + str(Season_num) + ': ' + up.breakupOutput2 + Outline_AllS)
    #
    #
    #         Outline_ALL_Episode_list = ['']
    #         # Call Outline - All Episodes
    #         Outline_ALL_Episodes = MondeVert.Basic_GPT_Query(self,
    #                                                          Line2_Role='Role Play as the following persona:' + Writer_Persona_Summary,
    #                                                          Line3_Format=Season_Outline_Format,
    #                                                          Line4_Task=Season_Outline_Task + """Use the following High level  {Season Specific Outline}  as a source for the creating the season specific outline you are working on  Outline for All Seasons in the season:###""" + Outline_AllS + """ Use the following characters: """ + CharactersTrim,
    #                                                          Special='', Line1_System_Rule=System, crazy=crazy,
    #                                                          Subject='')
    #
    #         if "@" in Outline_All_Episodes:
    #             Outline_ALL_Episodes_split = Outline_ALL_Episodes.split("@")
    #         else:
    #             Outline_All_Episodes = Outline_ALL_Episodes.replace("Episode", "@EPISODE")
    #             Outline_All_Episodes = Outline_All_Episodes.replace("EPISODE", "@EPISODE")
    #             Outline_ALL_Episodes_split = Outline_All_Episodes.split("@")
    #
    #         for s in Outline_ALL_Episodes_split:
    #             if "EPISODE" in s.upper():
    #                 Outline_ALL_Episode_list.append(s)
    #
    #         print('Created All Episode Outline')
    #
    #
    #
    #         Text2Add = 'Story Outline: ' + up.breakupOutput + Outline_Main + up.breakupOutput2 + 'All Seasons Outline: ' + Outline_ALL_Seasons +up.breakupOutput + 'All Episodes Outline: ' + up.breakupOutput + Outline_ALL_Episodes + up.breakupOutput2 + up.breakupOutput
    #         FileName_Details_Pre = FileName   +  ' Season ' + str(Season_num) + ' Outlines'
    #         cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=SavePath)
    #
    #         # Call Outline - Episode by episode
    #         Pilot_Short_story_fix = ''
    #
    #         print(Outline_ALL_Episode_list)
    #         for_num = Episode_Count + 1
    #         print(for_num)
    #         Outline_Episodes_by_episode = ''
    #
    #         for episode_num in range(1, for_num):
    #             Episode_Story = ''
    #             Episode_Story_Audio = ''
    #             Episode_Story_Novel = ''
    #             Episode_Story_Play = ''
    #
    #             print(episode_num)
    #             print(len(Outline_ALL_Episode_list) )
    #
    #             try:
    #                 if len(Outline_ALL_Episode_list) >= episode_num:
    #                     Outline_All = Outline_ALL_Episode_list[episode_num]
    #             except:
    #                 continue
    #
    #             print('Outline All:' + up.breakupOutput2 + Outline_All)
    #             if episode_num == 1:
    #                 Pilot_Short_story_fix = Pilot_Short_story_fix1
    #             else:
    #                 Pilot_Short_story_fix = ''
    #             print('Created Outline for Episode ' + str(episode_num))
    #             # Special = Episode_by_Episode_Outline_Special + str(episode_num) + "### " + Pilot_Short_story_fix
    #
    #             Outline_Episodes_by_episode = MondeVert.Basic_GPT_Query(self,
    #                                                                     Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
    #                                                                     Line3_Format=Episode_by_Episode_Outline_Format,
    #                                                                     Line4_Task=Episode_by_Episode_Outline_Task + """Episode Outline:### """ + Outline_All + ' ###' + 'Characters: ' + Characters,
    #                                                                     Line1_System_Rule=System, crazy=crazy,
    #                                                                     Subject='')
    #
    #             Episode_Outline.append(Outline_Episodes_by_episode)
    #             Outline_Episodes_by_episode_list = ['']
    #             if "@" in Outline_Episodes_by_episode:
    #                 Outline_Episodes_by_episode_Split = Outline_Episodes_by_episode.split("@")
    #             else:
    #                 Outline_Episodes_by_episode = Outline_Episodes_by_episode.replace("Scene", "@Scene")
    #                 Outline_Episodes_by_episode = Outline_Episodes_by_episode.replace("SCENE", "@SCENE")
    #                 Outline_Episodes_by_episode_Split = Outline_Episodes_by_episode.split("@")
    #
    #             for s in Outline_Episodes_by_episode_Split:
    #                 if "SCENE" in s.upper():
    #                     Outline_Episodes_by_episode_list.append(s)
    #                 else:
    #                     if s == Outline_Episodes_by_episode_Split[0]:
    #                         Episode_By_Episode_Details = s
    #
    #             Scene_Range = len(Outline_Episodes_by_episode_list) + 1
    #             print("Number of scenes: ")
    #             print (Scene_Range)
    #             for y in range(1,Scene_Range):
    #                 Scene_Num = y
    #
    #
    #                 if Outline_Episodes_by_episode == '':
    #                     Outline_Episodes_by_episode = Outline_All_Episodes
    #                 try:
    #                     try:
    #                         try:
    #                             Story1 = MondeVert.Basic_GPT_Query(self,
    #                                                                             Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
    #                                                                             Line3_Format=Episode_by_Episode_Format,
    #                                                                             Line4_Task=Episode_by_Episode_Task + """Scene Outline:### """ + Episode_By_Episode_Details + Outline_Episodes_by_episode_list[Scene_Num] + '  ###',
    #                                                                             Special=Pilot_Short_story_fix,
    #                                                                             Line1_System_Rule=System, crazy=crazy,
    #                                                                             Subject='', Outline='')
    #
    #                             Episode_Story_Audio  +=  'Season ' + str(Season_num) + ' Episode #' + str(episode_num) + ' Scene # ' + str(Scene_Num)+  Story1 + up.breakupOutput2
    #
    #                         except:
    #                             dn = 100
    #
    #                         try:
    #                             Story3 = MondeVert.Basic_GPT_Query(self,
    #                                                                       Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
    #                                                                       Line3_Format=lup.Short_Story_Format_Novel_Chapter,
    #                                                                       Line4_Task=lup.Short_Story_Task_Novel_Chapter + """Scene Outline:### """ + Episode_By_Episode_Details + Outline_Episodes_by_episode_list[Scene_Num] + '  ###',
    #                                                                       Special=Pilot_Short_story_fix,
    #                                                                       Line1_System_Rule=System,
    #                                                                       crazy=crazy, Subject='', Outline='')
    #                             Episode_Story_Novel +=  'Season ' + str(Season_num) + ' Episode #' + str(episode_num) + ' Scene # ' + str(Scene_Num)+  Story3 + up.breakupOutput2
    #
    #                         except:
    #                             dn = 100
    #                         try:
    #                             Story4 = MondeVert.Basic_GPT_Query(self,
    #                                                                Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
    #                                                                Line3_Format=lup.Short_Story_Format_Play_Scene,
    #                                                                Line4_Task=lup.Short_Story_Task_Play_Scene + """Scene Outline:### """ + Episode_By_Episode_Details +
    #                                                                           Outline_Episodes_by_episode_list[
    #                                                                               Scene_Num] + '  ###',
    #                                                                Special=Pilot_Short_story_fix,
    #                                                                Line1_System_Rule=System,
    #                                                                crazy=crazy, Subject='', Outline='')
    #                             Episode_Story_Play += 'Season ' + str(Season_num) + ' Episode #' + str(
    #                                 episode_num) + ' Scene # ' + str(Scene_Num) + Story4 + up.breakupOutput2
    #
    #                         except:
    #                             dn = 100
    #
    #                         try:
    #                             Story2 = MondeVert.Basic_GPT_Query(self,
    #                                                                       Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
    #                                                                       Line3_Format=lup.Short_Story_Format_Screenplay,
    #                                                                       Line4_Task=Episode_by_Episode_Task + """Scene Outline:### """ + Episode_By_Episode_Details + Outline_Episodes_by_episode_list[Scene_Num] + '  ###',
    #                                                                       Special=Pilot_Short_story_fix,
    #                                                                       Line1_System_Rule=System,
    #                                                                       crazy=crazy, Subject='', Outline='')
    #                             Episode_Story +=  'Season ' + str(Season_num) + ' Episode #' + str(episode_num) + ' Scene # ' + str(Scene_Num)+  Story2 + up.breakupOutput2
    #
    #
    #
    #                         except:
    #                             dn = 100
    #                     except:
    #                         Story2 = MondeVert.Basic_GPT_Query(self,
    #                                                                   Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
    #                                                                   Line3_Format=Episode_by_Episode_Format,
    #                                                                   Line4_Task=Episode_by_Episode_Task + """Episode Outline:### """ + Outline_Episodes_by_episode,
    #                                                                   Special=Pilot_Short_story_fix,
    #                                                                   Line1_System_Rule=System, crazy=crazy, Subject='',
    #                                                                   Outline='')
    #                         Episode_Story += 'Season ' + str(Season_num) + ' Episode #' + str(episode_num) + ' Scene # ' + str(Scene_Num) + Story2 + up.breakupOutput2
    #
    #
    #
    #
    #                 except:
    #                     print('Error making Scene # ' + str(Scene_Num) + 'Episode #' + str(episode_num))
    #
    #             print('Created Episode ' + str(episode_num)  + ' for Season ' + str(Season_num))
    #
    #             Episode3.append(Episode_Story_Novel)
    #             Episode.append(Episode_Story)
    #             Episode2.append(Episode_Story_Audio)
    #             Episode4.append(Episode_Story_Play)
    #             Text2Add = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story
    #             FileName_Episode = FileName + ' Season ' + str(Season_num) + ' EPISODE ' + str(episode_num)
    #             FileName_Episode2 = FileName +  ' Season ' + str(Season_num) + ' EPISODE ' + str(episode_num) + ' Audio'
    #             FileName_Episode3 = FileName + ' Act ' + str(Season_num) + ' Chapter ' + str(episode_num) + ' Novel'
    #             FileName_Episode4 = FileName + ' Act ' + str(Season_num) + ' Chapter ' + str(episode_num) + ' Play'
    #             csv1 = cu.SaveCSV(Text=Text2Add, Title=FileName_Episode, SavePath=SavePath)
    #             Text2Add2 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story_Audio
    #             csv2 = cu.SaveCSV(Text=Text2Add2, Title=FileName_Episode2, SavePath=SavePath)
    #             Text2Add3 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story_Novel
    #             csv3 = cu.SaveCSV(Text=Text2Add3, Title=FileName_Episode3, SavePath=SavePath)
    #             Text2Add4 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story_Play
    #             csv4 = cu.SaveCSV(Text=Text2Add4, Title=FileName_Episode4, SavePath=SavePath)
    #
    #             Text2Add5 = "Outline Details: " + up.breakupOutput2 + up.breakupOutput + Outline_Episodes_by_episode
    #             FileName_Episode = FileName  +  ' Season ' + str(Season_num) + ' Episode ' + str(episode_num) +   ' Outline '
    #             cu.SaveCSV(Text=Text2Add5, Title=FileName_Episode, SavePath=SavePath)
    #
    #             try:
    #
    #                 Voice = random.choices(SAF.Original_List_of_Voices_English[0])
    #
    #                 Voice_Audio = random.choices(SAF.Original_List_of_Voices_English[0])
    #
    #                 Voice_Novel = random.choices(SAF.Original_List_of_Voices_English[0])
    #
    #                 Voice_Play = random.choices(SAF.Original_List_of_Voices_English[0])
    #
    #
    #                 print('translate Langauge:')
    #                 print(Translate)
    #
    #                 # cu.SaveText2Audio(SavePath=SavePath, FileName=FileName_Episode, Voice=Voice, Neural='Neural',
    #                 #                   Mode='AUDIOBOOK', Chunk_Limit=1444, Artist_Persona=Art_Style_For_Story, Text=Text2Add,
    #                 #                   Translate=Translate)
    #                 #
    #                 # cu.SaveText2Audio(SavePath=SavePath, FileName=FileName_Episode2, Voice=Voice_Audio,
    #                 #                   Neural='Neural',
    #                 #                   Mode='AUDIOBOOK', Chunk_Limit=1444, Artist_Persona=Art_Style_For_Story,
    #                 #                   Text=Text2Add2,
    #                 #                   Translate=Translate)
    #                 #
    #                 #
    #
    #
    #                 try:
    #                     cu.SaveText2Audio(SavePath=SavePath, FileName=FileName_Episode3, Voice=Voice_Novel,
    #                                       Neural='Neural',
    #                                       Mode='AUDIOBOOK', Chunk_Limit=1444, Artist_Persona=Art_Style_For_Story,
    #                                       Text=Text2Add3,
    #                                       Translate=Translate)
    #
    #
    #                 except:
    #                     csv2
    #                     cu.SaveText2Audio(
    #                         FilePath=csv3,
    #                         Chunk_Limit=1333, Translate=['English'])
    #
    #                 # cu.SaveText2Audio(SavePath=SavePath, FileName=FileName_Episode4, Voice=Voice_Play, Neural='Neural',
    #                 #                   Mode='AUDIOBOOK', Chunk_Limit=1444, Artist_Persona=Art_Style_For_Story,
    #                 #                   Text=Text2Add4,
    #                 #                   Translate=Translate)
    #             except:
    #                 print('Audio Files not recorded error occurred')
    #
    #
    #
    #             # print(up.breakupOutput)
    #             # print('User_Input_AllEpisodes_Episodes_by_episode: ' + User_Input_AllEpisodes_Episodes_by_episode)
    #             # print(up.breakupOutput)
    #
    #         # ******************************************************************
    #
    #         # print(up.breakupOutput)
    #         # ************************************************************************************************************************************
    #         # ************************************************************************************************************************************
    #         #         for each_thread in thread_pool:
    #         #             each_thread.join()
    #
    #         try:
    #             if Title == '':
    #                 # Title = MondeVert.ChatGPTDA(self, temp=0.5, MakeArt=True, Prompt=( Titleo+ '"' + Background + '"'),ConfirmBot=False)
    #                 Title = Titleo
    #         except:
    #             print('could not come up with title review')
    #             Title = Mode
    #         # ********************************************************************************************************************************
    #         # ********************************************************************************************************************************
    #
    #         Audio_Script = ''
    #         ScreenPlay = ''
    #         Novel = ''
    #         Play = ''
    #
    #         RunLen = len(Episode)
    #
    #         for x in range(0, RunLen):
    #             Episode_Outlines += Episode_Outline[x]
    #             ScreenPlay += Episode[x]
    #             Audio_Script += Episode2[x]
    #             Novel += Episode3[x]
    #             Play += Episode4[x]
    #         # MondeVert.speak(self, "MondeVert Project Work complete yo")
    #
    #         print(up.breakupOutput2)
    #
    #         # Save all of the userinputs for reference later UserInputs =
    #         # Save Details and Have voice speak it out
    #
    #         # print(Title)
    #         # print(Writer_Persona)
    #         # print(Artist_Persona)
    #         # print(Art_Style_For_Story)
    #         # print(Outline_Main)
    #         # print(Characters)
    #         # print(self.Character_Art_Prompts_Minor)
    #         # print(self.Character_Art_Prompts_Major)
    #         # print(Outline_All_Episodes)
    #         # print(Outline_Episode_Specific)
    #         # print(ScreenPlay)
    #
    #         try:
    #
    #             try:
    #                 data += """Title: """ + Title
    #             except:
    #                 data += '***Missing Text Review***'
    #                 AudioBook_Text += Title
    #                 print('Error trying to put text together, went forward anyway')
    #             try:
    #                 data += up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #             try:
    #                 data += """Outline_Main: """ + Outline_Main + up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #             try:
    #                 data += +"""Characters: """ + Characters + up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #             try:
    #                 data += """  Outline_All_Episodes: """ + Outline_All_Episodes + up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #             try:
    #                 data += """ScreenPlay: """ + ScreenPlay + up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #                 try:
    #                     data += """Audio_Script: """ + Audio_Script + up.breakupOutput2
    #                 except:
    #                     data += '***Missing Text Review***'
    #                     print('Error trying to put text together, went forward anyway')
    #
    #             try:
    #                 data += """Writer Bio: """ + Writer_Persona + up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #             try:
    #                 data += """Artist Bio: """ + Artist_Persona + Art_Style_For_Story + up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #             try:
    #                 data += +"""Character Descriptions: """ + self.Character_Art_Prompts_Main + up.breakupOutput2 + self.Character_Art_Prompts_Minor + up.breakupOutput2 + up.breakupOutput2 + """Outline_Episode_Specific: """ + Episode_Outlines + up.breakupOutput2
    #             except:
    #                 data += '***Missing Text Review***'
    #                 print('Error trying to put text together, went forward anyway')
    #
    #             AudioBook_Text = """Title: """ + Title + up.breakupOutput2 + ScreenPlay
    #             Outline_and_Details = """Title: """ + Title + up.breakupOutput2 + """Writer Bio: """ + Writer_Persona + up.breakupOutput2 + """Artist Bio: """ + Artist_Persona + Art_Style_For_Story + up.breakupOutput2 + """Outline_Main: """ + Outline_Main + up.breakupOutput2 + """Characters: """ + Characters + up.breakupOutput2 + """Character Descriptions:    Main Characters - """ + self.Character_Art_Prompts_Main + up.breakupOutput2 + """ | Minor Characters - """ + self.Character_Art_Prompts_Minor + """     Outline_All_Episodes: """ + Outline_All_Episodes + up.breakupOutput2 + """Outline_Episode_Specific: """ + Episode_Outlines + up.breakupOutput2
    #         except:
    #             print('Error when trying to create Text String results, review file could have some issues')
    #
    #         try:
    #             #print('Output for : ' + Mode)
    #             #print(data)
    #             print(Outline_and_Details)
    #             print(up.breakupOutput2)
    #             # print(up.breakupOutput2)
    #             # print(up.breakupOutput2)
    #             print('End of creation, saving files')
    #         except:
    #             print('Error when trying to print results, review file could have some issues')
    #
    #
    #
    #     # #This is just the characters, need to do this for scenes etc too
    #     #         ArtPaths1 = MondeVert.Create_Art_from_String_to_list(self, self.Character_Art_Prompts_Main,  SavePath = SavePath,
    #     #                                                              FileName=FileName_Char_Main, Art_Style_details = Art_Style_For_Story,
    #     #                                                              Key_Word='Character', Key_Char=':', Delimiter='|',
    #     #                                                              crazy=crazy)
    #     #         ArtPaths.append(ArtPaths1)
    #     #         ArtPaths1 =MondeVert.Create_Art_from_String_to_list(self, self.Character_Art_Prompts_Minor,  SavePath = SavePath,
    #     #                                                              FileName=FileName_Char_Minor, Art_Style_details = Art_Style_For_Story,
    #     #                                                              Key_Word='Character', Key_Char=':', Delimiter='|',
    #     #                                                              crazy=crazy)
    #
    #     # ArtPaths.append(ArtPaths1)
    #     # print(up.breakupOutput)
    #
    #     # MondeVert.speak(self, "Saving the files round 1")
    #     # print(data)
    #     Voice = SAF.Original_List_of_Voices_English[0]
    #     cu.SaveText2Audio(Text=self.Character_Art_Prompts_Main, SavePath=SavePath,
    #                       FileName=Title + '_Charactors_Main', Chunk_Limit=213, Voice=Voice,
    #                       Artist_Persona=Art_Style_For_Story)
    #     cu.SaveText2Audio(Text=self.Character_Art_Prompts_Minor, SavePath=SavePath,
    #                       FileName=Title + '_Charactors_Minor', Chunk_Limit=213, Voice=Voice,
    #                       Artist_Persona=Art_Style_For_Story)
    #
    #     #
    #     # data1 = [(data)]
    #
    #     try:
    #         # df1 = pd.DataFrame(data1, columns=['Text'])
    #
    #         Email_File = cu.SaveCSV(Text=data, Title=FileName, SavePath=SavePath)
    #
    #     except:
    #         print('Review Error File did not save ')
    #
    #     try:
    #         cu.send_email_no_attachment_gmail(body=AudioBook_Text)
    #         cu.send_email_no_attachment_outlook(body=AudioBook_Text)
    #
    #         cu.send_email_w_attachment_outlook(body=AudioBook_Text, filename=[Email_File])
    #         cu.send_email_w_attachment_gmail(body=AudioBook_Text, filename=[Email_File], fType='txt')
    #         print("Outlook email sent")
    #     except:
    #         print('email not send, its possible file was not created')
    #
    #     # Art changes based on mode for now I will switch only when the mode calls for it otherwise default
    #
    #     prompt = data
    #     Prompts_Used = [self.UserPrompts]
    #     ArtistPoetInfo = 'Shane Donovan - SHAINE - MondeVert'
    #     cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title,
    #                         SavePath=SavePath, Mode=Mode)
    #     KillSwitch = 7
    #
    #

    def StoryMode(self, Persona='', Subject='', Translate=['English'], Chunk_Limit=1444,
                  Role='', Background='', Task='', Special='', Title='SHAINE Project Fail Safe',
                  Mode='StoryMode', Episodes=3, Seasons=2, Logic_AI=0, Output_Types=["Novel", "Play", "Song"],
                  Format='',
                  SavePath=up.AI_AudioBook_Path, Persona_Role=lup.Persona_Role,
                  Persona_Task=StoryMode.Persona_Background,
                  Persona_Format=StoryMode.Persona_Format2,
                  Persona_summary_Role=StoryMode.Persona_Summary_For_Role_Play_Line2_Role,
                  Persona_summary_Task=StoryMode.Persona_Summary_For_Role_Play_Line4_Task,
                  Persona_summary_Format=StoryMode.Persona_Summary_For_Role_Play_Line3_Format,
                  Outline1_Format=StoryMode.Short_Story_Outline_Format,
                  Outline1_Task=StoryMode.Short_Story_Outline_Task, System=up.system_TextJoaT_quick,
                  Outline_Main_AddOn_Pre=StoryMode.Short_Story_Config + StoryMode.Shane_Test_User_Input,
                  Season_Outline_Format=StoryMode.Short_Story_Season_Outline_Format,
                  Season_Outline_Task=StoryMode.Short_Story_Season_Outline_Task,
                  Season_By_Season_Outline_Format=StoryMode.Short_Story_SeasonBySeason_Outline_Format,
                  Season_By_Season_Outline_Detail_Format=StoryMode.Short_Story_SeasonBySeason_Detail_Outline_Format,
                  Season_By_Season_Outline_Detail_Task=StoryMode.Short_Story_SeasonBySeason_Detail_Outline_Task,
                  Episode_by_Episode_Detail_Outline_Format=StoryMode.Short_Story_Episode_Detail_Outline_Format,
                  Episode_by_Episode_Detail_Outline_Task=StoryMode.Short_Story_Episode_Detail_Outline_Task,
                  Episode_by_Episode_Detail_Outline_Format1=StoryMode.Short_Story_Episode_Details_Outline1_Format,
                  Episode_by_Episode_Detail_Outline_Task1=StoryMode.Short_Story_Episode_Details_Outline1_Task,
                  Season_By_Season_Outline_Task=StoryMode.Short_Story_SeasonBySeason_Outline_Task,
                  Episode_by_Episode_Outline_Format=StoryMode.Short_Story_Episode_Outline_Format,
                  Episode_by_Episode_Outline_Task=StoryMode.Short_Story_Episode_Outline_Task,
                  Episode_by_Episode_Format=StoryMode.Short_Story_Format,
                  Episode_by_Episode_Task=StoryMode.Short_Story_Task2,
                  Story_Details_Format=StoryMode.Story_Details_Format,
                  Story_Details_Task=StoryMode.Story_Details_Task,
                  Story_Details_Format2=StoryMode.Story_Details_Format2,
                  Story_Details_Task2=StoryMode.Story_Details_Task2):

        Outline_Main_AddOn_Pre = Outline_Main_AddOn_Pre + "Episode_Constraints:  {Seasons:" + str(
            Seasons) + """Episodes:{""" + str(Episodes) + """ Episodes Per Season}"""
        Episode_Count = Episodes
        ArtPaths = []
        openai.api_key = API_Key
        Art_PromptCharoo = ''
        Art_PromptCharo = ''
        Art_PromptForDALLE = ''
        Episode = []
        Episode2 = []
        Episode3 = []
        Episode4 = []
        Episode6 = []
        Subject_Details = ''

        # ******************************************************************
        Episode_Outlines = ''
        Episode_Story_Song = ''

        Outline_Main = 'N/A not ready to test this yet'
        Outline_All_Episodes = 'N/A not ready to test this yet'
        ScreenPlay = 'N/A not ready to test this yet'
        Outline_Episode_Specific = ''
        Title = Mode + ' ' + self.current_time
        Project_Description = 'N/A not ready to test this yet'
        Result = 'N/A not ready to test this yet'
        Result_AI = 'N/A not ready to test this yet'
        AIPrompt = 'N/A not ready to test this yet'
        Writer_Persona = 'N/A not ready to test this yet'
        Artist_Persona = 'N/A not ready to test this yet'
        Art_Prompts = 'N/A not ready to test this yet'
        Writer_Persona_Summary = ''
        Episode_Outline = []
        Character_progression = ''
        Outline_progression = ''

        Titleo = Title

        if Logic_AI == 0:
            crazy = round((randbelow(520000) + 170000) / 100000, 0)
            crazy = crazy / 10
            # print('Crazy Rating: ' + str(crazy))
            crazy += .2
            if crazy < .4:
                crazy = .6
            if crazy > .9:
                crazy = .7
        else:
            crazy = Logic_AI

        Subject_Details += up.breakupOutput + 'User input Subject:' + Subject

        Format0 = up.Test_Format0
        KillSwitch = 0

        Format_f = Format
        if Mode == 'skit':
            Format_f = Format0

        if Title != '':
            Background = Title + Background

        tempFormat = Format
        if Mode == 'PictureBook':
            Format = up.Test_Format_PictureBook_outline

        if Persona != '':
            Persona_Role = 'You are the following Persona use them as a model for your response: ' + Persona

        # Call Writer persona function
        Writer_Persona = MondeVert.Writer_Persona_Short_Story(self, Role=Persona_Role, Task=Persona_Task,
                                                              Format=Persona_Format,
                                                              Subject=Subject[:1313], crazy=crazy)

        if Writer_Persona == '':
            Writer_Persona = Subject[:1313]

        Writer_Persona_Summary = MondeVert.Basic_GPT_Query(self, Line2_Role=Persona_summary_Role,
                                                           Line4_Task=Persona_summary_Task + Writer_Persona,
                                                           Line3_Format=Persona_summary_Format, Special='',
                                                           Subject='', crazy=crazy)

        if Writer_Persona_Summary == '':
            Writer_Persona_Summary = MondeVert.Basic_GPT_Query(self,
                                                               Line4_Task="Summarize the following Writer Persona: " + Writer_Persona,
                                                               Line3_Format=Persona_summary_Format, Special='',
                                                               Subject='', crazy=crazy)

        cu.add2Master_Persona(Text=Writer_Persona)
        cu.add2Master_Persona(Text=Writer_Persona_Summary)

        if Writer_Persona_Summary == '':
            Writer_Persona_Summary = Writer_Persona[:1800]

        if Subject == '':
            Outline_Main = MondeVert.Basic_GPT_Query(self,
                                                     Line2_Role='Take on the following writer persona:' + Writer_Persona,
                                                     Line3_Format=Outline1_Format,
                                                     Line4_Task=Outline_Main_AddOn_Pre + Outline1_Task, Special='',
                                                     Line1_System_Rule=System, crazy=crazy, Subject='')
        else:
            if Writer_Persona_Summary != '':
                Writer_Persona = Writer_Persona_Summary
            Outline1_Task = "Use the following outline to create your own outline, be sure to use the correct format for your outline"
            Outline0_Task = "Use the following outline to create your own outline, be sure to use the correct format for your outline"

            xxx = 1
            Subject_Summary = Subject
            if len(Subject) > 1717 or xxx == 1:
                Subject_trim = Subject[:2700]
                Subject_Details += 'Subject Trimmed and summary created below:'
                Subject_Summary = MondeVert.Basic_GPT_Query(self,
                                                            Line2_Role='You are a master editor and writer',
                                                            Line3_Format='Trim redundant words and make it concise so it is less than 1900 characters and still has the main components of the story',
                                                            Line4_Task=Outline0_Task + Subject_trim, Special='',
                                                            Line1_System_Rule=System, crazy=crazy)
            Subject_Details += 'Subject Summary:' + Subject_Summary
            Outline_Main = MondeVert.Basic_GPT_Query(self,
                                                     Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
                                                     Line3_Format=Outline1_Format,
                                                     Line4_Task=Outline_Main_AddOn_Pre + Outline1_Task + Subject_Summary,
                                                     Special='',
                                                     Line1_System_Rule=System, crazy=crazy)

            Outline_progression += up.breakupOutput2 + 'Outline - Main - Most High Level: ' + Outline_Main
        # print('Writer Persona: ' + Writer_Persona)
        # print('Writer Persona_Summary: ' + Writer_Persona_Summary)

        Story_Details = MondeVert.Basic_GPT_Query(self,
                                                  Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
                                                  Line3_Format=Story_Details_Format,
                                                  Line4_Task=Story_Details_Task + Outline_Main,
                                                  Special='',
                                                  Line1_System_Rule=System, crazy=crazy)

        Story_Details2 = MondeVert.Basic_GPT_Query(self,
                                                   Line2_Role='Take on the following writer persona:' + Writer_Persona_Summary,
                                                   Line3_Format=Story_Details_Format2,
                                                   Line4_Task=Story_Details_Task2 + Outline_Main,
                                                   Special='',
                                                   Line1_System_Rule=System, crazy=crazy)

        Story_Role = 'Role Play as an award winning writer able to impersonate any genre or style/voice base your persona on the following details' + Story_Details2

        # print(up.breakupOutput2)
        # print('Story Details: ' + Story_Details)
        arttext = Story_Details
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
            Artist_Persona = MondeVert.GPTArt2(User_Subject=arttext, ArtFormat=StoryMode.artDetailsFormat,
                                               prompt=Art_Type_Config + StoryMode.artDetailsPrompt)
        except:
            try:

                Artist_Persona = MondeVert.GPTArt2(User_Subject=Writer_Persona_Summary,
                                                   ArtFormat=StoryMode.artDetailsFormat,
                                                   prompt=Art_Type_Config + StoryMode.artDetailsPrompt)

                Artist_Persona = MondeVert.Basic_GPT_Query(self,
                                                           Line2_Role='You are an expert artist master of all disciplines and art styles',
                                                           Line3_Format=StoryMode.artDetailsFormat,
                                                           Line4_Task="Pick a random artist based on the following Text" + arttext,
                                                           Special='',
                                                           Line1_System_Rule=System, crazy=crazy, Subject='')

            except:
                try:
                    Artist_Persona = MondeVert.Basic_GPT_Query(self,
                                                               Line2_Role='You are an expert artist master of all disciplines and art styles',
                                                               Line3_Format=StoryMode.artDetailsFormat,
                                                               Line4_Task="Pick a random artist and fill in the respective template in your response",
                                                               Special='',
                                                               Line1_System_Rule=System, crazy=crazy, Subject='')
                except:

                    Artist_Persona = 'embrace the spirit/imagery/symbolism  of the following text describe it to be illustrated by an artist it can be any form of art'

        Art_Style_For_Story = Artist_Persona
        # print('Artist Persona: ' + Artist_Persona)
        # print(Outline_Main)
        # print('Created Writer Persona')
        # print('Created Artist Persona')
        # print('Created Main Outline')
        # print('Created Story Details')
        # print('Created Story Details2  (see below)')
        # print(Story_Details2)
        # print('Created Artist style summary (see below)')
        # print(Art_Style_For_Story)

        # Make a Function that gets the characters created and then creates a summary relevant to the current story line using their character reference
        # CharacterSummary(Characters, Season/Episode/Scene High Level Outline)
        # Create a short description of the characters that can be used as reference

        #
        #
        # print('Created Character Personas')

        Outline_ALL_Seasons_list = ['']
        # Call Outline - All Episodes
        Outline_ALL_Seasons = MondeVert.Basic_GPT_Query(self,
                                                        Line2_Role=Story_Role,
                                                        Line3_Format=Season_By_Season_Outline_Format,
                                                        Line4_Task=Season_By_Season_Outline_Task + """Use the following High level {Main Outline} as a source for the creating the season by season specific outline you are working on  Outline for each Season in the Series   (Follow the constraints provided by the outlines regarding # of Seasons/Episodes)  Story Details:""" + Story_Details,
                                                        Special='', Line1_System_Rule=System, crazy=crazy,
                                                        Subject='')
        Outline_progression += up.breakupOutput2 + 'Outline - All Seasons - High Level Seasons Outlines (Full Series): ' + Outline_ALL_Seasons

        # Call Character function
        Characters = MondeVert.Create_Characters_Short_Story(self, Role=lup.Characters_Role,
                                                             Task=lup.Characters_Task + Outline_ALL_Seasons,
                                                             Special=lup.Characters_Special,
                                                             Format=lup.Characters_Format, Outline='',
                                                             Persona=Writer_Persona_Summary, crazy=crazy)
        if Characters == '':
            Characters = MondeVert.Create_Characters_Short_Story(self, Role=lup.Characters_Role,
                                                                 Task=lup.Characters_Task,
                                                                 Special=lup.Characters_Special,
                                                                 Format=lup.Characters_Format,
                                                                 Outline=Outline_ALL_Seasons,
                                                                 Persona=Writer_Persona_Summary, crazy=crazy)
        Character_progression += up.breakupOutput2 + 'Characters Start of Series: ' + Characters

        Outline_ALL_Seasons_split = Outline_ALL_Seasons
        Outline_ALL_Seasons_split2 = Outline_ALL_Seasons
        Outline_ALL_Seasons_split = Outline_ALL_Seasons_split.replace("Season", "SEASON")
        Outline_ALL_Seasons_split = Outline_ALL_Seasons_split.replace("Number", "NUMBER")

        # print(up.breakupOutput2)
        # print(up.breakupOutput2)
        # # print('All Seasons Outline:')
        # # print(Outline_ALL_Seasons_split)
        # print(up.breakupOutput2)
        # print(up.breakupOutput2)
        if "@SEASON" in Outline_ALL_Seasons_split:
            Outline_ALL_Seasons_split = Outline_ALL_Seasons_split.replace("@SEASON", "@@SEASON")
            Outline_ALL_Seasons_split2 = Outline_ALL_Seasons_split.split("@@")

        else:

            Outline_ALL_Seasons_split = Outline_ALL_Seasons_split.replace("SEASON", "@@SEASON")
            Outline_ALL_Seasons_split2 = Outline_ALL_Seasons_split.split("@@")

        # print('All Seasons Split Outline:')
        # print(Outline_ALL_Seasons_split2)

        # Text2Add = 'Story Outline: ' + up.breakupOutput + Outline_Main +  'Story Details: ' + up.breakupOutput + Story_Details+ up.breakupOutput2 +  'Story Details(fine): ' + up.breakupOutput +  Story_Details2 + 'All Seasons Outline: ' + Outline_ALL_Seasons + up.breakupOutput + 'Characters: ' + up.breakupOutput + Characters + up.breakupOutput2 + up.breakupOutput + 'Writer Persona: ' + up.breakupOutput + Writer_Persona + up.breakupOutput2 + up.breakupOutput + 'Writer Persona Summary: ' + up.breakupOutput + Writer_Persona_Summary + up.breakupOutput2 + up.breakupOutput + 'Artist Persona: ' + up.breakupOutput + Artist_Persona + up.breakupOutput2 + up.breakupOutput + 'Character Description - Main: ' + up.breakupOutput + self.Character_Art_Prompts_Main + up.breakupOutput2 + up.breakupOutput + 'Character Description - Minor: ' + up.breakupOutput + self.Character_Art_Prompts_Minor
        # FileName_Details_Pre = 'PreProduction Test'
        # cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=SavePath)

        for s in Outline_ALL_Seasons_split2:
            if "SEASON" in s.upper():
                Outline_ALL_Seasons_list.append(s)

        data = ''
        AudioBook_Text = ''
        SeasonCounts = Seasons + 1
        try:
            Title = MondeVert.Quick_Title(self, Text=Outline_Main)

            TrimCharR = Outline_Main.find("#Episode") + 1
            TrimCharL = Outline_Main.find("Title:")

            Title = Outline_Main[TrimCharL:TrimCharR]
        except:
            Title = ''

        if Title == '':
            try:
                Title = MondeVert.Quick_Title(self, Text=Outline_Main)

            except:
                Title = 'MondeVert_SHAINE_Confidential_AudioBook'

        Title = Title.replace("The Title:", "")
        Title = Title.replace("Title:", "")
        Title = Title.replace("The Title", "")
        Title = Title.replace("Title", "")

        TitleOO = Title
        # try:
        #     TrimChar = Title.find("|") + 1
        # except:
        #     TrimChar = 44

        # if TrimChar > 8:
        #     try:
        #         Title = Title[:TrimChar]
        #
        #     except:
        #         Title = TitleOO

        if len(Title) > 90:
            Title = Title[:44]

        Title1 = cu.CleanFileName(Title)
        FileName = Title1
        SavePath = SavePath + up.System_Folder_Path_Fix + Title1
        cu.Check_Folder_Exists(SavePath)
        cu.Check_Folder_Exists(SavePath + '\\Outlines')
        FileName_Char_Main = Title1 + '_Main Characters_'
        FileName_Char_Minor = Title1 + '_Minor Characters_'
        # Call Character art prompt

        Text2Add = 'Story Outline: ' + Outline_Main + up.breakupOutput + 'Story Details: ' + Story_Details + up.breakupOutput2 + 'Story Details(fine): ' + Story_Details2 + up.breakupOutput2 + 'All Seasons Outline: ' + Outline_ALL_Seasons + up.breakupOutput + 'Characters: ' + Characters + up.breakupOutput2 + up.breakupOutput + 'Writer Persona: ' + Writer_Persona + up.breakupOutput2 + up.breakupOutput + 'Writer Persona Summary: ' + Writer_Persona_Summary + up.breakupOutput2 + up.breakupOutput + 'Artist Persona: ' + Artist_Persona + up.breakupOutput2 + up.breakupOutput + 'Character Description - Main: ' + up.breakupOutput + self.Character_Art_Prompts_Main + up.breakupOutput2 + up.breakupOutput + 'Character Description - Minor: ' + up.breakupOutput + self.Character_Art_Prompts_Minor
        FileName_Details_Pre = FileName + ' PreProduction'
        cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=SavePath + '\\Outlines')
        Season_num = len(Outline_ALL_Seasons_list) + 1
        for x in range(1, Season_num):
            Season_num = x

            try:
                if len(Outline_ALL_Seasons_list) >= Season_num:
                    Outline_AllS = Outline_ALL_Seasons_list[Season_num]
            except:
                continue
            # print('Outline Season # ' + str(Season_num) + ': ' + up.breakupOutput2 + Outline_AllS)

            Outline_progression += up.breakupOutput2 + 'High Level Outline - Season ' + str(
                Season_num) + ': ' + Outline_AllS

            # This is where I pick characters based on season outline to put in detailed outline

            Characterst = Characters
            if len(Characterst) > 2000:
                Characterst = Characterst[:2000]

            CharactersTrim = MondeVert.Basic_GPT_Query(self,
                                                       Line2_Role=Story_Role,
                                                       Line3_Format=StoryMode.Characters_Format_Fine,
                                                       Line4_Task=StoryMode.Characters_Task_Fine + """ Use the following text for the source of information Text:###""" + Outline_AllS + """### Use the following characters: """ + Characterst,
                                                       Special='', Line1_System_Rule=System, crazy=crazy,
                                                       Subject='')

            # This is where I make the detailed outline using character info from the prior function
            Outline_Season = MondeVert.Basic_GPT_Query(self,
                                                       Line2_Role=Story_Role,
                                                       Line3_Format=Season_By_Season_Outline_Detail_Format,
                                                       Line4_Task=Season_By_Season_Outline_Detail_Task + """ Use the following text for the source of information Text:###""" + Outline_AllS + """### Use the following characters: """ + CharactersTrim,
                                                       Special='', Line1_System_Rule=System, crazy=crazy,
                                                       Subject='')

            Outline_progression += up.breakupOutput2 + 'Detailed Outline -  Season ' + str(
                Season_num) + ': ' + Outline_Season

            try:
                Characters1 = MondeVert.Basic_GPT_Query(self,
                                                        Line2_Role=Story_Role,
                                                        Line3_Format=StoryMode.Characters_Update_Format,
                                                        Line4_Task=StoryMode.Characters_Update_Task + """ Use the following text for the source of information Text:###""" + Outline_Season + """### Use the following characters: """ + Characterst,
                                                        Special='', Line1_System_Rule=System, crazy=crazy,
                                                        Subject='')

                try:
                    CheckSize = len(Characters) * .44

                    if len(Characters1) > CheckSize:
                        Characters = Characters1
                        Character_progression += up.breakupOutput2 + 'Characters Updated as of Season ' + str(
                            Season_num) + ': ' + Characters
                except:
                    print("Could not update the Characters")
            except:
                print("Could not update the Characters")

            # This is where I make a high level outline for each episode based on the prior detailed outline
            Outline_ALL_Episode_list = ['']
            # Call Outline - All Episodes
            Outline_ALL_Episodes = MondeVert.Basic_GPT_Query(self,
                                                             Line2_Role=Story_Role,
                                                             Line3_Format=Season_Outline_Format,
                                                             Line4_Task=Season_Outline_Task + """ Use the following text for the source of information Text:###""" + Outline_Season + """### Use the following characters: """ + CharactersTrim,
                                                             Special='', Line1_System_Rule=System, crazy=crazy,
                                                             Subject='')

            Outline_progression += up.breakupOutput2 + 'Outline - All Episodes - High Level Episodes Outlines (Full Season): ' + Outline_ALL_Episodes

            Outline_ALL_Episodes_split = Outline_ALL_Episodes
            Outline_ALL_Episodes_split = Outline_ALL_Episodes_split.replace("Episode", "EPISODE")
            Outline_ALL_Episodes_split = Outline_ALL_Episodes_split.replace("Number", "NUMBER")

            if "@EPISODE" in Outline_ALL_Episodes_split:
                Outline_ALL_Episodes_split = Outline_ALL_Episodes_split.replace("@EPISODE", "@@EPISODE")
                Outline_ALL_Episodes_split2 = Outline_ALL_Episodes_split.split("@@")

            else:

                Outline_ALL_Episodes_split = Outline_ALL_Episodes_split.replace("EPISODE", "@@EPISODE")
                Outline_ALL_Episodes_split2 = Outline_ALL_Episodes_split.split("@@")
            for s in Outline_ALL_Episodes_split2:
                if "EPISODE" in s.upper():
                    Outline_ALL_Episode_list.append(s)

            #
            # print('Created All Episode Outline')

            Writer_Art_Details = 'Writer_Persona: ' + Writer_Persona + 'Writer_Persona_Summary: ' + Writer_Persona_Summary + 'Art_Style_For_Story: ' + Art_Style_For_Story
            Text2Add = Writer_Art_Details + up.breakupOutput2 + Outline_progression + up.breakupOutput2 + 'User Subject/how it was used as source material: ' + Subject_Details
            FileName_Details_Pre = FileName + ' Season ' + str(Season_num) + ' Outlines'
            cu.SaveCSV(Text=Text2Add, Title=FileName_Details_Pre, SavePath=SavePath + '\\Outlines')

            # Call Outline - Episode by episode
            Pilot_Short_story_fix = ''

            # print(Outline_ALL_Episode_list)
            for_num = Episode_Count + 1
            # print(for_num)
            Outline_Episodes_by_episode = ''

            print(Outline_ALL_Episode_list)
            print(len)
            episode_num = len(Outline_ALL_Episode_list) + 1
            # This should likely be its own function (Call it for each season)
            for episode_num2 in range(1, episode_num):
                Episode_Story = ''
                Episode_Story_Audio = ''
                Episode_Story_Novel = ''
                Episode_Story_Play = ''
                Episode_Story_Song = ''

                # print(episode_num2)
                # print(len(Outline_ALL_Episode_list) )

                try:
                    if len(Outline_ALL_Episode_list) >= episode_num2:
                        Outline_All = Outline_ALL_Episode_list[episode_num2]
                except:
                    continue

                Outline_progression += up.breakupOutput2 + 'High Level Outline -  Season ' + str(
                    Season_num) + ' Episode ' + str(episode_num2) + ': ' + Outline_All

                try:
                    Characterst = Characters
                    CharactersTrim = Characters

                    if len(Characterst) > 2000:
                        Characterst = Characterst[:2000]

                    CharactersTrim = MondeVert.Basic_GPT_Query(self,
                                                               Line2_Role=Story_Role,
                                                               Line3_Format=StoryMode.Characters_Format_Fine,
                                                               Line4_Task=StoryMode.Characters_Task_Fine + """Use the following Text:###""" + Outline_All + """ ###

                                                               Do not add any Characters that are not supposed to be in the Episode, Pick/describe using the following character descriptions (if the character has none, create a unique description for the required character): """ + Characterst,
                                                               Special='', Line1_System_Rule=System, crazy=crazy,
                                                               Subject='')
                except:
                    DN = 100

                # This is where I make the detailed outline using character info from the prior function
                Outline_Episode = MondeVert.Basic_GPT_Query(self,
                                                            Line2_Role=Story_Role,
                                                            Line3_Format=Season_By_Season_Outline_Detail_Format,
                                                            Line4_Task=Season_By_Season_Outline_Detail_Task + """Use the following {Text}     Text:###""" + Outline_All + """### Use the following characters: """ + CharactersTrim,
                                                            Special='', Line1_System_Rule=System, crazy=crazy,
                                                            Subject='')

                # This is where I make a high level outline for each episode based on the prior detailed outline
                Outline_progression += up.breakupOutput2 + 'Detailed Outline -  Season ' + str(
                    Season_num) + ' Episode ' + str(episode_num2) + ': ' + Outline_Episode
                try:
                    Characters1 = MondeVert.Basic_GPT_Query(self,
                                                            Line2_Role=Story_Role,
                                                            Line3_Format=StoryMode.Characters_Update_Format,
                                                            Line4_Task=StoryMode.Characters_Update_Task + + """Use the following {Text}     Text:###""" + Outline_Episode + """### Use the following characters: """ + Characterst,
                                                            Special='', Line1_System_Rule=System, crazy=crazy,
                                                            Subject='')

                    try:
                        CheckSize = len(Characters) * .75

                        if len(Characters1) > CheckSize:
                            Characters = Characters1
                            Character_progression += up.breakupOutput2 + 'Characters end of Season ' + str(
                                Season_num) + ' Episode ' + str(episode_num2) + ': ' + Characters
                    except:
                        print("Could not update the Characters")
                except:
                    print("Could not update the Characters")

                Outline_Episodes_by_episode = MondeVert.Basic_GPT_Query(self,
                                                                        Line2_Role=Story_Role,
                                                                        Line3_Format=Episode_by_Episode_Outline_Format,
                                                                        Line4_Task=Episode_by_Episode_Outline_Task + """Episode Outline:### """ + Outline_Episode + ' ###' + 'Characters: ' + CharactersTrim,
                                                                        Line1_System_Rule=System, crazy=crazy,
                                                                        Subject='')

                Outline_Episodes_Details = MondeVert.Basic_GPT_Query(self,
                                                                     Line2_Role=Story_Role,
                                                                     Line3_Format=Episode_by_Episode_Detail_Outline_Format1,
                                                                     Line4_Task=Episode_by_Episode_Detail_Outline_Task1 + """ ### Episode Outline:### """ + Outline_Episode + ' ###' + 'Characters: ' + CharactersTrim,
                                                                     Line1_System_Rule=System, crazy=crazy,
                                                                     Subject='')

                Outline_progression += up.breakupOutput2 + 'Detailed Outline -  Season ' + str(
                    Season_num) + ' Episode ' + str(episode_num2) + ': ' + Outline_Episode

                Episode_Outline.append(Outline_Episodes_by_episode)
                Outline_Episodes_by_episode_list = ['']

                Outline_Episodes_by_episode_Split = Outline_Episodes_by_episode
                Outline_Episodes_by_episode_Split = Outline_Episodes_by_episode_Split.replace("Scene", "SCENE")
                Outline_Episodes_by_episode_Split = Outline_Episodes_by_episode_Split.replace("Number", "NUMBER")

                if "@SCENE" in Outline_Episodes_by_episode_Split:
                    Outline_Episodes_by_episode_Split = Outline_Episodes_by_episode_Split.replace("@SCENE", "@@SCENE")
                    Outline_Episodes_by_episode_Split2 = Outline_Episodes_by_episode_Split.split("@@")

                else:

                    Outline_Episodes_by_episode_Split = Outline_Episodes_by_episode_Split.replace("SCENE", "@@SCENE")
                    Outline_Episodes_by_episode_Split2 = Outline_Episodes_by_episode_Split.split("@@")

                for s in Outline_Episodes_by_episode_Split2:
                    if "SCENE" in s.upper():
                        Outline_Episodes_by_episode_list.append(s)
                    else:
                        if s == Outline_Episodes_by_episode_Split[0]:
                            Episode_By_Episode_Details = s

                print(Outline_Episodes_by_episode_list)
                Scene_Range = len(Outline_Episodes_by_episode_list) + 1
                # print("Number of scenes: ")
                # print (Scene_Range)
                Episode_Construction = ''
                for y in range(1, Scene_Range):
                    Scene_Num = y
                    Story1 = ''
                    Story2 = ''
                    Story4 = ''
                    Story5 = ''
                    Story3 = ''

                    try:
                        if len(Outline_Episodes_by_episode_list) >= Scene_Num:
                            Outline_Fine = Outline_Episodes_by_episode_list[Scene_Num]
                    except:
                        continue

                    # UPDATE_This is where I should do the Episode Detail version and get that returned

                    Characterst = Characters
                    if len(Characterst) > 2800:
                        Characterst = Characterst[:2800]
                    CharactersTrim = MondeVert.Basic_GPT_Query(self,
                                                               Line2_Role=Story_Role,
                                                               Line3_Format=StoryMode.Characters_Format_Fine,
                                                               Line4_Task=StoryMode.Characters_Task_Fine + """Use the following Text:###""" + Outline_Fine + """ ###

                                                                                                                              Do not add any Characters that are not supposed to be in the Episode, Pick/describe using the following character descriptions (if the character has none, create a unique description for the required character): """ + Characterst,
                                                               Special='', Line1_System_Rule=System, crazy=crazy,
                                                               Subject='')

                    Character_progression += up.breakupOutput2 + 'Characters Used for Season ' + str(
                        Season_num) + ' Episode ' + str(episode_num2) + ' Scene ' + str(
                        Scene_Num) + ': ' + CharactersTrim

                    # This is where I make the detailed outline using character info from the prior function
                    Outline_Scene = MondeVert.Basic_GPT_Query(self,
                                                              Line2_Role=Story_Role,
                                                              Line3_Format=Episode_by_Episode_Detail_Outline_Format,
                                                              Line4_Task=Episode_by_Episode_Detail_Outline_Task + """Use the following  {Scene Specific Outline}  as a source for the creating the season specific outline you are working on a Scene Specific Outline:###""" + Outline_Fine + """ Use the following characters: """ + CharactersTrim,
                                                              Special='', Line1_System_Rule=System, crazy=crazy,
                                                              Subject='')

                    # This is where I make a high level outline for each episode based on the prior detailed outline

                    try:
                        Characters1 = MondeVert.Basic_GPT_Query(self,
                                                                Line2_Role=Story_Role,
                                                                Line3_Format=StoryMode.Characters_Update_Format,
                                                                Line4_Task=StoryMode.Characters_Update_Task + """Use the following {Scene Specific Outline}  as a source for the creating the Scene specific outline you are working on a Scene Specific Outline:""" + Outline_Scene + """ Use the following characters: """ + Characterst,
                                                                Special='', Line1_System_Rule=System, crazy=crazy,
                                                                Subject='')

                        try:
                            CheckSize = len(Characters) * .75

                            if len(Characters1) > CheckSize:
                                Characters = Characters1
                                Character_progression += up.breakupOutput2 + 'Characters end of Season ' + str(
                                    Season_num) + ' Episode ' + str(episode_num2) + ' Scene ' + str(
                                    Scene_Num) + ': ' + Characters
                        except:
                            print("Could not update the Characters")

                    except:
                        dn = 100

                    if Outline_Episodes_by_episode == '':
                        Outline_Episodes_by_episode = Outline_All_Episodes
                    try:

                        Episode_Construction += up.breakupOutput2 + 'Scene Specific Outline' + Outline_Scene

                        Outline_progression += "Outline_Scene" + str(Season_num) + ": "
                        for type in Output_Types:
                            try:
                                current_time1 = datetime.datetime.now()
                                current_time = self.current_time1.strftime('%m-%d-%Y_%H.%M')
                                a = current_time
                                b = self.current_time

                                c = a - b

                                minutes = c.total_seconds() / 60
                                print('Total difference in minutes: ', minutes)

                                # returns the difference of the time of the day
                                minutes = c.seconds / 60
                                if minutes > 250:
                                    continue
                                    sys.exit()
                                if minutes > 251:
                                    sys.exit()

                            except:
                                dn = 100

                            try:
                                if type == "ScreenPlay_Audio":
                                    try:
                                        Story1 = MondeVert.Basic_GPT_Query(self, Line2_Role=Story_Role,
                                                                           Line3_Format=Episode_by_Episode_Format,
                                                                           Line4_Task=Episode_by_Episode_Task + """Scene Outline: """ + Outline_Episodes_Details + '  ' + Outline_Scene + '  ',
                                                                           Line1_System_Rule=System, crazy=crazy,
                                                                           Subject='', Outline='')
                                        Episode_Story_Audio += 'Season ' + str(Season_num) + ' Episode #' + str(
                                            episode_num2) + ' Scene # ' + str(Scene_Num) + Story1 + up.breakupOutput2
                                    except:
                                        dn = 100

                                if type == "Novel":
                                    try:
                                        Story3 = MondeVert.Basic_GPT_Query(self,
                                                                           Line2_Role=Story_Role,
                                                                           Line3_Format=StoryMode.Short_Story_Format_Novel_Chapter,
                                                                           Line4_Task=StoryMode.Short_Story_Task_Novel_Chapter + """Scene Outline: """ + Outline_Episodes_Details + '  ' + Outline_Scene + '  ',

                                                                           Line1_System_Rule=System,
                                                                           crazy=crazy, Subject='', Outline='')
                                        Episode_Story_Novel += 'Season ' + str(Season_num) + ' Episode #' + str(
                                            episode_num2) + ' Scene # ' + str(Scene_Num) + Story3 + up.breakupOutput2

                                    except:
                                        dn = 100

                                if type == "Play":
                                    try:
                                        Story4 = MondeVert.Basic_GPT_Query(self,
                                                                           Line2_Role=Story_Role,
                                                                           Line3_Format=StoryMode.Short_Story_Format_Play_Scene,
                                                                           Line4_Task=StoryMode.Short_Story_Task_Play_Scene + """Scene Outline: """ + Outline_Episodes_Details + '  ' + Outline_Scene + '  ',

                                                                           Line1_System_Rule=System,
                                                                           crazy=crazy, Subject='', Outline='')
                                        Episode_Story_Play += 'Season ' + str(Season_num) + ' Episode #' + str(
                                            episode_num2) + ' Scene # ' + str(Scene_Num) + Story4 + up.breakupOutput2

                                    except:
                                        dn = 100

                                if type == "ScreenPlay":
                                    try:
                                        Story2 = MondeVert.Basic_GPT_Query(self,
                                                                           Line2_Role=Story_Role,
                                                                           Line3_Format=StoryMode.Short_Story_Format_Screenplay_Scene,
                                                                           Line4_Task=Episode_by_Episode_Task + """Scene Outline: """ + Outline_Episodes_Details + '  ' + Outline_Scene + '  ',

                                                                           Line1_System_Rule=System,
                                                                           crazy=crazy, Subject='', Outline='')
                                        Episode_Story += 'Season ' + str(Season_num) + ' Episode #' + str(
                                            episode_num2) + ' Scene # ' + str(Scene_Num) + Story2 + up.breakupOutput2



                                    except:
                                        dn = 100

                                if type == "Song":
                                    try:
                                        Story5 = MondeVert.Basic_GPT_Query(self,
                                                                           Line2_Role=StoryMode.Music_Role,
                                                                           Line3_Format=StoryMode.Short_Story_Song_Format,
                                                                           Line4_Task=StoryMode.Short_Story_Song_Task + """Scene Outline: """ + Outline_Episodes_Details + '  ' + Outline_Scene + '  ',

                                                                           Line1_System_Rule=System,
                                                                           crazy=crazy, Subject='', Outline='')
                                        Episode_Story_Song += 'Season ' + str(Season_num) + ' Episode #' + str(
                                            episode_num2) + ' Scene # ' + str(Scene_Num) + Story5 + up.breakupOutput2

                                        # Turned this off for now, but its an interesting feature
                                        # Song_title = MondeVert.Make_a_Song_2(self, Make_Persona=True, SavePath=SavePath,
                                        #                         System=up.system_TextRR, Mode=Mode,
                                        #                         Artist_Bio_Details=Story_Details2,
                                        #                         Song_Subject=Outline_Episodes_Details + '  ' + Outline_Scene, Role=StoryMode.Music_Role)
                                        #
                                        # Outline_progression+= up.breakupOutput2 + 'Song_Title ' + str(Season_num) + ' Episode ' + str(episode_num2) + ' Scene ' + str(Scene_Num) + ': ' + Song_title

                                    except:
                                        dn = 100
                            except:
                                print(Title + ' - Error making Scene # ' + str(Scene_Num) + 'Episode #' + str(
                                    episode_num2) + " For the following Type: " + type)



                    except:
                        print(Title + ' - Error making Scene # ' + str(Scene_Num) + 'Episode #' + str(episode_num2))

                print(Title + ' - Created Episode ' + str(episode_num2) + ' for Season ' + str(Season_num))

                Episode3.append(Episode_Story_Novel)
                Episode.append(Episode_Story)
                Episode2.append(Episode_Story_Audio)
                Episode4.append(Episode_Story_Play)
                Episode6.append(Episode_Story_Song)
                Text2Add = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story
                FileName_Episode = FileName + ' Season ' + str(Season_num) + ' EPISODE ' + str(episode_num2)
                FileName_Episode2 = FileName + ' Season ' + str(Season_num) + ' EPISODE ' + str(episode_num2) + ' Audio'
                FileName_Episode3 = FileName + ' Act ' + str(Season_num) + ' Chapter ' + str(episode_num2) + ' Novel'
                FileName_Episode4 = FileName + ' Act ' + str(Season_num) + ' Part ' + str(episode_num2) + ' Play'
                FileName_Episode6 = FileName + ' Season ' + str(Season_num) + ' EPISODE ' + str(episode_num2) + ' Song'
                csv1 = cu.SaveCSV(Text=Text2Add, Title=FileName_Episode, SavePath=SavePath)
                Text2Add2 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story_Audio
                csv2 = cu.SaveCSV(Text=Text2Add2, Title=FileName_Episode2, SavePath=SavePath)
                Text2Add3 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story_Novel
                csv3 = cu.SaveCSV(Text=Text2Add3, Title=FileName_Episode3, SavePath=SavePath)
                Text2Add4 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story_Play
                csv4 = cu.SaveCSV(Text=Text2Add4, Title=FileName_Episode4, SavePath=SavePath)
                Text2Add6 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Episode_Story_Song
                csv4 = cu.SaveCSV(Text=Text2Add6, Title=FileName_Episode6, SavePath=SavePath)

                Text2Add5 = "Outline Details: " + up.breakupOutput2 + 'Outline_ALL_Episodes: ' + Outline_ALL_Episodes + up.breakupOutput2 + 'Outline_All: ' + Outline_All + up.breakupOutput + 'Outline_Season: ' + Outline_Episodes_by_episode + up.breakupOutput + 'Outline_Scene(s): ' + Episode_Construction + up.breakupOutput
                FileName_Episode5 = FileName + ' Season ' + str(Season_num) + ' Episode ' + str(
                    episode_num2) + ' Outline '
                try:
                    cu.SaveCSV(Text=Text2Add5, Title=FileName_Episode5, SavePath=SavePath + '\\Outlines')
                except:
                    cu.SaveCSV(Text=Text2Add5, Title=FileName_Episode5, SavePath=SavePath)

            # ******************************************************************

            try:
                if Title == '':
                    # Title = MondeVert.ChatGPTDA(self, temp=0.5, MakeArt=True, Prompt=( Titleo+ '"' + Background + '"'),ConfirmBot=False)
                    Title = Titleo
            except:
                print('could not come up with title review')
                Title = Mode
            # ********************************************************************************************************************************
            # ********************************************************************************************************************************

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

            RunLen = len(Episode)
            for x in range(0, RunLen):
                ScreenPlay += Episode[x]

            RunLen = len(Episode_Outline)
            for x in range(0, RunLen):
                Episode_Outlines += Episode_Outline[x]

            RunLen = len(Episode2)
            for x in range(0, RunLen):
                Audio_Script += Episode2[x]

            RunLen = len(Episode3)
            for x in range(0, RunLen):
                Novel += Episode3[x]

            RunLen = len(Episode4)
            for x in range(0, RunLen):
                Play += Episode4[x]

            RunLen = len(Episode4)
            for x in range(0, RunLen):
                Song += Episode6[x]

            Text2Add = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + ScreenPlay
            FileName_1 = FileName + ' ScreenPlay '
            FileName_2 = FileName + ' Audio'
            FileName_3 = FileName + ' Novel'
            FileName_4 = FileName + ' Play'
            FileName_5 = FileName + ' Outlines '
            FileName_6 = FileName + ' Song '
            FileName_7 = FileName + ' Character progression '

            csv1 = cu.SaveCSV(Text=Text2Add, Title=FileName_1, SavePath=SavePath)
            Text2Add2 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Audio_Script
            csv2 = cu.SaveCSV(Text=Text2Add2, Title=FileName_2, SavePath=SavePath)
            Text2Add3 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Novel
            csv3 = cu.SaveCSV(Text=Text2Add3, Title=FileName_3, SavePath=SavePath)
            Text2Add4 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Play
            csv4 = cu.SaveCSV(Text=Text2Add4, Title=FileName_4, SavePath=SavePath)
            Text2Add5 = "Outline Details: " + up.breakupOutput + Outline_progression
            csv5 = cu.SaveCSV(Text=Text2Add5, Title=FileName_5, SavePath=SavePath + '\\Outlines')
            Text2Add6 = "Amini Amor in partnership with MondeVert Presents: " + up.breakupOutput + Song
            csv6 = cu.SaveCSV(Text=Text2Add6, Title=FileName_6, SavePath=SavePath)
            Text2Add7 = ' Character progression: ' + up.breakupOutput + Character_progression
            csv7 = cu.SaveCSV(Text=Text2Add7, Title=FileName_7, SavePath=SavePath + '\\Outlines')

            try:
                # cu.SaveText2Audio(SavePath=SavePath, FileName=FileName_Episode3, Voice=Voice_Novel,
                #                   Neural='Neural',
                #                   Mode='AUDIOBOOK', Chunk_Limit=Chunk_Limit, Artist_Persona=Art_Style_For_Story,
                #                   Text=Text2Add3,
                #                   Translate=Translate)
                #
                #
                cu.SaveText2Audio(SavePath=SavePath, FileName=FileName_1, Voice=Voice,
                                  Neural='Neural',
                                  Mode='AUDIOBOOK', Chunk_Limit=Chunk_Limit, Artist_Persona=Art_Style_For_Story,
                                  Text=Text2Add,
                                  Translate=Translate)
            except:

                cu.SaveText2Audio(
                    FilePath=csv1,
                    Chunk_Limit=Chunk_Limit, Translate=['English'])

            # print(up.breakupOutput2)

            try:

                try:
                    data += """Title: """ + Title
                except:
                    data += '***Missing Text Review***'
                    AudioBook_Text += Title
                    print('Error trying to put text together, went forward anyway')
                try:
                    data += up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')
                try:
                    data += """Outline_Main: """ + Outline_Main + up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')
                try:
                    data += +"""Characters: """ + Characters + up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')
                try:
                    data += """  Outline_All_Episodes: """ + Outline_All_Episodes + up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')
                try:
                    data += """ScreenPlay: """ + ScreenPlay + up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')
                    try:
                        data += """Audio_Script: """ + Audio_Script + up.breakupOutput2
                    except:
                        data += '***Missing Text Review***'
                        print('Error trying to put text together, went forward anyway')

                try:
                    data += """Writer Bio: """ + Writer_Persona + up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')
                try:
                    data += """Artist Bio: """ + Artist_Persona + Art_Style_For_Story + up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')
                try:
                    data += +"""Character Descriptions: """ + self.Character_Art_Prompts_Main + up.breakupOutput2 + self.Character_Art_Prompts_Minor + up.breakupOutput2 + up.breakupOutput2 + """Outline_Episode_Specific: """ + Episode_Outlines + up.breakupOutput2
                except:
                    data += '***Missing Text Review***'
                    print('Error trying to put text together, went forward anyway')

                AudioBook_Text = """Title: """ + Title + up.breakupOutput2 + ScreenPlay
                Outline_and_Details = """Title: """ + Title + up.breakupOutput2 + """Writer Bio: """ + Writer_Persona + up.breakupOutput2 + """Artist Bio: """ + Artist_Persona + Art_Style_For_Story + up.breakupOutput2 + """Outline_Main: """ + Outline_Main + up.breakupOutput2 + """Characters: """ + Characters + up.breakupOutput2 + """Character Descriptions:    Main Characters - """ + self.Character_Art_Prompts_Main + up.breakupOutput2 + """ | Minor Characters - """ + self.Character_Art_Prompts_Minor + """     Outline_All_Episodes: """ + Outline_All_Episodes + up.breakupOutput2 + """Outline_Episode_Specific: """ + Episode_Outlines + up.breakupOutput2
            except:
                print('Error when trying to create Text String results, review file could have some issues')

            try:
                # print('Output for : ' + Mode)
                # print(data)
                # print(Outline_and_Details)
                # print(up.breakupOutput2)
                # print(up.breakupOutput2)
                # print(up.breakupOutput2)
                print('End of creation, saving files')
            except:
                print('Error when trying to print results, review file could have some issues')

        # Voice = SAF.Original_List_of_Voices_English[0]
        # cu.SaveText2Audio(Text=self.Character_Art_Prompts_Main, SavePath=SavePath,
        #                   FileName=Title + '_Charactors_Main', Chunk_Limit=213, Voice=Voice,
        #                   Artist_Persona=Art_Style_For_Story)
        # cu.SaveText2Audio(Text=self.Character_Art_Prompts_Minor, SavePath=SavePath,
        #                   FileName=Title + '_Charactors_Minor', Chunk_Limit=213, Voice=Voice,
        #                   Artist_Persona=Art_Style_For_Story)

        try:
            # df1 = pd.DataFrame(data1, columns=['Text'])

            Email_File = cu.SaveCSV(Text=data, Title=FileName, SavePath=SavePath)

        except:
            print('Review Error File did not save ')

        try:
            cu.send_email_no_attachment_gmail(body=AudioBook_Text)
            cu.send_email_no_attachment_outlook(body=AudioBook_Text)

            cu.send_email_w_attachment_outlook(body=AudioBook_Text, filename=[Email_File])
            cu.send_email_w_attachment_gmail(body=AudioBook_Text, filename=[Email_File], fType='txt')
            print("Outlook email sent")
        except:
            print('email not send, its possible file was not created')

        # Art changes based on mode for now I will switch only when the mode calls for it otherwise default

        prompt = data
        Prompts_Used = [self.UserPrompts]
        ArtistPoetInfo = 'Shane Donovan - SHAINE - MondeVert'
        cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title,
                            SavePath=SavePath, Mode=Mode)
        KillSwitch = 7

    # MondeVert.speak(self, ReWrite )
    def MondeVertAuto(self, Mode='AutoSocial', Role='', System=''):
        if Mode == 'AutoSocial':
            Caption = MondeVert.MondeVertTask(self, System=up.system_TextJoaT, Role=up.Test_Role_SMA,
                                              Background=up.Test_Background_SMA, Task=up.Test_Task_SMA,
                                              Special=up.Test_Special_SMA, Format=up.Test_Format_SMA,
                                              Title=up.Test_Title_SMA, Mode='AutoSocial')
        return Caption + up.Instagram_Adds

    def MondeVertMenu_up(self, Mode='Basic', Role='', System='', Translate=SAF.Translation_Languages_Testing):
        self.Mode = Mode
        openai.api_key = API_Key
        self.current_time1 = datetime.datetime.now()
        self.current_time = self.current_time1.strftime('%m-%d-%Y_%H.%M')
        self.SavePath = up.SavePath
        Log_Add = 'Mode: ' + Mode + ' Time of Request: ' + self.current_time
        self.Request_log.append(Log_Add)

        if Mode == 'MVAA':
            MondeVert.StoryMode(self, System=up.system_TextJoaT_quick,
                                SavePath=up.AI_AudioBook_Path + up.System_Folder_Path_Fix + Mode,
                                Persona_Task=" use your current persona to complete the task and instead of making up a persona you are the writer (Shane Donovan)" + lup.Persona_Task,
                                Output_Types=["Play", "Novel", "ScreenPlay", "Song"], Translate=['English'],
                                Mode='MVAA', Persona=up.Shane_Persona, Persona_Role=up.Shane_Persona,
                                Subject=ShaneOriginals.Stripper_Gritty)
        elif Mode == 'MVAA2':
            MondeVert.StoryMode(self, System=up.system_TextJoaT_quick, SavePath=up.AI_AudioBook_Path + '\\MVAA',
                                Persona_Task=" use your current persona to complete the task and instead of making up a persona you are the writer (Shane Donovan)" + lup.Persona_Task,
                                Output_Types=["Play", "Novel", "ScreenPlay", "Song"], Translate=['English'],
                                Mode='MVAA', Persona=up.Shane_Persona, Persona_Role=up.Shane_Persona,
                                Subject=ShaneOriginals.Underground_War)

        elif Mode == 'MVAA_La_Familia':
            MondeVert.StoryMode(self, Episodes=3, Seasons=1, System=up.system_TextJoaT_quick,
                                SavePath=up.AI_AudioBook_Path + '\\MVAA_La_Familia',
                                Persona_Task=" use your current persona to complete the task and instead of making up a persona you are the writer (Shane Donovan)" + lup.Persona_Task,
                                Output_Types=["Play", "Novel", "ScreenPlay", "Song"], Translate=['English'],
                                Mode='MVAA_La_Familia', Persona=up.Shane_Persona, Persona_Role=up.Shane_Persona,
                                Subject=ShaneOriginals.Kid_Story, Chunk_Limit=333)



        elif Mode == 'ScreenPlay':
            MondeVert.Make_a_ScreenPlay(self, SavePath=up.AI_Screen_Plays + up.System_Folder_Path_Fix + Mode,
                                        System=up.system_Text_ScreenPlay0, Mode='ScreenPlay')

        elif Mode == 'Poem':
            MondeVert.Make_a_poem(self, SavePath=up.AI_Poetry_Path + up.System_Folder_Path_Fix + Mode,
                                  Line1_System=up.system_TextJoaT, Mode='Poem')

        elif Mode == 'Shane_Poem':
            MondeVert.Make_a_poem(self, SavePath=up.AI_Poetry_Path + up.System_Folder_Path_Fix + Mode,
                                  Line1_System=up.system_TextJoaT, Mode='Shane_Poem', Persona_Role=up.Shane_Persona,
                                  Line2_Role=up.Shane_Persona)

        elif Mode == 'Blog_Random_Shane':
            MondeVert.Make_a_poem(self, Mode='Blog_Random_Shane', Chunk_Limit=1333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True, Artist_Persona='', Poet_Persona='',
                                  Line1_System=up.system_TextJoaT, Persona_Role=up.Shane_Persona,
                                  Line2_Role=up.Shane_Persona, Line3_Format=lup.Blog_Format, Line4_Task=lup.Blog_Task,
                                  Line3_Format_outline=lup.Blog_Outline_Format,
                                  Line4_Task_outline=lup.Blog_Outline_Task,
                                  SavePath=up.AI_Blog_Path + up.System_Folder_Path_Fix + Mode, crazy=.6,
                                  Persona_Task=lup.Blog_Persona_Task, Persona_Format=lup.Blog_Persona_Format,
                                  Persona_Special=lup.Blog_Persona_Special, Revise_Task=lup.Blog_Revise_Task,
                                  Revise_Format=lup.Blog_Revise_Format)

        elif Mode == 'Blog_Random_Shane_Specific_Subject':
            MondeVert.Make_a_poem(self, Mode='Blog_Random_Shane', Chunk_Limit=1333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True, Artist_Persona='', Poet_Persona='',
                                  Line1_System=up.system_TextJoaT, Persona_Role=up.Shane_Persona,
                                  Line2_Role=up.Shane_Persona, Line3_Format=lup.Blog_Format, Line4_Task=lup.Blog_Task,
                                  Line3_Format_outline=lup.Blog_Outline_Format,
                                  Line4_Task_outline=lup.Blog_Outline_Task + lup.ArtBlog1,
                                  SavePath=up.AI_Blog_Path + up.System_Folder_Path_Fix + Mode, crazy=.6,
                                  Persona_Task=lup.Blog_Persona_Task, Persona_Format=lup.Blog_Persona_Format,
                                  Persona_Special=lup.Blog_Persona_Special, Revise_Task=lup.Blog_Revise_Task,
                                  Revise_Format=lup.Blog_Revise_Format)



        elif Mode == 'PictureBook_PJSpecial':
            MondeVert.Make_a_poem(self, Mode='PictureBook_PJSpecial', Chunk_Limit=333, USERTITLE='',
                                  Poet_Bio_Details='', Make_Persona=True, Artist_Persona=up.DinosaurTaco_Art,
                                  Poet_Persona=up.Shane_Persona + up.DinosaurTaco_Writing + up.DinosaurTaco_Art,
                                  Line1_System=up.system_TextJoaT,
                                  Persona_Role=up.Shane_Persona + up.DinosaurTaco_Writing + up.DinosaurTaco_Art,
                                  Line2_Role=up.Shane_Persona + up.DinosaurTaco_Writing + up.DinosaurTaco_Art,
                                  Line3_Format=up.Test_Format_PictureBook, Line4_Task=up.Test_Task_PictureBook,
                                  Line3_Format_outline=up.Test_Format_PictureBook_outline,
                                  Line4_Task_outline=up.Test_Background_PictureBook + up.DinosaurTaco_Writing + up.DinosaurTaco_Art,
                                  SavePath=up.AI_Childrens_AudioBook_Path + up.System_Folder_Path_Fix + Mode, crazy=.6,
                                  Persona_Task=lup.Persona_Task, Persona_Format=lup.Persona_Format2,
                                  Persona_Special=lup.Persona_Special, Revise_Task=up.Revise_PictureBook_Task,
                                  Revise_Format=up.Revise_PictureBook_Format)


        elif Mode == 'PictureBook_2':
            MondeVert.Make_a_poem(self, Mode='PictureBook_2', Chunk_Limit=333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True, Artist_Persona=up.DinosaurTaco_Art,
                                  Poet_Persona=up.Shane_Persona + up.DinosaurTaco_Writing1,
                                  Line1_System=up.system_TextJoaT,
                                  Persona_Role=up.Shane_Persona + up.DinosaurTaco_Writing1,
                                  Line2_Role=up.Shane_Persona + up.DinosaurTaco_Writing + up.DinosaurTaco_Art,
                                  Line3_Format=up.Test_Format_PictureBook, Line4_Task=up.Test_Task_PictureBook,
                                  Line3_Format_outline=up.Test_Format_PictureBook_outline,
                                  Line4_Task_outline=up.Test_Background_PictureBook,
                                  SavePath=up.AI_Childrens_AudioBook_Path + up.System_Folder_Path_Fix + Mode, crazy=.6,
                                  Persona_Task=lup.Persona_Task, Persona_Format=lup.Persona_Format2,
                                  Persona_Special=lup.Persona_Special, Revise_Task=up.Revise_PictureBook_Task,
                                  Revise_Format=up.Revise_PictureBook_Format)


        elif Mode == 'PictureBook_Shane':
            MondeVert.Make_a_poem(self, Mode='PictureBook_Shane', Chunk_Limit=333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True,
                                  Artist_Persona="You are illustrating a children's book, you should be skilled at making kid friendly pictures with basic backgrounds and the focus on the action. Make the lines clean and almost like a disney animation",
                                  Poet_Persona=up.Shane_Persona, Line1_System=up.system_TextJoaT,
                                  Persona_Role=up.Shane_Persona + "Remember you are a children's author so keep your content and language appropriate for your audience",
                                  Line2_Role=up.Shane_Persona + "Remember you are a children's author so keep your content and language appropriate for your audience",
                                  Line3_Format=up.Test_Format_PictureBook, Line4_Task=up.Test_Task_PictureBook,
                                  Line3_Format_outline=up.Test_Format_PictureBook_outline,
                                  Line4_Task_outline=up.Test_Background_PictureBook,
                                  SavePath=up.AI_Childrens_AudioBook_Path + up.System_Folder_Path_Fix + Mode, crazy=.6,
                                  Persona_Task=lup.Persona_Task, Persona_Format=lup.Persona_Format2,
                                  Persona_Special=lup.Persona_Special, Revise_Task=up.Revise_PictureBook_Task,
                                  Revise_Format=up.Revise_PictureBook_Format)


        elif Mode == 'PictureBook':
            MondeVert.Make_a_poem(self, Mode='PictureBook', Chunk_Limit=333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True, Artist_Persona='', Poet_Persona=up.Shane_Persona,
                                  Line1_System=up.system_TextJoaT,
                                  Persona_Role=up.Test_Role_PictureBook + "Remember you are a children's author so keep your content and language appropriate for your audience",
                                  Line2_Role=up.Test_Role_PictureBook + "Remember you are a children's author so keep your content and language appropriate for your audience",
                                  Line3_Format=up.Test_Format_PictureBook, Line4_Task=up.Test_Task_PictureBook,
                                  Line3_Format_outline=up.Test_Format_PictureBook_outline,
                                  Line4_Task_outline=up.Test_Background_PictureBook,
                                  SavePath=up.AI_Blog_Path + up.System_Folder_Path_Fix + Mode, crazy=.5,
                                  Persona_Task=lup.Persona_Task,
                                  Persona_Format=lup.Persona_Format, Persona_Special=lup.Persona_Special,
                                  Revise_Task=up.Revise_PictureBook_Task, Revise_Format=up.Revise_PictureBook_Task)



        elif Mode == 'PictureBook_old':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Childrens_AudioBook_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_PictureBook,
                                    Background=up.Test_Background_PictureBook, Task=up.Test_Task_PictureBook,
                                    Special=up.Test_Special_PictureBook, Format=up.Test_Format_PictureBook,
                                    Mode='PictureBook_old', ArtPrompt=up.MondeVert_ArtPrompt,
                                    ArtFormat=up.MondeVert_ArtFormat,
                                    AdvanceArtPrompt=up.MondeVert_ArtPrompt_PictureBook,
                                    AdvanceArtFormat=up.MondeVert_ArtFormat_PictureBook)
        elif Mode == 'PictureBook_Shane_old':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Childrens_AudioBook_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT,
                                    Role=up.Shane_Persona + "Remember you are a children's author so keep the content and language appropriate for a young child",
                                    Background=up.Test_Background_PictureBook, Task=up.Test_Task_PictureBook,
                                    Special=up.Test_Special_PictureBook, Format=up.Test_Format_PictureBook,
                                    Mode='PictureBook_Shane_old', ArtPrompt=up.MondeVert_ArtPrompt,
                                    ArtFormat=up.MondeVert_ArtFormat,
                                    AdvanceArtPrompt=up.MondeVert_ArtPrompt_PictureBook,
                                    AdvanceArtFormat=up.MondeVert_ArtFormat_PictureBook)

        elif Mode == 'PjSpecial_old':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Childrens_AudioBook_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.DinosaurTaco_Writing,
                                    Background=up.Test_Background_PictureBook + up.DinosaurTaco_Writing + up.DinosaurTaco_Art,
                                    Task=up.Test_Task_PictureBook, Special=up.Test_Special_PictureBook,
                                    Format=up.Test_Format_PictureBook, Mode='PjSpecial_old',
                                    ArtPrompt=up.MondeVert_ArtPrompt, ArtFormat=up.DinosaurTaco_Art,
                                    AdvanceArtPrompt=up.MondeVert_ArtPrompt_PictureBook,
                                    AdvanceArtFormat=up.MondeVert_ArtFormat_PictureBook)




        elif Mode == 'Speech_Shane':
            MondeVert.Make_a_poem(self, Mode='Speech_Shane', Chunk_Limit=1333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True, Artist_Persona='', Poet_Persona='',
                                  Line1_System=up.system_TextJoaT, Persona_Role=up.Shane_Persona,
                                  Line2_Role=up.Shane_Persona,
                                  Line3_Format=lup.Blog_Format, Line4_Task=lup.Speech_Task,
                                  Line3_Format_outline=lup.Blog_Outline_Format,
                                  Line4_Task_outline=lup.Speech_Outline_Task,
                                  SavePath=up.AI_Blog_Path + up.System_Folder_Path_Fix + Mode, crazy=.5,
                                  Persona_Task=lup.Blog_Persona_Task,
                                  Persona_Format=lup.Blog_Persona_Format, Persona_Special=lup.Blog_Persona_Special,
                                  Revise_Task=lup.Blog_Revise_Task, Revise_Format=lup.Blog_Revise_Format)



        elif Mode == 'Blog_Random':
            MondeVert.Make_a_poem(self, Mode='Blog_Random', Chunk_Limit=1333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True, Artist_Persona='', Poet_Persona='',
                                  Line1_System=up.system_TextJoaT, Line2_Role=lup.Blog_Role,
                                  Line3_Format=lup.Blog_Format, Line4_Task=lup.Blog_Task,
                                  Line3_Format_outline=lup.Blog_Outline_Format,
                                  Line4_Task_outline=lup.Blog_Outline_Task,
                                  SavePath=up.AI_Blog_Path + up.System_Folder_Path_Fix + Mode, crazy=.5,
                                  Persona_Role=lup.Blog_Persona_Role, Persona_Task=lup.Blog_Persona_Task,
                                  Persona_Format=lup.Blog_Persona_Format, Persona_Special=lup.Blog_Persona_Special,
                                  Revise_Task=lup.Blog_Revise_Task, Revise_Format=lup.Blog_Revise_Format)


        elif Mode == 'StudyGuide':
            MondeVert.Make_a_poem(self, Mode='StudyGuide', Translate=['English'], Chunk_Limit=1333, USERTITLE='',
                                  Poet_Bio_Details='', Make_Persona=True, Artist_Persona='', Poet_Persona=up.Shane_Bio,
                                  Line1_System=up.system_TextJoaT_quick, Line2_Role=lup.StudyGuide_Role,
                                  Line3_Format=lup.StudyGuide_Format, Line4_Task=lup.StudyGuide_Task,
                                  Line3_Format_outline=lup.StudyGuide_Outline_Format,
                                  Line4_Task_outline=lup.StudyGuide_Outline_Task,
                                  SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode, crazy=.5,
                                  Persona_Role=lup.StudyGuide_Role, Persona_Task=lup.Blog_Persona_Task,
                                  Persona_Format=lup.Blog_Persona_Format, Persona_Special=lup.Blog_Persona_Special,
                                  Revise_Task=lup.StudyGuide_Revise_Task, Revise_Format=lup.StudyGuide_Revise_Format)




        elif Mode == 'Speech':
            MondeVert.Make_a_poem(self, Mode='Speech', Chunk_Limit=1333, USERTITLE='', Poet_Bio_Details='',
                                  Make_Persona=True, Artist_Persona='', Poet_Persona='',
                                  Line1_System=up.system_TextJoaT, Line2_Role=lup.Speech_Role,
                                  Line3_Format=lup.Blog_Format, Line4_Task=lup.Speech_Task,
                                  Line3_Format_outline=lup.Blog_Outline_Format,
                                  Line4_Task_outline=lup.Speech_Outline_Task,
                                  SavePath=up.AI_Blog_Path + up.System_Folder_Path_Fix + Mode, crazy=.5,
                                  Persona_Role=lup.Blog_Persona_Role, Persona_Task=lup.Blog_Persona_Task,
                                  Persona_Format=lup.Blog_Persona_Format, Persona_Special=lup.Blog_Persona_Special,
                                  Revise_Task=lup.Blog_Revise_Task, Revise_Format=lup.Blog_Revise_Format)


        elif Mode == 'Music':
            MondeVert.Make_a_Song_2(self, SavePath=up.AI_Music_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextRR, Mode='Music', )

        elif Mode == 'Music_Shane':
            MondeVert.Make_a_Song_2(self, Make_Persona=True, SavePath=up.AI_Music_Path, System=up.system_TextRR,
                                    Mode='Music_Shane', Artist_Bio_Details=up.Artist_Bio_DetailsSD,
                                    Song_Subject=up.Song_Subject,Task=lup.Song_Task)
        elif Mode == 'Music_Rich':
            MondeVert.Make_a_Song_2(self, Make_Persona=True,
                                    SavePath=Path(PureWindowsPath(up.AI_Music_Path)), Mode='Music_Rich',
                                    Artist_Bio_Details=up.Artist_Bio_DetailsRR, Song_Subject=up.Song_Subject_RR, Line4_Task_Outline=lup.Song_Outline_Task2, Task= lup.Song_Task2)
        elif Mode == 'Skit':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Screen_Plays + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_Skit,
                                    Background=up.Test_Background_Skit, Task=up.Test_Task_Skit,
                                    Special=up.Test_Special_Skit, Format=up.Test_Format_Skit, Mode='Skit')
        elif Mode == 'Basic':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_Explain,
                                    Background=up.Test_Background_Explain, Task=up.Test_Task_Explain,
                                    Special=up.Test_Special_Explain, Format=up.Test_Format_Explain,
                                    Title=up.Test_Title_Explain, Mode='Basic', Logic_AI=.5)
        elif Mode == 'Advance':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_Explain,
                                    Background=up.Test_Background_Explain, Task=up.Test_Task_Explain,
                                    Special=up.Test_Special_Explain, Format=up.Test_Format_Explain, Mode='Advance')
        elif Mode == 'Interview':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_Explain,
                                    Background=up.Test_Background_Explain, Task=up.Test_Task_Explain,
                                    Special=up.Test_Special_Explain, Format=up.Test_Format_Explain, Mode='Interview')
        elif Mode == 'Social':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_SM, Background=up.Test_Background_SM,
                                    Task=up.Test_Task_SM, Special=up.Test_Special_SM, Format=up.Test_Format_SM,
                                    Mode='Social')
        elif Mode == 'RealEstate':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_RE, Background=up.Test_Background_RE,
                                    Task=up.Test_Task_RE, Special=up.Test_Special_RE, Format=up.Test_Format_RE,
                                    Mode='RealEstate')





        elif Mode == 'JobDescription':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Test_Role_Summarize_JD,
                                    Background=lup.Test_Background_Summarize_JD, Task=lup.Test_Task_Summarize_JD,
                                    Special=lup.Test_Special_Summarize_JD, Format=lup.Test_Format_Summarize_JD,
                                    Mode='JobDescription')



        elif Mode == 'Social_Media_Clean_Post':

            Line3 = sms.Clean_Post_Line3 + sms.SHAINE_User_Inquiry
            Text = MondeVert.Basic_GPT_Query(self, Line1_System_Rule=sms.Clean_Post_Line1,
                                             Line2_Role=sms.Clean_Post_Line2, Line3_Format=Line3,
                                             Line4_Task=sms.Clean_Post_Line4, Mode='Social_Media_Clean_Post',
                                             SaveFile=True, MakeArt=True,
                                             SavePath=up.AI_Blog_Path + up.System_Folder_Path_Fix + Mode)



        elif Mode == 'Resume':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Test_Role_Resume,
                                    Background=lup.Test_Background_Resume, Task=lup.Test_Task_Resume,
                                    Special=lup.Test_Special_Resume, Format=lup.Test_Format_Resume, Mode='Resume')

        elif Mode == 'Resume_Review':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Test_Role_Resume_Review,
                                    Background=lup.Test_Background_Resume_Review, Task=lup.Test_Task_Resume_Review,
                                    Special=lup.Test_Special_Resume_Review, Format=lup.Test_Format_Resume_Review,
                                    Mode='Resume_Review')




        elif Mode == 'Resume_Consolidate_Old':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Test_Role_Resume_old,
                                    Background=lup.Test_Background_Resume_old, Task=lup.Test_Task_Resume_old,
                                    Special=lup.Test_Format_Resume_old, Format=lup.Test_Format_Resume_old,
                                    Mode='Resume_Consolidate_Old')



        elif Mode == 'Resume_Combine_old_new':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Test_Role_Resume_old_New_Combo,
                                    Background=lup.Test_Background_Resume_old_New_Combo,
                                    Task=lup.Test_Task_Resume_old_New_Combo,
                                    Special=lup.Test_Format_Resume_old_New_Combo,
                                    Format=lup.Test_Format_Resume_old_New_Combo, Mode='Resume_Combine_old_new')

        elif Mode == 'LinkedIn':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Test_Role_LinkedIn,
                                    Background=lup.Test_Background_LinkedIn, Task=lup.Test_Task_LinkedIn,
                                    Special=lup.Test_Format_LinkedIn, Format=lup.Test_Format_LinkedIn, Mode='LinkedIn')



        elif Mode == 'AUDIOBOOK':
            MondeVert.StoryMode(self, SavePath=up.AI_AudioBook_Path + up.System_Folder_Path_Fix + Mode,
                                Translate=['English'], Mode='AUDIOBOOK')

        elif Mode == 'AUDIOBOOK_Shane':
            MondeVert.StoryMode(self, SavePath=up.AI_AudioBook_Path + up.System_Folder_Path_Fix + Mode,
                                Persona_Task=" use your current persona to complete the task and instead of making up a persona you are the writer (Shane Donovan)" + lup.Persona_Task,
                                Translate=['English'], Mode='AUDIOBOOK_Shane', Persona=up.Shane_Persona,
                                Persona_Role=up.Shane_Persona)






        elif Mode == 'Freelance_Services':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Test_Role_Resume,
                                    Background=lup.Test_Background_Summarize_FL, Task=lup.Test_Task_Summarize_FL,
                                    Special=lup.Test_Special_Summarize_FL, Format=lup.Test_Format_Summarize_FL,
                                    Mode='Freelance_Services')


        elif Mode == 'Create_Persona_Writer':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=lup.Persona_Role,
                                    Background=lup.Persona_Background, Task=lup.Persona_Task,
                                    Special=lup.Persona_Special, Format=lup.Persona_Format,
                                    Mode='Create_Persona_Writer')



        elif Mode == 'Wedding Vows':
            MondeVert.MondeVert_SHAINE_WeddingVows(self, SavePath=up.AI_Wedding + up.System_Folder_Path_Fix + Mode,
                                                   Mode='Wedding Vows')



        elif Mode == 'ReSearch':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_ReSearch,
                                    Background=up.Test_Background_ReSearch, Task=up.Test_Task_ReSearch,
                                    Special=up.Test_Special_ReSearch, Format=up.Test_Format_ReSearch, Mode='Research')
        elif Mode == 'ReSearch2':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_ReSearch,
                                    Background=up.Test_Background_ReSearch, Task=up.Test_Task_ReSearch2,
                                    Special=up.Test_Special_ReSearch, Format=up.Test_Format_ReSearch2, Mode='Research2')
        elif Mode == 'ReSearch3':
            MondeVert.MondeVertTask(self, SavePath=up.AI_Task_Path + up.System_Folder_Path_Fix + Mode,
                                    System=up.system_TextJoaT, Role=up.Test_Role_ReSearch,
                                    Background=up.Test_Background_ReSearch, Task=up.Test_Task_ReSearch3,
                                    Special=up.Test_Special_ReSearch, Format=up.Test_Format_ReSearch3, Mode='Research3')

        elif Mode == 'Book':
            MondeVert.Make_a_ScreenPlay(self, Mode='ScreenPlay',
                                        SavePath=up.AI_Screen_Plays + up.System_Folder_Path_Fix + Mode)
        # elif Mode == 'Series':
        #     MondeVert.Series(self, Mode='Series', Episodes= 10, Seasons = 1, Audience = 'Kids')

        # atexit.register(MondeVert.saveTranscript(self))

    def MondeVertTask(self, System='', Role='', Background='', Task='', Special='', Title='', Mode='Basic', Logic_AI=0,
                      Format=up.Test_Format_PictureBook, OutlineFormat=up.Test_Format_PictureBook_outline,
                      SavePath=up.AI_Task_Path, ArtPrompt=up.MondeVert_ArtPrompt, ArtFormat=up.MondeVert_ArtFormat,
                      AdvanceArtPrompt=up.MondeVert_ArtPrompt_PictureBook,
                      AdvanceArtFormat=up.MondeVert_ArtFormat_PictureBook, ART_System=up.system_Text_Art, Big=False):

        ArtPaths = []
        openai.api_key = API_Key
        Art_PromptCharoo = ''
        Art_PromptCharo = ''
        Art_PromptForDALLE = ''

        Titleo = Title

        if Titleo == '':
            Titleo = Mode + self.current_time

        cu.Check_Folder_Exists(SavePath)
        SavePath = SavePath + up.System_Folder_Path_Fix + Titleo
        cu.Check_Folder_Exists(SavePath)

        if Logic_AI == 0:
            crazy = round((randbelow(520000) + 170000) / 100000, 0)
            crazy = crazy / 10
            print(crazy)
            crazy += .2
            if crazy < .4:
                crazy = .6
            if crazy > .9:
                crazy = .7
        else:
            crazy = Logic_AI

        #
        # cu.Check_Folder_Exists(SavePath)
        # SavePath1 = SavePath + up.System_Folder_Path_Fix + Title
        #
        # cu.Check_Folder_Exists(SavePath1)

        Project_Description = 'N/A not ready to test this yet'
        Result = 'N/A not ready to test this yet'
        Result_AI = 'N/A not ready to test this yet'
        AIPrompt = 'N/A not ready to test this yet'
        Result_Combine = 'N/A not ready to test this yet'
        Bitter_Critic = 'N/A not ready to test this yet'

        Task2 = up.Test_Task_Critic
        Format2 = up.Test_Format_Critic
        Special2 = up.Test_Special_Critic
        Role2 = up.Test_Role_Critic

        Format0 = up.Test_Format0
        KillSwitch = 0

        if Title != '':
            Background = Title + Background

        tempFormat = Format
        if Mode == 'PictureBook' or Mode == 'PictureBook_Shane' or Mode == 'PjSpecial':
            Format = up.Test_Format_PictureBook
            OutlineFormat = up.Test_Format_PictureBook_outline

        if Mode == 'PictureBook':
            Writer_Persona = MondeVert.Writer_Persona_Short_Story(self,
                                                                  Special='You are writing a children story so make your character extremely fit for children storyies with a clean bio and approachable to families, content should be 100% family friendly')
        elif Mode == 'PictureBook_Shane':
            Writer_Persona = MondeVert.Writer_Persona_Short_Story(self, Role=up.Shane_Persona,
                                                                  Special='You are writing a children story so make your character extremely fit for children storyies with a clean bio and approachable to families, content should be 100% family friendly')
        elif 'PjSpecial' in Mode:
            Writer_Persona = MondeVert.Writer_Persona_Short_Story(self, Role=up.DinosaurTaco_Writing,
                                                                  Special='You are writing a children story so make your character extremely fit for children storyies with a clean bio and approachable to families, content should be 100% family friendly')
        else:
            Writer_Persona = MondeVert.Writer_Persona_Short_Story(self)

        Format_f = OutlineFormat
        if Mode == 'skit':
            Format_f = Format0

        Role = Role + ' You are specifically taking on the role of the following persona: ' + Writer_Persona

        while KillSwitch < 7:
            KeepGoing = False
            while KeepGoing == False and KillSwitch < 6:
                # dummy = 1
                # if dummy ==1:
                try:  # This is for the result when you ask AI to summarize the project
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": up.system_TextJoaT + Role},
                            {"role": "user", "content": Role},
                            {"role": "user", "content": Format_f},
                            {"role": "user", "content": Special},
                            {"role": "user", "content": Background}
                        ], temperature=crazy
                    )

                    Project_Description = response.choices[0].message.content

                    if Title != '':
                        Project_Description = Title + Project_Description
                    else:
                        Project_Description = Project_Description

                    KeepGoing = True

                except:

                    print(
                        '1). Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                    KillSwitch += 1
                    if KillSwitch == 6:
                        Project_Description = Background
                    continue

                Format = tempFormat

                print(
                    '************************************************************************************************')

            # This was misguided lol but I think getting rid of prompt for now is ok eventually maybe this will cause an issue, going to be fully reworked soon
            if 'RESUME' in Mode.upper():
                Resume_Fix = Project_Description
            else:
                Resume_Fix = up.AI_Background_Prompt + Project_Description

            KeepGoing = False
            KillSwitch = 0
            while KeepGoing == False and KillSwitch < 6:
                try:
                    # This is for the result if you let the AI describe project and details and then make the response
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": up.system_TextJoaT + Role},
                            {"role": "user", "content": Role},
                            {"role": "user", "content": Format},
                            {"role": "user", "content": Resume_Fix},
                            {"role": "user", "content": Task + Special},
                        ]
                        , temperature=crazy
                    )
                    Result = response.choices[0].message.content

                    KeepGoing = True
                except:
                    print(
                        '2). Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                    KillSwitch += 1
                    continue

                print(up.breakupOutput)

                KillSwitch = 0
                while KeepGoing == False and KillSwitch < 6:
                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": up.system_TextJoaT + Role},
                                {"role": "user", "content": up.Role_Play_Prompt + Role},
                                {"role": "user", "content": up.UserRequest + Format + Special + Task},
                                # {"role": "user", "content": up.USER_SPECIAL_Prompt + Special},
                                {"role": "user", "content": up.AI_Background_Prompt + Project_Description},
                                {"role": "user",
                                 "content": up.CombineBothResults + "Result: " + Result + Special},
                                # {"role": "user", "content": up.USER_Task_Prompt + Task},
                            ]
                            , temperature=crazy
                        )
                        Result_Combine = response.choices[0].message.content
                        KeepGoing = True
                    except:
                        print(
                            '5). Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                        # KillSwitch += 1

                        try:
                            Result2 = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system", "content": up.system_TextJoaT + Role},
                                    {"role": "user", "content": Role},
                                    {"role": "user", "content": Format + Special},
                                    # {"role": "user", "content": up.USER_SPECIAL_Prompt + Special},
                                    # {"role": "user", "content": Project_Description},
                                    {"role": "user",
                                     "content": up.CombineBothResults + "Result : " + Result + Task},
                                    # {"role": "user", "content": up.USER_Task_Prompt + Task},
                                ]
                                , temperature=crazy
                            )
                            Result_Combine = Result2.choices[0].message.content
                            print("Only revised v1")
                            KeepGoing = True
                        except:
                            print("could not combine 2 versions")
                            print(
                                '6). Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                            KillSwitch += 1
                            continue

                if Mode == 'PictureBook' or Mode == 'script':
                    Bitter_Critic = MondeVert.Bitter_Critic(self, Project_Description=Project_Description,
                                                            Result=Result, Title=Title)

                KillSwitch = 0
                KeepGoing = False
                while KeepGoing == False and KillSwitch < 6:
                    try:
                        if Title == '':
                            Title = MondeVert.Get_Title_GPT(self, Project_Description=Project_Description)
                            KeepGoing = True
                        else:
                            KeepGoing = True
                    except:
                        try:
                            Title = MondeVert.Get_Title_GPT(self, Project_Description=Background)
                            print('First try did not work for title, but went through second time')
                        except:
                            print(Mode)
                            print(Title)
                            print(
                                '7). Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                            KillSwitch += 1
                            continue

            try:
                if Title == '':
                    # Title = MondeVert.ChatGPTDA(self, temp=0.5, MakeArt=True, Prompt=( Titleo+ '"' + Background + '"'),ConfirmBot=False)
                    Title = Titleo
            except:
                print('could not come up with title review')
                Title = Mode

            Title = Title.replace("The Title:", "")
            Title = Title.replace("Title:", "")
            Title = Title.replace("The Title", "")
            Title = Title.replace("Title", "")

            # if Mode =='PictureBook':
            # SavePath1= up.AI_Childrens_AudioBook_Path

            # this should be a utility
            Title1 = cu.CleanFileName(Title)
            folder = Title1
            if len(folder) > 44:
                folder = folder[0:44]
            Title1 = str(Title1)
            # if len(Title1) > 44:
            #     Title1 = Title1[0:44]
            SavePath = SavePath + up.System_Folder_Path_Fix + folder

            print('************************************************************************************************')
            print('************************************************************************************************')
            print('************************************************************************************************')

            # MondeVert.speak(self, "MondeVert Project Work complete yo")
            try:
                data = """Project_Description: """ + Project_Description + up.breakupOutput2 + """Title: """ + Title + up.breakupOutput2 + """     Result: """ + Result + up.breakupOutput2 + """Results 2.0 (reworked a second time): """ + Result_Combine + up.breakupOutput2 + """Bitter_Critic: """ + Bitter_Critic
                print('Output for : ' + Mode)
                print(data)
            except:
                print('Error when printing, but kept script going with error handling, file may not work')

            # MondeVert.speak(self, "Saving the files round 1")
            # print(data)

            data1 = [(Result)]

            try:
                # df1 = pd.DataFrame(data1, columns=['Text'])

                Title1 = cu.CleanFileName(Title)
                filename = Title1
                if filename == '':
                    filename = Result[8:30] + self.current_time
                    Title1 = Result[8:33]
                    filename = cu.CleanFileName(filename)
                    Title1 = cu.CleanFileName(Title1)
                CSVLocation = cu.SaveCSV(Text=str(data), Title=filename, SavePath=SavePath)
                CSVLocation2 = cu.SaveCSV(Text=str(Result), Title=filename + '_Result Only', SavePath=SavePath)
                print('CSVLocation')
                print(CSVLocation)

                try:
                    if Mode == 'PictureBook' or Mode == 'Skit' or Mode == 'PjSpecial' or Mode == 'PictureBook_Shane':
                        if 'PjSpecial' in Mode:
                            Project_Description = up.DinosaurTaco_Art

                        Artist_Persona = MondeVert.Artist_Persona_Short_Story(self,
                                                                              Writer_persona=Writer_Persona + Project_Description)

                        MondeVert.summarize_art_style_for_short_story(self, Artist_Persona=Artist_Persona,
                                                                      Writer_Persona=Writer_Persona,
                                                                      outline=Project_Description)

                        # MondeVert.Manual_Audio_File(CSVLocation, SavePath=SavePath, FileName=filename)
                        try:
                            FilePath_email = cu.SaveText2Audio(SavePath=SavePath, Text=Project_Description,
                                                               FileName=filename + 'Outline_Art',
                                                               Voice=
                                                               random.choices(SAF.Original_List_of_Voices_English)[0],
                                                               Neural='Neural', Mode=Mode, Chunk_Limit=213,
                                                               Artist_Persona=Artist_Persona,
                                                               Translate=['English', 'Swahili'])
                        except:
                            print('Error making audio/art for outline, not a major issue')

                        try:
                            FilePath_email = cu.SaveText2Audio(SavePath=SavePath, Text=Result, FileName=filename,
                                                               Voice=
                                                               random.choices(SAF.Original_List_of_Voices_English)[0],
                                                               Neural='Neural', Mode=Mode, Chunk_Limit=213,
                                                               Artist_Persona=Artist_Persona,
                                                               Translate=['English', 'Swahili'])
                        except:
                            print('Review this could be an issue where audio did not get recorded')


                except:
                    print('Error Making Audio Files')


            except:
                print('Review Error File did not save ')

            try:
                cu.send_email_no_attachment_gmail(body=Project_Description)
                cu.send_email_no_attachment_outlook(body=Project_Description)

                cu.send_email_w_attachment_outlook(body=Project_Description, filename=[CSVLocation])
                cu.send_email_w_attachment_gmail(body=Project_Description, filename=[CSVLocation], fType='txt')
                print("Gmail email sent")
                print("Outlook email sent")
            except:
                print('email not send, its possible file was not created')

            # Art changes based on mode for now I will switch only when the mode calls for it otherwise default
            if Mode == 'PictureBook':
                ArtPrompt_Mondevert = ArtPrompt + Result
                # ArtFormat_Mondevert = ArtPrompt + Result
            else:
                ArtPrompt_Mondevert = ArtPrompt + Project_Description
                # ArtFormat_Mondevert = ArtFormat

            # ArtPrompt_Mondevert0 = up.MondeVert_ArtFormat

            # MondeVert.speak(self, "Making the art, painting yo picture")

            crazyArt = crazy
            crazyArt = .4
            try:
                Art_PromptForDALLE = MondeVert.GPTArt(self, crazy, prompt=AIPrompt, Plot=ArtPrompt_Mondevert,
                                                      ArtFormat=' The following artist is going to be illustrating the text please see the artist info for refernce: ' + Artist_Persona + ArtFormat,
                                                      sys_prompt=ART_System)
            except:
                Art_PromptForDALLE = 'Make a work of art based on the following text:' + Result

            # Art_Prompt1 = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",
            #     messages=[
            #         {"role": "system", "content": up.system_Text_Art},
            #         {"role": "user", "content": ArtPrompt_Mondevert},
            #         {"role": "user", "content": ArtFormat},
            #     ], temperature=crazyArt
            # )
            #
            # Art_PromptForDALLE = Art_Prompt1.choices[0].message.content
            print("Work of Art Inspiration:" + Art_PromptForDALLE)

            try:
                ArtPath2 = MondeVert.makeArt(self, Art_PromptForDALLE)
                ArtPaths.append(ArtPath2)

            except:
                ArtPath2 = ''

            # MondeVert.speak(self, "Saving the files round 2")

            # try:
            #     if '|' in Project_Description:
            #         Art_PromptForDALLE_Simple = Project_Description.split('|')
            #         Art_PromptForDALLE_Simple = Art_PromptForDALLE_Simple[-1:]
            #     else:
            #         Art_PromptForDALLE_Simple = Project_Description.replace("Illustration:", "|")
            #         # Art_PromptForDALLE_Simple = Art_PromptForDALLE_Simple.replace("Illustration", "|")
            #         if '|' in Art_PromptForDALLE_Simple:
            #             Art_PromptForDALLE_Simple = Art_PromptForDALLE_Simple.split('|')
            #
            #     Art_PromptForDALLE_Simple = Art_PromptForDALLE_Simple[:-1]
            #
            # except:
            #     print('Error did not Properly split the list')
            #
            #
            #
            # if Mode == 'PictureBook' or Mode == 'script':
            #     try:
            #         # Art_PromptCharo = MondeVert.GPTArt(self, crazy, prompt = AdvanceArtPrompt , Plot =   Art_PromptForDALLE_Simple, ArtFormat = AdvanceArtFormat,
            #         #                               sys_prompt=up.system_Text_Art_PictureBook)
            #         #
            #         Characters= []
            #         for c in Art_PromptForDALLE_Simple:
            #             try:
            #                 Art_PromptCharo = MondeVert.GPTArt2(self, crazy, prompt = Art_PromptForDALLE , Plot =   c, ArtFormat = ArtFormat,sys_prompt=up.system_Text_Art_PictureBook)
            #                 if len(Art_PromptCharo) > 25:
            #                     Characters.append(Art_PromptCharo)
            #             except:
            #                 Characters.append(Art_PromptForDALLE)
            #     except:
            #         print('Error Trying to make original Painting')
            #         if len(c) > 25:
            #             Characters.append(c)
            #
            #     Art_PromptCharoo = Art_PromptCharo
            #     # ArtPrompt_Mondevert = + Result
            #     # ArtPrompt_Mondevert = ArtFormatAdvance + Result
            #
            #     # try:
            #     #     if '|' in Art_PromptCharo:
            #     #         Art_PromptCharo = Art_PromptCharo.split('|')
            #     #     else:
            #     #         Art_PromptCharo = Art_PromptCharo.replace("Page:", "|")
            #     #         Art_PromptCharo = Art_PromptCharo.replace("Page", "|")
            #     #
            #     #
            #     #     if '|' in Art_PromptCharo:
            #     #         Art_PromptCharo = Art_PromptCharo.split('|')
            #     #     else:
            #     #         Art_PromptCharo = Art_PromptCharo.replace(":", "|")
            #     #         Art_PromptCharo = Art_PromptCharo.split('|')
            #     #
            #     #     # Test_Skel1 = Result.replace("Page:", "#")
            #     #     # Test_Skel1 = Test_Skel1.replace("Page", "#")
            #     #
            #     #     print('Art_PromptCharo')
            #     #     print(Art_PromptCharo)
            #     #     print (len(Art_PromptCharo))
            #     #
            #     #
            #     # except:
            #     #     print('Could not properly split out the string for multiple illustrations')
            #
            #
            #     KillSwitch =0
            #     KeepGoing = False
            #     while KeepGoing == False and KillSwitch < 6:
            #         try:
            #             # Characters = []
            #             # x = len(Art_PromptCharo)
            #             # for c in range(0, x):
            #             #     # print(c)
            #             #
            #             #     Art_PromptCharo[c] = 'Make a work of art based on the following text:' + Art_PromptCharo[c]
            #             #     if len(c)>25:
            #             #         Characters.append(Art_PromptCharo[c])
            #
            #             print('Characters')
            #             print(Characters)
            #
            #             for c in Characters:
            #                 print(' ')
            #                 print('-------------------------------------------')
            #                 print('-------------------------------------------')
            #                 print("Character: " + Art_PromptForDALLE + c)
            #                 print('-------------------------------------------')
            #                 #print("Character Art1: " + up.Character_Art1 + c)
            #                 ArtPath2 = MondeVert.makeArt(self, Art_PromptForDALLE + c)
            #                 ArtPaths.append(ArtPath2)
            #                 print(ArtPath2)
            #
            #
            #         except:
            #             print('Error Trying to create multiple paintings')
            #             KillSwitch += 1
            #         KeepGoing = True

            prompt = data + "Work of Art Inspiration(s):" + Art_PromptForDALLE + "     Work of Art Inspiration(scene by scene):" + Art_PromptCharoo
            Prompts_Used = [
                up.system_Text + up.RolePlay_SongArtist + "AI Created a Persona shown as the Artist Bio Above" + up.Song_prompt + up.ArtPrompt_SongArtist]
            ArtistPoetInfo = 'Lyrics Written By: ' + up.Song_Writer + '      (' + 'Artwork by: ' + up.AI_ArtistName + ')'
            cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title,
                                SavePath=SavePath, Mode=Mode)
            KillSwitch = 7

        # This is funny content where the AI reviews the youtube script

    def Bitter_Critic(self, Project_Description, Result, Title, Role2=up.Test_Role_Critic, Task2=up.Test_Task_Critic,
                      Special2=up.Test_Special_Critic, Format2=up.Test_Format_Critic,
                      Background=up.Test_Background_Critic, crazy=.5, Mode='Bitter Critic',
                      Persona='Make a persona that is a bitter critic come up with a name and usernames for various social media sites, you are a spoof and supposed to be funny'):
        KillSwitch = 0
        KeepGoing = False
        while KeepGoing == False and KillSwitch < 6:

            try:

                # Create original details
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": up.system_TextJoaT + Role2},
                        {"role": "user", "content": up.Role_Play_Prompt + Role2},
                        {"role": "user",
                         "content": up.UserRequest + Format2 + Special2 + Project_Description + Task2 + Title},
                        {"role": "user", "content": up.USER_SPECIAL_Prompt + Special2},
                        {"role": "user", "content": Background + Result},
                        # {"role": "user", "content": up.USER_Task_Prompt + Task2},
                    ], temperature=crazy
                )

                Bitter_Critic = response.choices[0].message.content

                KeepGoing = True
                continue
            except:
                print(
                    '8). Error ChatGPT failed, trying to rerun prompt now.... if this happens too many times we will kill the script')
                KillSwitch += 1
                continue

        return Bitter_Critic

    def GPTSummary(self, crazy='', prompt=up.GPT_Summary, Plot='',
                   sys_prompt=up.system_Text_ScreenPlay0 + up.system_Text_ScreenPlay3):

        openai.api_key = API_Key

        if crazy != '':
            crazy = round((randbelow(520000) + 170000) / 100000, 0)
            crazy = crazy / 10

        print(crazy)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt + Plot}

            ], temperature=crazy
        )

        Skeleton_Story = response.choices[0].message.content
        return Skeleton_Story

    # Every Scene I should come up with pictures to show (find things to trigger a picture getting created and multi-thread it so it does not stop anything, I should have it nice and output within the App if possible
    # Also I should have the ability to assign a voice to a given character and keep that for the audio transcript/recording. Also provide the Raw Words.
    # Snatch prequel
    # Big Lewbowski Prequel and Sequel
    # Something about Mary Sequel (add my own ideas)
    # Ancient egyption culture and other cultures
    # #(have the different technologies showing how they use sound and frequencies to move giant stones underground. Large caves and artifical light makes the world seem like another planet,
    # #have it seem like a distant planet etc, also have some of the extinct animals and animals/plants we never heard of. Describe landscape in vivid detail and make the reader fall in love with the lore.
    # Twist is they end up being underground and when humans are dealing with global warming we break in and accidentally become slaves.
    #   eventually we try to become a unified people as they realize we made the same mistakes as them
    #    #Write the MetaVerse Elon Musk Story -- This is going to be a video game too(like pokemon)
    def GPTArt2(self, crazy=.5, prompt=sms.ArtPrompt_Clean_Social_Media_Post_Line2_Prompt,
                User_Subject='Pick a random subject and medium go wild and make it exciting, beautiful and shocking',
                ArtFormat=sms.ArtPrompt_Clean_Social_Media_Post_Line3,
                sys_prompt=sms.ArtPrompt_Sys):

        keepgoing = True
        GPTARTPROMPT = User_Subject
        while keepgoing == True:
            try:

                Art_Prompt1 = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": sys_prompt},
                        {"role": "user", "content": prompt + User_Subject},
                        {"role": "user", "content": ArtFormat}
                    ], temperature=crazy
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

    def GPTArt(self, crazy=.5, prompt=up.ArtPrompt_ScreenPlay, SavePath=up.AI_Screen_Plays,
               Plot='Pick a random subject and medium go wild and make it exciting, beautiful and shocking',
               ArtFormat=up.MondeVert_ArtFormat,
               sys_prompt=up.system_Text_Artist_ScreenPlay):
        openai.api_key = API_Key

        Art_Prompt1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt + Plot},
                {"role": "user", "content": ArtFormat}
            ], temperature=crazy
        )

        GPTARTPROMPT = Art_Prompt1.choices[0].message.content
        return GPTARTPROMPT

    #
    # $$$$$Savetime

    # Give artist a profile and save it for use - make them have a set style that is repeated for the entire book (will be great for gothic and kid stories)

    # 1). Adapt for Movie/Book/Short Story/Indie Film
    #     2). Enhance the tool so you have option to pass in subject (by Default choose a random genre
    # 3). Need to build a google search version where I ask open ended questions and it summarizes and provides useful links for me to explore
    # 4). Coding version of this and start to use it
    # 5). Update Rap one for me and make it indie etc.
    # 6). create a version that does advertisements
    # 7). Animation
    # 8). Take all of the notes I add and make a story
    # 9). Make a tool that starts with basic idea, makes song.... book, short story, Movie
    # 10. Make tool post to instagram and twitter (do this asap and start doing it)
    # 11). Have a folder of pictures that it goes through and 3 times a day or something posts to my sites. Then it moves to another folder. Take poetry and maybe post it with all nuts and bolts ready
    # 12). For sampler, maybe build a tool to go out and download songs from itunes when it suggests it so I can mess around
    # 13). Tabs in and out (edit sounds to be other instruments)
    # 14). Edit the voice output so I can text to speech sound better
    # 15). make a play out of the voices we already have??
    # 16 get picture working with comma separated list.

    def Make_a_ScreenPlay(self, System='', Mode='ScreenPlay', SavePath=up.AI_Screen_Plays):
        Summary_Episodes = []
        ScreenPlay = []
        i = 0
        data = []
        Outline_Next2_Ref2 = ''
        Outline_Details = ''
        Plot = ''
        Add_IN = ''
        Summary_Summer_90s = ''
        filename = []
        filename1 = []
        Outline_Next2 = ''
        Outline_Next = ''
        self.Mode = 'ScreenPlay'
        ArtPaths = []
        openai.api_key = API_Key
        Plot = ""
        crazy = round((randbelow(520000) + 170000) / 100000, 0)
        crazy = crazy / 10
        if crazy < .3:
            crazy += .1

        print('Crazy Factor: ' + str(crazy))

        UserInput = False

        if UserInput == False:
            Subject = up.RandomGenre()
        else:
            Subject = UserInput
        print('Subject: ' + Subject)

        # Create original details
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_Text_ScreenPlay0 + up.system_Text_ScreenPlay2},
                {"role": "user", "content": up.Direction_ScreenPlay_Detail},
                {"role": "user", "content": up.Direction_ScreenPlay_Detail2},
                {"role": "user", "content": up.Direction_ScreenPlay_Detail3 + Subject},
                {"role": "user", "content": up.Setting_ScreenPlay},
                {"role": "user", "content": up.Characters_ScreenPlay},
                # {"role": "user", "content": up.Title_ScreenPlay}

            ], temperature=crazy
        )

        Skeleton_Story1 = response.choices[0].message.content

        # Create original details
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_Text_ScreenPlay0 + up.system_Text_ScreenPlay2},
                {"role": "user", "content": up.Title_ScreenPlay + Skeleton_Story1}

            ], temperature=crazy
        )

        Skeleton_Story2 = response.choices[0].message.content

        Skeleton_Story = Skeleton_Story2 + Skeleton_Story1

        print('***********************************************************************************')
        print(Skeleton_Story)
        print('***********************************************************************************')

        # MondeVert.speak(self, Skeleton_Story)

        # Create full outline
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_Text_ScreenPlay0 + up.system_Text_ScreenPlay4},
                {"role": "user", "content": up.Create_Outline1 + Skeleton_Story},

                # {"role": "user", "content": up.Title_ScreenPlay}

            ], temperature=crazy
        )

        Outline_All = response.choices[0].message.content

        print(Outline_All)

        print('***********************************************************************************')
        print('***********************************************************************************')

        # This is how I set up the prompts for the show, I could randomize when to activate red herrings etc based on Add-In Feature
        Direction_ScreenPlay = []
        Direction_ScreenPlay.append(up.Direction_ScreenPlay_Pilot)
        Direction_ScreenPlay.append(up.Direction_ScreenPlayMiddle)
        Direction_ScreenPlay.append(up.Direction_ScreenPlayMiddleLate)
        Direction_ScreenPlay.append(up.Direction_ScreenPlayMiddleLate)
        Direction_ScreenPlay.append(up.Direction_ScreenPlayFinal)

        ScreenPlay_Final = ''
        Episode_Count = 5
        for i in range(0, Episode_Count):
            Episode_Direction = Direction_ScreenPlay[i]

            Add_IN = ''
            # if i == 1:
            #     Add_IN = up.RedHerring_ScreenPlay
            # elif i == 2:
            #     Add_IN = up.UnsungHero + up.Twist_ScreenPlay
            # elif i == 3:
            #     Add_IN = up.Mystery_Character_Past + up.VillanOrigin

            # Prior to writing an episode we should create the outline for the episode based on

            if i != 0:

                # Create outline for next 2 episodes
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": up.system_Text_ScreenPlay0 + up.system_Text_ScreenPlay4},
                        {"role": "user", "content": up.Compare_Detail_v_Summary1 + Plot},
                        {"role": "user", "content": up.Compare_Detail_v_Summary2 + Outline_All},
                        {"role": "user", "content": up.Compare_Detail_v_Summary3},

                        # {"role": "user", "content": up.Title_ScreenPlay}

                    ], temperature=crazy
                )

                Outline_Next2 = response.choices[0].message.content

                # Store this to maybe use later as a way to keep story moving together well

                # Revise
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": up.system_Text_ScreenPlay0 + up.system_Text_ScreenPlay4},
                        {"role": "user", "content": up.Compare_Detail_v_Summary_Outline_New + Outline_Next2},
                        {"role": "user", "content": up.Compare_Detail_v_Summary_Revise},
                        {"role": "user", "content": up.Compare_Detail_v_Summary_Summary_New + PriorScreenPlay},
                        # {"role": "user", "content": up.Title_ScreenPlay}

                    ], temperature=crazy
                )

                Outline_Next = response.choices[0].message.content

            else:
                # if i = 0 want to create an outline for next episode

                # Create outline for next 2 episodes
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": up.system_Text_ScreenPlay0 + up.system_Text_ScreenPlay4},
                        {"role": "user", "content": up.Compare_Detail_v_Summary2 + Outline_All},
                        {"role": "user", "content": up.Outline_Pilot}

                        # {"role": "user", "content": up.Title_ScreenPlay}

                    ], temperature=crazy
                )

                Outline_Next = response.choices[0].message.content

            print('  ')
            print('  ')
            print('  ')
            # print('***********************************************************')
            # print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print('  ')
            print('  ')
            print('  ')
            print('Episode ' + str(i + 1))
            Add_IN = ''

            Song1 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": up.system_Text_ScreenPlay + up.system_Text_ScreenPlay1},
                    {"role": "system", "content": up.Tie_In_ScreenPlay + Skeleton_Story},
                    {"role": "system", "content": up.Tie_In_ScreenPlay2 + Outline_Next},
                    {"role": "system", "content": up.Direction_ScreenPlayALL},
                    {"role": "system", "content": up.Direction_ScreenPlayALL2},
                    {"role": "system", "content": up.Direction_ScreenPlayALL3},
                    ##--------------------Common Above/Unique Below----------
                    # {"role": "system", "content":  Episode_Direction+ Add_IN},
                    {"role": "system", "content": Episode_Direction},
                    ##--------------------Dialog----------
                    {"role": "system", "content": up.Dialog_ScreenPlay}
                ], temperature=crazy)
            ScreenPlay0 = Song1.choices[0].message.content
            ScreenPlay.append(ScreenPlay0)

            print(ScreenPlay[i])

            Summary_Episode1 = MondeVert.GPTSummary(self, crazy, up.Summarize_ScreenPlay, ScreenPlay[i])
            Summary_Episodes.append(Summary_Episode1)

            PriorSummary = Summary_Episodes[i]
            PriorScreenPlay = ScreenPlay[i]
            PriorNext2 = Outline_Next2
            PriorOutline = Outline_Next

            # print('***********************************************************')
            # print("Summary Episode " + str(i + 1))
            # print(Summary_Episodes[i])
            Plot += Summary_Episodes[i]
            ScreenPlay += "EPISODE " + str(i + 1) + ScreenPlay[i]
            Outline_Details = Skeleton_Story + Outline_All
            Outline_Next2_Ref2 += Outline_Next2

        Title = MondeVert.Get_Title_GPT(self, Plot)
        Title = Title.replace("The Title:", "")
        Title = Title.replace("Title:", "")
        Title = Title.replace("The Title", "")
        Title = Title.replace("Title", "")
        # f2 = FolderPath

        Title1 = cu.CleanFileName(Title)
        folder = Title1
        if len(folder) > 44:
            folder = folder[0:44]
        Title1 = r"\\" + str(Title1) + "_"
        Title11 = str(Title1) + "_"
        # if len(Title1) > 44:
        #     Title1 = Title1[0:44]
        SavePath = SavePath + r"\\" + folder

        filename1.append('Screen Play - ' + Title11)
        filename1.append('Details_Outline - ' + Title11)
        filename1.append('OutlineNext2_Ref - ' + Title11)
        filename1.append('Summaries - ' + Title11)

        print('Review the filnames:')
        print(filename)

        data.append([ScreenPlay])
        data.append([Outline_Details])
        data.append([Outline_Next2_Ref2])
        data.append([Plot])
        filenames = []
        for x in range(0, 4):
            # print(data)
            try:

                Text = data[x]
                FName = filename1[x]
                filename = cu.SaveCSV(Text=Text, Title=FName, SavePath=SavePath)
                # MondeVert.SaveText(self,df1,'MondeVert Assistant', 'Full Transcript')
                filenames.append(filename)
                # MondeVert.add2Master2(df1)
            except:
                print('Review Error File did not save ')

        try:

            cu.send_email_no_attachment_gmail(body=Skeleton_Story)
            cu.send_email_no_attachment_outlook(body=Skeleton_Story)

            cu.send_email_w_attachment_outlook(body=Skeleton_Story, filename=filenames)
            cu.send_email_w_attachment_gmail(body=Skeleton_Story, filename=filenames, fType='txt')

            print('Outlook Email Sent ')

        except:
            print('email not send, its possible file was not created')

        try:
            Remove_l = (-1) * len(Summary_Episodes[4] + Summary_Episodes[5])
            Plot_NoSpoiler = Plot[Remove_l:]
            print(Plot_NoSpoiler)
        except:
            print('error on no spoiler')
        # MondeVert.speak(self, ScreenPlay_Final)

        try:
            Summary_Summer_90s = MondeVert.GPTSummary(self, crazy, up.GPT_90s_Summary, Plot_NoSpoiler)
        except:
            print('error on 90s trailer')

            print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print("90s Movie Preview: ")
            print(Summary_Summer_90s)
            # MondeVert.speak(self, Summary_Summer_90s)

            print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print("Character Art prompts ")

            # ''
            # if this does not work I can make replace that text with the char so it works
            # Test_Skel1 = Skeleton_Story.replace(":", "")

            print('Skeleton_Story')
            print(Skeleton_Story)

            if '|' in Skeleton_Story:
                Test_Skel = Skeleton_Story.split('|')
            else:
                Test_Skel = Skeleton_Story.replace("Characters:", "|")
                Test_Skel = Test_Skel.replace("Characters", "|")
                Test_Skel = Test_Skel.split('|')

            print('Test_Skel')
            print(Test_Skel)

            # Test_Skel = Test_Skel.split('')
            # print('Test_Skel')
            # print(Test_Skel)
            Details = Test_Skel[0]

            Characters = []
            x = len(Test_Skel)
            for c in range(0, x):
                # print(c)
                if c != 0:
                    Characters.append(Test_Skel[c])

            print('Characters')
            print(Characters)

            for c in Characters:
                print(' ')
                print('-------------------------------------------')
                print('-------------------------------------------')
                # print("Character: " + c)
                print('-------------------------------------------')
                print("Character Art1: " + up.Character_Art1 + c)
                Art_PromptChar = MondeVert.GPTArt(self, crazy, up.Character_Art2 + c, Plot=Skeleton_Story)

                print("Character Art2: " + up.Character_Art2 + c)
                Art_PromptChar2 = MondeVert.GPTArt(self, crazy, up.Character_Art2 + c, Plot=Skeleton_Story)

            try:
                # MondeVert.speak(self, Art_PromptChar)
                print(Art_PromptChar)
                ArtPath2 = MondeVert.makeArt(self, Art_PromptChar)
                ArtPaths.append(ArtPath2)
            except:
                dn = ''

            try:
                # Art_PromptChar2)
                print(Art_PromptChar2)
                ArtPath2 = MondeVert.makeArt(self, Art_PromptChar2)
                ArtPaths.append(ArtPath2)
            except:
                dn = ''

            print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print('***********************************************************')
            print("Art prompts ")

            try:
                Art_Prompt = MondeVert.GPTArt(self, crazy,
                                              up.direction_Text_Artist_ScreenPlay + up.ArtPrompt_ScreenPlay,
                                              Skeleton_Story,
                                              sys_prompt=up.system_Text_Artist_ScreenPlay + up.system_Text_ScreenPlay_Art1)
                # Art_Prompt)
                print('***********************************************************')
                print("Art prompt Movie Poster ")
                print(Art_Prompt)
                try:
                    ArtPath2 = MondeVert.makeArt(self, Art_Prompt)
                    ArtPaths.append(ArtPath2)
                except:
                    d = ''
            except:
                ArtPath2 = ''
            # Art_Prompt = Art_Prompt11.choices[0].message.content

            for x in range(0, 5):

                Summary_Episode = Summary_Episodes[x]

                try:
                    Art_Prompt1 = MondeVert.GPTArt(self, crazy,
                                                   up.direction_Text_Artist_ScreenPlay + up.ArtPrompt_ScreenPlay_Scene,
                                                   Summary_Episode,
                                                   sys_prompt=up.system_Text_Artist_ScreenPlay + up.system_Text_ScreenPlay_Art1 + up.system_Text_ScreenPlay_Art)
                except:
                    print('Error did not work but kept going')

                try:

                    # Test_Skel1 = Skeleton_Story.replace("Art Prompts:", "")
                    # Test_Skel1 = Test_Skel1.replace("Art Prompts", "#")
                    # ''

                    if '|' in Skeleton_Story:
                        Test_Skel = Skeleton_Story.split('|')
                    else:
                        Test_Skel = Skeleton_Story.replace("Art Prompt:", "|")
                        Test_Skel = Test_Skel.replace("Art Prompt", "|")
                        Test_Skel = Test_Skel.split('|')

                    # Test_Skel = Art_Prompt1.split('#')

                    Art_Prompts_pre = []
                    Art_Prompts = []
                    x = len(Test_Skel)
                    for c in range(0, x):
                        # print(c)
                        if c != 0:
                            Art_Prompts_pre.append(Test_Skel[c])

                    print(Art_Prompt1)
                    Test_Skel = Art_Prompt1.split(';')
                    print("Test_Skel: " + Test_Skel)

                    x = len(Test_Skel)
                    for c in range(0, x):
                        Art_Prompts.append(Test_Skel[c])

                    for ap in Art_Prompts:
                        # MondeVert.speak(self, ap)
                        print('***********************************************************')
                        print("Art prompt Movie Poster ")
                        print(ap)
                        ArtPath2 = MondeVert.makeArt(self, ap)
                        ArtPaths.append(ArtPath2)

                except:
                    print("New stuff failed yo")

            # Art_Prompt2 = MondeVert.GPTArt(self, crazy, up.direction_Text_Artist_ScreenPlay + up.ArtPrompt_ScreenPlay_Scene, Summary_Episode2, sys_prompt= up.system_Text_Artist_ScreenPlay + up.system_Text_ScreenPlay_Art1 +up.system_Text_ScreenPlay_Art)
            # Art_Prompt3 = MondeVert.GPTArt(self, crazy, up.direction_Text_Artist_ScreenPlay + up.ArtPrompt_ScreenPlay_Scene, Summary_Episode3, sys_prompt= up.system_Text_Artist_ScreenPlay + up.system_Text_ScreenPlay_Art1 +up.system_Text_ScreenPlay_Art)
            # Art_Prompt4 = MondeVert.GPTArt(self, crazy, up.direction_Text_Artist_ScreenPlay + up.ArtPrompt_ScreenPlay_Scene, Summary_Episode4, sys_prompt= up.system_Text_Artist_ScreenPlay + up.system_Text_ScreenPlay_Art1 +up.system_Text_ScreenPlay_Art)
            # Art_Prompt5 = MondeVert.GPTArt(self, crazy, up.direction_Text_Artist_ScreenPlay + up.ArtPrompt_ScreenPlay_Scene, Summary_EpisodeFinal,sys_prompt= up.system_Text_Artist_ScreenPlay + up.system_Text_ScreenPlay_Art1 +up.system_Text_ScreenPlay_Art)
            #

        # ScreenPlay = "EPISODE I      :" +  ScreenPlay[0] +"               EPISODE II: " +  ScreenPlay2 + "       EPISODE III: " + ScreenPlay3 +"         EPISODE IV:" +  ScreenPlay4+"         EPISODE V:" +  ScreenPlayFinal

        # Title = 'SD - MondeVert Productions - Classified'

        if len(Title) > 45:
            Title = Title[0:45]

        ArtPrompt_Combined = ''

        for f in Art_Prompt:
            ArtPrompt_Combined += f

        prompt = " 90s Summer Preview: " + Summary_Summer_90s + " Details:" + Skeleton_Story + 'Summary: ' + Plot + "Work of Art Inspiration:" + ArtPrompt_Combined + "      Song:" + ScreenPlay
        Prompts_Used = [
            up.system_Text + up.RolePlay_SongArtist + "AI Created a Persona shown as the Artist Bio Above" + up.Song_prompt + up.ArtPrompt_SongArtist]
        ArtistPoetInfo = 'Lyrics Written By: ' + up.Song_Writer + '      (' + 'Artwork by: ' + up.AI_ArtistName + ')'
        cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title=Title,
                            SavePath=SavePath, Mode='Screen Play' + Mode)

    def quickArt(self):
        prompt = MondeVert.ChatGPTDA(self, MakeArt=True, Prompt=(up.QuickArt))

        ArtPaths = []
        try:
            ArtPath = MondeVert.makeArt(self, prompt)
            ArtPaths.append(ArtPath)
        except:
            # MondeVert.speak(self, 'Could not make the Art due to an error')
            print('Could not make the Art due to an error')

        Prompts_Used = [str('Quick_Art_Prompt: ' + up.QuickArt)]
        ArtistPoetInfo = 'Written By: ' + up.Bot_Name + '      (' + 'Artwork by: ' + up.AI_ArtistName + ')'
        cu.NamePoemSavePoem(self, prompt, ArtPaths, Prompts_Used, ArtistPoetInfo, title='Quick_Art')

    def Get_Title_GPT(self, Text, Role='', mood='', bio='', crazy=.5):

        # Create original details
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": up.system_TextJoaT},
                # {"role": "user", "content": up.Role_Play_Prompt + Role},
                {"role": "user", "content": up.MondeVert_Title + Text}

            ], temperature=crazy
        )

        Title = response.choices[0].message.content

        Title = Title.replace("Title:", "")
        Title = Title.replace("Title", "")
        return Title

    # Blog Make Art Live mode

    # test this to see how to generate images from another one
    def animate(self, image, Prompt):
        response = openai.Image.create_edit(
            image=open(
                "A:\AI Art\Approved Quality Art\Favorites\Art_Blunts_Using_the_classic_style_of_Pablo_Picasso_create_a_unique_work_of_art_that_celebrates_the_creative_combination_of_Snoop_Dogg_and_Backwood.png",
                "rb"),
            mask=open("mask.png", "rb"),
            prompt="A sunlit indoor lounge area with a pool containing a flamingo",
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']


#
# from multiprocessing.dummy import Pool as ThreadPool
#
# # urls = [
# #   'http://www.python.org',
# #   'http://www.python.org/about/',
# #   'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
# #   'http://www.python.org/doc/',
# #   'http://www.python.org/download/',
# #   'http://www.python.org/getit/',
# #   'http://www.python.org/community/',
# #   'https://wiki.python.org/moin/',
# # ]
#
# # Make the Pool of workers
# pool = ThreadPool(3)
#
# # Open the URLs in their own threads
# # and return the results
# results = pool.map(urllib2.urlopen, urls)
#
# # Close the pool and wait for the work to finish
# pool.close()
# pool.join()
#


# def run_the_command(index, command_array):
#     try:
#         command_array = ...
#         number_of_commands = len(command_array)
#
#         exec
#         command_array[index]
#     except:
#         print('Error but powering through it')

#
# def run_the_command(index):
#     exec
#     command_array[index]


# def SHAINEBootUP(Functions, Args = ['Basic'], MultiT = False, PostInsta = False):
def SHAINEBootUP(Args='Basic'):
    dummy = 1
    if dummy == 1:
        # try:
        x = MondeVert()
        x.MondeVertMenu_up(Mode=Args)
    # except:
    #     print('Error unable to pull the value from the ARGs parameter')


if __name__ == '__main__':
    # main method for executing
    # the functions
    Record = ''

    # args = ['JobDescription']
    # args = ['Resume_Consolidate_Old']
    # args = ['Resume_Consolidate_Old','Resume', 'Resume_Combine_old_new']
    # args = ['Resume_Combine_old_new']

    # args = ['ReSearch3', 'ReSearch',  'ReSearch2']
    # args = ['ReSearch2']
    #
    # args = ['Freelance_Services', 'JobDescription','Resume']
    # args = ['Freelance_Services']
    # args = ['Resume']

    # args = ['LinkedIn', 'Create_Persona_Writer', 'Resume_Review', 'Basic']
    # args = ['MondeVert_Audio_Video_Story']
    # args = ['Wedding Vows']
    # args = ['PjSpecial', 'PjSpecial', 'MondeVert_Audio_Video_Story',  'PictureBook']

    # args= ['Music_Rich','Music_Shane', 'Music', 'Poem']

    # args= ['Blog_Random']
    # args= ['Speech']
    # args = ['Music_Rich']
    #    args = ['Blog_Random_Shane']
    # args = ['Speech_Shane']
    # args = ['PictureBook_Shane']

    # args = ['PictureBook_PJSpecial']
    #    args = ['PictureBook_Shane','PictureBook_2','Shane_Poem']
    # args = ['PictureBook_2', 'Blog_Random_Shane', 'AUDIOBOOK_Shane', 'MondeVert_Audio_Video_Story']
    # args = ['Blog_Random_Shane_Specific_Subject']
    # args = ['PictureBook_2']

    # args = ['ShaneOriginal', 'AUDIOBOOK_Shane']
    # args = ['MVAA']
    # args = ['MVAA','MVAA2']
    # args = ['MVAA', 'MVAA2', 'MVAA_La_Familia']
    args = ['Music_Shane']

    #args = ['Music_Rich','Music_Shane']

    #

    #
    # args.append(args)
    # args.append(args)

    number_of_commands = len(args)

    threads = []
    for i in range(number_of_commands):
        ArgX = args[i]
        # Dummy line
        i2 = 1

        if i2 == 1:
            # try:

            print("Start Thread " + str(i))
            t = threading.Thread(target=SHAINEBootUP, args=(ArgX,)).start()
            threads.append(t)

        # except:
        #     print('Error - Could not start new thread')

    # Wait for all of them to finish
    #    for t in threads:
    #        t.join()
    print("Job Complete!")

# IP.upload_pictures()
# Image1 = x.animate(image= r"A:\AI Art\DALLE_please_create_an_art_piece_that_showcases_a_luxurious_and_modern_real_estate_property_The_property_should_have_a_stunning_view_and_be_surroun.png", Prompt = "Add a Stick Figure with long blonde hair to the following image")
# Image1 = x.Take_query(image = Image1, Prompt= 'Make a variation where everything is the same but you put the stick figure in a slightly different position')
# Testing
# x.Make_a_ScreenPlay_Testing()
# x.Make_a_ScreenPlay()
# x.saveTranscript()




