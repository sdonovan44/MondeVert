import User_Prefs as up
import os
import pandas as pd
import pyttsx3
import datetime
import re


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
