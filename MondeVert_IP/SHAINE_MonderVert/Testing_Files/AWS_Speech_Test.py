from MondeVert_IP.SHAINE_MonderVert import SHAINE as GPT

from MondeVert_IP.SHAINE_MonderVert.Utilities import Common_Utilities as cu
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Stories_For_Audio_Files as SFA
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up




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
audio_new4 ="A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\AI_Childrens_AudioBooks\PictureBook_Shane\The Adventures of Zephyr the Zebra\The Adventures of Zephyr the Zebra_.txt"
audio_new3 ="A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\AI_Childrens_AudioBooks\PictureBook_Shane\The Little Explorers Big Adventure\The Little Explorers Big Adventure.txt"
audio_new2 ="A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\AI_Childrens_AudioBooks\PictureBook_Shane\The Adventures of the Littlest Explorer\The Adventures of the Littlest Explorer.txt"

audio_new = r"A:\Amini Amor\SHAINE\Requests\Beta\AI AudioBooks\AI_Childrens_AudioBooks\PictureBook_Shane\Kikis Adventure\Kikis Adventure.txt"
audio_File_name = 'King Richard Reid'
#x.Manual_Audio_File(SavePath =up.AI_AudioBook_Path ,FileName=  audio_File_name, Source_FilePath = audio_new)

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
Runs.append('Blog_Random')
Runs.append('Speech')
Runs.append('PictureBook')
Runs.append('PjSpecial')
Runs.append('MondeVert_Audio_Video_Story')
# Runs.append('PictureBook')
# Runs.append('MondeVert_Audio_Video_Story')
# Runs.append('ReSearch3')
# Runs.append('Basic')
# Runs.append('Wedding Vows')

# for i in Runs:
#     x.MondeVertMenu_up(Mode=i)

#cu.SaveText2Audio( FilePath = audio_new, Chunk_Limit=444)

cu.SaveText2Audio( FilePath = audio_new4, Chunk_Limit=444)

cu.SaveText2Audio( FilePath = audio_new3, Chunk_Limit=444)

cu.SaveText2Audio( FilePath = audio_new2, Chunk_Limit=444)

#


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
#cu.SaveText2Audio(FilePath=r"A:\Amini Amor\SHAINE\Requests\Beta\AI Blogs\Blog_Random\Prioritizing Mental Health in Communities of Color\Prioritizing Mental Health in Communities of Color.txt", Chunk_Limit=1333 )

#x.MondeVertMenu_up(Mode = 'Social_Media_Clean_Post')