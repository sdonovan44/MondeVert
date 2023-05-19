import pandas as pd
import wikipedia

global Record
import sys
from threading import Event
from gingerit.gingerit import GingerIt
import threading
import numpy

# from exceptions import PendingDeprecationWarning

Record = ''
import webbrowser

from MondeVert.SHAINE_MonderVert.Utilities import ShakesBot as s
from MondeVert.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up

import random
import openai
import pyttsx3
# Import the speech recognition library
import speech_recognition as sr
from MondeVert.SHAINE_MonderVert.Utilities.DoNotCommit import API_Key

import atexit

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


#
# class GingerIt(object):
#     def __init__(self):
#         self.url = URL
#         self.api_key = API_KEY
#         self.api_version = "2.0"
#         self.lang = "US"
#
#     def parse(self, text, verify=True):
#         session = cloudscraper.create_scraper()
#         request = session.get(
#             self.url,
#             params={
#                 "lang": self.lang,
#                 "apiKey": self.api_key,
#                 "clientVersion": self.api_version,
#                 "text": text,
#             },
#             verify=verify,
#         )
#         data = request.json()
#         return self._process_data(text, data)


class MenuMode():
    def __init__(self, voice=3, language_settings=1):
        self.voice = voice
        self.language_settings = language_settings
        self.AssistantName = up.getAssistantName()
        self.UserName = up.getUserName()
        self.transcript_Final = ''
        self.API_Key = API_Key
        self.Correction_Comment = ''
        self.AI_Corrected_Content = ''
        self.SilentMode = False
        global xVoice
        global voice_set
        voice_set = self.voice
        xVoice = 1

    def Open_Web(url):
        url = url
        webbrowser.open_new_tab(url)

    def speak(self, audio, Add2T=True, voice=''):
        if voice == '':
            voice = self.voice

        if Add2T == True:
            MenuMode.Add2Transcript(self, self.AssistantName + ': ' + audio)
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
            MenuMode.Add2Transcript(self, self.AssistantName + ': ' + audio)
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
            MenuMode.Add2Transcript(self, text2Add=message)
            set1 = False

            for voice in voices:
                indexCount += 1

            while set1 == False:
                if index <= indexCount:
                    print(f'index-> {index} -- {voices[index].name}')
                    engine.setProperty('voice', voices[index].id)
                    engine.say(message)
                    MenuMode.speak(self, speak1)
                    Query = MenuMode.getUserResponse(self)

                    if "yes" in Query or "set" in Query or ("make" in Query and "active" in Query) or (
                            "set" in Query and "active" in Query):
                        self.voice = index
                        voice_set = self.voice
                        xVoice = index
                        MenuMode.speak(self, 'Voice Set')
                        set1 = True

                    index += 1
                    engine.runAndWait()
                else:
                    MenuMode.Setvoices(self, Quick=True)

        else:
            self.voice = int(input('What Voice do you want to make active?'))
            MenuMode.speak(self, 'Voice Set')

        ####################################################################################################################################################################################
        ## Below are more utlities that help me to do repetitive tasks quicker
        ####################################################################################################################################################################################

    def ActivateSilentMode(self):
        self.SilentMode = True

    def ActivateLoudMode(self):
        self.SilentMode = False

    def cleanText(self, text):
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
                        result1 = [result1 + texttemp + '\\n' + '\\n']
                result = pd.DataFrame(result1, columns='result')

            if len(result.loc[0, 'result']) > 0:
                # print(result.loc[:,'result'].values)
                rr = str(result.loc[0, 'result'])
                self.Correction_Comment += 'Corrections Made.'
            else:
                rr = text
                self.Correction_Comment += 'No Corrections Needed.'


        except:
            print('Text was not properly cleaned: ' + text)
            # print(text)
            rr = text
            self.Correction_Comment += 'No Corrections Needed (Caused an error and did not return anything).'
            return rr

        return rr

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Above is code I did not write, below is code that allows user to update values of respective values
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    def getfilename(self):
        self.FileName = MenuMode.getdata(self, 'FileName')

    def getsubject(self):
        self.subject = MenuMode.getdata(self, 'subject')

    def getDictation_Type(self):
        self.Dictation_Type = MenuMode.getdata(self, 'Type')

    def getSignificance(self):
        self.Significance = MenuMode.getdata(self, 'Significance')

    def getNote(self):
        self.Notes += '|' + MenuMode.getdata(self, 'Notes')

    def getdata(self, Field):

        MenuMode.speak(self, 'what is the ' + Field)
        print('Please confirm the ' + Field)
        s = True
        Query = ''
        while (s == True):
            Query = MenuMode.getUserResponse(self)
            Query2 = ''
            WaitforResponse = False
            while (WaitforResponse == False):
                MenuMode.speak(self, Query + ' Is that correct?')
                Query2 = MenuMode.getUserResponse(self)
                if "yes" in Query2 or "correct" in Query2 or "ya" in Query2 or "yeah" in Query2:
                    MenuMode.speak(self, 'Thanks for confirming the ' + Field)
                    s = False
                    WaitforResponse = True
                    continue
                if "no" in Query2 or "wrong" in Query2 or "not it" in Query2 or "nope" in Query2:
                    MenuMode.speak(self, 'ok  please say the ' + Field + ' you want to set')
                    print('ok  please say the ' + Field + ' you want to set')
                    WaitforResponse = True
                    continue
                else:
                    MenuMode.speak(self, 'Lets try that again what is the ' + Field)
                    Event().wait(1)
                    continue
        return Query

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################ below is code that allow me to confirm with the user the inputs are correct
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    def takeCommand(self):
        Query = MenuMode.getUserResponse(self, Response="Action Requested")
        return Query

    def getUserResponse(self, pause=.5, Response='You Said'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = pause
            audio = r.listen(source)
            try:
                Query = r.recognize_google(audio, language='en-in')
                MenuMode.Add2Transcript(self, self.UserName + ': ' + Query)
                print(Response + ": ", Query)

            except Exception as e:
                print(e)
                print("Please repeat Words not understood...")
                Query = MenuMode.getUserResponse(self)
                # Event().wait(2)
            return Query

    def ConfirmUR(self, prompt):
        MenuMode.speak(self, 'You Said ' + prompt + ' is this correct?')
        query = MenuMode.getUserResponse(self)

        if 'yes' in query or 'correct' in query or 'yeah' in query or 'submit' in query:
            self.promptB = True

    def editBotPrompt(self, message):
        MenuMode.speak(self, 'Edit Mode Activated', voice=4)
        MenuMode.speak(self, 'What do you want to use for a prompt?', voice=4)
        query = MenuMode.getUserResponse(self)

        if 'cancel' in query:
            r = message
            # Do nothing
        else:
            MenuMode.ConfirmBOT(self, query)
            if self.promptB == True:
                self.message = query

    def ConfirmBOT(self, message):
        MenuMode.speak(self, 'Chat GPT responded with: ' + message + ' do you want to use this prompt?', voice=4)
        query = MenuMode.getUserResponse(self)

        if 'yes' in query or 'correct' in query or 'yeah' in query or 'submit' in query:
            self.promptB = True

        if 'edit' in query or 'change' in query and ('prompt' in query or 'words' in query):
            MenuMode.editBotPrompt(self, message)

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Above  is ChatGPT (I did not write original code but adapted for my use case)
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

    def editentry(self, Query1):
        MenuMode.Add2Transcript(self, ' \n')
        Prior_Mode = self.Mode
        self.Mode = 'Edit Mode'
        MenuMode.Add2Transcript(self, text2Add=(Prior_Mode + ' - ' + self.Mode + ':'))
        s = True
        while (s == True):
            MenuMode.speak(self, 'I am ready to make the edit please proceed')
            print('ready to make the edit please proceed')
            print('Original Entry: ' + Query1)
            Query2 = MenuMode.getUserResponse()

            ss = True
            while (ss == True):
                print(Query2)
                MenuMode.speak(self, Query2 + 'Are you satisfied with your edits?')
                print('Options: Yes/Correct, Not yet/Redo, Add as Note, Combine, Cancel')

                Query3 = MenuMode.getUserResponse(self)

                if "yes" in Query3 or "correct" in Query3 or "ya" in Query3 or "yeah" in Query3 or "looks good" in Query3 or "keep new" in Query3 or "new one" in Query3:
                    MenuMode.speak(self, 'Thanks for confirming, I will make the updates you provided')
                    print('Thanks for confirming, I will make the updates you provided')
                    Query_Final = Query2
                    s = False
                    ss = False


                elif "not yet" in Query3 or 'redo' in Query3 or 'try again' in Query3 or 'again' in Query3 or 'one more' in Query3:
                    MenuMode.speak(self, 'ok, lets go again')
                    print('ok, lets go again')
                    ss = False
                    continue

                elif "add as note" in Query3 or "include note" in Query3 or "as note" in Query3:
                    MenuMode.speak(self, 'Thanks for confirming, I will add this as a note')
                    print('Thanks for confirming, I will add this as a note')
                    Query_Final = ''
                    self.Notes = Query2
                    # when this is a class I can update the df for now I will add it to the end same as when I say combine them
                    s = False
                    ss = False

                elif "add to original" in Query3 or "both" in Query3 or 'combine' in Query3 or 'combination' in Query3 or 'merge' in Query3 or 'together' in Query3:
                    MenuMode.speak(self, 'Thanks for confirming, I will join the two thoughts')
                    print('Thanks for confirming, I will join the two thoughts')
                    Query_Final = Query1 + ' ' + Query2
                    # when this is a clas I can update the df for now I will add it to the end same as when I say combine them
                    s = False
                    ss = False

                elif 'cancel' in Query3 or 'end' in Query3 or 'stop' in Query3 or 'stop trying' in Query3:
                    MenuMode.speak(self, 'Thanks for confirming, I will remove these edits')
                    print('Thanks for confirming, I will remove these edits')
                    Query_Final = ''
                    s = False
                    ss = False

                else:
                    Event().wait(1)

        return Query_Final

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Long Code where I give Digital Assistant commands##    (user menus)
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

    def RunChatGPT(self):
        self.Mode = 'Chat GPT -  Menu'

        MenuMode.speak(self, self.Mode + ' What Chat GPT mode do you want to use?')

        print(self.Mode + ' What Chat GPT mode do you want to use?')

        s2 = True
        while (s2 == True):
            MenuMode.Add2Transcript(self, ' \n')
            query = MenuMode.takeCommand(self).lower()

            # Say Quick Art or Auto Art or Basic Art
            if 'normal' in query or 'conv' in query or 'reg' in query or 'talk' in query:
                prompt = MenuMode.ChatGPTDA(self)
                MenuMode.RunChatGPT(self)
                s2 = False

            elif "art" in query and ("basic" in query or "auto" in query or "quick" in query):
                MenuMode.quickArt(self)
                MenuMode.RunChatGPT(self)
                s2 = False

            # Say Prompted Art or super Art or advanced Art
            elif "art" in query and ("advance" in query or "super" in query or "open" in query or (
                    "with" in query and "prompt" in query)):
                prompt = MenuMode.ChatGPTDA(self, MakeArt=True, UseArtPrompt=True)

                ArtPath = MenuMode.makeArt(self, prompt)
                MenuMode.RunChatGPT(self)
                s2 = False

            elif 'shake' not in query and ("inspire" in query or "unique" in query or ("own" in query) or (
                    "version" in query and "3" in query) or ('quick' in query and 'poem' in query) or (
                                                   "poem" in query or 'poetry' in query)):
                # make program to ask how spicy to make it lol
                Poem_Type = random.choices(up.Random_Poem)
                Poem_Type = Poem_Type[0]
                MenuMode.Quick_Poem_v1(self, GPTPrompt=Poem_Type)
                s2 = False
                MenuMode.RunChatGPT(self)


            elif "shake" in query and ("poem" in query or "poet" in query or ("version" in query and "1" in query)):
                MenuMode.Shake_Poem_v1(self)
                s2 = False
                MenuMode.RunChatGPT(self)

            elif ("poem" in query or 'poetry' in query or 'shake' in query) and (
                    "inspire" in query or "unique" in query or ("make" in query or "own" in query) or (
                    "version" in query and "2" in query)):
                MenuMode.Shake_Poem_v2(self)
                s2 = False
                MenuMode.RunChatGPT(self)


            elif ("sunday" in query and ('scary' in query or 'scaries' in query)) or (
                    "sunday" in query and ("poem" in query or "story" in query)):
                MenuMode.SundayScary_Poem(self)
                s2 = False
                MenuMode.RunChatGPT(self)


            elif (("live" in query and 'art in query') or ('podcast' in query or 'stream' in query)):
                MenuMode.MakeArtLive(self)
                s2 = False
                MenuMode.RunChatGPT(self)





            elif ('chorus' in query or 'song' in query) or ("brick" in query and ("sing" in query or "dj" in query)):

                Song_Genre = random.choices(up.Random_Song_Genre_List)
                Song_Genre = Song_Genre[0]
                Song_Genre = 'v3'
                # Song_Genre = 'techno'

                if 'v1' in Song_Genre:
                    MenuMode.Make_a_Song(self)
                    MenuMode.speak(self, 'Make a quick song Version 1 Complete')
                elif 'v2' in Song_Genre:
                    MenuMode.Make_a_Chorus(self)
                    MenuMode.speak(self, 'Make a quick song Version 2 Complete')
                elif 'v3' in Song_Genre:
                    MenuMode.Make_a_Song(self)
                    MenuMode.speak(self, 'Make a quick song Version 3 Complete')

                elif 'Techno' in Song_Genre:
                    DigitalAssist.Make_a_Chorus(self, Mode='Techno')
                    DigitalAssist.speak(self, 'Techno Lyrics Complete')
                    DigitalAssist.Sampler(self, Mode='Techno')
                    DigitalAssist.speak(self, 'Techno Samples Provided Complete', voice=9)
                elif Song_Genre == 'SadRap':
                    DigitalAssist.Make_a_Rap(self, Mode='SadRap')
                    DigitalAssist.speak(self, 'Sad Rap Lyrics Complete')
                elif Song_Genre == 'Reggae':
                    DigitalAssist.Make_a_Rap(self, Mode='Raggae')
                    DigitalAssist.speak(self, 'Reggae Lyrics Complete')
                elif Song_Genre == 'Rap':
                    DigitalAssist.Make_a_Rap(self, Mode='Rap')
                    DigitalAssist.speak(self, 'Rap Lyrics Complete')
                else:
                    DigitalAssist.Make_a_Rap(self, Mode='Raggae')
                    DigitalAssist.speak(self, 'Reggae Lyrics Complete')

                s2 = False
                DigitalAssist.RunChatGPT(self)



            elif 'basic' in query or 'shake' in query:
                DigitalAssist.makeQuickPoem(self)
                DigitalAssist.makeArt(self, self.Words)
                s2 = False
                DigitalAssist.RunChatGPT(self)


            elif 'dad' in query or 'timmy' in query or ' guy' in query or 'tim ' in query or (
                    ('simon' in query or 'old man' in query or 'timmy d' in query) and 'help' in query) or (
                    'timmy' in query and 'd' in query):
                DigitalAssist.TimmyDMode(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)

            elif 'blog' in query or 'website post' in query or 'post' in query:
                Blog_Topic = random.choices(up.Random_Blog_Topic)

                Blog_Topic = Blog_Topic[0]

                # DigitalAssist.makeBlogPost(self, GPTprompt=Blog_Topic)
                # DigitalAssist.makeBlogPost(self, GPTprompt=up.RandomTopic)
                DigitalAssist.makeBlogPost(self, GPTprompt=up.CorrectText)

                s2 = False
                DigitalAssist.RunChatGPT(self)


            # Make a program that makes a short background for a character, also have a duo/relationship of some sort and make an interesting scene for a play/screenplay

            elif 'wiki' in query or 'wikipedia' in query or (
                    ('pen name' in query or 'page' in query or 'mode' in query) and 'wiki' in query):
                DigitalAssist.Wiki4PenNames(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)


            elif 'cancel' in query or 'stop' in query or 'quit' in query or 'done' in query or 'exit' in query:
                DigitalAssist.saveTranscript(self)
                sys.exit()
                s2 = False

            else:
                print('Please try again, ')
                continue

    # def Shake_Art_v1(self, prompt)

    def YayorNay(self):
        self.Mode = 'Yay or Nay -  Menu'

        DigitalAssist.speak(self, self.Mode + ' What did you think ' + self.UserName)

        print(self.Mode + ' What did you think ' + self.UserName)

        s2 = True
        while (s2 == True):
            DigitalAssist.Add2Transcript(self, ' \n')
            query = DigitalAssist.takeCommand(self).lower()

            # Say Quick Art or Auto Art or Basic Art
            if 'awesome' in query or 'love' in query or 'yay' in query or 'yes' in query or 'best' in query:
                rr = '- Sounded Great'
                s2 = False
                continue

            elif 'good' in query or 'love' in query or 'yay' in query or 'yes' in query:
                rr = '- Good - POTENTIAL HERE'
                s2 = False
                continue

            elif 'ok' in query or 'okay' in query or 'not bad' in query or 'so so' in query:
                rr = ' - So So'
                s2 = False

            elif 'no' in query or 'hate' in query or 'bad' in query or 'terrible' in query or 'yuck' in query:
                rr = ' - BAD'
                s2 = False
            else:
                rr = ''
                s2 = False

        return rr

    # Blog Make Art Live mode
    def MakeArtLive(self):
        self.onlyMyWords = ''
        self.onlyMyWordsLatest2 = ''
        self.onlyMyWordsLatest = []
        self.Mode = 'Make Art Live Mode'
        Title = DigitalAssist.getfilename(self)

        # Ask user if you should have silent mode on?

        s2 = True
        while (s2 == True):

            DigitalAssist.speak(self, 'Do you Want Silent Mode activated for Chat GPT?')
            query = DigitalAssist.takeCommand(self).lower()
            # DigitalAssist.Add2Transcript(self,text2Add=query)
            if "yes" in query or "silent" in query:
                self.SilentMode = True
                s2 = False
                DigitalAssist.speak(self, 'Silent Mode Activated', voice=1)
            elif "no" in query or "nope" in query or "loud" in query:
                DigitalAssist.speak(self, 'Interrupt Mode Activated', voice=1)
                self.SilentMode = False
                s2 = False
            else:
                print("Gonna Have to Repeat That....")

        HowManyLinestoAdd = 7
        self.LineCount = 0
        LiveMode = True
        while (LiveMode == True):
            print(self.onlyMyWordsLatest2)
            self.LineCount = self.LineCount + 1
            self.query1 = DigitalAssist.transcribe_Build_Query(self, 1.44).lower()
            self.query1 = self.query1 + '.' + '\n'
            self.onlyMyWords = self.onlyMyWords + self.query1
            self.onlyMyWordsLatest2 = self.onlyMyWordsLatest2 + self.query1
            self.onlyMyWordsLatest.append(self.query1)

            if 'loud mode' in self.query1:
                self.SilentMode = False
            elif ((
                          "brick top" in self.query1 or "bricktop" in self.query1 or "show me" in self.query1 or "extra" in self.query1 or "additional" in self.query1) and (
                          "option" in self.query1 or "tool" in self.query1)) or ("edit mode" in self.query1) or (
                    "need to" in self.query1 and "make edit" in self.query1):
                s3 = True
                while (s3 == True):
                    # this is where you say next steps (This can be a separate function)
                    query2 = DigitalAssist.transcribe_Build_Query_Pause(self).lower()
                    print(query2)

                    if 'chat' in query2 and ('gpt' in query2 or 'bot' in query2 or 'ai' in query2 or 'mode' in query2):
                        DigitalAssist.RunChatGPT(self)
                    elif ('take' in query2 or 'note' in query2 or 'write' in query2 or 'transcribe' in query2):
                        DigitalAssist.transcribe(self)
                    elif (
                            'none' in query2 or 'no ' in query2 or 'mistake' in query2 or 'my bad' in query2 or 'go back' in query2):
                        s3 == True
                    elif ('stop' in query2 or 'cancel' in query2 or 'quit' in query2 or 'cut' in query2):
                        sys.exit()
                        continue
            else:
                SubjectMatter = DigitalAssist.Pick_Random_Lines(self, SetofLines=self.onlyMyWordsLatest, LineCount=2)
                if self.LineCount == HowManyLinestoAdd + 1:
                    DigitalAssist.LiveArt(self, SubjectMatter, Title=Title)
                    self.onlyMyWordsLatest = []
                    self.onlyMyWordsLatest2 = ''

        Script1 = 'Human Transcript: ' + self.onlyMyWords + '\n' + 'Full Transcript: ' + self.transcript_Final
        DigitalAssist.NamePoemSavePoem(self, Script1, [], '', 'Shane Donovan - MondeVert CEO',
                                       title=Title + '_' + self.current_time22, FolderPath=up.AI_Live_Art_Path,
                                       ArtType='MondeVert Podcast with Live Art')

    def LiveArt(self, SubjectMatter='Random subject of your choice, weirder the better', Title='Podcast UnNamed'):
        # LiveArt1 = DigitalAssist.ChatGPTDA(self, temp=0.5, MakeArt=True, Prompt=(up.MakeArtLive_prompt1), ConfirmBot=False)
        # ArtPath1 = DigitalAssist.makeArt(self, LiveArt1)
        ArtPath2 = DigitalAssist.makeArt(self, up.MakeArtLive_prompt2 + ': ' + SubjectMatter)
        # ArtPaths = [ArtPath1, ArtPath2]
        ArtPaths = [ArtPath2]
        DigitalAssist.SaveLiveArt(self, ArtPaths, Title)

    def Pick_Random_Lines(self, SetofLines, LineCount=2):
        Line1 = random.choices(SetofLines)
        Line1 = Line1[0]
        Line2 = Line1
        while Line2 == Line1:
            Line2 = random.choices(SetofLines)
            Line2 = Line2[0]
            continue
        return str(Line1 + Line2)

    # Main Menu
    def Take_query(self):
        DigitalAssist.Hello(self)

        self.Mode = 'Main Menu'
        # DigitalAssist.Add2Transcript(self,text2Add= ( self.Mode + ':'))
        s2 = True
        while (s2 == True):
            self.Mode = 'Main Menu'
            DigitalAssist.speak(self, self.Mode)
            query = DigitalAssist.takeCommand(self).lower()
            # DigitalAssist.Add2Transcript(self,text2Add=query)
            if "company dashboard" in query or "open dashboard" in query:
                DigitalAssist.speak(self, "Opening MondDay Vert's Dasboard, good luck with your work!")

                # in the open method we just to give the link
                # of the website and it automatically open
                # it in your default browser
                Mondevert = "http://mondeVert.co"
                godaddy = 'https://dashboard.godaddy.com/'
                Mail = 'https://outlook.office.com/mail/'
                Square_store = 'https://square.online/app/home/'
                DigitalAssist.Open_Web(Mail)
                DigitalAssist.Open_Web(Square_store)
                DigitalAssist.Open_Web(Mondevert)
                DigitalAssist.Open_Web(godaddy)
                continue

            elif "pay bills" in query or "pay credit cards" in query:
                DigitalAssist.speak(self,
                                    "Bills Suck man, at least you are getting them done, Hope you have a nice day!")

                Liberty_Bay_CC = "https://www.myaccountaccess.com/onlineCard/login.do"
                Home_Depot_CC = 'https://citiretailservices.citibankonline.com/RSnextgen/svc/launch/index.action?siteId=PLCN_HOMEDEPOT#signon'
                Macys_CC = 'https://www.macys.com/my-credit/gateway/guest'
                Insurance = 'https://customer.concordgroupinsurance.com/ccp/login'
                National_Grid = 'https://login.nationalgridus.com/loginnationalgridus.onmicrosoft.com/oauth2/v2.0/authorize?cancel_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauth%2Fsso%2FNGP_SignIn_MA_Electric_Home&client_id=88d004b4-3d39-4599-b410-093849907ee5&customer_type=home&p=B2C_1A_UWP_NationalGrid_convert_merge_signin&redirect_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauthcallback%2FNGP_SignIn_MA_Electric_Home&region=masselec&response_type=code&scope=https%3A%2F%2Flogin.nationalgridus.com%2Fapi%2Fread+openid+profile+email+offline_access&state=CAAAAYUokN2YMDAwMDAwMDAwMDAwMDAwAAAA8Iy1JaCJ8hTkDIfqZ5i6KE2oIrQFv5bPH9zBI_P-5wWki9riiDhgLKrNlnVD4FeR38QBEzYH17vRm_CbsR8msY3J3fEDKFqtBsup_Bp9KwM-Flb38WYF6YqeqejsI-Iuj-yWpXfajw6-QKG_DMoOBtkqcL8zubs4c8KgKiuF-yIk3yoa1_vp_KqVAuBw0DSopTJrDwsYAZN5qW9zaUmwyW-wk6zbTNddqu24EJObkHkfEGKHEKQwrqArl40WukP3dxbKBfj7sSMhdqjTPa0ido8%3D&switch_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fs%2Flogin'
                LLBean_CC = 'https://citiretailservices.citibankonline.com/RSauth/signon?pageName=signon&siteId=PLCN_LLBEAN&langId=en_US'
                Amazon_CC = 'https://secure07ea.chase.com/web/auth/#/logon/logon/chaseOnline'
                DigitalAssist.Open_Web(Liberty_Bay_CC)
                DigitalAssist.Open_Web(Home_Depot_CC)
                DigitalAssist.Open_Web(Macys_CC)
                DigitalAssist.Open_Web(Insurance)
                DigitalAssist.Open_Web(National_Grid)
                DigitalAssist.Open_Web(LLBean_CC)
                DigitalAssist.Open_Web(Amazon_CC)
                continue


            elif ("chat" in query and "bot" in query) or ("gpt" in query and "chat" in query) or (
                    "smart" in query and "assist" in query) or ("extra" in query and "help" in query) or (
                    "artificial" in query and "intellig" in query):

                DigitalAssist.RunChatGPT(self)
                DigitalAssist.speak(self, "High Tech!")
                # prompt = DigitalAssist.ChatGPTDA(self)
                continue

            elif ("make" in query and "art" in query) or ("make" in query and "picture" in query) or (
                    "ai" in query and "art" in query) or ("art" in query and "mode" in query) or (
                    "super" in query and "shake" in query and 'art' in query):

                DigitalAssist.speak(self, "High Tech and sheek!")
                if 'super' in query or 'using' in query or 'extra' in query:
                    if 'poem' in query or 'shake' in query or 'poet' in query:
                        DigitalAssist.makeQuickPoem(self)
                        prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True, Prompt=(
                                    'make a prompt for openai  DALL-E program to create a work of art that is based on the following poem. ' + '\n' + '\n' + self.Words))
                        DigitalAssist.makeArt(self, prompt)
                    else:
                        prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True)
                        DigitalAssist.makeArt(self, prompt)

                else:

                    if 'poem' in query or 'shake' in query or 'poet' in query:
                        DigitalAssist.makeQuickPoem(self)
                        DigitalAssist.makeArt(self, self.Words)
                    else:
                        DigitalAssist.makeArt(self)
                        continue



            elif "stop" in query or "all set" in query or "quit" in query or "m done" in query or "thank" in query or "peace out" in query:
                DigitalAssist.speak(self, "Happy to help, Peace out brothah man")
                s2 = False

            elif (
                    "record" in query or "listen up" in query or "can you right" in query or "record mode" in query or "transcribe" in query or "could you write" in query or "transcribe" in query or "can you write" in query) and 'stop' not in query:
                DigitalAssist.speakSweet(self, "Dictated but not Red Mode Activated")
                DigitalAssist.transcribe(self)
                continue


            elif ("blog" in query) and (
                    "create" in query or "together" in query or "put" in query or "make" in query) or (
                    "add" in query and "blog" in query):
                DigitalAssist.speakSweet(self,
                                         "Mon Day Vert is lucky to have a great CEO this is going to be a great post!")
                DigitalAssist.CompileBlog(self)
                DigitalAssist.speakSweet(self, "Blog Consolidation Complete Shane D")
                continue

            elif (("consolidate" in query or "compile" in query or "collect" in query) and (
                    "file" in query or "folder" in query or "list" in query)) or ("add" in query and "master" in query):
                DigitalAssist.speakSweet(self, "Consolidation in progress")
                DigitalAssist.compileFiles(self)
                DigitalAssist.speakSweet(self, "Consolidation Complete my dude")
                continue

            elif "make list" in query or " list" in query or "to do" in query or "tracker" in query or "checklist" in query or "make a plan" in query or "quick note" in query or "quick plan" in query or "take note" in query:
                # DigitalAssist.speak("Sure thing, One moment while I prepare")
                DigitalAssist.makelist(self)
                continue


            elif "poetic" in query or "swoon me" in query or "me a poem" in query or "poem" in query or "while I think you" in query or "poetry will help me think" in query or "write me a poem" in query or "we need some inspiration" in query or "some art" in query or "be creative" in query or "inspire me" in query:
                x22 = s.PoemBot(1, 1, 1, 1, 40, 3)
                x22.ReloadModel("model.h5")
                x22.setupdata()
                self.Words = x22.shakesbot_DA()
                print(self.Words)
                DigitalAssist.speakSweet(self, self.Words)
                continue




            elif ("play" in query or "script" in query) and (
                    "make" in query or "write" in query or "create" in query or "mode" in query):
                # Call for the save file name after listing all of the subjects to the user
                self.Words = ''
                self.Correction_Comment = ''
                self.Type = 'AI Script Break'
                self.Significance = '**AI content attached'
                self.FileName = 'AI ShakeScript'
                self.Subject = 'AI ShakeScript'
                DigitalAssist.speak(self, 'I like your style, my man')

                DigitalAssist.Make_Script(self)

                DigitalAssist.speakSweet(self, self.Words)
                s3 = pd.DataFrame()
                s3['Script'] = [self.Words]
                s3['Script - Corrected'] = [self.AI_Corrected_Content]
                s3['Correction Comment'] = [self.Correction_Comment]
                DigitalAssist.SaveText(self, s3, self.FileName, self.Subject)
                continue

            elif ("go" in query or 'try' in query or "mode" in query) and ("greek" in query or "myth" in query):
                # Call for the save file name after listing all of the subjects to the user
                self.Words = ''
                self.Type = 'Greek Script Break'
                self.Significance = '**AI content attached'
                self.FileName = 'AI Going Greek'
                self.Subject = 'AI Going Greek'
                DigitalAssist.speak(self, 'I like your style, my man... Dont eat too much tzatziki!')
                self.pb = s.PoemBot(1, 1, 1, 1, 40, 3)
                self.pb.ReloadModel("model_Greek.h5")
                self.pb.setupdata()
                size = 3
                trd = numpy.empty(size, dtype=str)
                w = numpy.empty(size, dtype=str)
                for i in range(0, size - 1):
                    globals()[f"trd{i}"] = threading.Thread(target=DigitalAssist.generateGreek(self))
                    w[i] = globals()[f"trd{i}"].start()  # starting the thread i

                for i in range(0, size - 1):
                    threading.active_count()
                    threading.enumerate()
                    if i == 0:
                        self.Words += w[i]
                    else:
                        i2 = i - 1
                        globals()[f"trd{i2}"].join()
                        globals()[f"trd{i}"].join()
                        self.Words += w[i]
                        print(self.Words)

                DigitalAssist.speak(self, self.Words)
                s3 = pd.DataFrame()
                s3['Script'] = [self.Words]
                DigitalAssist.SaveText(self, s3, self.FileName, self.subject)
                continue



            elif "social media" in query or "marketing" in query:
                DigitalAssist.speak(self, "Will do")

                # in the open method we just to give the link
                # of the website and it automatically open
                # it in your default browser
                Facebook = "https://www.facebook.com/"
                Insta = 'https://www.instagram.com/'
                TikTok = 'https://www.tiktok.com/'
                Twitter = 'https://twitter.com/home'
                DigitalAssist.Open_Web(Facebook)
                DigitalAssist.Open_Web(TikTok)
                DigitalAssist.Open_Web(Twitter)
                DigitalAssist.Open_Web(Insta)
                continue

            elif "open google" in query:
                DigitalAssist.speak(self, "Opening Google ")
                url = "http://google.com"
                DigitalAssist.Open_Web(url)
                continue



            elif (("voice" in query or "person" in query or "bot" in query or "ai" in query) and (
                    "change" in query or "update" in query or "switch" in query or "set" in query)):

                if "quick" in query or "manual" in query:
                    DigitalAssist.Setvoices(self, Quick=True)
                    print('Quick mode activated')
                else:
                    DigitalAssist.Setvoices(self)
                continue

            elif "s the date" in query:
                DigitalAssist.tellDay(self)
                continue

            elif "the time" in query or "what time" in query or "clock mode" in query:
                DigitalAssist.tellTime(self)
                continue

            # this will exit and terminate the program
            elif "bye" in query:
                DigitalAssist.speak(self, "Peace Out!")
                s2 = False

            elif "from wikipedia" in query or "wikipedia" in query:
                DigitalAssist.speak(self, "Checking the wikipedia ")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=4)
                DigitalAssist.speak(self, "According to wikipedia")
                DigitalAssist.speak(self, result)



            elif "tell me your name" in query or "your name" in query or "introduce yourself" in query or "introduce your self" in query:
                DigitalAssist.speak(self,
                                    "I am Big Master Funk the fourth also known as Brick top, AND i AM  Your personal desktop Assistant")


            elif "shut up" in query:
                DigitalAssist.speak(self, "my bad I am tripping, I will leave you be Shane D")
                s2 = False

            else:
                # uk = cs.DA_Unknown_Command()
                # DigitalAssist.speak(uk)
                # print(uk)
                # Event().wait(1)
                continue

    def transcribe(self):
        self.entry = 1

        DigitalAssist.createDF(self)
        self.subject = 'Default'
        self.FileName = 'Default'
        s2 = True
        DigitalAssist.getsubject(self)
        self.visualList = 'Subject: ' + self.subject + ' \n'
        self.visualList2 = 'Subject*: ' + self.subject + ' \n'
        DigitalAssist.speak(self, "Please prepare for recording")
        print("Please prepare for recording...")
        while (s2 == True):
            xx = ''
            self.query1 = ''
            self.new_Query = ''
            self.Type = ''
            self.Significance = ''
            self.Words = ''
            self.Notes = ''
            self.Added2TextFile = ''
            self.Completed = ''
            print(self.visualList)
            print(self.visualList2)
            self.query1 = DigitalAssist.transcribe_Build_Query(self, 1.44).lower()
            self.query1 = self.query1 + '.'
            self.Type = 'Original'
            self.Significance = 'Default'

            if "stop recording" in self.query1 or "m all set" in self.query1 or "end list" in self.query1 or "stop listening" in self.query1 or "save this file" in self.query1 or "save this recording" in self.query1:
                # Call for the save file name after listing all of the subjects to the user
                DigitalAssist.getfilename(self)
                DigitalAssist.SaveText(self, self.transcript, self.FileName, self.subject)
                DigitalAssist.add2Master(self.transcript)
                s2 = False
                DigitalAssist.saveTranscript(self)
                sys.exit()
                continue


            elif ((
                          "brick top" in self.query1 or "bricktop" in self.query1 or "show me" in self.query1 or "extra" in self.query1 or "additional" in self.query1) and (
                          "option" in self.query1 or "tool" in self.query1)) or ("edit mode" in self.query1) or (
                    "need to" in self.query1 and "make edit" in self.query1):
                s3 = True
                while (s3 == True):
                    # this is where you say next steps (This can be a separate function)
                    query2 = DigitalAssist.transcribe_Build_Query_Pause(self).lower()
                    print(query2)

                    if "continue" in query2 or "just thinking" in query2 or "yes" in query2 or "chill" in query2 or "just thinking" in query2 or "keep going" in query2:
                        DigitalAssist.speak(self, 'no worries, still here')
                        s3 = False
                        # continue



                    elif "change subject" in self.query1 or "update subject" in self.query1 or "switch category" in self.query1 or "change category" in self.query1:
                        # transcript2[self.subject] = [str(self.visualList)]
                        # DigitalAssist.SaveText(self.transcript2, self.FileName + 'v2' + self.subject, self.subject)
                        DigitalAssist.getsubject(self)
                        s3 = False
                        # continue


                    elif "change" in query2 or "fix" in query2 or "edit" in query2 or "fix that" in query2 or "not quite" in query2 or "review last" in query2 or "back to me" in query2 or "read that back" in query2:
                        # Call for the save file name after listing all of the subjects to the user
                        self.Type = 'Edited'
                        self.Significance = 'Review edits'
                        self.new_Query = DigitalAssist.editentry(self, self.query1)
                        s3 = False
                        # continue


                    elif "while I think you" in query2 or "poetry will help me think" in query2 or "write me a poem" in query2 or "we need some inspiration" in query2 or "some art" in query2 or "be creative" in query2 or "inspire me" in query2 or (
                            "poem" in query2 and ("write" in query2 or "create" in query2 or "shake" in query2)):
                        # Call for the save file name after listing all of the subjects to the user
                        self.Type = 'Poetry Break'
                        self.Significance = '**AI content attached'
                        DigitalAssist.speakSweet(self, 'I like your style, Shane you are brilliant and beautiful')
                        x = s.PoemBot(1, 1, 1, 1, 40, 3)
                        x.ReloadModel("model.h5")
                        x.setupdata()
                        self.Words += x.shakesbot_DA()
                        print(self.Words)
                        DigitalAssist.speakSweet(self, self.Words)
                        s3 = False
                        # continue

                    elif ("chat" in query2 and "bot" in query2) or ("gpt" in query2 and "chat" in query2) or (
                            "smart" in query2 and "assist" in query2) or ("extra" in query2 and "help" in query2):
                        DigitalAssist.speak(self, "High Tech!")
                        prompt = DigitalAssist.ChatGPTDA(self)
                        self.Type = 'AI Conversation with Chat GPT'
                        self.Words += prompt
                        self.Significance = '**AI content attached'
                        continue

                    elif ("make" in query2 and "art" in query2) or ("make" in query2 and "picture" in query2) or (
                            "ai" in query2 and "art" in query2) or ("art" in query2 and "mode" in query2) or (
                            "super" in query2 and "shake" in query2 and 'art' in query2):

                        DigitalAssist.speak(self, "High Tech and sheek!")
                        if 'super' in query2 or 'using' in query2 or 'extra' in query2:
                            if 'poem' in query2 or 'shake' in query2 or 'poet' in query2:
                                DigitalAssist.makeQuickPoem(self)
                                prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True, Prompt=(
                                            'Using the poem that follows make a prompt to create a work of art that describes the feelings or the scene that fits the poem. ' + '\n' + '\n' + self.Words))
                                DigitalAssist.makeArt(self, prompt)
                            else:
                                prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True)
                                DigitalAssist.makeArt(self, prompt)
                            self.Type = 'AI Made Art - Add to BLOG?'
                            self.Words += prompt
                            self.Significance = '**AI content Please see image that goes with prompt'
                        else:

                            if 'poem' in query2 or 'shake' in query2 or 'poet' in query2:
                                DigitalAssist.makeQuickPoem(self)
                                DigitalAssist.makeArt(self, self.Words)
                            else:
                                DigitalAssist.makeArt(self)
                        continue

                    elif ("play" in query2 or "script" in query2) and (
                            "make" in query2 or "write" in query2 or "create" in query2 or "mode" in query2):
                        # Call for the save file name after listing all of the subjects to the user
                        self.Type = 'AI Script Break'
                        self.Significance = '**AI content attached'

                        DigitalAssist.speak(self, 'I like your style, my man')

                        DigitalAssist.Make_Script(self)
                        DigitalAssist.speakSweet(self, self.Words)

                        s3 = False
                        # continue
                    elif ("go" in query2 or 'try' in query2 or "mode" in query2) and (
                            "greek" in query2 or "myth" in query2):
                        # Call for the save file name after listing all of the subjects to the user
                        self.Words = ''
                        self.Type = 'Greek Script Break'
                        self.Significance = '**AI content attached'
                        self.FileName = 'AI Going Greek'
                        self.Subject = 'AI Going Greek'
                        DigitalAssist.speak(self, 'I like your style, my man... Dont eat too much tzatziki!')
                        self.pb = s.PoemBot(1, 1, 1, 1, 40, 3)
                        self.pb.ReloadModel("model_Greek.h5")
                        self.pb.setupdata()
                        size = 3
                        trd = numpy.empty(size, dtype=str)
                        w = numpy.empty(size, dtype=str)
                        for i in range(0, size - 1):
                            globals()[f"trd{i}"] = threading.Thread(target=DigitalAssist.generateGreek(self))
                            w[i] = globals()[f"trd{i}"].start()  # starting the thread i

                        for i in range(0, size - 1):
                            threading.active_count()
                            threading.enumerate()
                            if i == 0:
                                self.Words += w[i]
                            else:
                                i2 = i - 1
                                globals()[f"trd{i2}"].join()
                                globals()[f"trd{i}"].join()
                                self.Words += w[i]
                                print(self.Words)

                        DigitalAssist.speak(self, self.Words)

                        continue
                    elif "stop recording" in query2 or "m all set" in query2 or "no thanks" in query2 or "stop recording" in query2 or "save" in query2 or "no" in query2:
                        # Call for the save file name after listing all of the subjects to the user
                        print(self.subject)
                        DigitalAssist.getfilename(self)
                        DigitalAssist.SaveText(self, self.transcript, self.FileName, self.subject)
                        DigitalAssist.add2Master(self.transcript)
                        s3 = False
                        s2 = False
                        continue


                    elif query2 == 'none':
                        zz = 1
                        # Event().wait(1)

                    else:
                        zz = 1
                        # Event().wait(1)

            elif self.query1 == 'none':
                # Event().wait(1)
                continue
            else:

                self.AI_Corrected_Text = DigitalAssist.cleanText(self, self.query1)
                DigitalAssist.adddata2DF(self)
                self.visualList += str(self.entry) + '). ' + self.query1 + ' \n'
                self.visualList2 += str(self.entry) + '). ' + self.AI_Corrected_Text + ' \n'
                self.entry += 1

            # Do the dataframe stuff here

    def makelist(self):
        self.entry = 1
        self.transcript2 = pd.DataFrame()
        # self.transcript = pd.DataFrame()
        DigitalAssist.createDF(self)
        self.subject = 'To Do'
        self.FileName = 'To Do '
        s2 = True
        DigitalAssist.getsubject(self)
        DigitalAssist.speak(self, "Please prepare for recording")
        print("Please prepare for recording...")
        self.visualList = ''
        self.visualList2 = ''
        self.Type = 'To Do list'
        self.Significance = 'High'
        while (s2 == True):
            self.xx = ''
            self.query1 = ''
            self.new_Query = ''
            self.Words = ''
            self.Notes = ''
            self.Added2TextFile = ''
            self.Completed = ''
            print(self.visualList)
            print(self.visualList2)
            self.query1 = DigitalAssist.transcribe_Build_Query(self, 1.3).lower()
            self.query1 = self.query1 + '.'

            if "stop recording" in self.query1 or "m all set" in self.query1 or "end list" in self.query1 or "stop listening" in self.query1 or "save this file" in self.query1 or "save this recording" in self.query1:
                # Call for the save file name after listing all of the subjects to the user
                DigitalAssist.SaveText(self, self.transcript, self.FileName, self.subject)
                DigitalAssist.add2Master(self.transcript)
                s2 = False
                sys.exit()
                continue

            elif "change subject" in self.query1 or "update subject" in self.query1 or "switch category" in self.query1 or "change category" in self.query1:
                # transcript2[self.subject] = [str(self.visualList)]
                # DigitalAssist.SaveText(self.transcript2, self.FileName + 'v2' + self.subject, self.subject)
                DigitalAssist.getsubject(self)

                continue
            elif self.query1 == 'none':
                continue

            else:
                self.AI_Corrected_Text = DigitalAssist.cleanText(self, self.query1)
                DigitalAssist.adddata2DF(self)
                self.visualList += str(self.entry) + '). ' + self.query1 + ' \n'
                self.visualList2 += str(self.entry) + '). ' + self.AI_Corrected_Text + ' \n'
                self.entry += 1


