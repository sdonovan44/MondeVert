from MondeVert.SHAINE_MonderVert import SHAINE as GPT
from MondeVert.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Stories_For_Audio_Files as SFA
from MondeVert.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import User_Prefs as up




x = GPT.MondeVert()
#x.Manual_Audio_File(FilePath = r"A:\MondeVert Productions\SHAINE - MondeVert AI Assistant\AI Tasks\MondeVert_Audio_Video_Story\Echoes of the Heart_Miniseries.txt")




Role = """you are an expert marketing agent and PR rep, with mastery of getting audience hooked and also have the message clear and not too wordy."""
Format = """Provide a short 10 second intro for an audio book that is professional and welcoming and makes the listener feel appreciated for their time. They should look forward to more content from me in the future. And they should be eager to try to win money with my contests I am offering"""
Text = """The following   Audio   is copyrighted by Monde  Vert  Studios.....  MondeVert - because the world needs less stress and more success.         If you enjoy this content please subscribe and follow Monde Vert's Social Media Sites and check out our website at www.MondeVert.co. Our team has recently started up a patreon with exclusive content and soon will be holding several paid contest for people to submit their own original work Submissions as low as $1 to win $100. Additionally, Here at MondeVert we are working with new talent to foster their brand and help them succeed. I hope you enjoy the following audiobook we have published for your entertainment; reach out to our team and you could have your content featured in the future. thanks for watching feel free to comment we look forward to hearing from you"""
Task = """Task:###Clean the following {Text} and use the {format} guidelines provided### 
Text:###""" + Text + """###"""


# NewText = '' + str(x.Basic_GPT_Query(Line2_Role=Role, Line3_Format= Format, Line4_Task=Task)) + ''
# print(NewText)
#
# x.Manual_Audio_File(Text_override=NewText)
#x.Manual_Audio_File(SavePath = r'A:\MondeVert Productions\SHAINE - MondeVert AI Assistant\AI Tasks\MondeVert_Audio_Video_Story',FileName= 'Echoes of the Heart', FilePath = r"A:\MondeVert Productions\SHAINE - MondeVert AI Assistant\AI Tasks\MondeVert_Audio_Video_Story\Echoes of the Heart_Miniseries.txt")
#x.Manual_Audio_File(Text_override = SFA.MondeVert_Promo)
#MondeVert_Promo
audio_new = r"A:\MondeVert Productions\SHAINE - MondeVert AI Assistant\SHAINE_Requests\Beta - Testing\AI Tasks\The Magic Forest Adventures.txt"
audio_File_name = 'The Magic Forest Adventures'
#x.Manual_Audio_File(SavePath =up.Children_audio_book ,FileName=  audio_File_name, FilePath = audio_new)

x.MondeVertMenu_up(Mode = 'Social_Media_Clean_Post')