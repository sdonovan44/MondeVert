#
# from ffmpeg import Progress
# from ffmpeg.asyncio import FFmpeg
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import smtplib

import random
from MondeVert_IP.SHAINE_MonderVert import Instagram_Posts as IP
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Long_User_Prompts as lup
import shutil
from docx import Document
import pandas as pd
import pyttsx3
import datetime
import re
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
from tempfile import gettempdir
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Stories_For_Audio_Files as SAF
import MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS.User_Prefs as up
from MondeVert_IP.SHAINE_MonderVert.Utilities import DoNotCommit as DNC

from MondeVert_IP.SHAINE_MonderVert import SHAINE as GPT
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Stories_For_Audio_Files as sfa



current_time1 = datetime.datetime.now()
current_time = current_time1.strftime('%m-%d-%Y_%H.%M')



def Check_Folder_Exists(SavePath):
    try:
        isExist = os.path.exists(SavePath)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(SavePath)
            print("Created new filePath: " + SavePath)
    except:
        dn = True





def speak(self, audio, Add2T=True, voice=''):
    if voice == '':
        voice = self.voice

    if Add2T == True:
        Add2Transcript(self, self.AssistantName + ': ' + audio)
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




def Add2Transcript(self, text2Add):
    transcript_Final = ''
    transcript_Final += text2Add + ' \n'
    current_time1 = datetime.datetime.now()
    current_time = current_time1.strftime('%m-%d-%Y_%H.%M.%S')

    data = [(current_time, text2Add)]
    print(data)
    try:
        df1 = pd.DataFrame(data, columns=["TimeStamp", "Transcript"])
        add2Master2(df1)
    except:
        print('Error could not add to transcript')

def add2Master2(df1):
     f2 = up.getMF2Path()
     df2 = pd.read_excel(f2)
     df3 = pd.concat([df1, df2])
     df3.iloc[:, 1:]
     df3.drop_duplicates()

     # creating a new excel file and save the data
     df3.to_excel(f2, index=False)







def SaveCSV(Text, Title, SavePath):


    Title1  = CleanFileName(Title)
    folder = str(Title1)
    if len(folder) > 44:
        folder = folder[0:44]
    Title1 = '\\' + str(Title1) + "_"
    if len(Title1) > 44:
        Title1 = Title1[0:44]

    Title2 = SavePath + Title1  + '.txt'

    Check_Folder_Exists(SavePath)


    Text1 = ('Time: ' + str(current_time) + '| Title:' + Title+'| Text:' + Text)

    Data1 = [(Text1)]


    try:
        df1 = pd.DataFrame(data=Data1)
        df1.to_csv(Title2)
        print(Title2)
    except:
        print('Review Error File did not save ')
    try:

        # MondeVert_IP.SaveText(self,df1,'MondeVert_IP Assistant', 'Full Transcript')
        add2Master2(df1)

    except:
        print('Review  did not save to master df2 file ')

    return Title2


# ********************************
"""Getting Started Example for Python 2.7+/3.3+"""

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).

from pydub import AudioSegment
def Combine_Splitsof_audio(AudioFiles_ordered,FilePath, SavePath = up.SavePath,Opening_Sound = up.MondeVertIntro, Voice = random.choices(SAF.Original_List_of_Voices_English)[0]):
    Check_Folder_Exists(SavePath)
    Merged_Audio = Opening_Sound

    counter = 1
    len_Audio = len(AudioFiles_ordered)
    for x in range (0,len_Audio):
        if x ==0:
            #print(Opening_Sound)
            Opening = AudioSegment.from_mp3(Opening_Sound)
            Merged_Audio = Opening

        else:
            sound2add = AudioSegment.from_mp3(AudioFiles_ordered[x])
            Merged_Audio += sound2add

    try:
    # simple export
         FilePath = Merged_Audio.export(FilePath, format="mp3")
    except:
         print('could not save file audio file')
    #     FilePath = 'No File Saved'

    return FilePath