if __name__ == '__main__':
    # main method for executing
    # the functions
    Record = ''

    x = DigitalAssist(1)
    x.Take_query()

    # x.saveTranscript()
    atexit.register(x.saveTranscript)


    # Turn this back on after issue is understood

    # try:
    #     x = DigitalAssist(1)
    #     x.Take_query()
    #     x.saveTranscript()
    # except:
    #     x.saveTranscript()
    #     atexit.register(x.saveTranscript)

    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Above is code I did not write, below is code that allows user to update values of respective values
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    def getfilename(self):
        self.FileName = DigitalAssist.getdata(self, 'FileName')


    def getsubject(self):
        self.subject = DigitalAssist.getdata(self, 'subject')


    def getDictation_Type(self):
        self.Dictation_Type = DigitalAssist.getdata(self, 'Type')


    def getSignificance(self):
        self.Significance = DigitalAssist.getdata(self, 'Significance')


    def getNote(self):
        self.Notes += '|' + DigitalAssist.getdata(self, 'Notes')


    def getdata(self, Field):

        DigitalAssist.speak(self, 'what is the ' + Field)
        print('Please confirm the ' + Field)
        s = True
        Query = ''
        while (s == True):
            Query = DigitalAssist.getUserResponse(self)
            Query2 = ''
            WaitforResponse = False
            while (WaitforResponse == False):
                DigitalAssist.speak(self, Query + ' Is that correct?')
                Query2 = DigitalAssist.getUserResponse(self)
                if "yes" in Query2 or "correct" in Query2 or "ya" in Query2 or "yeah" in Query2:
                    DigitalAssist.speak(self, 'Thanks for confirming the ' + Field)
                    s = False
                    WaitforResponse = True
                    continue
                if "no" in Query2 or "wrong" in Query2 or "not it" in Query2 or "nope" in Query2:
                    DigitalAssist.speak(self, 'ok  please say the ' + Field + ' you want to set')
                    print('ok  please say the ' + Field + ' you want to set')
                    WaitforResponse = True
                    continue
                else:
                    DigitalAssist.speak(self, 'Lets try that again what is the ' + Field)
                    Event().wait(1)
                    continue
        return Query


    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################ below is code that allow me to confirm with the user the inputs are correct
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    def takeCommand(self):
        Query = DigitalAssist.getUserResponse(self, Response="Action Requested")
        return Query


    def getUserResponse(self, pause=.5, Response='You Said'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = pause
            audio = r.listen(source)
            try:
                Query = r.recognize_google(audio, language='en-in')
                DigitalAssist.Add2Transcript(self, self.UserName + ': ' + Query)
                print(Response + ": ", Query)

            except Exception as e:
                print(e)
                print("Please repeat Words not understood...")
                Query = DigitalAssist.getUserResponse(self)
                # Event().wait(2)
            return Query


    def ConfirmUR(self, prompt):
        DigitalAssist.speak(self, 'You Said ' + prompt + ' is this correct?')
        query = DigitalAssist.getUserResponse(self)

        if 'yes' in query or 'correct' in query or 'yeah' in query or 'submit' in query:
            self.promptB = True


    def editBotPrompt(self, message):
        DigitalAssist.speak(self, 'Edit Mode Activated', voice=4)
        DigitalAssist.speak(self, 'What do you want to use for a prompt?', voice=4)
        query = DigitalAssist.getUserResponse(self)

        if 'cancel' in query:
            r = message
            # Do nothing
        else:
            DigitalAssist.ConfirmBOT(self, query)
            if self.promptB == True:
                self.message = query


    def ConfirmBOT(self, message):
        DigitalAssist.speak(self, 'Chat GPT responded with: ' + message + ' do you want to use this prompt?', voice=4)
        query = DigitalAssist.getUserResponse(self)

        if 'yes' in query or 'correct' in query or 'yeah' in query or 'submit' in query:
            self.promptB = True

        if 'edit' in query or 'change' in query and ('prompt' in query or 'words' in query):
            DigitalAssist.editBotPrompt(self, message)


    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Above  is ChatGPT (I did not write original code but adapted for my use case)
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

    def editentry(self, Query1):
        DigitalAssist.Add2Transcript(self, ' \n')
        Prior_Mode = self.Mode
        self.Mode = 'Edit Mode'
        DigitalAssist.Add2Transcript(self, text2Add=(Prior_Mode + ' - ' + self.Mode + ':'))
        s = True
        while (s == True):
            DigitalAssist.speak(self, 'I am ready to make the edit please proceed')
            print('ready to make the edit please proceed')
            print('Original Entry: ' + Query1)
            Query2 = DigitalAssist.getUserResponse()

            ss = True
            while (ss == True):
                print(Query2)
                DigitalAssist.speak(self, Query2 + 'Are you satisfied with your edits?')
                print('Options: Yes/Correct, Not yet/Redo, Add as Note, Combine, Cancel')

                Query3 = DigitalAssist.getUserResponse(self)

                if "yes" in Query3 or "correct" in Query3 or "ya" in Query3 or "yeah" in Query3 or "looks good" in Query3 or "keep new" in Query3 or "new one" in Query3:
                    DigitalAssist.speak(self, 'Thanks for confirming, I will make the updates you provided')
                    print('Thanks for confirming, I will make the updates you provided')
                    Query_Final = Query2
                    s = False
                    ss = False


                elif "not yet" in Query3 or 'redo' in Query3 or 'try again' in Query3 or 'again' in Query3 or 'one more' in Query3:
                    DigitalAssist.speak(self, 'ok, lets go again')
                    print('ok, lets go again')
                    ss = False
                    continue

                elif "add as note" in Query3 or "include note" in Query3 or "as note" in Query3:
                    DigitalAssist.speak(self, 'Thanks for confirming, I will add this as a note')
                    print('Thanks for confirming, I will add this as a note')
                    Query_Final = ''
                    self.Notes = Query2
                    # when this is a class I can update the df for now I will add it to the end same as when I say combine them
                    s = False
                    ss = False

                elif "add to original" in Query3 or "both" in Query3 or 'combine' in Query3 or 'combination' in Query3 or 'merge' in Query3 or 'together' in Query3:
                    DigitalAssist.speak(self, 'Thanks for confirming, I will join the two thoughts')
                    print('Thanks for confirming, I will join the two thoughts')
                    Query_Final = Query1 + ' ' + Query2
                    # when this is a clas I can update the df for now I will add it to the end same as when I say combine them
                    s = False
                    ss = False

                elif 'cancel' in Query3 or 'end' in Query3 or 'stop' in Query3 or 'stop trying' in Query3:
                    DigitalAssist.speak(self, 'Thanks for confirming, I will remove these edits')
                    print('Thanks for confirming, I will remove these edits')
                    Query_Final = ''
                    s = False
                    ss = False

                else:
                    Event().wait(1)

        return Query_Final


    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################Long Code where I give Digital Assistant commands##    (user menus)
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

    def RunChatGPT(self):
        self.Mode = 'Chat GPT -  Menu'

        DigitalAssist.speak(self, self.Mode + ' What Chat GPT mode do you want to use?')

        print(self.Mode + ' What Chat GPT mode do you want to use?')

        s2 = True
        while (s2 == True):
            DigitalAssist.Add2Transcript(self, ' \n')
            query = DigitalAssist.takeCommand(self).lower()

            # Say Quick Art or Auto Art or Basic Art
            if 'normal' in query or 'conv' in query or 'reg' in query or 'talk' in query:
                prompt = DigitalAssist.ChatGPTDA(self)
                DigitalAssist.RunChatGPT(self)
                s2 = False

            elif "art" in query and ("basic" in query or "auto" in query or "quick" in query):
                DigitalAssist.quickArt(self)
                DigitalAssist.RunChatGPT(self)
                s2 = False

            # Say Prompted Art or super Art or advanced Art
            elif "art" in query and ("advance" in query or "super" in query or "open" in query or (
                    "with" in query and "prompt" in query)):
                prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True, UseArtPrompt=True)

                ArtPath = DigitalAssist.makeArt(self, prompt)
                DigitalAssist.RunChatGPT(self)
                s2 = False

            elif 'shake' not in query and ("inspire" in query or "unique" in query or ("own" in query) or (
                    "version" in query and "3" in query) or ('quick' in query and 'poem' in query) or (
                                                   "poem" in query or 'poetry' in query)):
                # make program to ask how spicy to make it lol
                Poem_Type = random.choices(up.Random_Poem)
                Poem_Type = Poem_Type[0]
                DigitalAssist.Quick_Poem_v1(self, GPTPrompt=Poem_Type)
                s2 = False
                DigitalAssist.RunChatGPT(self)


            elif "shake" in query and ("poem" in query or "poet" in query or ("version" in query and "1" in query)):
                DigitalAssist.Shake_Poem_v1(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)

            elif ("poem" in query or 'poetry' in query or 'shake' in query) and (
                    "inspire" in query or "unique" in query or ("make" in query or "own" in query) or (
                    "version" in query and "2" in query)):
                DigitalAssist.Shake_Poem_v2(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)


            elif ("sunday" in query and ('scary' in query or 'scaries' in query)) or (
                    "sunday" in query and ("poem" in query or "story" in query)):
                DigitalAssist.SundayScary_Poem(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)


            elif (("live" in query and 'art in query') or ('podcast' in query or 'stream' in query)):
                DigitalAssist.MakeArtLive(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)





            elif ('chorus' in query or 'song' in query) or ("brick" in query and ("sing" in query or "dj" in query)):

                Song_Genre = random.choices(up.Random_Song_Genre_List)
                Song_Genre = Song_Genre[0]
                Song_Genre = 'v3'
                # Song_Genre = 'techno'

                if 'v1' in Song_Genre:
                    DigitalAssist.Make_a_Song(self)
                    DigitalAssist.speak(self, 'Make a quick song Version 1 Complete')
                elif 'v2' in Song_Genre:
                    DigitalAssist.Make_a_Chorus(self)
                    DigitalAssist.speak(self, 'Make a quick song Version 2 Complete')
                elif 'v3' in Song_Genre:
                    DigitalAssist.Make_a_Song(self)
                    DigitalAssist.speak(self, 'Make a quick song Version 3 Complete')

                elif 'Techno' in Song_Genre:
                    DigitalAssist.Make_a_Chorus(self, Mode='Techno')
                    DigitalAssist.speak(self, 'Techno Lyrics Complete')
                    DigitalAssist.Sampler(self, Mode='Techno')
                    DigitalAssist.speak(self, 'Techno Samples Provided Complete', voice=9)
                elif Song_Genre == 'SadRap':
                    DigitalAssist.Make_a_Rap(self, Mode='SadRap')
                    DigitalAssist.speak(self, 'Sad Rap Lyrics Complete')
                elif Song_Genre == 'Reggae':
                    DigitalAssist.Make_a_Rap(self, Mode='Raggae')
                    DigitalAssist.speak(self, 'Reggae Lyrics Complete')
                elif Song_Genre == 'Rap':
                    DigitalAssist.Make_a_Rap(self, Mode='Rap')
                    DigitalAssist.speak(self, 'Rap Lyrics Complete')
                else:
                    DigitalAssist.Make_a_Rap(self, Mode='Raggae')
                    DigitalAssist.speak(self, 'Reggae Lyrics Complete')

                s2 = False
                DigitalAssist.RunChatGPT(self)



            elif 'basic' in query or 'shake' in query:
                DigitalAssist.makeQuickPoem(self)
                DigitalAssist.makeArt(self, self.Words)
                s2 = False
                DigitalAssist.RunChatGPT(self)


            elif 'dad' in query or 'timmy' in query or ' guy' in query or 'tim ' in query or (
                    ('simon' in query or 'old man' in query or 'timmy d' in query) and 'help' in query) or (
                    'timmy' in query and 'd' in query):
                DigitalAssist.TimmyDMode(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)

            elif 'blog' in query or 'website post' in query or 'post' in query:
                Blog_Topic = random.choices(up.Random_Blog_Topic)

                Blog_Topic = Blog_Topic[0]

                # DigitalAssist.makeBlogPost(self, GPTprompt=Blog_Topic)
                # DigitalAssist.makeBlogPost(self, GPTprompt=up.RandomTopic)
                DigitalAssist.makeBlogPost(self, GPTprompt=up.CorrectText)

                s2 = False
                DigitalAssist.RunChatGPT(self)


            # Make a program that makes a short background for a character, also have a duo/relationship of some sort and make an interesting scene for a play/screenplay

            elif 'wiki' in query or 'wikipedia' in query or (
                    ('pen name' in query or 'page' in query or 'mode' in query) and 'wiki' in query):
                DigitalAssist.Wiki4PenNames(self)
                s2 = False
                DigitalAssist.RunChatGPT(self)


            elif 'cancel' in query or 'stop' in query or 'quit' in query or 'done' in query or 'exit' in query:
                DigitalAssist.saveTranscript(self)
                sys.exit()
                s2 = False

            else:
                print('Please try again, ')
                continue


    # def Shake_Art_v1(self, prompt)

    def YayorNay(self):
        self.Mode = 'Yay or Nay -  Menu'

        DigitalAssist.speak(self, self.Mode + ' What did you think ' + self.UserName)

        print(self.Mode + ' What did you think ' + self.UserName)

        s2 = True
        while (s2 == True):
            DigitalAssist.Add2Transcript(self, ' \n')
            query = DigitalAssist.takeCommand(self).lower()

            # Say Quick Art or Auto Art or Basic Art
            if 'awesome' in query or 'love' in query or 'yay' in query or 'yes' in query or 'best' in query:
                rr = '- Sounded Great'
                s2 = False
                continue

            elif 'good' in query or 'love' in query or 'yay' in query or 'yes' in query:
                rr = '- Good - POTENTIAL HERE'
                s2 = False
                continue

            elif 'ok' in query or 'okay' in query or 'not bad' in query or 'so so' in query:
                rr = ' - So So'
                s2 = False

            elif 'no' in query or 'hate' in query or 'bad' in query or 'terrible' in query or 'yuck' in query:
                rr = ' - BAD'
                s2 = False
            else:
                rr = ''
                s2 = False

        return rr


    # Main Menu
    def Take_query(self):
        DigitalAssist.Hello(self)

        self.Mode = 'Main Menu'
        # DigitalAssist.Add2Transcript(self,text2Add= ( self.Mode + ':'))
        s2 = True
        while (s2 == True):
            self.Mode = 'Main Menu'
            DigitalAssist.speak(self, self.Mode)
            query = DigitalAssist.takeCommand(self).lower()
            # DigitalAssist.Add2Transcript(self,text2Add=query)
            if "company dashboard" in query or "open dashboard" in query:
                DigitalAssist.speak(self, "Opening MondDay Vert's Dasboard, good luck with your work!")

                # in the open method we just to give the link
                # of the website and it automatically open
                # it in your default browser
                Mondevert = "http://mondeVert.co"
                godaddy = 'https://dashboard.godaddy.com/'
                Mail = 'https://outlook.office.com/mail/'
                Square_store = 'https://square.online/app/home/'
                DigitalAssist.Open_Web(Mail)
                DigitalAssist.Open_Web(Square_store)
                DigitalAssist.Open_Web(Mondevert)
                DigitalAssist.Open_Web(godaddy)
                continue

            elif "pay bills" in query or "pay credit cards" in query:
                DigitalAssist.speak(self,
                                    "Bills Suck man, at least you are getting them done, Hope you have a nice day!")

                Liberty_Bay_CC = "https://www.myaccountaccess.com/onlineCard/login.do"
                Home_Depot_CC = 'https://citiretailservices.citibankonline.com/RSnextgen/svc/launch/index.action?siteId=PLCN_HOMEDEPOT#signon'
                Macys_CC = 'https://www.macys.com/my-credit/gateway/guest'
                Insurance = 'https://customer.concordgroupinsurance.com/ccp/login'
                National_Grid = 'https://login.nationalgridus.com/loginnationalgridus.onmicrosoft.com/oauth2/v2.0/authorize?cancel_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauth%2Fsso%2FNGP_SignIn_MA_Electric_Home&client_id=88d004b4-3d39-4599-b410-093849907ee5&customer_type=home&p=B2C_1A_UWP_NationalGrid_convert_merge_signin&redirect_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauthcallback%2FNGP_SignIn_MA_Electric_Home&region=masselec&response_type=code&scope=https%3A%2F%2Flogin.nationalgridus.com%2Fapi%2Fread+openid+profile+email+offline_access&state=CAAAAYUokN2YMDAwMDAwMDAwMDAwMDAwAAAA8Iy1JaCJ8hTkDIfqZ5i6KE2oIrQFv5bPH9zBI_P-5wWki9riiDhgLKrNlnVD4FeR38QBEzYH17vRm_CbsR8msY3J3fEDKFqtBsup_Bp9KwM-Flb38WYF6YqeqejsI-Iuj-yWpXfajw6-QKG_DMoOBtkqcL8zubs4c8KgKiuF-yIk3yoa1_vp_KqVAuBw0DSopTJrDwsYAZN5qW9zaUmwyW-wk6zbTNddqu24EJObkHkfEGKHEKQwrqArl40WukP3dxbKBfj7sSMhdqjTPa0ido8%3D&switch_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fs%2Flogin'
                LLBean_CC = 'https://citiretailservices.citibankonline.com/RSauth/signon?pageName=signon&siteId=PLCN_LLBEAN&langId=en_US'
                Amazon_CC = 'https://secure07ea.chase.com/web/auth/#/logon/logon/chaseOnline'
                DigitalAssist.Open_Web(Liberty_Bay_CC)
                DigitalAssist.Open_Web(Home_Depot_CC)
                DigitalAssist.Open_Web(Macys_CC)
                DigitalAssist.Open_Web(Insurance)
                DigitalAssist.Open_Web(National_Grid)
                DigitalAssist.Open_Web(LLBean_CC)
                DigitalAssist.Open_Web(Amazon_CC)
                continue


            elif ("chat" in query and "bot" in query) or ("gpt" in query and "chat" in query) or (
                    "smart" in query and "assist" in query) or ("extra" in query and "help" in query) or (
                    "artificial" in query and "intellig" in query):

                DigitalAssist.RunChatGPT(self)
                DigitalAssist.speak(self, "High Tech!")
                # prompt = DigitalAssist.ChatGPTDA(self)
                continue

            elif ("make" in query and "art" in query) or ("make" in query and "picture" in query) or (
                    "ai" in query and "art" in query) or ("art" in query and "mode" in query) or (
                    "super" in query and "shake" in query and 'art' in query):

                DigitalAssist.speak(self, "High Tech and sheek!")
                if 'super' in query or 'using' in query or 'extra' in query:
                    if 'poem' in query or 'shake' in query or 'poet' in query:
                        DigitalAssist.makeQuickPoem(self)
                        prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True, Prompt=(
                                    'make a prompt for openai  DALL-E program to create a work of art that is based on the following poem. ' + '\n' + '\n' + self.Words))
                        DigitalAssist.makeArt(self, prompt)
                    else:
                        prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True)
                        DigitalAssist.makeArt(self, prompt)

                else:

                    if 'poem' in query or 'shake' in query or 'poet' in query:
                        DigitalAssist.makeQuickPoem(self)
                        DigitalAssist.makeArt(self, self.Words)
                    else:
                        DigitalAssist.makeArt(self)
                        continue



            elif "stop" in query or "all set" in query or "quit" in query or "m done" in query or "thank" in query or "peace out" in query:
                DigitalAssist.speak(self, "Happy to help, Peace out brothah man")
                s2 = False

            elif (
                    "record" in query or "listen up" in query or "can you right" in query or "record mode" in query or "transcribe" in query or "could you write" in query or "transcribe" in query or "can you write" in query) and 'stop' not in query:
                DigitalAssist.speakSweet(self, "Dictated but not Red Mode Activated")
                DigitalAssist.transcribe(self)
                continue


            elif ("blog" in query) and (
                    "create" in query or "together" in query or "put" in query or "make" in query) or (
                    "add" in query and "blog" in query):
                DigitalAssist.speakSweet(self,
                                         "Mon Day Vert is lucky to have a great CEO this is going to be a great post!")
                DigitalAssist.CompileBlog(self)
                DigitalAssist.speakSweet(self, "Blog Consolidation Complete Shane D")
                continue

            elif (("consolidate" in query or "compile" in query or "collect" in query) and (
                    "file" in query or "folder" in query or "list" in query)) or ("add" in query and "master" in query):
                DigitalAssist.speakSweet(self, "Consolidation in progress")
                DigitalAssist.compileFiles(self)
                DigitalAssist.speakSweet(self, "Consolidation Complete my dude")
                continue

            elif "make list" in query or " list" in query or "to do" in query or "tracker" in query or "checklist" in query or "make a plan" in query or "quick note" in query or "quick plan" in query or "take note" in query:
                # DigitalAssist.speak("Sure thing, One moment while I prepare")
                DigitalAssist.makelist(self)
                continue


            elif "poetic" in query or "swoon me" in query or "me a poem" in query or "poem" in query or "while I think you" in query or "poetry will help me think" in query or "write me a poem" in query or "we need some inspiration" in query or "some art" in query or "be creative" in query or "inspire me" in query:
                x22 = s.PoemBot(1, 1, 1, 1, 40, 3)
                x22.ReloadModel("model.h5")
                x22.setupdata()
                self.Words = x22.shakesbot_DA()
                print(self.Words)
                DigitalAssist.speakSweet(self, self.Words)
                continue




            elif ("play" in query or "script" in query) and (
                    "make" in query or "write" in query or "create" in query or "mode" in query):
                # Call for the save file name after listing all of the subjects to the user
                self.Words = ''
                self.Correction_Comment = ''
                self.Type = 'AI Script Break'
                self.Significance = '**AI content attached'
                self.FileName = 'AI ShakeScript'
                self.Subject = 'AI ShakeScript'
                DigitalAssist.speak(self, 'I like your style, my man')

                DigitalAssist.Make_Script(self)

                DigitalAssist.speakSweet(self, self.Words)
                s3 = pd.DataFrame()
                s3['Script'] = [self.Words]
                s3['Script - Corrected'] = [self.AI_Corrected_Content]
                s3['Correction Comment'] = [self.Correction_Comment]
                DigitalAssist.SaveText(self, s3, self.FileName, self.Subject)
                continue

            elif ("go" in query or 'try' in query or "mode" in query) and ("greek" in query or "myth" in query):
                # Call for the save file name after listing all of the subjects to the user
                self.Words = ''
                self.Type = 'Greek Script Break'
                self.Significance = '**AI content attached'
                self.FileName = 'AI Going Greek'
                self.Subject = 'AI Going Greek'
                DigitalAssist.speak(self, 'I like your style, my man... Dont eat too much tzatziki!')
                self.pb = s.PoemBot(1, 1, 1, 1, 40, 3)
                self.pb.ReloadModel("model_Greek.h5")
                self.pb.setupdata()
                size = 3
                trd = numpy.empty(size, dtype=str)
                w = numpy.empty(size, dtype=str)
                for i in range(0, size - 1):
                    globals()[f"trd{i}"] = threading.Thread(target=DigitalAssist.generateGreek(self))
                    w[i] = globals()[f"trd{i}"].start()  # starting the thread i

                for i in range(0, size - 1):
                    threading.active_count()
                    threading.enumerate()
                    if i == 0:
                        self.Words += w[i]
                    else:
                        i2 = i - 1
                        globals()[f"trd{i2}"].join()
                        globals()[f"trd{i}"].join()
                        self.Words += w[i]
                        print(self.Words)

                DigitalAssist.speak(self, self.Words)
                s3 = pd.DataFrame()
                s3['Script'] = [self.Words]
                DigitalAssist.SaveText(self, s3, self.FileName, self.subject)
                continue



            elif "social media" in query or "marketing" in query:
                DigitalAssist.speak(self, "Will do")

                # in the open method we just to give the link
                # of the website and it automatically open
                # it in your default browser
                Facebook = "https://www.facebook.com/"
                Insta = 'https://www.instagram.com/'
                TikTok = 'https://www.tiktok.com/'
                Twitter = 'https://twitter.com/home'
                DigitalAssist.Open_Web(Facebook)
                DigitalAssist.Open_Web(TikTok)
                DigitalAssist.Open_Web(Twitter)
                DigitalAssist.Open_Web(Insta)
                continue

            elif "open google" in query:
                DigitalAssist.speak(self, "Opening Google ")
                url = "http://google.com"
                DigitalAssist.Open_Web(url)
                continue



            elif (("voice" in query or "person" in query or "bot" in query or "ai" in query) and (
                    "change" in query or "update" in query or "switch" in query or "set" in query)):

                if "quick" in query or "manual" in query:
                    DigitalAssist.Setvoices(self, Quick=True)
                    print('Quick mode activated')
                else:
                    DigitalAssist.Setvoices(self)
                continue

            elif "s the date" in query:
                DigitalAssist.tellDay(self)
                continue

            elif "the time" in query or "what time" in query or "clock mode" in query:
                DigitalAssist.tellTime(self)
                continue

            # this will exit and terminate the program
            elif "bye" in query:
                DigitalAssist.speak(self, "Peace Out!")
                s2 = False

            elif "from wikipedia" in query or "wikipedia" in query:
                DigitalAssist.speak(self, "Checking the wikipedia ")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=4)
                DigitalAssist.speak(self, "According to wikipedia")
                DigitalAssist.speak(self, result)



            elif "tell me your name" in query or "your name" in query or "introduce yourself" in query or "introduce your self" in query:
                DigitalAssist.speak(self,
                                    "I am Big Master Funk the fourth also known as Brick top, AND i AM  Your personal desktop Assistant")


            elif "shut up" in query:
                DigitalAssist.speak(self, "my bad I am tripping, I will leave you be Shane D")
                s2 = False

            else:
                # uk = cs.DA_Unknown_Command()
                # DigitalAssist.speak(uk)
                # print(uk)
                # Event().wait(1)
                continue


    def transcribe(self):
        self.entry = 1

        DigitalAssist.createDF(self)
        self.subject = 'Default'
        self.FileName = 'Default'
        s2 = True
        DigitalAssist.getsubject(self)
        self.visualList = 'Subject: ' + self.subject + ' \n'
        self.visualList2 = 'Subject*: ' + self.subject + ' \n'
        DigitalAssist.speak(self, "Please prepare for recording")
        print("Please prepare for recording...")
        while (s2 == True):
            xx = ''
            self.query1 = ''
            self.new_Query = ''
            self.Type = ''
            self.Significance = ''
            self.Words = ''
            self.Notes = ''
            self.Added2TextFile = ''
            self.Completed = ''
            print(self.visualList)
            print(self.visualList2)
            self.query1 = DigitalAssist.transcribe_Build_Query(self, 1.44).lower()
            self.query1 = self.query1 + '.'
            self.Type = 'Original'
            self.Significance = 'Default'

            if "stop recording" in self.query1 or "m all set" in self.query1 or "end list" in self.query1 or "stop listening" in self.query1 or "save this file" in self.query1 or "save this recording" in self.query1:
                # Call for the save file name after listing all of the subjects to the user
                DigitalAssist.getfilename(self)
                DigitalAssist.SaveText(self, self.transcript, self.FileName, self.subject)
                DigitalAssist.add2Master(self.transcript)
                s2 = False
                DigitalAssist.saveTranscript(self)
                sys.exit()
                continue


            elif ((
                          "brick top" in self.query1 or "bricktop" in self.query1 or "show me" in self.query1 or "extra" in self.query1 or "additional" in self.query1) and (
                          "option" in self.query1 or "tool" in self.query1)) or ("edit mode" in self.query1) or (
                    "need to" in self.query1 and "make edit" in self.query1):
                s3 = True
                while (s3 == True):
                    # this is where you say next steps (This can be a separate function)
                    query2 = DigitalAssist.transcribe_Build_Query_Pause(self).lower()
                    print(query2)

                    if "continue" in query2 or "just thinking" in query2 or "yes" in query2 or "chill" in query2 or "just thinking" in query2 or "keep going" in query2:
                        DigitalAssist.speak(self, 'no worries, still here')
                        s3 = False
                        # continue



                    elif "change subject" in self.query1 or "update subject" in self.query1 or "switch category" in self.query1 or "change category" in self.query1:
                        # transcript2[self.subject] = [str(self.visualList)]
                        # DigitalAssist.SaveText(self.transcript2, self.FileName + 'v2' + self.subject, self.subject)
                        DigitalAssist.getsubject(self)
                        s3 = False
                        # continue


                    elif "change" in query2 or "fix" in query2 or "edit" in query2 or "fix that" in query2 or "not quite" in query2 or "review last" in query2 or "back to me" in query2 or "read that back" in query2:
                        # Call for the save file name after listing all of the subjects to the user
                        self.Type = 'Edited'
                        self.Significance = 'Review edits'
                        self.new_Query = DigitalAssist.editentry(self, self.query1)
                        s3 = False
                        # continue


                    elif "while I think you" in query2 or "poetry will help me think" in query2 or "write me a poem" in query2 or "we need some inspiration" in query2 or "some art" in query2 or "be creative" in query2 or "inspire me" in query2 or (
                            "poem" in query2 and ("write" in query2 or "create" in query2 or "shake" in query2)):
                        # Call for the save file name after listing all of the subjects to the user
                        self.Type = 'Poetry Break'
                        self.Significance = '**AI content attached'
                        DigitalAssist.speakSweet(self, 'I like your style, Shane you are brilliant and beautiful')
                        x = s.PoemBot(1, 1, 1, 1, 40, 3)
                        x.ReloadModel("model.h5")
                        x.setupdata()
                        self.Words += x.shakesbot_DA()
                        print(self.Words)
                        DigitalAssist.speakSweet(self, self.Words)
                        s3 = False
                        # continue

                    elif ("chat" in query2 and "bot" in query2) or ("gpt" in query2 and "chat" in query2) or (
                            "smart" in query2 and "assist" in query2) or ("extra" in query2 and "help" in query2):
                        DigitalAssist.speak(self, "High Tech!")
                        prompt = DigitalAssist.ChatGPTDA(self)
                        self.Type = 'AI Conversation with Chat GPT'
                        self.Words += prompt
                        self.Significance = '**AI content attached'
                        continue

                    elif ("make" in query2 and "art" in query2) or ("make" in query2 and "picture" in query2) or (
                            "ai" in query2 and "art" in query2) or ("art" in query2 and "mode" in query2) or (
                            "super" in query2 and "shake" in query2 and 'art' in query2):

                        DigitalAssist.speak(self, "High Tech and sheek!")
                        if 'super' in query2 or 'using' in query2 or 'extra' in query2:
                            if 'poem' in query2 or 'shake' in query2 or 'poet' in query2:
                                DigitalAssist.makeQuickPoem(self)
                                prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True, Prompt=(
                                            'Using the poem that follows make a prompt to create a work of art that describes the feelings or the scene that fits the poem. ' + '\n' + '\n' + self.Words))
                                DigitalAssist.makeArt(self, prompt)
                            else:
                                prompt = DigitalAssist.ChatGPTDA(self, MakeArt=True)
                                DigitalAssist.makeArt(self, prompt)
                            self.Type = 'AI Made Art - Add to BLOG?'
                            self.Words += prompt
                            self.Significance = '**AI content Please see image that goes with prompt'
                        else:

                            if 'poem' in query2 or 'shake' in query2 or 'poet' in query2:
                                DigitalAssist.makeQuickPoem(self)
                                DigitalAssist.makeArt(self, self.Words)
                            else:
                                DigitalAssist.makeArt(self)
                        continue

                    elif ("play" in query2 or "script" in query2) and (
                            "make" in query2 or "write" in query2 or "create" in query2 or "mode" in query2):
                        # Call for the save file name after listing all of the subjects to the user
                        self.Type = 'AI Script Break'
                        self.Significance = '**AI content attached'

                        DigitalAssist.speak(self, 'I like your style, my man')

                        DigitalAssist.Make_Script(self)
                        DigitalAssist.speakSweet(self, self.Words)

                        s3 = False
                        # continue
                    elif ("go" in query2 or 'try' in query2 or "mode" in query2) and (
                            "greek" in query2 or "myth" in query2):
                        # Call for the save file name after listing all of the subjects to the user
                        self.Words = ''
                        self.Type = 'Greek Script Break'
                        self.Significance = '**AI content attached'
                        self.FileName = 'AI Going Greek'
                        self.Subject = 'AI Going Greek'
                        DigitalAssist.speak(self, 'I like your style, my man... Dont eat too much tzatziki!')
                        self.pb = s.PoemBot(1, 1, 1, 1, 40, 3)
                        self.pb.ReloadModel("model_Greek.h5")
                        self.pb.setupdata()
                        size = 3
                        trd = numpy.empty(size, dtype=str)
                        w = numpy.empty(size, dtype=str)
                        for i in range(0, size - 1):
                            globals()[f"trd{i}"] = threading.Thread(target=DigitalAssist.generateGreek(self))
                            w[i] = globals()[f"trd{i}"].start()  # starting the thread i

                        for i in range(0, size - 1):
                            threading.active_count()
                            threading.enumerate()
                            if i == 0:
                                self.Words += w[i]
                            else:
                                i2 = i - 1
                                globals()[f"trd{i2}"].join()
                                globals()[f"trd{i}"].join()
                                self.Words += w[i]
                                print(self.Words)

                        DigitalAssist.speak(self, self.Words)

                        continue
                    elif "stop recording" in query2 or "m all set" in query2 or "no thanks" in query2 or "stop recording" in query2 or "save" in query2 or "no" in query2:
                        # Call for the save file name after listing all of the subjects to the user
                        print(self.subject)
                        DigitalAssist.getfilename(self)
                        DigitalAssist.SaveText(self, self.transcript, self.FileName, self.subject)
                        DigitalAssist.add2Master(self.transcript)
                        s3 = False
                        s2 = False
                        continue


                    elif query2 == 'none':
                        zz = 1
                        # Event().wait(1)

                    else:
                        zz = 1
                        # Event().wait(1)

            elif self.query1 == 'none':
                # Event().wait(1)
                continue
            else:

                self.AI_Corrected_Text = DigitalAssist.cleanText(self, self.query1)
                DigitalAssist.adddata2DF(self)
                self.visualList += str(self.entry) + '). ' + self.query1 + ' \n'
                self.visualList2 += str(self.entry) + '). ' + self.AI_Corrected_Text + ' \n'
                self.entry += 1

            # Do the dataframe stuff here


    def makelist(self):
        self.entry = 1
        self.transcript2 = pd.DataFrame()
        # self.transcript = pd.DataFrame()
        DigitalAssist.createDF(self)
        self.subject = 'To Do'
        self.FileName = 'To Do '
        s2 = True
        DigitalAssist.getsubject(self)
        DigitalAssist.speak(self, "Please prepare for recording")
        print("Please prepare for recording...")
        self.visualList = ''
        self.visualList2 = ''
        self.Type = 'To Do list'
        self.Significance = 'High'
        while (s2 == True):
            self.xx = ''
            self.query1 = ''
            self.new_Query = ''
            self.Words = ''
            self.Notes = ''
            self.Added2TextFile = ''
            self.Completed = ''
            print(self.visualList)
            print(self.visualList2)
            self.query1 = DigitalAssist.transcribe_Build_Query(self, 1.3).lower()
            self.query1 = self.query1 + '.'

            if "stop recording" in self.query1 or "m all set" in self.query1 or "end list" in self.query1 or "stop listening" in self.query1 or "save this file" in self.query1 or "save this recording" in self.query1:
                # Call for the save file name after listing all of the subjects to the user
                DigitalAssist.SaveText(self, self.transcript, self.FileName, self.subject)
                DigitalAssist.add2Master(self.transcript)
                s2 = False
                sys.exit()
                continue

            elif "change subject" in self.query1 or "update subject" in self.query1 or "switch category" in self.query1 or "change category" in self.query1:
                # transcript2[self.subject] = [str(self.visualList)]
                # DigitalAssist.SaveText(self.transcript2, self.FileName + 'v2' + self.subject, self.subject)
                DigitalAssist.getsubject(self)

                continue
            elif self.query1 == 'none':
                continue

            else:
                self.AI_Corrected_Text = DigitalAssist.cleanText(self, self.query1)
                DigitalAssist.adddata2DF(self)
                self.visualList += str(self.entry) + '). ' + self.query1 + ' \n'
                self.visualList2 += str(self.entry) + '). ' + self.AI_Corrected_Text + ' \n'
                self.entry += 1





if __name__ == '__main__':
    # main method for executing
    # the functions
    Record = ''

    x = DigitalAssist(1)
    x.Take_query()

    # x.saveTranscript()
    atexit.register(x.saveTranscript)

# Turn this back on after issue is understood

# try:
#     x = DigitalAssist(1)
#     x.Take_query()
#     x.saveTranscript()
# except:
#     x.saveTranscript()
#     atexit.register(x.saveTranscript)
