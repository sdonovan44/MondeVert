from MondeVert_IP.SHAINE_MonderVert import SHAINE as GPT

from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Stories_For_Audio_Files as SFA, ReWrites as RW
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up
import threading
import pandas as pd


x = GPT.MondeVert()
#x.Manual_Audio_File(FilePath = r"A:\MondeVert_IP Productions\SHAINE - MondeVert_IP AI Assistant\AI Tasks\MondeVert_Audio_Video_Story\Echoes of the Heart_Miniseries.txt")




Role = """you are an expert marketing agent and PR rep, with mastery of getting audience hooked and also have the message clear and not too wordy."""
Format = """Provide a short 10 second intro for an audio book that is professional and welcoming and makes the listener feel appreciated for their time. They should look forward to more content from me in the future. And they should be eager to try to win money with my contests I am offering"""
Text = """The following   Audio   is copyrighted by Monde  Vert  Studios.....  MondeVert - because the world needs less stress and more success.         If you enjoy this content please subscribe and follow Monde Vert's Social Media Sites and check out our website at www.MondeVert.co. Our team has recently started up a patreon with exclusive content and soon will be holding several paid contest for people to submit their own original work Submissions as low as $1 to win $100. Additionally, Here at MondeVert_IP we are working with new talent to foster their brand and help them succeed. I hope you enjoy the following audiobook we have published for your entertainment; reach out to our team and you could have your content featured in the future. thanks for watching feel free to comment we look forward to hearing from you"""
Task = """Task:###Clean the following {Text} and use the {format} guidelines provided### 
Text:###""" + Text + """###"""


# NewText = '' + str(x.Basic_GPT_Query(Line2_Role=Role, Line3_Format= Format, Line4_Task=Task)) + ''
# print(NewText)
#
# x.Manual_Audio_File(Text_override=NewText)
#x.Manual_Audio_File(SavePath = r'A:\MondeVert_IP Productions\SHAINE - MondeVert_IP AI Assistant\AI Tasks\MondeVert_Audio_Video_Story',FileName= 'Echoes of the Heart', FilePath = r"A:\MondeVert_IP Productions\SHAINE - MondeVert_IP AI Assistant\AI Tasks\MondeVert_Audio_Video_Story\Echoes of the Heart_Miniseries.txt")
#x.Manual_Audio_File(Text_override = SFA.MondeVert_Promo)
#MondeVert_Promo


#
audio_new4 =r"A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\AI_Childrens_AudioBooks\PictureBook_Shane\The Adventures of Zephyr the Zebra\The Adventures of Zephyr the Zebra_.txt"
audio_new3 =r"A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\AI_Childrens_AudioBooks\PictureBook_Shane\The Magic Forest Adventures\The Magic Forest Adventures.txt"
audio_new2 =r"A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\AI_Childrens_AudioBooks\PictureBook_Shane\Cherishing Memories and Protecting the Magic Within\Protect the Magic Within.txt"

audio_new = r"A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\ShaneOriginal\Shanes Journey\Shanes JourneySeason 1EPISODE 2__07-27-2023_20.14.txt"
audio_File_name = 'King Richard Reid'
# x.Manual_Audio_File(SavePath =up.AI_AudioBook_Path ,FileName=  audio_File_name, Source_FilePath = audio_new)

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

# args= ['Music_Rich','Music_Shane', 'Music', 'PjSpecial']

args = ['Poem']


Runs = []
# Runs.append('Music_Shane')
# Runs.append('Blog_Random')
# Runs.append('Speech')
# Runs.append('PictureBook')
# Runs.append('PjSpecial')
Runs.append('Social_Media_Clean_Post')
#Runs.append('AUDIOBOOK_Shane')
# Runs.append('PictureBook')
# Runs.append('MondeVert_Audio_Video_Story')
# Runs.append('ReSearch3')
# Runs.append('Basic')
# Runs.append('Wedding Vows')

# for i in Runs:
#     x.MondeVertMenu_up(Mode=i)

# cu.SaveText2Audio( FilePath = audio_new3, Chunk_Limit=444)

#cu.SaveText2Audio( FilePath = audio_new, Chunk_Limit=444)

# cu.SaveText2Audio( FilePath = audio_new4, Chunk_Limit=444)
#
#
# cu.SaveText2Audio( FilePath = audio_new2, Chunk_Limit=444)
#
# #