#on character list Have Narrator Scene (stern and manly) and then you have preferred Narrators to choose from (to do all other narrations)
#Split on Space and :
#also look for Narrator, for now we should mostly ignore whats in the parenthesis so I will work to remove these
#Setting and other parts are Narrator1, and then narrator2
#def SplitScriptbyPart(Script,Character_Voice_Relationship,FileName,SavePath )
#remove (voiceover), otherwise have the system remove anywhere that has the parenthesis as its not important for audio
#(in person) (on the phone)
#Grab the Left most item on the line
#Def Clean_Text_For_Script

#Remove - FADE OUT.
#(Impressed) dip in the voice idk
#(defeated)/(Nervous) make quieter -2/(relieved) quiet but happy

#(Excited).(Urgently)/(upset)  - speed up maybe --> Make it louder

#other parenthesis should be spoken by one of the narrators or just the one

# not sure what to do maybe add a pause or something like that(smiles)
#Replace with onomonapea
#(sighs)
#(Laughs)


#Remove the reduandant parts like out loud and voiceover etc. eventually I can key off this but dont need it
#if line above is NULL or " " then you look for : if no : then ignore the line completely
#if the line says Music: send to GPT to come up with a quick prompt to relate it to the story/scene
#Make sure to add results to a script so we can use it again (Call it on the fly Revisions)
#if line says Narrator, remove parenthesis and just talk for the most part
#If its not a scenario above it is a character so we identify the name prior to the : and after the line before that is NULL or " "
#We eventually try to map the name to a voice and then we use the same voice for the character (for now we can live with random and maybe assign it and remove it from the list)
#We will eventually have the narrator say the lines that are in parenthesis, we can have the words split up or something


def Split_Audio(Text, SavePath, FileName,FilePath = '', OpeningSound = up.MondeVertIntro, Chunk_Limit = 1500, Voice = random.choices(SAF.Original_List_of_Voices_English)[0], Translate = sfa.Translation_Languages_Testing, Chunk_Replaces = ['.','?','\n'], Chunk_Delimiter = '!',Artist_Persona = 'embrace the spirit and culture of the following text describe it to be illustrated by an artist'):
    Length_Text = len(Text)
    Chunk_Limit = Chunk_Limit -20
    Text_Chunks = []
    Text_New = Text
    FilePaths = []
    length = len(Text)
    Audio_File_Count= 1
    SavePath_Chunks = SavePath + r'\Audio Chunks'
    Check_Folder_Exists(SavePath)
    Check_Folder_Exists(SavePath_Chunks)
    RunningCheck = 0
    LastPunc = 100
    New_Text_Translated=[]

    while  LastPunc != -1:
        Text_Chunk = Text_New[:Chunk_Limit]
        for i in Chunk_Replaces:
            Text_Chunk_Info_only = Text_Chunk.replace(i, Chunk_Delimiter)


            #Text_Chunk_Info_only = Text_Chunk.replace('.','!')
            #Text_Chunk_Info_only = Text_Chunk_Info_only.replace('?', '!')

        #print(Text_Chunk_Info_only)
        # print('Last Punc Position')
        # print(LastPunc)
        LastPunc =Text_Chunk_Info_only.rfind(Chunk_Delimiter)

        # print('Last Punc Position')
        # print(LastPunc)
        Audio_File_Count = 1
        Text_Chunk_Final = Text_New[:LastPunc]
        Voices = []
        countl = 0
        TranslateLanguages = []
        for l in Translate:
            Voices.append(SAF.Pick_Voice(Language=l))
            New_Text_Translated.append('Voice: ' + str(Voices[countl]) + '   '  + str(l) + '_Translation_: ')
            countl += 1

        countl = 0
        for l in Translate:
            # print(l)
            # print(countl)
            # print(Voices[countl])
            # print(New_Text_Translated[countl])
            New_Text_Translated_Temp = ''

            #print(Text_Chunk_Final)
            x = GPT.MondeVert()
            if l != 'English':

                tempTranslate = x.Translate(Text = Text_Chunk_Final, Language_Final=l)
                Translate_Voice = Voices[countl]
                New_Text_Translated[countl] += tempTranslate
                try:
                    FilePath = SaveText2Audio(Text=Text_Chunk_Final, SavePath=SavePath_Chunks,
                                          FileName=FileName + '_Chunk_'+ str(l) + '_' + str(Audio_File_Count),
                                          Voice=Translate_Voice)
                except:
                    print('Error could not create audio for this text')
                try:
                    ArtPrompt = x.GPTArt2( User_Subject='Create a prompt for an artist to create a work of art based on the following text: '  +tempTranslate, ArtFormat=Artist_Persona + 'adapt the text to a person from a country that speaks: '+ str(l))
                except:
                    ArtPrompt = Artist_Persona + tempTranslate
                    ArtPrompt[:313]
