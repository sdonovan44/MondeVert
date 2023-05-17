import time

import User_Prefs as up
import random
import os
import pandas as pd
import pyttsx3
import datetime
import re
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import Stories_For_Audio_Files as SAF
import User_Prefs as up
from pydub import AudioSegment
import DoNotCommit as DNC

def Check_Folder_Exists(SavePath):
    isExist = os.path.exists(SavePath)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(SavePath)
        print("Created new filePath: " + SavePath)






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
    current_time2 = current_time1.strftime('%m-%d-%Y_%H.%M.%S')

    data = [(current_time2, text2Add)]
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







def SaveCSV(Text, Title, FolderPath_original,FolderPath_Final):
    current_time1 = datetime.datetime.now()
    current_time2 = current_time1.strftime('%m-%d-%Y_%H.%M.%S')
    f2 = FolderPath_original
    SavePath1 = f2
    invalidCharRemoved = re.sub(r"[^a-zA-Z0-9 ]", "", Title)
    folder = str(invalidCharRemoved)
    if len(folder) > 44:
        folder = folder[0:44]
    Title1 = '\\' + str(invalidCharRemoved) + "_"
    if len(Title1) > 44:
        Title1 = Title1[0:44]
    SavePath2 = SavePath1 + '\\' + folder
    Title2 = SavePath2 + Title1 + current_time2 + '.txt'


    Check_Folder_Exists(FolderPath_Final)



    try:
        df1 = pd.DataFrame(Text, columns=["TimeStamp", "Transcript"])
        print(df1)

        df1.to_csv(Title2 )
        # MondeVert.SaveText(self,df1,'MondeVert Assistant', 'Full Transcript')
        add2Master2(df1)
    except:
        print('Review Error File did not save ')

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
            Opening = AudioSegment.from_file(Opening_Sound, format="mp3")
            Merged_Audio = Opening

        else:
            sound2add = AudioSegment.from_file(AudioFiles_ordered[x], format="mp3")
            Merged_Audio += sound2add

  #  try:
    # simple export
    FilePath = Merged_Audio.export(FilePath, format="mp3")
    # except:
    #     print('could not save file audio file')
    #     FilePath = 'No File Saved'

    return FilePath

#on character list Have Narrator Scene (stern and manly) and then you have preferred Narrators to choose from (to do all other narrations)
#Split on Space and :
#also look for Narrator, for now we should mostly ignore whats in the parenthesis so I will work to remove these
#Setting and other parts are Narrator1, and then narrator2
#def SplitScriptbyPart(Script,Character_Voice_Relationship,FileName,SavePath )
#remove (voiceover), otherwise have the system remove anywhere that has the parenthesis as its not important for audio

#Grab the Left most item on the line


def Split_Audio(Text, SavePath, FileName,FilePath = '', OpeningSound = up.MondeVertIntro, Chunk_Limit = 1500, Voice = random.choices(SAF.Original_List_of_Voices_English)[0] ):
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
    while RunningCheck < (Length_Text-10) and LastPunc != -1:
        Text_Chunk = Text_New[:Chunk_Limit]
        Text_Chunk_Info_only = Text_Chunk.replace('.','!')
        Text_Chunk_Info_only = Text_Chunk_Info_only.replace('?', '!')

        #print(Text_Chunk_Info_only)
        # print('Last Punc Position')
        # print(LastPunc)
        LastPunc =Text_Chunk_Info_only.rfind("!")

        print('Last Punc Position')
        print(LastPunc)
        Text_Chunk_Final = Text_New[:LastPunc]
        #print(Text_Chunk_Final)
        FilePath = SaveText2Audio(Text = Text_Chunk_Final, SavePath = SavePath_Chunks, FileName=FileName + '_Chunk_' +str(Audio_File_Count), Voice = Voice )
        FilePaths.append(FilePath)
        Text_Chunks.append(Text_Chunk_Final)
        RunningCheck +=len(Text_Chunk_Final)

        try:
            #length = len(Text_New)
            New_pos = (LastPunc + 1)
            Text_New = Text_New[New_pos:]
            #length = len(Text_New)
        except:
            print('Review Error Triggered, could be just how this has to work')
            #print(Text_New)
            #print(len(Text_New))

    FilePath2 = Combine_Splitsof_audio(AudioFiles_ordered = FilePaths, FilePath=FilePath,SavePath= SavePath)
    return FilePath2

def CleanFileName(Text):
    Text = re.sub(r"[^a-zA-Z0-9 ]", "", Text)
    return Text
def SaveText2Audio(Text = SAF.Text, SavePath =up.SavePath, FileName="Text2Audio", FilePath = '', Voice="Olivia", Neural='Neural', Mode='Text2Audio', Chunk_Limit = 1500):
    Voice = CleanFileName(Voice)
    current_time1 = datetime.datetime.now()
    current_time2 = current_time1.strftime('%m-%d-%Y_%H.%M.%S')

    Check_Folder_Exists(SavePath)

    FilePaths = ''
    FileName = FileName + '_' + current_time2
    FilePath1 = 'No File Saved'
    FilePath = SavePath + '\\' + FileName  + '.mp3'
    print(len(str(Text)))

    #polly = Session(region_name='eu-west-2').client('polly')



    if len(str(Text)) >= Chunk_Limit:
        #try:
        FilePath = Split_Audio(Text = Text,SavePath = SavePath, FileName=FileName, FilePath=FilePath, Chunk_Limit= Chunk_Limit)
        # except:
        #     print('Error trying to create audio file try again later')

    else:
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
                        FilePath1 = FilePath
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