#
#
# text = '''Once upon a time, there was a young girl named Zara who had a passion for gardening. She loved spending time in her garden, tending to the plants and flowers, and watching the garden creatures go about their business. One day, while watering her garden, she noticed something strange. The plants were growing bigger, the colors were brighter, and the garden creatures could talk!
#
# Zara was amazed and a little scared, but she decided to investigate. She met Mr. Snail, a friendly snail who helped her tend to her garden, and Lola, a curious ladybug who loved to explore. Together, they discovered that the garden was magical, and they embarked on an adventure to explore it and meet all of its inhabitants.
#
# As they journeyed through the garden, they encountered different garden creatures, such as butterflies, bees, and birds. They learned important lessons about friendship and teamwork, and they discovered that the garden's magic came from the love and care they gave it.
#
# But their adventure wasn't all fun and games. Pippin, a mischievous squirrel, played a prank on Zara and her friends. At first, Zara and her friends were angry and upset, but they learned about forgiveness and the importance of not holding grudges.
#
# As Zara and her friends continued their adventure, they also learned about the importance of taking care of the environment. They realized that the garden's magic came from the love and care they gave it, and they made a promise to always take care of it.
#
# Zara woke up from her magical adventure, but she knew that she could use the lessons she learned in her everyday life. She was grateful for her garden and the memories she made with her friends.
#
# The Adventures of Zara and Her Magical Garden is a wonderful story about the power of friendship, teamwork, and taking care of the environment. It is a story that will excite kids to read with their parents, and it has a positive message that will inspire them to be kind and caring to the world around them.
# '''
#
#
# cu.SaveText2Audio(FilePath=r"A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\ShaneOriginal\ Shanes Journey A Gritty Tale of SelfDiscovery and Redemption\ Shanes Journey A Gritty Tale of SelfDiscovery and Redemption Act 1 Chapter 4 Novel__07-28-2023_01.26.txt", Chunk_Limit=1333,Translate= ['English'] )
# cu.SaveText2Audio(FilePath=r"A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\ShaneOriginal\ Shanes Journey A Gritty Tale of SelfDiscovery and Redemption\ Shanes Journey A Gritty Tale of SelfDiscovery and Redemption Act 1 Chapter 4 Play__07-28-2023_01.26.txt", Chunk_Limit=1333, Translate= ['English'] )

# x.MondeVertMenu_up(Mode = 'Social_Media_Clean_Post')


#cu.Resume()
import datetime
current_time1 = datetime.datetime.now()
current_time = current_time1.strftime('%m-%d-%Y_%H.%M.%S')
# Movie = "A:\Amini Amor\SHAINE\Requests\Beta\Test 1\A Tale of Two Kitties (1942).mp4"
# Movie = "A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Movie2Audio\IMG_1966.MOV.crdownload"
# Movie2 ="A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Movie2Audio\LaPardon64.mp4"
# Movie3 = r"A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Movie2Audio\Task 1 2023-09-28 02-16-58.mp4"
# Movie4 = r"A:\Amini Amor\Live Recordings Raw\Task 3.mp4"
# Movie5 = "A:\Amini Amor\Live Recordings Raw\Task4.mp4"
# Movie5 = r"A:\Amini Amor\Live Recordings Raw\2023-10-03 04-22-52.mp4"
# Youtube = "https://youtu.be/skrdyoabmgA?si=fPDFIIqzVp2LE9ia"
# # t = threading.Thread(target=cu.MovieSubtitles, args = (Movie,)).start()
# # t = threading.Thread(target=cu.MovieSubtitles, args = (Movie2,"French", "English")).start()
# # t = threading.Thread(target=cu.YouTube, args = (Youtube,)).start()
#
# Richie = r"A:\Amini Amor\Live Recordings Raw\2023-10-11 15-52-34.mp4"
# #cu.Movie2Audio(Richie)
#
#
#
# #cu.MovieSubtitles(Movie, Rewrite = True)
# # cu.MovieSubtitles(Movie5, Rewrite = True , AI_Task=True)
# Pictures = r"A:\Amini Amor\Live Recordings Raw\2023-09-28 03-59-14.mp4"
# mili1 = 2000
# mili = 20000
# #cu.extractImages(Richie, up.AI_Audio_Transcript + '\\' + 'Extracted images', MakeVar=True, Millisecs=mili)
# # cu.extractImages(Richie, up.AI_Audio_Transcript + '\\' + 'Extracted images', MakeVar=False, Millisecs=mili1)
#
# pic = r"A:\Amini Amor\SHAINE\Requests\Beta\AI Art\Approved Quality Art\Curated\MondeVert Studio\SHAINE Favorites\Art_Blunts_Using_the_classic_style_of_Pablo_Picasso_create_a_unique_work_of_art_that_celebrates_the_creative_combination_of_Snoop_Dogg_and_Back - Copy.png"
# pic2 = r"A:\Amini Amor\SHAINE\Requests\Beta\AI Art\Approved Quality Art\Curated\MondeVert Studio\SHAINE Favorites\The artwork depicts a woman with flowing blue hair surrounded by a vibrant and colorful cityscape Her eyes are closed and a serene expression is on.png"
# pic3 = r"A:\Amini Amor\SHAINE\Requests\Beta\AI Art\Approved Quality Art\Curated\MondeVert Studio\SHAINE Favorites\2_stoners_playing_rock_paper_scissors_in_the_style_of_norman_rockwell.png"
# pic4 = r"A:\Amini Amor\SHAINE\Requests\Beta\AI Art\Approved Quality Art\Curated\MondeVert Studio\SHAINE Favorites\The portrait depicts a young woman with piercing blue eyes surrounded by a dreamlike aura of vibrant colors and intricate details Her face is a mix .png"
# # Version2 = cu.MakeVariationArt(Pic= pic2, FileName='Favorite Variant1' + current_time)
# # Version3 = cu.MakeVariationArt(Pic= Version2, FileName='Favorite Variant2' + current_time)
# # Version4 = cu.MakeVariationArt(Pic= Version3, FileName='Favorite Variant2' + current_time)
#
# pic22 = r"A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Extracted images\Blue Hair Variants\Favorite Variant  6  09282023042651.png"
# pic222 = r"A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Extracted images\Blue Hair Variants\Favorite Variant  6  10142023155339.png"
# #
# # Version1 = pic22
# # for i in range (1,15):
# #     Version1 = cu.MakeVariationArt(Pic=Version1, FileName='Favorite Variant  ' + str(i) + '  '+ current_time)
# # Version1 = pic22
# # for i in range (1,4):
# #     Version2 = cu.MakeVariationArt(Pic=Version1, FileName='Favorite Variant v2   ' + str(i) + '  '+ current_time)
#
#
# Insta = r"A:\Amini Amor\Live Recordings Raw\2023-10-14 15-09-39.mp4"