#+ 'Embrace/depict the cultures around the world that speak '


                try:
                    PicPath = x.makeArt(Prompt=ArtPrompt)
                    newPicPath = FilePath[:-4] + '.png'
                    shutil.copy(PicPath,newPicPath)
                except:
                    print('Art not made, not an issue for now, maybe down the road')
                print('successfully made a work of art in foreign language')
                if LastPunc == -1:
                    SaveCSV(SavePath=SavePath, Title= FileName+l, Text=New_Text_Translated[countl])

            else:
                FilePath = SaveText2Audio(Text = Text_Chunk_Final, SavePath = SavePath_Chunks, FileName=FileName + '_Chunk_' +str(Audio_File_Count), Voice = Voice )
                ArtPrompt = x.GPTArt2(User_Subject='Create a prompt for an artist to create a work of art based on the following text: ' + Text_Chunk_Final)
                try:
                    PicPath = x.makeArt(Prompt=ArtPrompt)
                    newPicPath = FilePath[:-4] + '.png'
                    shutil.copy(PicPath, newPicPath)
                except:
                    print('Art not made, not an issue for now, maybe down the road')


            FilePaths.append(FilePath)
            Text_Chunks.append(Text_Chunk_Final)
            RunningCheck +=len(Text_Chunk_Final)
            Audio_File_Count +=1

            countl += 1

        FilePath2 = FilePaths[0]
        try:
            #length = len(Text_New)
            New_pos = (LastPunc + 1)
            Text_New = Text_New[New_pos:]
            #length = len(Text_New)
        except:
            print('Review Error Triggered, could be just how this has to work')
            #print(Text_New)
            #print(len(Text_New))
    # try:
    #     FilePath2 = Combine_Splitsof_audio(AudioFiles_ordered = FilePaths, FilePath=FilePath,SavePath= SavePath)
    # except:
    #     FilePath2 = FilePaths[0]

        print('Error COuld not parse files together, see chunks for now')
    return FilePath2

def CleanFileName(Text):
    Text = re.sub(r"[^a-zA-Z0-9 ]", "", Text)
    return Text
def SaveText2Audio(Text = SAF.Text, SavePath =up.SavePath, FileName="Text2Audio", FilePath = '', Neural='Neural', Mode='Text2Audio', Chunk_Limit = 1500,Voice = random.choices(SAF.Original_List_of_Voices_English)[0], Chunk_Replaces = ['.','?','\n'], Chunk_Delimiter = '!',Artist_Persona = 'embrace the spirit and culture of the following text describe it to be illustrated by an artist'):
    Voice = CleanFileName(Voice)

    Check_Folder_Exists(SavePath)



    #polly = Session(region_name='eu-west-2').client('polly')



    if len(str(Text)) >= Chunk_Limit:
        try:
            FilePath = Split_Audio(Text = Text,SavePath = SavePath, FileName=FileName, FilePath=FilePath, Chunk_Limit= Chunk_Limit, Voice = Voice, Chunk_Replaces = Chunk_Replaces, Chunk_Delimiter =Chunk_Delimiter, Artist_Persona = Artist_Persona)
        except:
            print('Error trying to create audio file try again later')

    else:
        FilePaths = ''
        FileName = FileName + '_' + Voice
        FilePath1 = 'No File Saved'
        if FilePath =='':
            FilePath = SavePath + '\\' + FileName + '.mp3'
        else:
            FilePath = FilePath[:-4] + '.mp3'
        # print(FilePath)
        # print(len(str(Text)))

        try:
            session = Session(aws_access_key_id=DNC.aws_access_key_id, aws_secret_access_key=DNC.aws_secret_access_key,
                              region_name='us-west-2')
            polly = session.client("polly")
            response = polly.synthesize_speech(Text=Text, OutputFormat="mp3",
                                               VoiceId=Voice, Engine='neural', )

            # # Request speech synthesis #StartSpeechSynthesisTask #synthesize_speech
            # response = polly.start_speech_synthesis_task(Text=Text, OutputFormat="mp3",
            #                                    VoiceId=Voice, Engine='neural',
            #                                 OutputS3KeyPrefix= "InputAudio",
            #                                 OutputS3BucketName='s3bucketname',)
        except (BotoCoreError, ClientError) as error:
            # The service returned an error, exit gracefully
            print(error)
            sys.exit(-1)

        # Access the audio stream from the response
        if "AudioStream" in response:
            # Note: Closing the stream is important because the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), FilePath)


                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        #FilePath = FilePath
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio as file is large, trying alternate ways")
           # Monitor_Audio_File(FileName, FilePath)
            sys.exit(-1)
        #
        # # Play the audio using the platform's default player
        # if sys.platform == "win32":
        #     os.startfile(output)
        # else:
        #     # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
        #     opener = "open" if sys.platform == "darwin" else "xdg-open"
        #     subprocess.call([opener, output])
        #


    return FilePath