#cu.MovieSubtitles(Insta, Rewrite = True)

Journal_Video = r"A:\Amini Amor\Live Recordings Raw\2023-10-17 03-34-34.mp4"
#Journal_Video = r"A:\Amini Amor\Live Recordings Raw\2023-10-17 04-24-29.mp4"

#Journal_Video = r"A:\Amini Amor\Live Recordings Raw\2023-10-17 14-18-25.mp4"
#Journal_Video = r"A:\Amini Amor\Live Recordings Raw\2023-10-17 14-39-06.mp4"
#Journal_Video = r"A:\Amini Amor\Live Recordings Raw\2023-10-17 14-55-01.mp4"


#Make it so I have folder in the live recordings for Journal and maybe have a script running to trigger this program so it automatically adds the new items and creates the respective files
#Also make it so all of the ToDo Lists through time are added to the



cu.MovieSubtitles(Journal_Video, Rewrite = True , Journal=True, Output=["English"], ToDo= True)


#This needs to be reran for summarizing text
# for i in range(0, len(RW.Personal_Message) ):
#     Summarized_text = cu.SummarizeText((RW.Personal_Message[i]), Task=RW.Personal_Message_Task)
#     Name = RW.Personal_Message_Names[i]
#     Title = "Personal Message"
#     Title = Title + ' ' + Name
#     FilePath = cu.SaveCSV(Text= Summarized_text, SavePath=up.AI_Task_Path + '\\Personal Message\\' +Title, Title=Title )
#     cu.SaveText2Audio(FilePath=FilePath)
#
#     print(Summarized_text)



#cu.MovieSubtitles(Movie2, Origin="French", Output=["English"])
#cu.DownloadYoutubeMovie(video_url = Youtube)
#Make a function that has a suite of tools, first you select the mode, then you get the output
#Step 1 have user send in instructions to the system depending on what mode they choose
# Step 2 Have the mode kick off and if anything is unclear get clarity so that the task can be completed.
# Maybe make it so it can break down complex things into each task so the responses are longer (take the edited version and maybe have it formatted as a list that can be regexed)


#1. Audio File/Video convert - Configs include revise mode and task mode
#2 Look at the prompts about research etc. Use chat GPT to categorize task and pick the correct prompts to make the best results.
#3 allow user to feed in a file, if the task is to load data from a file and recreate or summarize ask for the file etc.
#4 other tasks maybe make song/story (you can mostly use #1 for this but maybe there is a mode to make another layer if needed)



FilePath = r"A:\Amini Amor\Secret Law of Attraction.txt"
#Text  = pd.read_csv(FilePath)

#
# with open(FilePath,'r') as file:
# 	Text = " ".join(line.rstrip() for line in file)
# 	#print(Text)
#
# cu.speak(Text)