#
#
# import boto3
# def Monitor_Audio_File(FileName,FilePath):
#
#     session = Session(aws_access_key_id=DNC.aws_access_key_id, aws_secret_access_key=DNC.aws_secret_access_key,
#                       region_name='us-west-2')
#     polly = session.client("polly")
#     s3 = boto3.client('s3', aws_access_key_id=DNC.aws_access_key_id, aws_secret_access_key=DNC.aws_secret_access_key)
#     #somhow download whatever this is lol
#     while FileDone ==False:
#         polly.get_speech_synthesis_task()
#         try:
#             s3.get_object(
#                 #Bucket=self._bucket,
#                 Key=FileName,
#             )
#             FileDone =  True
#         except s3.exceptions.NoSuchKey:
#             FileDone =  False
#             print('File not there, waiting 15 seconds')
#             time.sleep(15)
#     polly.download_file('your_bucket',FileName,FilePath)





def add2Master_Persona(df1 = '', Text = 'No Data Provided'):
    if df1 != '':
        df1 = df1
    else:
        data = ([Text])
        df1 = pd.DataFrame(data)

    f2 =  up.MasterFilePersona
    df2 = pd.read_excel(f2)
    df3 = pd.concat([df1, df2])
    df3.drop_duplicates()
    df3.iloc[:, 1:]
    # creating a new excel file and save the data
    df3.to_excel(f2, index=False)




def add2Master_Character(df1 = '', Text = 'No Data Provided'):

    if df1 !='':
        df1 = df1
    else:
        data = ([Text])
        df1 = pd.DataFrame(data)

    f2 =  up.MasterFile_Character
    df2 = pd.read_excel(f2)
    df3 = pd.concat([df1, df2])
    df3.drop_duplicates()
    df3.iloc[:, 1:]
    # creating a new excel file and save the data
    df3.to_excel(f2, index=False)





def add2Master(df1):
    f2 = up.getMFPath()
    df2 = pd.read_excel(f2)
    df3 = pd.concat([df1, df2])
    df3.drop_duplicates()
    df3.iloc[:, 1:]
    # creating a new excel file and save the data
    df3.to_excel(f2, index=False)

def add2Master2(df1):
    f2 = up.getMF2Path()
    df2 = pd.read_excel(f2)
    df3 = pd.concat([df1, df2])
    df3.iloc[:, 1:]
    df3.drop_duplicates()

    # creating a new excel file and save the data
    df3.to_excel(f2, index=False)

def add2Master3(df1):
    f2 = up.MasterFile3
    df2 = pd.read_excel(f2)
    df3 = pd.concat([df1, df2])
    df3.iloc[:, 1:]
    df3.drop_duplicates()

    # creating a new excel file and save the data
    df3.to_excel(f2, index=False)



def SaveText( df, FileName, tabname):

    text1 = df
    f2 = up.getPath()
    SavePath1 = f2
    invalidCharRemoved = re.sub(r"[^a-zA-Z0-9 ]", "", FileName)
    Filename = '\\' + str(invalidCharRemoved) + "_"
    SavePath2 = SavePath1 + Filename + ".xlsx"
    # SavePath2 = r'D:\ShakeBot Testing\ShaKeBotTest for DA - 12-20-2022.xlsx'
    try:
        with pd.ExcelWriter(SavePath2) as writer:
            text1.to_excel(writer, sheet_name=str(tabname))
            #MondeVert_IP.speak(self, 'File Saved')
            print('File Saved')
    except:
        Exception




def saveTranscript(Transcript,current_time):


    Filename = 'SHAINE Transcript v1'
    Filename = '\\' + Filename + "_"
    f2 = up.getPath()
    SavePath1 = f2
    data = [(current_time, Transcript)]
    print(data)
    try:
        df1 = pd.DataFrame(data, columns=["TimeStamp", "Transcript"])
        # df1 = pd.DataFrame(data)
        df1.to_csv(SavePath1 + Filename + current_time + '.csv')

        # MondeVert_IP.SaveText(self,df1,'MondeVert_IP Assistant', 'Full Transcript')
        add2Master2(df1)
    except:
        print('Review Error')


def Add2MasterLyrics(self, current_time2, Mode, title, ArtistPoetInfo, poem, Tag, SavePath2, Prompts):
    data = [(current_time2, Mode, title, ArtistPoetInfo, poem, Tag, SavePath2, Prompts)]
    df = pd.DataFrame(data, columns=['Date_Time_Added', 'Art_Type', 'Title', 'Poet_Artist_Info', 'Poem_Song_Lyrics',
                                     'Quality', 'Folder_Path', 'Prompts_Used'])
    add2Master3(df)






def NamePoemSavePoem(self, poem, ArtPaths, Prompts_Used, ArtistPoetInfo, title='', SavePath=up.AI_Poetry_Path,
                     Mode='SHAINE', current_time = current_time ):


    try:
        dfPrompts = ''
        Tag = ''
        if Mode == 'Poem':
            title_p = up.Poem_Title_Prompt
        else:
            title_p = up.Song_Title_Prompt
        try:
            if title == '':
                x = GPT.MondeVert()
                Title = x.Get_Title_GPT(  Text= poem[:1500] )
            else:
                Title = title

        except:
            print('error could not get title')

        if Title == '':
            Title = 'AI - No Name Project'

        Title1 = CleanFileName(Title)

        Title1 = '\\' + str(Title1) + "_"
        if len(Title1) > 60:
            Title1 = Title1[0:60]


        Title2 = SavePath + Title1

        Check_Folder_Exists(SavePath)





        data = Title +  ArtistPoetInfo + poem +  SavePath+  Mode +  Tag
        # print(dat

        Text = 'Time: ' + current_time + '| Title:' + Title + '| Text:' + data

        Data1 = [(Text)]

        try:
            df1 = pd.DataFrame(Text, columns=["TEXT"])
            print(df1)
            print(Title2)
            df1.to_csv(Title2 + '.txt')
            Add2MasterLyrics(self, current_time, Mode, title, ArtistPoetInfo, poem, Tag, SavePath,dfPrompts)
            # MondeVert_IP.SaveText(self,df1,'MondeVert_IP Assistant', 'Full Transcript')
            try:
                add2Master2(df1)

            except:
                print('Did not add to master, error')
        except:
            print('Review Error')

            try:
    #Word Doc Creation below, not quite what I need so I do text file too above
                document = Document()
                document.add_heading(Title, 0)
                document.add_heading(ArtistPoetInfo, 1)
                p = document.add_paragraph()
                r = p.add_run()
                # r.add_text(ArtistPoetInfo)
                p = document.add_paragraph()
                r = p.add_run()
                r.add_text(poem)
                p = document.add_paragraph()
                r = p.add_run()
                image_counter = 0
                for i in ArtPaths:
                    image_counter += 1
                    r.add_picture(i)
                    original = i
                    target = SavePath + Title1 + str(image_counter)  + '.png'
                    shutil.copyfile(original, target)

                    try:
                        IP.png2JPG(original, up.PNGPath, Title1, up.PNGPath_Archive, Del=False)

                    except:
                        print('instagram failed, as always!')
                document.add_heading('AI Prompts used: ', 7)

                for i in Prompts_Used:
                    p = document.add_paragraph()
                    r = p.add_run()
                    r.add_text(i)
                    dfPrompts += i + '|'
                document.save(Title2 + '_Details.docx')

                document2 = Document()
                document2.add_heading(Title, 0)
                document2.add_heading(ArtistPoetInfo, 1)

                p = document2.add_paragraph()
                r = p.add_run()
                r.add_text(poem)
                document2.save(Title2 + '.docx')
            except:
                print('Error saving word doc')
    except:
        print('Error did not save file')

def MultiThread(self, Functions, Args):
    thread_list = []
    print("Start")
    print(Args)

    t = threading.Thread(target=Functions, args=(Args))
    thread_list.append(t)

    # Starts threads
    for thread in thread_list:
        print("New Thread Started")
        thread.start()


    # This blocks the calling thread until the thread whose join() method is called is terminated.
    # From http://docs.python.org/2/library/threading.html#thread-objects
    for thread in thread_list:
        thread.join()

# Demonstrates that the main process waited for threads to complete
    print("Done")


def send_email_w_attachment_outlook(to, subject, body, filename):
    sender = DNC.OutlookEmail
    receivers = to
    #smtp
    smtpHost = 'smtp.office365.com'
    smtpPort = 587
    password = DNC.Outlookpassword
    subject = "outlook email test"
    # Add the From: and To: headers at the start!
    message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
           % (sender, ", ".join(receivers), subject))
    message += """This is a test e-mail message."""
    print (message)
    try:
        smtpObj = smtplib.SMTP(smtpHost, smtpPort)
        #smtpObj.set_debuglevel(1)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(sender,password)
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()
        print ("Successfully sent email")
    except:
        print ("Error: unable to send email")


def send_email_w_attachment_gmail(to, subject, body, filename):
    # create message object
    to = 'sdonovan@mondevert.co'#; RichardDX44@gmail.com'
    subject = 'New Song for Rich'
    message = MIMEMultipart()
    # add in header
    message['From'] = Header(up.user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject)
    # attach message body as MIMEText
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # locate and attach desired attachments

    for n in filename:
        att_name = os.path.basename(filename[n])
        _f = open(filename[n], 'rb')
        att = MIMEApplication(_f.read(), _subtype="txt")
        _f.close()
        att.add_header('Content-Disposition', 'attachment', filename=att_name)
        message.attach(att)

    # setup email server
    server = smtplib.SMTP_SSL(DNC.host, DNC.port)
    server.login(DNC.gmail_user, DNC.gmail_pass)

    # send email and quit server
    server.sendmail(DNC.user, to, message.as_string())
    server.quit()


def send_email_no_attachment_gmail(to, subject, body):
    # create message object
    to = 'sdonovan@mondevert.co'
    subject = 'New Song for Rich'

    message = MIMEMultipart()

    # add in header
    message['From'] = Header(up.user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject)

    # attach message body as MIMEText
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # setup email server
    server = smtplib.SMTP_SSL(DNC.host, DNC.port)
    server.login(DNC.user, DNC.gmail_pass)

    # send email and quit server
    server.sendmail(DNC.user, to, message.as_string())
    server.quit()








def CutUP_long_String_to_list(self, Text, SavePath, FileName, Art_Style_details,Key_Words = ['Characters','Character', 'Page', 'Illustration Details'], Key_Char = ':',Delimiter = '|', crazy = .5):
    dummy =1
    ArtPaths = []
    if dummy ==1:
        try:
            Art_Prompt_Chop = Text
        except:
            print('Error Trying to make original Painting')
            Art_PromptCharo =  Text

        Art_PromptCharoo = Art_Prompt_Chop
        # ArtPrompt_Mondevert = + Result
        # ArtPrompt_Mondevert = ArtFormatAdvance + Result

        for Key_Word in Key_Words:
            try:
                if Delimiter in Art_Prompt_Chop:
                    Art_Prompt_Chop = Art_Prompt_Chop.split(Delimiter)
                else:
                    Art_Prompt_Chop = Art_Prompt_Chop.replace(Key_Word + Key_Char, Delimiter)
                    Art_Prompt_Chop = Art_Prompt_Chop.replace(Key_Word, Delimiter)
                    if Delimiter in Art_Prompt_Chop:
                        Art_Prompt_Chop = Art_Prompt_Chop.split(Delimiter)
                    else:
                        Art_Prompt_Chop = Art_Prompt_Chop.replace(Key_Char, Delimiter)
                        Art_Prompt_Chop = Art_Prompt_Chop.split(Delimiter)




                # Test_Skel1 = Result.replace("Page:", "#")
                # Test_Skel1 = Test_Skel1.replace("Page", "#")

               # print('Art_PromptCharo')
                #print(Art_PromptCharo)



            except:
                print('Could not properly split out the string for multiple illustrations')

        return Art_Prompt_Chop




def Create_Art_from_String_to_list(self, Text, SavePath, FileName, Art_Style_details,Key_Words = ['Characters','Character', 'Page', 'Illustration Details'], Key_Char = ':',Delimiter = '|', crazy = .5):
    dummy = 1
    ArtPaths = []
    if dummy == 1:
        try:
            Art_Prompt_Chop = Text
        except:
            print('Error Trying to make original Painting')
            Art_PromptCharo = Text

        Art_PromptCharoo = Art_Prompt_Chop
        # ArtPrompt_Mondevert = + Result
        # ArtPrompt_Mondevert = ArtFormatAdvance + Result

        for Key_Word in Key_Words:
            try:
                if Delimiter in Art_Prompt_Chop:
                    Art_Prompt_Chop = Art_Prompt_Chop.split(Delimiter)
                else:
                    Art_Prompt_Chop = Art_Prompt_Chop.replace(Key_Word + Key_Char, Delimiter)
                    Art_Prompt_Chop = Art_Prompt_Chop.replace(Key_Word, Delimiter)

                if Delimiter in Art_Prompt_Chop:
                    Art_Prompt_Chop = Art_Prompt_Chop.split(Delimiter)
                else:
                    Art_Prompt_Chop = Art_Prompt_Chop.replace(Key_Char, Delimiter)
                    Art_Prompt_Chop = Art_Prompt_Chop.split(Delimiter)

                # Test_Skel1 = Result.replace("Page:", "#")
                # Test_Skel1 = Test_Skel1.replace("Page", "#")

            # print('Art_PromptCharo')
            # print(Art_PromptCharo)

            except:
                print('Could not properly split out the string for multiple illustrations')

        #ore sending as art I should do one more clean up of the language/prompt to make it best

        KillSwitch = 0
        KeepGoing = False
        while KeepGoing == False and KillSwitch < 6:
            try:
                Art_PromptCharoo + 'Revised Prompts: '
                Characters = []
                x = len(Art_Prompt_Chop)
                for c in range(0, x):
                    # print(c)
                    #Do the change here before setting the value or keep both
                    if len(Art_Prompt_Chop[c])>22:
                        Characters.append(Art_Prompt_Chop[c])
                        Clean_Prompt_User_GPT_Input = GPT.MondeVert.Basic_GPT_Query(self,   Line2_Role = lup.Clean_Role_after_Delimit + c , Line3_Format = lup.Clean_Format_after_Delimit,Line4_Task= lup.Clean_Task_after_Delimit ,Special = 'Use the following Text for the styles to embody/artist persona to embody###  ' + Art_Style_details+ c + '###',Line1_System_Rule = up.system_Text_Art, crazy = .5, Subject= '')
                        Characters.append(Art_Prompt_Chop[Clean_Prompt_User_GPT_Input])

                        Art_PromptCharoo +=Clean_Prompt_User_GPT_Input


                #print('Characters')
                #print(Characters)

                for c in Characters:
                    print(' ')
                    print('-------------------------------------------')
                    print('-------------------------------------------')
                    print("Character: " +  c)
                    print('-------------------------------------------')
                    # print("Character Art1: " + up.Character_Art1 + c)
                    if len(Art_Prompt_Chop[c]) > 22:
                        ArtPath2 = GPT.MondeVert.makeArt(self, Art_Prompt_Chop + c)
                        ArtPaths.append(ArtPath2)
                    #print(ArtPath2)


            except:
                print('Error Trying to create multiple paintings')
                KillSwitch += 1
            KeepGoing = True

    return ArtPaths #after its returned I append this to the folder with all relevant data