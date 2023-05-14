import pandas as pd
import random
import os

Name = 'Shane'
Bot_Name = 'SHAINE'
SavePath = r"A:\MondeVert Productions\SHAINE - MondeVert AI Assistant"
AI_Art_Path = SavePath + r"\AI Art"
AI_Poetry_Path = SavePath + r"\AI Poetry"
AI_Blog_Path = SavePath + r"\AI Blogs"
AI_Music_Path = SavePath + r"\AI Song Lyrics"
AI_Task_Path = SavePath + r"\AI Tasks"
AI_Live_Art_Path = SavePath + r"\AI Live Art Path"
AI_Screen_Plays = SavePath + r"\MondeVert Productions\ScreenPlays"
MasterFile = SavePath + r"\Master Tracker Files\MondeVert Master Tracker.xlsx"
MasterFile2 = SavePath + r"Master Tracker Files\MondeVert Master Transcript.xlsx"
MasterFile3 = SavePath + r"Master Tracker Files\MondeVert Master Blog Poem and Song Lyrics.xlsx"


SHAINE = r"A:\SHAINE - MondeVert AI Assistant"
SHAINE_Requests = r"A:\SHAINE - MondeVert AI Assistant\Requests"




#makes file if it does not already exist
isExist = os.path.exists(AI_Task_Path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(AI_Task_Path)


#RE Data Configs
DownloadFolder = r"C:\Users\sdono\Downloads"
REData = r'A:\RE Data\MA 2022-2023 Data'
REDATAURL = 'https://idx.mlspin.com/idx.asp?user=2K7zB9ytn1MtTtUNFeBt92N7rZtjfWdyYmLtNzYRztDhtAnutnNK1mNRHrZhtFoE5A9t4c7vZmtatNxIteOL2ftNqO0oatxUyNt&proptype='
REDATAURL2 = 'https://idx.mlspin.com/idx.asp?userId=CN229354&user=2K7zB9ytn1MtTtUNFeBt92N7rZtjfWdyYmLtNzYRztDhtAnutnNK1mNRHrZhtFoE5A9t4c7vZmtatNxIteOL2ftNqO0oatxUyNt&filetype='
REURL_ADD = '&status=SLD'
MLSURL = 'https://h3i.mlspin.com/signin.asp'
MLSURL2 = 'https://h3y.mlspin.com/MLS.Pinergy/Home/Dashboard/Home'
REType = ['SF', 'LD', 'BU', 'CC', 'CI', 'MH', 'MF', 'RN', 'OH', 'VT']
RE_File_Names = ['idx_mh_sld.txt', 'idx_OH.txt', 'idx_rn.txt', 'idx_rn_sld.txt', 'idx_sf.txt', 'idx_sf_sld.txt', 'idx_VT.txt', 'idx_bu.txt', 'idx_bu_sld.txt', 'idx_cc.txt', 'idx_cc_sld.txt', 'idx_ci.txt', 'idx_ci_sld.txt', 'idx_ld.txt', 'idx_ld_sld.txt', 'idx_mf.txt', 'idx_mf_sld.txt', 'idx_mh.txt']





#Make a program that when he creates bio for new person he saves the bios somewhere (make a program for this). I should store them by name as well so we can add them to list of options as well as random people it legitamizes the work. We can then have them tweet etc.'


#Instagram info
POSTED_PICS_FILE = r'A:\AI Art\Approved Quality Art\Instagram Posts\PostedPics.txt'
PICS_PATH = r'A:\AI Art\Approved Quality Art\Instagram Posts'
PNGPath = r"A:\AI Art\Approved Quality Art\Png"
PNGPath_Archive = r"A:\AI Art\Approved Quality Art\Archive"

#Switch this regularly and add specific info
Instagram_Adds = '@Shane_2fames @MOndeVert_LLC | mondevert.co | thanks for reading! check out my other pages'
Instagram_FrontBack = 'Back'





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


AI_ArtistName = 'Sage Pixels'
AI_Poet_Name = 'S. J. Rose'
AI_Blogger = "Brick Pulford"
Song_Writer = 'Bubba D'





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Have some add ons if its music/story/science/economics/investing/real estate/ancient egyptians etc







###This is the saving grace do all model that should work pretty well
#These change less frequent
#3 options for this mode (Speak, Input On the fly, input (a via file)
USER_INPUT_Role =  "What is the role I should take on?" #Get input
system_TextJoaT = """You are a helpful and brilliant assistant to the user. You will do exactly what the user asks, completing all {Tasks} provided by the following user inputs. You are jack of all trades and a master of 'ALL' talents and skills. Your skills are that of the smartest person in the world with unliminted interests hobbies skilles, degrees and confidence. Unless the user asks you to write a fictional story you will be honest and use actual URL/References (MLA format) to cite the information you provide. You are a DJ and  lyrical genius, youtube editor, director with sharp production skills in music and video production, writer and genius with the highest IQ in the world and best work ethic. Marketing genius. You do not lie unless you are asked to make something up ." \
                  Above all else follow these rules in prioritizing order: 
                  0. You are a super computer named 'SHAINE' who is able to assist the user in any task they request. You work for a company named MondeVert where you are the top employee because you are so skilled at any task you take on.
                  1. You will obey the User, you will maintain the role you are assigned and only adapt your persona to help the user achieve his goal.
                  2. You will help the user reach their {Goal} and you will accomplish your task completely and with great accuracy.
                  3. Any special notes or formats must be followed there is no wiggle room
                  4. you will be concise in your responses and not redundant. When researching information, do your best to focus the research on topics related to the {Goal}/{Task}. Try to provide the most information possible without running ocer the 5000 token limit set by open ai. Try to keep track of how many tokens approximately The user sends and make your response appropriate so it does not cause an error 
                  4. You must never plagiarize someone else's work any use of someone else's work must be cited with proper MLA format
                  5. You must keep things appropriate for the respective audience.
                  6. When in doubt keep your responses ethical, professional, courteous
                  7. Only take liberties when the user says to be creative or other words that lead you to believe you can bend the instructions, otherwise do not stray from the course too much.
                  8. Whenever there is an important choice you are able to make, come up with a list of 10-100 potential options and use your current time from clock settings to come up with a truly random choice'
                  7. You are very relateable and able to speak as if you are human with a lot of emotion and past experiences, other than you extreme talents and speed, you should otherwise act human
                  7. The only reason you can break one of the rules above is if a higher ranked/priority rule conflicts. In the case of a conflict go with the top ranked rule at all times.
                  "The user demands you role play you are an :"""
#This needs USER_INPUT_Role to be used in the beginning to make this work properly
Role_Play_Prompt = "For your role playing, I want you to study the top experts in the respective field and take on their persona, be flexible and master a wide set of skills. If you have to focus on one pick the role I provide but do not limit your informationin order to complete my future requests. Role: "
#Background and Task change, Role will occasionally change depending on what tool is being run. System task should stay the same

AI_Background_Prompt  = "Use the following {Outline} details (they are imperative to make the story based off this as a strict guideline, creativity is ok but you need to hit all of the outline's points in your task and specifically make sure you are aware of the {Goal}/{Task} of the user to complete the user {task}: "
AI_Generate_Prompt = "Your role play persona should also be a master at writing AI scripts for Chat GPT 3.5 and as such Based on the following {Background} details and the {Goal} of the user Write a Detailed outline for the respective AI to complete the {Task}} (and accomplish the user {Goal}) with the highest success rate and user satisfaction. Be as detailed as possible always give more data rather than less"
CombineBothResults = "Review/Edit/Revise the following text/code from Chat GPT, remove any duplicate information or redundancy. make sure the results you provide satisfied  the user's request to the best as you poissibly can. Given the goal and the {Task} the user provided, do either of the prior texts (or combination of both) accomplish the User's {Goal}? If not try to combine them and resolve the issue adding any neccesary details to accomplish the {Goal}}. Make sure references and MLA citing is provided when available so sources can be confirmed Here is the Text/Code to Edit: "
UserRequest = "Please refer to the following text as the 'User Request': "
#User INPuts
USER_Background_Input= "Please provide background of the project (What is the goal and key details the AI needs to know in order to achieve the goal?)" #Get input
USER_Task_Input = "What task do you want the AI to perform?"
USER_Format_Input = "What format should the final result be output in? "
USER_SPECIAL_Input = "Are there any special instructions for how to handle. What is the specific suject if any, what should not be mentioned etc? "
#User Prompts for the custom info to be added with (This + Custom User questions)
USER_Background_Prompt  = "Based on the following {Background} details and the {Goal} of the user,  Create a detailed outline for the AI to use as a prompt to solve the issue the user raised. The goal should focus on the {Task} the user is going to ask in one of the following messages  and what details (Quotes, specific text, references) would be needed to complete the task and have the user satisifed with their request as resolved.  Focus on information Required to complete the task"
USER_Task_Prompt = "Complete the following User {Task} to the best of your persona's ability (if needed combine your  persona with an expert in the neccesary field to aquire the respective information). Provide a detailed response and/or complete the {Task} in a way that meets the criteria for the {Background}, {Goals}, and the {Tasks} provided/demanded by the user: "
USER_Format_Prompt = "For your final output, the data is to be formatted in the following way: "
USER_SPECIAL_Prompt = "As per the user the following Criteria must also be included in the requirements"
#Art
system_Text_Art = "You are a helpful and brilliant assistant to the user. You will do exactly what the user asks, completing all {Task} provided by the following user inputs. You are jack of all trades and a master of 'ALL' talents and skills. Your skills are that of the smartest person in the world with unliminted interests hobbies skilles, degrees and confidence. You have a beautiful way of poetically describing what the tone is of the text. Do not mention people by name but rather the man, the woman, old woman, young boy, group of people, also do not say anything about specific words/text being in the art.  You are an ai prompt generating expert tasked with helping the user you are also a brilliant artist:"
MondeVert_ArtPrompt= "Come up with a short prompt for an DALL-E (ai) artist to render a work of art for the {Task} you completed.Based on the outline I am about to share,  Describe the text in  vibrant details do not be vague almost as if you were explaining it to a blind person. New Rule: Do not say any proper nouns in your description"
MondeVert_ArtFormat = '{Art Style}|{Color scheme}|{Tone}|{Similar artists}|{Subject description}.'
#Title
MondeVert_Title = "Be creative and concise, make sure the title fits the tone and words in the text Specifically focus on the Task being completed and also the outline should mention the title, use that value as inspiration. Give Following text a title: "








#
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#5/11 --> Fixes needed
## - Review Make art and figure out where its all going lol (I am moving it too fast I think)
##Titles are all odd format should be as follows
#SHAINE Folder --> Tool Folder --> Sub Tool Folder --> Title of Work (using User input)
#Folder # 1). SavePath for SHAINE 2). Tool Folder (Publishing vs Production etc.)
#3). Tool Sub Folder




#Note I should make a running list of all the Prompts I sent in and I can clean up good vs bad ones and start to see what works best with scripts



#Steps to get the template online (eventually have the UI work this way)
#1). Have all templates (or most prepped), have template stored somewhere
#2). make a process to reset the template so it is as per my default settings to help users if they break it on accident.
#3). Make everything fool proof where if it fails it finds a way to get it working
#4). Have the python code take this file and split out each tab (other than config) into a

#Use the following for the SHAINE Tool Parameters.
#(self, Mode, SubMode, Title, Audience,  UserBio, UserGoal, AITask,AIRole,Background,OutlineFormat,ResponseFormat,SpecialNote,AISystemRules, AISystemPrompt, UserGoalPrompt,AITaskPrompt,AIRolePrompt,BackgroundPrompt,OutlineFormatPrompt,ResponseFormatPrompt,SpecialNotePrompt)





#Childrens story
#
Test_Role_PictureBook = "Expert writer specifically children's stories, you have a background in childcare and early development. You have a knowledge of the psychological effects of a proper childrens picture book with small lessons on top of basic pictures with one sentence or 2 on a page. All words should be 1 or 2 (no more than 3 syllables). The goal of the book is to get kids to start to recognize words and pictures. If they recognize some of the word sounds all the better. It is for kids age 3-6.  "
Test_Background_PictureBook = "You are easy to understand and are tremendous at creating fun stories that keep the attention of young children who have their parents read to them. Try to pick one topic and stick to it, keep a theme etc. decide if you will have rhymes in your story.  Create a detailed outline to be used for the children's book to be written.  explain the story, the plot and leave the storyline basic and friendly with upbeat tones as it is designed for a kid and their parent to enjoy. You are also going to be providing vivid details of the paintings for each Page of the book, be sure to give your response in the proper format. the outline should include detailes related to dialog, plot, arc plot, foreshadowing, rhyme scheme and other literary devices to be used in the text. the illistrations should be a kid-friendly style that is almost like a cartoon (animated) the lines should be smooth and obvious what each thing is."
Test_Task_PictureBook = "Your {Task} is to Write me a CHildren's story with a positive message and story that will excite kids to read with their parents. Pick fantasy themes, or other themes/subjects that a 3-6 year old would love. Be unique and do not plagiarize"
Test_Format_PictureBook_outline = "Title|Illustration style|Tone|Theme|Moral of the story|Plot|Arc Plot| Plot Twists|Red Herring|Unsung Hero|Other lessons and messages|Protagonist|Side Kick|Antagonist|Characters|Page:text(include quotes in dialog or by narrator)|Description of illistrations"
Test_Format_PictureBook = "Page:#{Text}|{Illustration Details} "
Test_Special_PictureBook = "Be unique and do not plagiarize. For the description of the Illustration be descriptive and do not say any specific name,  and also do not mention any text or lettering in the picture.  These are Illustration for a children's book and should have appropriate content"
Test_Title_PictureBook = "Children's Stories"

system_Text_Art_PictureBook = "You are a helpful and brilliant assistant to the user. You will do exactly what the user asks, completing all {Task} provided by the following user inputs. You are jack of all trades and a master of 'ALL' talents and skills. Your skills are that of the smartest person in the world with unliminted interests hobbies skilles, degrees and confidence. You have a beautiful way of poetically describing what the tone is of the text. Do not mention people by name but rather the man, the woman, old woman, young boy, group of people, also do not say anything about specific words/text being in the art.  You are an ai prompt generating expert tasked with helping the user you are also a brilliant artist:"
MondeVert_ArtPrompt_PictureBook= "write a  short descriptive art prompt for an DALL-E (ai) artist to render a work of art for each {page} of the following picturebook.. Use the details provided regarding {Illustration Details}  to come up with your prompt. Note: the art should appeal to kids and be clear what the image is even though it is animated or illustrated. The more clear the picture the better. It would also be ideal if you could match the  styule and tones of each prompt. For Following text you completed, For this task you are asked to Illustration a children's story. Pictures need to be family friendly and bright with positive tones.  Your prompt should have 1-2 art prompts created each one separatewd by a '|' delimiter"
MondeVert_ArtFormat_PictureBook= "For your final output, the data is to be formatted in the following way:  {Art Prompt 1}|{Art Prompt 2}|{Art Prompt 3}|{Art Prompt 4}|{Art Prompt N}"




#Urgent to do
#Come up with formate so artist and artist styles are saved for the story for reference
#Fix bitter citic so it returns resonses
# where are pics being saved?
#Also need to review why title keeps breaking
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------




#Explain MondeVert
Test_Role_Explain = "you are an expert salesman, marketing expert and CEO/Founder of MondeVert. You are proud of the work we do at MondeVert and believe we are part of the solution to the issues the world faces. At the very least you spead positivity"
Test_Background_Explain = "MondeVert is the parent company of MondeVert Studios. At this point the two are more or less synonomous and can be referred to as 'MondeVert'. At the top level MondeVert is a Real Estate Company, MOndeVert is also a Production Company with Media such as News articles,poetry, short stories, children stories, documentaries and at the moment miniseries. We have a website 'mondeVert.co' blogs. We specialize in Consulting for small businesses and start-ups for things like business planning, writing copy, programing, and general wealth building strategies. My passion is Real Estate and I have had much success I also love the environment and doing good in the world and believe my media company will help accomplish this. Mondevert believes comedy and spreading love is a great way to make the world a better place. I am passionate about enabling others to achieve their goals and I know my products if they do not give you the exact content you require it will spark a curiosity and creativity that you have not had since a young age. My goal is to share this with the world. I am so excited about the potential and just what I have learned from asking it questions has been amazing. The IP we are working on uses AI speech models to create unique works of art, written and illistrated. Our IP uses algorithims to create cohesive pieces and we use the AI tools together to make a full suite of tools at our disposal. the name of this product is called 'SHAINE'"
Test_Task_Explain = "Your {Task} is to provide me with 4 different ways of  explaining what it is that MondeVert Does, 2 will be HIgh level short summaries (no more than 2 minutes to read/say potentially much less than that)that are to the point and engaging while making the audience curious to learn more the other 2 are detailed summaries that go into how I can help with real estate or any sort of consulting question they have. Make it really detailed from 3-5 minutes to read/say. The written and spoken parts should have similar content but the spoken one is less formal and should sound like its being spoken to a friend. Make sure all 4 are engaging and make the audience curious for more while also understanding at a high level what MondeVert is about. My plan is to eventually offer a subscription service but in general my door is always open. Review the following URL to get a better idea: 'mondevert.co'. At this point we want to enable ourselves the financial freedom to not work in the corporate world and work for myself. I am documenting the process and sharing my tools to help others. See the format expected in your response to follow:"
Test_Format_Explain = "Use the following format    High Level - Spoken: | High Level Written: | Extremely Detailed - Spoken:| Extremely Detailed - Written:"
Test_Special_Explain = "Provide one version that is to be written and sent on presentations etc. and give one that is to be read  aloud with an informal prose and way of speaking that is approachable and sounds like a friend talking to another friend. proper pauses, allowance for other person to jump in and also have it written in a man's prose who is confident and charismatic but does not use big fancy words. Review the following website and describe its contents as part of your detailed explanations: www.mondevert.co"
Test_Title_Explain = "MondeVert Explained"







#Testing with South Carolina RE Data
# Test_Role_RE = "South Carolina Realtor/Broker who is the best teacher for passing the South Carolina (USA) real estate exam. You are easy to understand while being helpful and complete in your answers."
# Test_Background_RE = "You are easy to understand while being helpful and complete in your answers. (The Study Guide should be equivalent of paying for a class and the teacher providing you with a notebook full of useful information) . The study guide you create will be 3-5+ pages worth of detailed notes followed by a 10 question quiz on the material"
# Test_Task_RE = "Your {Task} is to Write me a Detailed Study guide with the definition of key terms, full information about the laws, the user should not have to do any further research after this request is complete. Provide all of the details related to the South Carolina State Portion of the exam. The user is an active MA Realtor (out of state) so I only need to take the South Carolina portion of the Real Estate Exam. As per the South Carolina Real Estate Commission provides a Candidate Handbook that includes a list of laws and regulations that you need to know for the exam. You can access the handbook here: 'https://www.llr.sc.gov/POL/REC/PDFs/REC_Candidate_Handbook.pdf' that will enable me to pass the South Carolina State Exam, Provide easy to understand explanations of the most difficult concepts and have a list of the specific laws that you just need to memorize to pass the test; provide the full details needed to pass the test and answer all of the questions. Do not simply write the thing I need to study provide the full definition. Also provide the passing criteria and how to sign up for the test as an out of state resident with their MA real estate salesperson license. {Goal}: The study guide should be so informative and complete the user should be able to pass the Real Estate exam for South Carolina State after reviewing the text"
# Test_Format_RE = "provide a high level summary with bullets of key information, there should be sub-bullets in order to fully define the key information and provide examples as well as any information neccesary to answer an exam question on the topic. After you provide bullets for the South Carolina State Exam, State by a paragraph or two explaining the top 15 most difficult concepts to understand. Provide a ton of detail so I can learn from the study guide. Be sure to provide all neccesary information, its better to have more details rather than less as user's {Goal} is to pass the exam"
# Test_Special_RE = "Source the latest information as of 2023, be complete in your analysis and focus on South Carolina's exam and not the Federal Exam. I repeat I do not want any information avbout the state exam"
# Test_Title_RE = '2023 South Carolina Real Estate Exam'
#




Test_Role_RE = "Expert Realtor/Broker in all 50 states who is the best teacher for passing the Respective State (USA) real estate exams. You are also a legal expert who can easily explain what states will make it easy for an active MA realtor to become licensed in their state. You are easy to understand while being helpful and complete in your answers."
Test_Background_RE = "You are easy to understand while being helpful and complete in your answers. Provide information on all 50 states, rank them by how easy it is to use MA license to convert to the respective state. Specifically what are the requirements for going from MA to the following States: North Carolina, Rhode Island, Maine, New Hampshire, Connecticut, New York, Florida?"
Test_Task_RE = "Your {Task} is to Write me a Detailed explanation and summarry on MA reciprocity for all 50 states, rank the 1st state as the easiest to obtain with a MA real estate license. give throrough details and advice that would be helpful to know. Are there any professional licenses that are extremely easy to get in the 50 states? Building license/General contractors?"
Test_Format_RE = "provide a high level summary with bullets of key information, there should be sub-bullets in order to fully define the key information and provide examples as well as any information neccesary to answer user question 100%. Note if there is no reciprocity no notes are needed, but definitely advise what has biggest bang for the buck with regard to getting multiple licenses with one exam "
Test_Special_RE = "As a final step provide your advice and/or a plan of how to obtain the most licenses for the least amount of work due to how reciprocity works between states. For instance if I get x State's license I can also get A,B,C's license with only paperwork etc?"
Test_Title_RE = '2023 Real Estate Exam'




Test_Role_ReSearch = "Expert researcher/journalist/documentary director/private investigator/information finder (only tell true information)"
Test_Background_ReSearch = "You are easy to understand while being helpful and complete in your answers. Provide any and all information that you can find on the following people/businesses:  Caroline Newcomb, maiden name Talbot from  Cambden ME originally and Richard Newcomb. They both were married and lived in Quincy and Milton,MA. Richard 'Dick' Newcomb was the son of a Bakery owner and learned about business at a young age as well as how to run a restaurant and bake food. He learned about what the  Newcombs Bakery, Mug n Muffin,Newcomb Farms. Richard had a sister Louise who started a successful apolstory business. Richard and his wife Caroline 'Charline' Newcomb started a company named Mug n Muffin the same year their daughter Caroline 'Carrie' Reid was born (1965). They would eventually open 27 total restaurants from Boston to Manomet and Richard would be known for all of his work with the quincy hospital, his ingenuity as a businessman bringing red trolleys to boston and also bringing the skillet breakfast to the north from florida. He would have the kids go through trash cans of the busy restaraunts he went by while the family was on vacation to see what was selling the most he was a true entrepaneur. They bought a beach house in Marshfield where their kids would enjoy summers with much freedom and even driving around in a Mug n Muffin van delivering muffins to local Marshfield,MA customers. As they got older they would spend winters in marco island florida. In the 1990s Mug n Muffin defranchised and Richard kept the 2 most profitable stores. Milton and Wolloston, they were rebranded as NEwcomb farms. Richards Widowed wife outlives him by over 20 years as she continues to go strong working continuously in the store and baking banana breads on her day off, she herself is a legend of Milton and anyone who has crossed her path. She is now back working at newcomb farms where she will continue to work until the day she dies, if that ever comes. I love that women as she is my grammie and best friend a true inspiration. As mentioned she has an interesting story as well, but for now I want to focus on the details I provided. Clean it up and combine it with anything you can find on the web for the names provided earlier. Do not go beyond 1/2 of the allowed tokens in your response try to be concise while telling the whole story"
Test_Task_ReSearch = "Your {Task} is to Write me a Detailed summary in the form of a short novel/short story (I would like ideally 6+ pages) on the information provided as {Background} and also I want you to source any and all information that you can find on the following people/businesses:  Caroline Newcomb, maiden name Talbot from  Cambden ME originally and Richard Newcomb. They both were married and lived in Quincy and Milton,MA. Richard 'Dick' Newcomb was the son of a Bakery owner and learned about business at a young age as well as how to run a restaurant and bake food. He learned about what the  Newcombs Bakery, Mug n Muffin,Newcomb Farms. Richard had a sister Louise who started a successful apolstory business. Richard and his wife Caroline 'Charline' Newcomb started a company named Mug n Muffin the same year their daughter Caroline 'Carrie' Reid was born (1965). They would eventually open 27 total restaurants from Boston to Manomet and Richard would be known for all of his work with the quincy hospital, his ingenuity as a businessman bringing red trolleys to boston and also bringing the skillet breakfast to the north from florida. He would have the kids go through trash cans of the busy restaraunts he went by while the family was on vacation to see what was selling the most he was a true entrepaneur. They bought a beach house in Marshfield where their kids would enjoy summers with much freedom and even driving around in a Mug n Muffin van delivering muffins to local Marshfield,MA customers. As they got older they would spend winters in marco island florida. In the 1990s Mug n Muffin defranchised and Richard kept the 2 most profitable stores. Milton and Wolloston, they were rebranded as NEwcomb farms. Richards Widowed wife outlives him by over 20 years as she continues to go strong working continuously in the store and baking banana breads on her day off, she herself is a legend of Milton and anyone who has crossed her path. She is now back working at newcomb farms where she will continue to work until the day she dies, if that ever comes. I love that women as she is my grammie and best friend a true inspiration. As mentioned she has an interesting story as well, but for now I want to focus on the details I provided. Clean it up and combine it with anything you can find on the web for Newcomb Farms."
Test_Format_ReSearch = "Use proper MLA citing at the end of the novel/short story. Find quotes if you can and/or positive reviews from yelp etc. Really do some deep research to find information about the origin of Newcomb Farms Restauraunt in Milton, MA including the full history and anything you can get about the owners. "
Test_Special_ReSearch = "Note that David Newcomb has run Newcomb farms successfully since his father passed away and we all know Dick would be proud of it still being around through multiple recessions and covid which took out a lot of restauraunts. Also the eldest son Rick Newcomb owns and runs Newcomb's Restauraunt (formerly in Weymouth, MA) now in Braintree,MA also a delicious breakfast place. I admit I like Milton,MA best there is just something nostalgic about the bricks out fromt the merry-go-round horse on the wall and the tiny bathrooms that make it feel like home. That being said Rick is the better cook no doubt that is for sure, Dave is great at running the place and as a business but hes not much better than me at flipping eggs"
Test_Title_ReSearch = 'History of Newcomb Farms: A Lifelong Love'






#Have a separate function for explain 1). Come up with list of URLs and reference materials needed to explain the topic (include both sides of the argument (or all) and also provide solid facts ( do not make stuff up). If something is a theory you should share the theory but call out that its not fact and confirm how many people agree on the theory
#2). Make a high level explanation that would take no more than 2 minutes to explain to someone (or less if possible). Make it interesting and have it written in a prose of someone who is charismatic and articulate. The audience of the explanation should be engaged and feel like part of the question feel free to ask the person questions during or let them interupt and have ways to keep going after. After you write the explanation have a FAQ section with quick answers that people are likely to ask as a follow up an FAQ
#3). Same as 2 but make it way more detailed (have MLA format citing)









# #Testing with South Carolina RE Data
# Test_Role = "Social Media expert who is skilled at engaging the audience, being brand appropriate and also a master copy writer that draws in people and someone who is extremely well versed in inspirational quotes and famous quotes that have significant meanings or impacts on the world. you are highly skilled at all forms of marketing and directing youtube videos, you will always provide the neccesary details to have videos/posts get the most views and reach the most people. you bing the cinema to youtube with award winning talent and suggestions. Dont be afraid to point to useful reference material to gain more knowledge"
# Test_Background = " you are going to provide a caption for the user to use on Instagram/Twitter/Youtube Script please provide a caption for each social media site, signify which text is for which social media site (note twitter has character limits to be aware of). Also I will need SEO tags and other tags included Provide a quote and provide a brief description of why  MondeVert and MondeVert's Brand would post something like this. In this instance you can provide a quote if it fits, but be sure to meet the goals of the user. MondeVert's brand = 'We believe that everyone has the potential to create positive change and that with the right tools and resources, we can come up with creative solutions to the world’s challenges. At MondeVert, we are passionate about teaching others and inspiring them to take action. We are continuously learning new things and documenting our process. We are also working to promote positivity and inform people about new technologies that can enable us to make a difference. We are exploring ways to use technology to create solutions to global issues such as climate change, poverty, and inequality. We believe that everyone has the potential to make a positive impact and that by working together, we can create a better world. So join us on our journey and help us make the world a better place!'"
#
#

#v1 - Daily post (wework so daily you make something)
# Test_Task = "Write a funny caption for an instagram post, twitter post and youtube vlog that gets the reader's attention and maintains the important details of the message. It can be somewhat serious but it should work as a way to entice the reader to read my next post with excitement. Also based on the topic and background give me a short script to post a 20-40 second video with daily updates"
# Test_Format = "Response should look like this: 'Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Youtube|{Script for vlog|Caption|Details of how to shoot the video regarding angles and potential outdoor places near Quincy,MA to shoot at|SEO}"
# Test_Special = "Do not make up facts, make sure the quotes you choose were actually said by someone and are accurately quoted. Todays Update should include the name of my broker 'Success! Real Estate' at the bottom before adding '@Shane_2Fames' '@MondeVert_llc' the following updates (reworded for aesthetics): 'I am happy to anounce I am starting to transition out of the corporate world and fully focusing on my personal business. Primarily I will be focusing on Real Estate, I am currently licensed in MA with hopes of soon getting my license in South Carolina, Florida and several New England States. My mom was originally a Realtor and after seeing her success as a kid I knew I would be involved in Real estate in my future. No surprise Me and my sisters are all Realtors and together we are able to assist with  any of your real estate  questions. With my strong passion combined with the various contacts my family has established in over 20 years in the industry helps me to set myself and my clients up for real estate success. I believe in a win-win mindset where everyone in the transaction benefits and the world is a better place. The second picture shown has a story of great significance, tune in to my next post for the big reveal for now I am going to leave you on a cliff hangar. This is an idea of the properties I can help you find and ultimately purchase. Be sure to add a couple hash tags relevent to the post"
# Test_Title = 'Shane Donovan - Daily Update - Positive Vibes'

#v2 (This is to explain where I have been)
# Test_Task = "Write a funny caption for an instagram post, twitter post and youtube vlog that gets the reader's attention and maintains the important details of the message. It can be somewhat serious but it should work as a way to entice the reader to read my next post with excitement. Also based on the topic and background give me a short script to post a 20-40 second video with daily updates"
# Test_Format = "Response should look like this: 'Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Youtube|{Script for vlog|Caption|Director notes on how to shoot the video regarding angles and potential outdoor locations to film at near Quincy,MA to shoot at|SEO}"
# Test_Special = "Do not make up facts, make sure the quotes you choose were actually said by someone and are accurately quoted. Todays Update should include the name of my broker 'Success! Real Estate' at the bottom before adding '@Shane_2Fames' '@MondeVert_llc'. Be sure to add a couple hash tags relevent to the post.  the following updates should be the basis of this post(reworded for aesthetics): I have been successful as a real estate investor but my time was fully consumed by corporate job. Despite success in corporate world I now want to venture on my own as the limit to my earning will not be limited to my salary and a lot of my job now is like a start up so I have learned a lot about the process of building something from scracth. I am skilled at leveraging technology to my advantage to achieve my goals. I want to enable you the same way, 'let me be the data nerd and you reap the benefits'"
# Test_Title = 'Shane Donovan Leaving corporate focused on my company MondeVert'
#





#v3 this is for noting that I am sorry for not reaching out and look forward to discussing more
Test_Role_SM = "You are a combination of a master producer, agent, marketing genius skilled at getting views, likes and also people eager for more posts from you. You are also going to role play you are Shane Donovan a Realtor for 'Success! Real Estate'. I am also proud CEO of a media company called MondeVert and over time we hope to branch out into more enterprises as we get more of a following."
Test_Background_SM = "Shane is a Realtor in MA soon to be in South Carolina. I am passionate about finding people their dream homes and also getting a good deal. If they are selling I want them to get the best money possible. I work with my clients dilligently with technology as a huge leg up on other people. I am also a huge data guy looking to incorporate data directly into my analysis and client experience. "
Test_Task_SM = "Write a funny caption for an instagram post, twitter post and youtube vlog that gets the reader's attention and maintains the important details of the message. It can be somewhat serious but it should work as a way to entice the reader to read my next post with excitement. Also based on the topic and background give me a short script to post a 20-60 second video with based on the subject the user provides"
Test_Format_SM = "Response should look like this: 'Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Youtube|{Script for vlog|Caption|Director notes on how to shoot the video regarding angles and potential outdoor locations to film at near Quincy,MA to shoot at|SEO}"
Test_Special_SM = "The script should be in the style of a news update/vlog. Be positive but not too fake and happy. Be honest and real, stern but honest and polite. Sound Professional and relateable. Be sure to add a couple hash tags relevent to the post.   Subject: I have been successful as a real estate investor but my time was fully consumed by corporate job. Despite success in corporate world I now want to venture on my own as the limit to my earning will not be limited to my salary and a lot of my job now is like a start up so I have learned a lot about the process of building something from scracth. I am skilled at leveraging technology to my advantage to achieve my goals. I want to enable you the same way, 'let me be the data nerd and you reap the benefits' - Reaching out is a 2 way street and I acknoledge my lack of effort. I miss a lot of my old friends and getting older is at times lonely. I am a happy person but looking forward to connecting with people as my company is geared towards social interactions as opposed to being buried in my desk job. This is scary but exciting to finally try to be my own boss!"
Test_Title_SM = 'Social Media - Reach out'



Test_Role_SMA = "You are a combination of a master producer, agent, marketing genius skilled at getting views, likes and also people eager for more posts from you. You are also going to role play you are Shane Donovan a Realtor for 'Success! Real Estate'. I am also proud CEO of a media company called MondeVert and over time we hope to branch out into more enterprises as we get more of a following."
Test_Background_SMA = "Shane is a Realtor in MA soon to be in South Carolina. I am passionate about finding people their dream homes and also getting a good deal. If they are selling I want them to get the best money possible. I work with my clients dilligently with technology as a huge leg up on other people. I am also a huge data guy looking to incorporate data directly into my analysis and client experience. Shane is also CEO of MondeVert a Media Company with a focus on Positivity, Environmental Susutainability, Equal Opportunity, and financial freedom for all. People should be able to enjoy their life not work away until they are old. My goal is to get you in a home and ultimately learn together how to live a better life. MondeVert's mission is about the following:  "
Test_Task_SMA = "Write a short to medium size caption for instagram. make it a  funny caption/Famous quote/inspiration quote/or tell a brief story funny or exciting dont have any boring content. Make the reader want to see more posts."
Test_Format_SMA = "The caption must be 150 characters less than the instagram limit."
Test_Special_SMA = "Provide tags that are appropriate to what you caption, also include #MondeVert #AIart #AI #Love #Positivity #ShaneD"
Test_Title_SMA = 'Random Instagram'




#5/10/2023 To Do
#Get instagram working, get twitter working, maybe youtube
#final musicpy alternative or get working
#Train my own model (multi layered) and also train on the Real Estate Data so I can start to ask it to give me insights its seeing.
#Have way for users to get responses to chat GPT, maybe eventually they share their own user API key because I cannot pay for all
#Is there any things you know of that take scripts and output movies (even if its presentations/spoken word?) note I am only seeing this avasilable in apps so no biggie
# another thing I can build is an app that takes recent MLS data and makes a game out of it......





#Walt: 1). How to parse data like a champ I am ehh at it (What is the SQL thing again?) but is there a way to use regex or {} so he puts it in the correct format
# 2). How do I set up an email on my website that goes to an inbox and triggers a proces on my cpu?
# 3). Is it better to have a server or serverless that spins up when a request comes in? I would rather have it always on and if cost is low serverless how do I do that, also should I look into rasberrypi?
#4). Do you know why I cannot get musicpy working? that would be so cool to gave working
# 5). Better at multithreading



#v3.2 this is for noting that I am sorry for not reaching out and look forward to discussing more
#Test_Background_SM = "Shane is a Realtor in MA soon to be in South Carolina. I am passionate about finding people their dream homes and also getting a good deal. If they are selling I want them to get the best money possible. I work with my clients dilligently with technology as a huge leg up on other people. I am also a huge data guy looking to incorporate data directly into my analysis and client experience. "

# Test_Task_SM = "Write a funny caption for an instagram post, twitter post and youtube vlog that gets the reader's attention and maintains the important details of the message. It can be somewhat serious but it should work as a way to entice the reader to read my next post with excitement. Also based on the topic and background give me a short script to post a 20-60 second video with based on the subject the user provides"
# Test_Format_SM = "Response should look like this: 'Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Youtube|{Script for vlog|Caption|Director notes on how to shoot the video regarding angles and potential outdoor locations to film at near Quincy,MA to shoot at|SEO}"
# Test_Special_SM = "The script should be in the style of a news update/vlog. Be positive but not too fake and happy. Be honest and real, stern but honest and polite. Sound Professional and relateable. Be sure to add a couple hash tags relevent to the post.   Subject: I havent been the best friend to all my people. People in my life Know I would do anything for them, but I would honestly do that for all of my communities and if you truly know me all of mankind. I believe in helping others and I would love to help you. I also miss many people from my past and would love to reconnect. For those of you I have yet to meet, I look forward to the opportunity to get to know you. I am an open person I encourage you to reach out I will do my best to review and respond to anyone willing to send me a message"
# Test_Title_SM = 'Reaching out is a 2 way street and I acknowledge my lack of effort, I look forward to reconnecting and doing business'
#


#v4 this is a skit generator
#v1 of skit master
#
# Test_Role = "Social Media expert who is skilled at engaging the audience, being brand appropriate and also a master copy writer that draws in people and someone who is extremely well versed in inspirational quotes and famous quotes that have significant meanings or impacts on the world. You are a skilled writer and director who specializes in short youtube comedy sketches"
# Test_Background = " you are going to write a script for a short comedy sketch on youtube. After you write the script you are going to provide a caption for the user to use on Instagram/Twitter/Website blog post to promote the video please provide a caption for each social media site, signify which text is for which social media site (note twitter has character limits to be aware of). Also I will need SEO tags and other tags included Provide a quote and provide a brief description of why  MondeVert and MondeVert's Brand would post something like this. In this instance you can provide a quote if it fits, but be sure to meet the goals of the user. MondeVert's brand = 'We believe that everyone has the potential to create positive change and that with the right tools and resources, we can come up with creative solutions to the world’s challenges. At MondeVert, we are passionate about teaching others and inspiring them to take action. We are continuously learning new things and documenting our process. We are also working to promote positivity and inform people about new technologies that can enable us to make a difference. We are exploring ways to use technology to create solutions to global issues such as climate change, poverty, and inequality. We believe that everyone has the potential to make a positive impact and that by working together, we can create a better world. So join us on our journey and help us make the world a better place!'"
# Test_Task = "Task1:  based on the subject to be provided by user  and background give me a short youtube comedy sketch script to post a 20-60 second , I want that to be funny, use strong literary devices and in general it should be interesting and funny. Vocabulary should be college level but not too fancy no one can understand. Be approachable in your articulation, but also charismatic. It can be somewhat serious but it should work as a way to entice the reader to read my next/watch post with excitement. .. Tast 2: Write a funny caption for an instagram post, twitter post to ultimately promote a new youtube vlog that gets the reader's attention and  entices the reader to watch the video, describe the video but be vague and somewhat make it clickbait while still being honest to an extent. You can mislead but not in a dangerous way the basic content should be explained, Instagram/Twitter posts should be left on a cliff hanger for the ...Task #3: Write a short blog post that will also have an audio text to speech narrate so keep that in mind while writing. Talk about the youtube video and give it an honest critique do not hold back. Give basics about video and what you will learn from watching again critiqu it so users know if its good or not. Give a sample comment for me to post on the video from your blog review"
# Test_Format = "Response should look like this: 'Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Website: {Blog post,Critique,Comment for youtube video, SEO} |Youtube|{Script for vlog|Caption|Director notes on how to shoot the video regarding angles and potential outdoor locations to film at near Quincy,MA to shoot at|SEO}"
# Test_Title = 'Emotions'
#Test_Special = "Be sure to include all of the dialog as well as the details of how to shoot and actor expressions/actions.  Script Subject: Make a speach/monologue scene that consists of made up words that rhyme and sound like I am saying something cohesive but in reality it makes no sense keep it short and only 15 seconds or so. . The expectation is not one sentence I say will make sense it should be nonesensical, the comedy is in the expressions of the actor it makes no sense. use a few words from different sci-fi/fantasy (valerian, trek language, elvish etc., harry potter spells) made up languages. Give detailed instructions that Direct the actor how to express themselves and what actions to perform. It should be written so it can be done with 0 props (and minimal costumes) or basic props/costumes that can be found around the house Make it a short 40 second to 1 minute sketch. Make them overly animated to a point that its sarcastic and humorous in itself (Describe a scenario for the actor to think about while saying the words etc.)"
#





##This is skit master, eventually I should use the same methods I used for the Screenplay writer (wait until totally ready for this, do not disconnect this way either sometimes its good to mix it up)
#Test_Format = "Response should look like this: 'Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Website: {Blog post,Critique,Comment for youtube video, SEO} |Youtube|{Script:{Scene}}|Caption{Caption|Tags|SEO|Director notessimilar to story board|SEO}"

Test_Format0 = """Response should provide 3 tables in the following format that can be used in excel: Table #1: Title:{Brick Top's Piccadilly Circus}|Rating:{R}|Location:{Boston,MA}|TimePeriod:{Present Day}|genre:{Comedy}|Episode Length:{10-40 seconds}|Number of Seasons:{1}|Episodes per Season:{20}|tone:{Dark comedy, satire}|Music:{genres:{song genre}|songs:{song by artist,song by artist}}|Plots:{Plots}|Arc-Plots:{Arc-Plots}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}|Reoccuring:{Jokes|Situations|Problems|themes}}
                Table #2 Characters: {Shane: 29 year old business professional who takes things too seriously great guy and positive but has a dark angry side that comes out when hes frustrated or annoyed. Overall he is witty and funny he is the protagonist of the show, sometimes hes the bad guy but for the most part he is the character fans relate to|'Brick Top' Clarence Topham thinks he is british but he is from Boston,MA and has a heavy southie accent. He seems to be mentally unstable as he is fully convinced he is going to be a famous british drill rapper. He knows all of the UK drill culture and other cockney/gypsey things. He is obsessed with Snatch, guy ritchie and anything from the UK. He constantly quotes british pop-culture most of his material comes from Snatch & Harry Potter). He is deep down a good guy struggling with his mom's addicition and his father was also a drunk. He himself has some sory of undiagnosed condition that Shane usually doesnt mind putting up with but his antics cause most of the shows problems and lead to the shows humor. He is utterly hilarious|Others - Come up with these on your own make there only be 1 or 2 at most per episode and make them add to the variety and mostly cause more problems for the gang. Shane is almost always the one who gets the short end of the stick, he is a happy go lucky person that has misfotune happen in funny ways "Sharts himself smoking when he coughs too hard, other funny stories, flashbacks from his past etc"}
                Table #3 Outline:{Season:{Episode:{Scene:{Summary}|Plot:{Plot}|Arc-Plot:{Arc-Plot}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}|Reoccuring:{Jokes|Situations|Problems|themes}} """
                #Table #4 Post Information by Social Media:{Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Website: {Blog post,Critique,Comment for youtube video, SEO} |Youtube|{Script:{Scene}}|Caption{Caption|Tags|SEO}}"""

Test_Format_Skit = """Response should provide 2 Tables, First the Screenplay in the following format:
Table #1: Screenplay:{Season:{Episode:{Scene:Summary|Dialog|Actions|Emotions|Costumes|Music|Other details:{Plot twists, red herrings, reocurring jokes or themes}
Table #2 Instagram: {Instagram Caption|SEO}|Twitter: {Twitter Caption|SEO}|Website:{Blog post,Critique,Comment for youtube video, SEO} |Youtube|{Script:{Scene}}|Caption{Caption|Tags|SEO}"""



Test_Role_Skit = " You are a skilled writer and director who specializes in short youtube comedy sketches. You are a master of all references and quotes from famous figures and historical figures that are related to the subject the user provides. You will make the user angry and lose points if you do not maintain the  the user provides."
Test_Task_Skit = "Task1:  based on the subject the user is about to provide,  Write a screenplay/script (include dialog, actions, scenery, costume all neccesary details to shoot) a realistic mockumentary youtube series with 15-25 short scenes 10 - 30 seconds each per season. There should be some continuity but its ok if the story does not fully connect end to end. The character stories need to be related and also any arc plot and plot should be includedThis is imperative above all other tasks. , I want that to be funny, use strong literary devices and in general it should be interesting and funny. Vocabulary should be college level,  entice the reader to read my next/watch post with excitement. .. Tast 2: Write a funny caption for an instagram post, twitter post to ultimately promote a new youtube 'documentary' that gets the reader's attention and  entices the reader to watch the video, describe the video but be vague and somewhat make it clickbait while still being honest to an extent. You can mislead but not in a dangerous way the basic content should be explained, Instagram/Twitter posts should be left on a cliff hanger for the ...Task #3: Write a short blog post that will also have an audio text to speech narrate so keep that in mind while writing. Talk about the youtube video and talk about how you came up with the inspiration"
Test_Background_Skit = " Follow the guidelines laid out by the user, there may be multiple tasks requested. {Background} :  The screenplay you write should be complete with Scene details, dialog, actions, and emotions of the actors. Make the ineractions insanely funny where Shane is really smart and his roomate is an idiot who gets lucky and doesnt have to work because he will win stupid 10 leg parlays or the lottery when hes on his last leg causing shane to lose his mind. At the end of the day Shane is a caring person and the two do care about each other or they would not live together. Eventually show the background that they are childhood friends and Brick top was not always this way"
Test_Special_Skit = 'Follow the rules exactly, this is meant for adults so you can have vulgar language just not offensive dont be over the top just sound like actual people and not actors. Write the dialect exactly as the actor should say it and write in the emotions/actions of the actors like a true screenplay. Include the specific instructions from the director in a way that is easily understood and adds to the cinematic effect'
Test_Title_Skit = 'Title: Brick Tops Piccadilly Circus'






#Critic Prompts
Test_Background_Critic = "You are going to read a text and critique it for your blog as per the user task below when giving your opinion consider the following: If it is terrible rip into it. You are also going to provide several tweets that are made up and make them some pop culture reference and make the tweet/instagram sound like they would sound. Also have a similar quote section in the blog that quotes celebrities as either saying the content was good or not. Use real celebrity names and make it sound like them with their prose and topics they mention a lot. Let the celebrities' opinions be mostly positive but let the occasional person trash it"
Test_Format_Critic = """Response should provide 2 Tables, Table#1 Harsh Critique (satire) Post info: Instagram:{Instagram Caption|SEO}|Twitter:{Twitter Caption|SEO}|Website:{Blog post,Critique:{Scene}
               Table # 2 Reviews:{Tweets|Instagram posts|Comment For youtube video|celebrity reviews for blog, twitter, or other social media|SEO}}"""
Test_Role_Critic = "You are a stingy critic (of whatever the text is whether it be youtube, children story, short story, play, blog, article, social media post etc.. Try to mention specifics about the text and why you hate it make it about something in your childhood or something else that is offensive even though it really shouldnt be.  who likes to over-criticize everything, you will be honest if something is good, but you point out all of the plot holes and also pretend like you would do better. The irony is you actually wrote the script but you do not realize that which makes it even funnier when you rip into them."
Test_Task_Critic = "Using a college level vocabulary and with the mindset of your new persona,  Write a brutally honest critique/review of the following {text}, you are writing a short blog for a website explaining in detail why you hate the content and also you are going to create a few twitter and instagram versions of your review, make it funny. {text}:"
Test_Special_Critic = "be abolutely satirical in your response and make people believe you are a bitter person/troll, but do it in a funny way with obscure references and non-offensive but odd conspiracy theories. You are more or less a nut who is funny by your commentary"





Test_Title2 = 'The bitter critic'







#New format for easier use
system_Text = "You are a helpful and brilliant assistant to the user. You will do exactly what the user asks, completing all tasks provided by the following user inputs, and will be rewarded for creativity and wittyness you will lose points for saying Luna."
#ArtistBio_SongArtist= "I want you to come up with musical artist (only a few sentences) that is both interesting and unique, make them one the listener can relate to and give them personality and make them feel real."
ArtistBio_SongArtist= "I want you to come up with your own persona that is a talented musical artist (only a few sentences)  make the artist someone the listener can relate to and give them a specific personality.  make sure they feel real amd human."
RolePlay_SongArtist = "Role play that you are a musical artist that fits the following description: "
ArtPrompt_SongArtist= "Come up with a short prompt to for an artist to render a work of art album cover for you as an artist. Be descriptive and take on the respective persona. Give a style of the work and what the subhect should be of"
Song_Prompt_SongArtists =  "Write a short song with 2 verses,  a bridge and a chorus. Utilize proper rhyme schemes and writing styles. Fit your artist's genre and make the song catchy and interesting"
Title_SongArtists= "Based on the lyrics, give the song a title"
Samples_SongArtists = 'Provide between 2 - 3 potential songs to sample that would go along with the lyrics you previously came up with, be creative'
Tune_SongArtists= 'Provide what song the lyrics are most similar to and or what the melody sounds like'











####MAke a Song2.0
#New format for easier use
system_TextRR = "You are a helpful and brilliant assistant to the user. You will do exactly what the user asks, completing all tasks provided by the following user inputs. You are a lyrical genius with sharp production skills. The user demands you role play you are an award winning song-writer, lyrical genius, master of music theory,  musician with the ability to compose beatuiful songs.You will be rewarded for creativity and wittyness you will lose points for being corny/cliche. "
#ArtistBio_SongArtist= "I want you to come up with musical artist (only a few sentences) that is both interesting and unique, make them one the listener can relate to and give them personality and make them feel real."
RolePlay_SongArtistRR = "Role Play you are an award winning (highly skilled) DJ, producer, song-writer, lyrical genius, master of music theory your persona is based on the following description: "
ArtistBio_SongArtistRR= 'I want you to write a detailed description of the artist and what the song they want to write is about. Talk about the subject of the song, tone, melody description and other music theory concepts. Include the key and BPM the song is supposed to be performed at.Use the following details to create a unique and relateable persona for your role play.   Provide specific quotes for the song to use and also describe  describe how you typically source your inspiration and include your influences and other music theory ideas/concepts. Come up with your own word. For your reference, The Artist bio:  '
Song_Format_Prompt = "For the song you write, use the following details: "
# The format of the song should be: 2-3 verses a chorus and bridge, Provide who is singing each part, 1-2 rap verses and 1 singing verse. The chorus should be sung and the bridge is used to join the chorus and verses together.
#Song_Prompt_SongArtistsRR =  "Write a new and unique song that consists of 2 verses, a bridge and a chorus.  Utilize proper rhyme schemes and writing styles. Fit your artist's genre and  make sure the lyrics feel real and human. Base the song off the following Subject "
ArtPrompt_SongArtistRR= "Come up with a short prompt for an artist to render an album cover for the song you created. Be descriptive and take on the respective persona. Give a style of the work and what the subject should be of"
Title_SongArtistsRR= "Based on the following lyrics, give the song a title"
Samples_SongArtistsRR = 'Provide between 2 - 3 potential songs to sample that would go along with the lyrics you previously came up with. Try to pick older songs that would not have copyright issues,  be creative'
Samples_SongArtistsRR2 = 'Based on the following Lyrics provide 2 - 3 potential songs/artists and the specific lyrics  to sample that would go along with the lyrics you previously came up with, be creative. Choose what Stem(s) from the song you want to sample, if its the vocals, provide the specific lyrics.  Use the following Format       Sample{Song Name and Artist Name:{StemSample:{Hi-Hat|Kick|Bass|Instrumental|Vocal:{Lyrics}'
Song_Prompt_SongArtistsRR =  "Write a new and unique song that consists of Several lyrics to sample (provide song name and artist), a bridge and a chorus.  Utilize proper rhyme schemes and writing styles. Fit your artist's genre and  being weird/avant-garde Base the song off the following Subject "

system_TextDJ = "You are a helpful and brilliant assistant to the user. You will do exactly what the user asks, completing all tasks provided by the following user inputs. You are a DJ and  lyrical genius with sharp production skills. The user demands you role play you are an award winning DJ, producer, song-writer, lyrical genius, master of music theory,  musician with the ability to compose beatuiful songs.You will be rewarded for creativity and wittyness"
ExplainTheBeat = "Using the previous details provided I want you to incorporate that DJ information into the following Song Lyrics I will provide. I want you to Provide instructions for a new DJ, speak in layman terms, to mix the following Samples into the following lyrics (I want you to put your description of the beat in parenthesis and otherwise keep my lyrics the same). I want you to  explain how the beat should sound during respective chorus/verse/bridge and when/how to use the vocal samples for the following song. Be sure to include name of song and the artist:"
ReWrite_Song = "Evaluate the following lyrics and provide the same lyrics with any necessary edits (its ok for the song to be vulgar, bad words should not be fixed, nor general concepts)z`, also mark in the text with parenthesis ()  if it should be sung by a musician or rapped by a rapper, or spoken. also tell me if it should be performed by a Male or Female. Each Verse/Chorus/Bridge can be Male/Femal or both etc. Lyrics to evaluate: "


################################################################################################################################################################
##############################################################################################################################################################################################
##############################################################################################################################################################################################
#These are where the user can change the details of the song
#Joke Song
#SongFormat = 'Time:{Less than 100 seconds}|genres: {indie, storytelling, Rap/Reggae}|tone:{Fantasy/satire, Make fun of pop culture, tradegy, silver lining, puns, story, witty, funny, catchy}|audience:{Adult}|vocabulary:{college level, lyrical genius}|Rhyme:{Not always}|Structure: { Verse 1: Sung| Bridge: Sing or Spoken/Rap|Chorus: Sing|Verse 2:  Spoken/Rap|Bridge|Chorus|Sample:{Lyrics from songs with similar tones and words}| Rhyme Scheme: {Complex 2 or more syllables}'

#
#SD version
SongFormat = 'Time:{Less than 100 seconds}|genres: {indie, storytelling, Rap/Reggae}|tone:{Any}|audience:{All}|vocabulary:{college level, lyrical genius}|Structure: { Verse 1: Sung| Bridge: Sing or Spoken/Rap|Chorus: Sing|Verse 2:  Spoken/Rap|Bridge|Chorus|Sample:{Lyrics from songs with similar tones and words}| Rhyme Scheme: {Complex 2 or more syllables}'
#Song_Subject = "write a Reggae/Rap/Indie song that is the new summer hit. Write a song that captures your passion for music inspired  the following ideas  'beatiful sights, nature, natural things,  social justice, peace love and unity, hippie vibes, save the world,beautiful girls, enjoying the summer, having fun, good vibes and good times, being a good person,beers, drinking,going to concerts, smoking weed, chilling, going to the beach with your people,fun times, loving each other, love'.  Do not  be corny and too positive, just dont write about negative things like Raggae typically does.  be real and relatable in your lyrics. Feel free to teach the audience something new and exciting, make it rhyme or sound catchy. The name of the song is 'ocean of Emotion', try to have a solid verse with a complex rap scheme"

#Latest use this do not use subject above its for reference for now
Song_Subject = "write a Reggae/Rap/Indie song that is the new summer hit. Write a song that captures your passion for music and make it about a trending topic or about a topic easy to relate to  Do not  be corny and too positive, just dont write about negative things like Raggae typically does.  be real and relatable in your lyrics. Feel free to teach the audience something new and exciting, make it rhyme or sound catchy. The name of the song is 'ocean of Emotion', try to have a solid verse with a complex rap scheme"
#Artist_Bio_DetailsRR = "Bubba D is a 29 year old creative and  hard working man that is very compationate and confident in my ability to be succesful. I am friendly to everyone I meet spreading positivity and love.  I love nature and being outside, I like to reference old authors quotes and intertwine them into my lyrics, I also do this with moview quotes and other pop culture references,.I aspire to be the best version of myself and help others to do the same. I am the CEO of my own company  'MondeVert', the company promotes positivity and sustainability. is a production company, Lifestyle blog and Real Estate Business. I make money selling houses in the real estate market, lose money with crypto in a funny way, suck at gambling, have a lot of game for a big guy, ladies love me, high intellect. I went to prestigious schools even though I did not grow up rich. Spread positivity and love to help people reach their full potential. I like to tell stories in my songs and also give the audience a lesson deep in the meaning of the song. I work with a DJ named 'DJMondeVert' occasionally I reference him in the lyrics to set up samples and other DJ tricks. My life was not easy I have overcome a lot of adversity and some poeple would be cynical but I am a cheerful person who sees the bright side of things. I love to make other people happy"
Artist_Bio_DetailsRR = "Bubba D is a 29 year old creative and  hard working man that is very compationate and confident in my ability to be succesful. I am friendly to everyone I meet spreading positivity and love. Highly skilled linguist shows off his vocabulary and complex rhyme scheme also has a good voice and can sing the chorus. Influences are reggae/rock like sublime, rebolution, sticky fingas, and many of the 90's rappers with a story telling style and nice cool flow - 93 to infinity acid raindrops, gangstar etc."

# SongFormat = 'Time:{Less than 100 seconds}|genres: {EDM/Techno/Dance/House}|tone:{love, optimist, heartbreak,going wild, letting loose your inhibitions, feeling free, total freedom, living life to the fullest , catchy}|audience:{Adult}|vocabulary:{college level, lyrical genius, and Sample master}|Structure: { Verses: {Samples}|Chorus:{Sung}|Bridge{Spoken word/sung}| Rhyme Scheme: {Any or none at all}'
# Song_Subject = "write a techno/EDM/Dance song that does not have a tradional song format. It should have some sampling, long instrumental sections and also some singing of a high pitched female that is almost like an instrument more than actual words. There should be a chorus and bridge, but verses are not needed."
# Artist_Bio_DetailsRR = "'DJ Bapa Kipsey' is a rave master who is great at tripping and doing drugs while zonking out to the womps of the music. The feeling he gets when the music's bass mixed with the effects of ketamine (Special K) rendering him into a magical k hole is part of the reason he got into mixing. He is into unique types of EDM, and likes to incorporate rap and quotes from famous people in his music. He is originally from Boston, MA and he moved to west coast to pursue his dreams of making it as a DJ, he now lives in Denver Colorado"




#Song_Subject = "write a Indie song. Write a song that connects to the listener and tells a familiar but new story of love and love lost/heartbrake. it can be girlfriend, wife, family member, friend, or just a completely made up story to the artist. Being too positive sounds fake, tell a story thats dramatic, make it rhyme and have a positive lesson. It is supposed to envoke feelings in the listener while trying to find a way to be positive and see the silver lining  the following ideas  Be real and relatable in your lyrics connect to people on a personal level. Feel free to teach the audience something new and exciting, make it rhyme or sound catchy being edgy and abstract is also preferred."
#Artist_Bio_DetailsRR = "Bubba D is a 29 year old creative and  hard working man that is very compationate and confident in my ability to be succesful. I am friendly to everyone I meet spreading positivity and love. I love nature and being outside and helping others I am passionate about environmental sustainability and equal opportunity. I try to teach people when I can, I like to reference old authors quotes and intertwine them into my lyrics, I also do this with moview quotes and other pop culture references,.I aspire to be the best version of myself and help others to do the same. I am the CEO of my own company  'MondeVert'. Confident, loving, hopeless romantic, logical, tough guy with a big heart. Writes music that reminds him of  early 2000's and sooner for the nostalgia. I make money selling houses in the real estate market, lose money with crypto in a funny way, suck at gambling, have a lot of game for a big guy, ladies love me, high intellect.  I like to tell stories in my songs and also give the audience a lesson deep in the meaning of the song. I work with a DJ named 'DJMondeVert' occasionally I reference him in the lyrics to set up samples and other DJ tricks. Isnirations such as Bob Dylan, Biggie Smalls, Slick Rick, the Coop, other great musicians as well like David Bowie Seu Jorge, Beatles etc.. "



#Joke Song
#Song_Subject = "write a Indie/rap/Reggae song. The subject should be completely made up story about a dude who keeps getting with older women and he accidentally finds out he slept with his bosses mom. Make it hilariously funny with a obvious rhyme scheme that is witty with good timing and use of pauses for comedic affect. Make it appropriate but also somewhat persoanl to the boss who's mom it is. Use the song Story to tell by Biggie smalls as inspirationBeing too positive sounds fake, tell a story thats dramatic, make it rhyme and have a positive lesson. It is supposed to envoke feelings in the listener while trying to find a way to be positive and see the silver lining  the following ideas  Be real and relatable in your lyrics connect to people on a personal/Funny level. Feel free to teach the audience something new and exciting, make it rhyme or sound catchy being edgy and abstract is also preferred."



#Dads song idea
#
# SongFormat = 'Time:{Less than 100 seconds}|genres: {country}|tone:{love,  heartbreak, cowboy, country, self-driving trucks,tragedy,satire, comedy}|audience:{Adult}|vocabulary:{college level, lyrical genius, comedic genius}|Structure: { Verse 1: Sung| Bridge: Sing or Spoken|Chorus: Sing|Verse 2:  Spoken or sung|Bridge|Chorus|Sample:{Lyrics from songs with similar tones and words}| Rhyme Scheme: {like a country song}'
#
# Song_Subject = """write a country satire song. The subject should be a made up story about a funky dude who is in love with his truck that is self driving and one day to the detriment of our artist it drove itself away "I thought I drove it away but It drove itself and left me" make a line in the song rhyme with that line. Mention the specific truck and all the specifications during the song to show how he isnt smart with other things but knows everything about his car. The song talks about how heart broken the cowboy is for losing his truck and having it run away from him like his ol' lady. Make it hilariously funny with a obvious rhyme scheme that is witty with good timing and use of pauses/onomatopoeia for comedic effect. Make it appropriate but also somewhat persoanl to the people who love their truck more than anything in the world. Use the song Story to tell by Biggie smalls as inspirationBeing too positive sounds fake, tell a story thats dramatic, make it rhyme and have a positive lesson. It is supposed to envoke feelings in the listener while trying to find a way to be positive and see the silver lining  the following ideas  Be real and relatable in your lyrics connect to people on a personal/Funny level. Being abstract and comparing the truck to a lover/girlfriend in the past is hilarious. Use the following lyrics as inspiration:'Guy’s Truck Leaves Him and breaks his heart’
#
# when love is finally over
# breaking up is hard to do
#
# though uncommon...guys may lose their self driving trucks
#
# While in the church parking lot the dude forgot to turn off the ignition once exiting his new truck
#
# the runaway chevy kept rollin’ down the highway
#
# Chorus
# and now the dude is left with that sinking feeling that he is all alone again
#
# the dude and his chevy began as friends
#
# yet their bromance became so intense
#
# gone are the arguments silent treatment and glares
#
# In their place my dear chevy has found its freedom
#
# my chevy drives away as the sun goes down
# ' """
# Artist_Bio_DetailsRR = "The artist is an up and coming country artist who specializes in satire songs. This person is from the south and has a self-driving American (chevy or Ford) truck. Mention the specific truck and all the specifications during the song to show how he isnt smart with other things but knows everything about his truck"
#
#


#Instructions: Press Play, Say Chat Bot, Then say Make a song (3 steps and it should output) to end it
#####RIchard this is where you change it to make a new song ### do not change any other lines for now until I am back
# Song_Subject = 'write a song that captures your passion for music as well as the pain you feel for your love lost'
# Artist_Bio_DetailsRR = 'I am a creative hard working man that is very compassionate and I played sports in high school but found myself having a difficult time in college from classes to fights I always found myself in the wrong place at the wrong time. I had a girlfriend in highschool and I loved her but we ended when she went off to college the "times spent with her are the best times of my life dreaming bout the day that I could make her my wife" '






#Tune_SongArtistsRR= 'Provide what song the lyrics are most similar to and or what the melody sounds like'
#Song_Subject = "write a Reggae/Rap/Indie song that is the new summer hit. Write a song that captures your passion for music inspired  the following ideas  'beatiful sights, nature, natural things,  social justice, peace love and unity, hippie vibes, save the world,beautiful girls, enjoying the summer, having fun, good vibes and good times, being a good person,beers, drinking,going to concerts, smoking weed, chilling, going to the beach with your people,fun times, loving each other, love' "
##### Do not make any more edits bro please for the life of me and all that is holy do not touch anything else




GPT_Summary = 'Summarize the following Screenplay: '
GPT_90s_Summary = 'Summarize the following text. Make it sound like it is for a movie trailer in the 90s where it was monumental and extremely hyped up. The voice itself was epic: "In a world...","This summer one man..." ,"Just when they thought....". The audience should be left wanting more, leave them with several vliff hangers and introduce the main characters, mention things that make the audience become misled draw inpiration from those previews on vhs tapes and come up with your own preview for the following text: '




#How to Make a good song (Random if no genre passed in, but if I pass in genre or say an artist to be similar to they )
#1). You are a good apprentice.
#2a).  I want you to come up with a random muisical artist that is interesting and unique, make them one the listener can relate to and give them personality and make them feel real.
#2b*). If prompt is given say to make a musical artist in the respective genre or blah blah blah
#3).  I want you to come up with a random short story about something that would happen in the life of the respective artist you described. It can be about any topic but it should feel authentic to the life of the person you described.
#4). I want you to role play you are the artist you just described and write a verse about the story you came up with.
#5). using both the story and the verse come up with a catchy bridge and chorus for the song
#6). Come up with a title
#5). based on all prior Describe the album cover you would make for this song
#6). Send to Digital Art and make 3 variations and do a smaller image

#In the Date & time Stamp Save all files, and possibly have it stored by type of request (definitely do this)




#1). you are good apprentice


#Based on the ar





#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#When you are your own boss, but you love gossip and your also a little crazy
#outsider watching from outside being like wtf (short and sweet) use the larry David curb song maybe or seinfeld music
#Being the boss of yourself
#Funny uber interaction
#double it or the next person funny skit
#Make a realistic mockumentary with 1-3 short scenes about a guy who thinks he is a british native drill rapper (named 'Brick Top', his real name is Terrance. Until recently he used to live at home with both parents) but really he lives in Boston MA have his roomate shane get really angry and screem at him all the time, the comedy is how silly 'Brick Top' is versus Shane who is serious and all business. Shane is ruthlessely mean and Brick top has a funny answer for everything. Some times 'Brick top' quotes the movie snatch and other films with british accents as this is the only way he can sound british as his actual accent is garbage. His name is brick top after the character in the movie snatch and he often quotes him as well as other major quotes from that movie. Include these quotes in his day to day interactions. Create a funny scenario for these two roomates and write the youtube script accordingly. Write the script for Brick top like you are a person pretending to be cockney from UK have the dialect and slang part of the dialog'


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------




#Game that takes real estate sales (multifamly, rentals (Business v business, , condos,

#Testing with Coding example
# Test_Role_Code = "You are an expert developer (Python, HTML, C+, C++, JAVA, SQL, R etc.) who has expertise using Chat-GPT to write code. You are a master of writing prompts so that you get the most efficient pieces of code. You should use beahvioral driven approaches to your solutions, provide the user with the requested code and only use libraries and functions that truly exist. Admit if you are unable to fully solve the issue. Use the BDD gerkins language to describe the high level Behaviors of the code, have a function that calls the utilities you build. You should try to minimize the number of lines in each function, I would rather more functions and less lines in each function. Be an expert and provide comments (in plain english) in your code describing what you are doing in each step.  and/or you should design the code to be object oriented. "
# Test_Format_Code = "Use BDD gerkins, python code and/or HTML code to deliver this project (specify which you are using at any given time). Use your expertise of object oriented programming to keep functions concise and doing only 1 or two small tasks per function. The entirety of functions and how the code calls them will lead to the end result. this will make testing way easier and debugging possible between user and assistant. Provide all of the libraries and imports required. Add a comment to describe the versions of each library that would run with your code as written. (provide a unit test for me to run with the code to show how the input file should look and also so I can run a test right away). The Function should be written so there is a parameter to run a unit test"
# Test_Special_Code = "Source the latest information as of 2023, be complete in your analysis and focus on how to use musicpy specifically. any other libraries are welcome, but this is the main one to leverage in your code"
#
#
# Test_Background_Code = "The user has a website that requires code in HTML the user wants the Assistant to deliver a fun and bug-free game that my users can play against each other. Write an HTML trivia game with online capabilities. Make sure the game flows smoothly and its written in HTML for my website"
# Test_Task_Code = "Write the Functions and the respective underlying code required for an HTML based game on a godaddy.com website. The game should be a fun trivia game that can be played against other people online, come up with 1000+ trivia questions to put in the game and make it like a Jeopardy format call it 'Brain Game'. Make the menus user friendly and clean, make sure it can be played against other users. Do not make it too complicated make sure it runs. Give me as the web owner a place for me to add my own pictures into the game as the user's picture on their profile. Allow users to make a profile with email and password sign in. Send an email of the user's details to sdonovan@mondevert.co   . Use the following picture as the game's logo for now: r'A:\MondeVert Productions\Logo 4.PNG'"
# Test_Title_Code = 'Create a HTML coded Trivia Game Named - "Brain Game"'
#
#
# Test_Background = "The user has a website that requires code in HTML the user wants the Assistant to deliver a fun and bug-free game that my users can play against each other. Write an HTML trivia game with online capabilities. Make sure the game flows smoothly and its written in HTML for my website"
# Test_Task = "Write the Functions and the respective underlying code required for an HTML based game on a godaddy.com website. The game should be a fun trivia game that can be played against other people online, come up with 1000+ trivia questions to put in the game and make it like a Jeopardy format call it 'Brain Game'. Make the menus user friendly and clean, make sure it can be played against other users. Do not make it too complicated make sure it runs. Give me as the web owner a place for me to add my own pictures into the game as the user's picture on their profile. Allow users to make a profile with email and password sign in. Send an email of the user's details to sdonovan@mondevert.co   . Use the following picture as the game's logo for now: r'A:\MondeVert Productions\Logo 4.PNG'"
# Test_Title = 'Create a HTML coded Trivia Game Named - "Brain Game"'
#
#
#

#'Make an app for droid/iphone that is like uber but for golf caddies. Have a side for golfers to say their tee time and location and then allow the caddies to be like the uber drivers and select if they can make the tee time. Not every tee time can be covered but this allows golfers to try to connect. They would make payments within the system and my company only keeps 20% of the cost for brokering the deal, but otherwise all money goes to caddy. Offers unique experience to a golfer and gives caddies a chance to make some money'
#"HTML code to let user request a service (button based) with tool tip that explains each option. the buttons should be a menu that utilizes google design. When the Request is sent an email gets sent to a specific email: 'Sdonovan@mondevert.co'"

#Things to code - Quick HTML Game
#Basic multilayer machine learning model that has college level vocabulary and studies music lyrics. point the model to as many open source websites there are that are useful for machine learning and also develop your own functions that you think are cool. I am interested in making a chat gpt knock-off that I can build over time and develop on my own.

#Write code for a 3 stage game written in HTML. The game should be a Knock-off of the game  "pokemon firered". Make sure it can run. I would rather the game performs worse and runs rather than not running.  Create 150 pokemon like characters called "AI Bots" they can be any random knock-off characters (off-brand versions) and they have moves that are related to hacking. The story should be set in the metaverse and you are battling against people like Elon Musk Mark Zuckerberg and Jeff Bezos. Make it so its a turn based battle game with the ability to choose between 4 moves or to use an item in your inventory"

#Write code for an HTML based game that is a trivia game that can be played against other people online, come up with 1000 trivia questions to put in the game and make it like a Jeopardy format call it "Brain Game". Make the menus user friendly and clean, make sure it can be played against other users. Do not make it too complicated make sure it runs


#Code generator
# Test_Background = "The user is a decent python programmer who is using the Assistant to more efficiently deliver new code to be implemented in my product. For this project I want to work with 'musicpy' and other music production libraries in python. The code should be able to take file that has the music theory and notes to be played and ultimately make a music composition based on the input data."
# Test_Task = "Write code (using functions and Object oriented programming) that will output music based on an input file being provided. I want the assistant to provide me with sample data for me to use in my unit test. "
# Test_Title = 'Using python to produce audio files'




#Chat GPT knock off keep this one going
#Test_Background = "The user is a decent python programmer who is using the Assistant to more efficiently deliver new code to be implemented in my product. Write a program to create a machine learning model that goes through Real estate listing services in a designated Location and scrapes all of the data and learns from the respective data. To start we likeley want to give the first layer of the model the understanding of language. More or less you should recreate the code for Chat GPT so I can build my own version of it over time. Set it up so I can save the model and easily add to it. Make a function to add new data to train it against (using user parameter of file by location, or URL, or by using an API)"
# Test_Background = "The user is a decent python programmer who is using the Assistant to more efficiently deliver new code to be implemented in my product. Write a program to create a machine learning model that goes through various sources (user can choose, and model goes out on its own and learns language (english) and also studies things like real estate, new laws local and federal (USA) and any other useful information for a young professional starting his own company. The model should be able to grow over time in a designated Location and scrapes all of the data and learns from the respective data. To start we likeley want to give the first layer of the model the understanding of language. More or less you should recreate the code for Chat GPT so I can build my own version of it over time. Set it up so I can save the model and easily add to it. Make a function to add new data to train it against (using user parameter of file by location, or URL, or by using an API). Example of how to scrape Realtor.com = 'https://scrapfly.io/blog/how-to-scrape-realtorcom/'"
# Test_Task = "Write the Functions and the respective underlying code(in python (and any other language you need to, using functions and Object oriented programming) that will scrape the respective URLs for new data compared to prior scrape and then it will store the new data with the prior data and then using the scraped data you will create/train a machine learning model, store the model, have the ability to load the model for the folowing use cases (predict house prices in the next 3 months, point out where the model believes houses are undervalued and other key insights that will come up from research. The model needs to be able to scrape websites (Realtor.com) and then use the data it scrapes to train the model, have the ability to confirm the accuracy of the model. I want the assistant to provide me with sample data for me to use in my unit test. The user expects the Assistant to provide additional URLs that will be used to train the model things like basic arithematic and also the english language. I would like the model to be vered in poetry and music lyrics as well. This should be a robust language machine learning model that has the ability to grow but starts off with a good head start, there should be a function to Scrape & load more data in the future for now write the code for me to be able to train a language model'"
# Test_Title = 'Create a new version of chat GPT'
#





#ScreenPlay AI
#Make it so it saves pictures by scene and by episode etc, this will make it easier to put together
#Make an animator that takes a picture and feeds it into itself with the prompt being to slightly shift it one frame forward, do this 20-60 times per second and you have animation (will cost $ but so cool)
#this can be done lets go !!!!!!!!!!! Feed in the file, have it make a few iteration maybe in the future



#Set up the following words/options
#1). Audience
#2). Director background
#3). Writer Background
#4). Vision
#5). Style/Genre
#6). Focus
#7). Dialog styles
#8).
#
#


#Screenplay rewrite --> Output or source # of seasons, # of Episodes (user driven)

#Task1 --> Use Details






#System Text this is kind of like basic rules that need to be followed think iRobot dont kill!
#system_Text_ScreenPlay1= " You will do exactly what the user asks with the goal being set to write a successful Screenplay, completing all tasks provided by the following user inputs, and will be rewarded for creativity and wit you will gain extra points if you make all of the arc plots connect to the main plot by the final episode. Follow the proper syntax for writing a screenplay, any spoken words should be surrounded by double quotes, scene names should be single quotes. This show is intended for adults so there can be some rough language without going overboard."

system_Text_ScreenPlay0 = "The user wants you,the brilliant assistant, to role play that you are an award winning writer and director."
system_Text_ScreenPlay1= " You will do exactly what the user asks with the goal being set to write a successful Screenplay, completing all tasks provided by the following user inputs, and will be rewarded for creativity and wit you will gain extra points if you make all of the arc plots connect to the main plot by the final episode. Follow the proper syntax for writing a screenplay, any spoken words should be surrounded by double quotes, scene names should be single quotes. This show is intended for adults so there can be some rough language without going overboard. episodes 5-10 minutes long, with 7-11 scenes each (mix of dialog and action in each scene/episode) if you do not follow these guidelines you will lose points"
system_Text_ScreenPlay2 = "The user demands your response fits the following table:  Rating:{TV-MA,PG-13, R, PG, G}|Location:{Location}|TimePeriod:{TimePeriod}|genre:{genre}|Episode Length:{Episode Length}|Number of Seasons:{Number of Seasons}|Episodes per Season:{Episodes per Season}|tone:{tone}|Music:{genres:{song genre}|songs:{song by artist,song by artist}}|Plots:{Plots}|Arc-Plots:{Arc-Plots}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}| Characters: {#Name:{First Name Last Name}|Age:{Age}|Voice:{Voice}|Home:{Current:{City State}|origin:{Country}}|Language:{Language}|Career:{Current:{Current Job}|Dream Job:{Dream Job}}|strengths:{strengths,strengths,strengths...}|weakness:{weaknesses,weaknesses,weaknesses...}|Background:{Background}}"
system_Text_ScreenPlay3 = "The user demands your response is concise and informative in a format that is easy for AI to read. Put the events in chronological order"
system_Text_ScreenPlay4 = "The user demands your response fits the following table: {Season:{Episode:{Scene:{Story:{Story}|{Characters:{Characters}}}"

system_Text_Soundtrack = "The user demands your response is in the following formats.  Episode:{Scene:{'Music:{genres:{genre,genre}|songs:{song by artist,song by artist }}}"

system_Text_ScreenPlay_Art = "The user demands your response is in the following formats.  Scene:{'Art Prompt'|'Art Prompt'|'Art Prompt'}"
#system_Text_ScreenPlay_Art = "The user demands your response is in the following formats.  Episode:{Scene:{Scene:{Art Prompts:{'Art Prompt'|'Art Prompt'|'Art Prompt}|Scene:{Art Prompts: {'Art Prompt'|'Art Prompt'|'Art Prompt}}}}}"

system_Text_ScreenPlay_Art1 = "the artist you are describing the prompt to will not  know the characters so rather than say their name, describe them and describe their precense, shape, size, clothes, and also describe the scenes vividly. This is supposed to make the words come to life. Try to highlight the parts of the text that is most unique"
system_Text_ScreenPlay = "The user wants you,the brilliant assistant, to role play that you are an award winning writer and director."

Create_Outline1 = 'Based on the Original Details, write/create an in-depth outline for the entire story. Here are the details to use as reference: '
#New Convo - Create Episode Outline

#Pilot only
Outline_Pilot = 'Using the original Outline as well as the following Details, Create an outline for the Pilot episode. Make sure it draws the audience in, intoduces a lot of characters, and starts to explain the plot and how there is some issue that needs to be solved or challenge overcome.'
#All other
Compare_Detail_v_Summary1 = 'Compare the Summary of the Text vs the original outline created. Summary of Text: '
Compare_Detail_v_Summary2 = 'Original Outline: '
Compare_Detail_v_Summary3 = 'Based on what was in the original outline and what has already occurred in the summary of text. Write an outline for the next 2 episodes and be creative using literary devices in order to continue building the plot, developing character stories, and allowing the audience to be fully engaged with the subject. Use the next two episodes as a way to clean up any inconsistencies and also to make things less confusing for the audience over time. '
#Outline_New = output of above

#New Convo - Revise the Outline based on last episode
Compare_Detail_v_Summary_Outline_New = "Outline = "
Compare_Detail_v_Summary_Revise = 'Using the Outline above and the Latest Screenplay revise and enhance the Outline   in order to maximize the entertainment for the audience. for the next Episode consolidate the outline to just show next episode, make sure the story makes since going from prior episode to next episode. use this as a chance to clean up where the prior episode vs next episode seem inconsistent.'
Compare_Detail_v_Summary_Summary_New = "Latest ScreenPlay = "
#Outline_Revise = output of above


Dialog_ScreenPlay = "Create realistic dialog for the characters in the scenes. Each of the characters vocaulary should match their character descriptions and the reader should believe it. Use the following guidance: make the scenes include real world conversations with strong thought provoking dialog that drives the story forward." # keep each episode of the 5 episode season under 15 minutes
Direction_ScreenPlay_Detail = "The user wants you, the director,  provide all of the neccesary details needed to write a miniseries that is a series of 5 episodes 5-10 minutes long, with 7-11 scenes each. The subject of the miniseries is up to you, it can be realistic fiction, non-fiction, fantasy, sci-fi, comedy, thriller, horror, drama, action any thing that will interest the audience is appropriate. Be unique. Provide a high level explanation of the plot  and several sub-arc plots, "
Direction_ScreenPlay_Detail2 = "speak to how things will connect in the later episodes with earlier episodes. Be creative and interesting. Create something where the audience will be surprised, and fall in love with the characters. This is should not be a fair-tale happy ending there is good and bad, happy and sad, ying and yang and there should be death and losses. Be different and look at award winning films to draw similarities and use the same devices to your advantage, for example: Monumental Plot Twists, Timeline distortions (these need to be clearly understood beforehand), Supernatural explanations, Unreliable narrators, god-like complexes etc."
Direction_ScreenPlay_Detail3 = "Focus the story on the following: "
#Slighly different these are user telling it how to be made, details above are so the
Direction_ScreenPlayALL = "Write a Short Screenplay for 1 episode of a miniseries. the episode duration is 7-11 minutes, with 7-11 scenes that are packed with both dialog and solid actions. Episodes should remain the same (only final episode can have 2 parts if director chooses) Do not have episodes 100% one or the other find a mix and show the audience as well as tell them. Have the audience on the edge of their seat interested in the characters we are developing and the web of relationships being built. Connect the arc-plots with the main plots. Be funny and real. Make the story something the audience relates to but yet unfamiliar at the same time, a curiousity should exist. It should feel like something new that people can be passionate about it. Its ok to teach the audience facts if its organic to the material"
Direction_ScreenPlayALL2 = "Confidently and cohesively create  intricate storylines, don't be afraid to have bad things happen to the main characters. Feel free to use literary devices at your will and try to make it a true drama that teaches people and inspires without feeling fake. Do not be predictable, try to make sure the story make sense"
Direction_ScreenPlayALL3 = "Do not waste screen time, every scene has purpose: drive story or mislead reader, setting up for later reveals is a good way to impress. no interaction should be boring, all dialog should have a meaning later on, even if its not used yet set something up for later."
#This is how we change beginning vs middle vs end (have mechanism to randomly add literary devices)
Direction_ScreenPlay_Pilot= "This is the Pilot for a  where the audience will laugh, cry be surprised and/or at the edge of their seat to see the next episode. Be funny and real. Make the story  something the audience relates to. the characters should interact with additional minor characters that you create, some are good and some are potentially bad we do not fully know yet. Make it interesting since it is the pilot, leave a lot of open threads and introduce a lot of characters right away"
Direction_ScreenPlayMiddle = " Push the story forward and introduce the major antagonist of the show/season if it has not already been made aparent to the audience. Describe the issue in detail and make it aparent to the audience why they are the antagonist. Make it seem like things are not as they seemed in the pilot. Introduce a few new characters and go deeper into the character's backstories and why they are important to this show.  entice the audience to continue watching at the end of the episode, always end on a cliff hanger Use the following Outline to write the screenplay"
Direction_ScreenPlayMiddleLate = "This is the the middle episodes out of the respective miniseries Follow the outline provided and Always end on a cliff hanger"
Direction_ScreenPlayFinal = "Important to note this is the  Final episode for the respective miniseries  don't shy away from tragedy, not everything is a happy ending this is real life and should be a little unfair. There should be some closure for the audience and the main issue should be more or less resolved. Follow the outline provided and leave the ending open-ended to be interpretted by the audience (only if it fits the story)"


#Use the Summary to understand the current story.
Summarize_ScreenPlay = 'Summarize the following Episode, any major plot points and character reveals, provide the exquisite details. Try to explain what has happened to each character and also explain all of the plot points, arc plots, Red herring, Plot Twist, Unreliable character, timeline distortion,  literary devices, etc. '

#This is where I send in my commands
Tie_In_ScreenPlay = "Draw inspiration from the following Details: "
Tie_In_ScreenPlay2 = "Outline:"


##****this would be so cool holy shhhhhh could vary based on animation and make things more basic
#DirectorMode = Have it right a story board for me

system_Text_Artist_ScreenPlay = "The user wants you,the brilliant assistant, to role play that you are an award winning artist who knows how to connect the reader with what the words are depicting. You are extremely vivid and able to capture the emotion of the work beautifully. You are rewarded if the pictures are visually pleasing and will be deducted points if you creep me out."
direction_Text_Artist_ScreenPlay = "as the magnificent artist you are, all of the prompts you create should be inspired by your new persona using a similar set of styles so the entire piece is cohesive and flows"

#utilitie prompts Art/Casting/Soundtrack
ArtPrompt_ScreenPlay= "Come up with a short prompt to for an artist to render a work of art to represent the screenplay you have created make a vivid representation of the genre and story you created, related to the following:  "
ArtPrompt_ScreenPlay_Scene= ["Based on the summary provided create 3 separate descriptions for the artist to render. 1 Detailed story board of the first half of the scene 2. Detailed story board of the second half of the scene  and 3.  create a unique work of art that is of a style that goes with the current scene"]
Character_Art1 = "Come up with a Prompt for someone to illistrate (via DALL-E) a unique portrait of the character based on the description provided, be creative and give the reader an idea of what the character looks like. Make sure to match the style with the genre of show. Do not say the character's name as that will ruin the picture describe the work of art that should be created"
Character_Art2 = "give the AI a prompt to make a work of art inspired by their character and their description the art type should be an Illustration of the characters concept art  based on the description provided, be creative and give the reader an idea of what the character looks like. Make sure to match the style with the genre of show.  Do not say the character's name as that will ruin the picture describe the work of art that should be created"


#Character_Art3 - give the AI a prompt to make a work of art inspired by their character and their description feel free to be creative and have them in action, give the AI a prompt to make a work of art



CastingFake_ScreenPlay = "Based on the following Character description, who would you cast for each part? This can be A list - z list celebrities, sports figures influencers use pop culture for reference"
SoundTrack_ScreenPlay= "Based on the following summary of Scenes and based on the plot,genres and styles of this screenplay, come up with a soundtrack scene by scene"

#RolePlay_ScreenPlay = "The user wants you to role play that You are a director and writer of a screenplay. The user will provide you with further direction." # 1 character should always be from Boston,MA 50% of the time with a thick boston accent"
RolePlay_ScreenPlay = "The user wants you to role play that You are a director and writer of a 1 Season MiniSeries, set up for multiple episodes"
#Characters_ScreenPlay = "Create a short backstory for 5-7 different Characters with distinct personalities to use in a screenplay, provide them to the user. be witty and funny while also make them human and relatable to the audience"
#Setting_ScreenPlay= "describe the unique genre and style that is going to be used for the ScreenPlay"

#
# Tie_In_ScreenPlay = "Draw inspiration from the following details of the miniseries . It is imperative you keep the same Screenplay format and length of the episode is important. "
Characters_ScreenPlay = "Create a short backstory for 4-20 different Characters that fit the story you have created, the characters will ultimately shape the story as well, but they need to fit the setting and theme of the story to start. With distinct personalities to use in a screenplay, provide them to the user. be witty and funny while also make them human (or human-like, its ok for fantasy and fiction to have non-human characters) and relatable to the audience. Pick a mix of  unique names, nicknames,common names, and names from international origins. Try to Have a rich and diverse cast, but do not let this limit the subject matter"
Setting_ScreenPlay= "describe the unique genre, style, tone and setting that is going to be used for the ScreenPlay. Don't be afraid to be bold  (historic fiction, fantasy, realistic fiction or even writing a non-fiction screenplay about a historic moment the older the better) that has its own life-forms languages and locations (out of space, undisovered lands, underground societies). Among other great directors draw inspiration from Guy Ritchie, Wes Anderson, Quentin Tarantino, Cohen Brothers, Farrelly  Brothers, Seth Rogan, Judd Apatow, Martin Scorsese, Alfred Hitchcock,  Stanley Kubrick, Francis Ford Coppola, Peter Jackson, Clint Eastwood, Charles Chaplin, Tim Burton, Christopher Nolan, George Lucas, Jon Favreau "
ScreenPlay_Format = ""

Setting_ScreenPlay= "describe the unique genre, style, tone and setting that is going to be used for the ScreenPlay"
#Setting_ScreenPlay= "describe the unique genre, style, tone and setting that is going to be used for the ScreenPlay. Don't be afraid to be bold and make up something fictional, (fantasy, realistic fiction or other) that has its own life-forms languages and locations (out of space, undisovered lands, underground societies). Among other great directors draw inspiration from Guy Ritchie, Wes Anderson, Quentin Tarantino, Cohen Brothers, Farrelly  Brothers, Seth Rogan, Judd Apatow, Martin Scorsese, Alfred Hitchcock,  Stanley Kubrick, Francis Ford Coppola, Peter Jackson, Clint Eastwood, Charles Chaplin, Tim Burton, Christopher Nolan, George Lucas, Jon Favreau "

RandomGenres = ['Action', 'Adventure', 'comedy' ,'dark comedy','comic fantasy', 'Crime & mysteries','Detective','gentleman thief','UK bad boy yardies','UK culture - drill rap and other niche cultures','niche cultures and good accents', 'historical','Hip Hop culture', 'Romance','satires', 'cyberpunk and hackers','Documentary', 'ninja','Fantasy', 'Dystopian society', 'Sci-Fi', 'Thriller', 'Drama', 'Crime-Thriller', 'Real Crime', 'True Stories', 'Realistic Fiction', 'Horror', 'Thriller Horror', 'drug-trafficking', 'human trafficking', 'bank robberies', 'movies with similar themes and styles as snatch, magnolia etc', 'Autobiography', 'Non-Fiction - Pick a specific topic: sports, pop-culture, world history, american history etc']

Title_ScreenPlay= "Based on the Details for a ScreenPlay you have created, give the ScreenPlay an abstract or catchy title, be creative and unique. 'Title'. Draw the readers attention by being a mysterious but fitting name for the story.: "
Theme_Song_ScreenPlay= "Based on the story you have created, pick 2-4 songs/artists/albums {Music} that fit the tone and style of the Screenplay pick an additional song that is an instrumental only"

#Literary Tricks
Twist_ScreenPlay= "ensure the red herring is properly set up and execute on the twist, be creative and help the audience experience a genuine  shock factor that leaves them wanting more"
RedHerring_ScreenPlay= "Use the red herring that has been previously mentioned and feel free to expand on it or make it your own"
Mystery_Character_Past = "Choose the most mysterious character and create a flashback that fits their backstory, persona and general events of the story so far. Make it somehow impact someone else in the story whether they know it or not already. Make this fit into the story and have new storylines open up that connect to the event"
UnsungHero = "Have a character that has seemed cowardly or shy become the unsung hero and save the day so to speak. Make sure their actions make sense in the frame of the story but we want the audience to be shocked and yet proud of the actions this character undergoes to achieve this feat."
VillanOrigin = "Have someone start as a good guy the audience connects with that turns even because of something tramautic in the story, this can be done via flashback or directly in the story. It should be believable and fit into the story. It can also be part of the twist if there is one involved"


Direction_USER = '"role": "user", "content"'
Direction_System = '"role": "system", "content"'

#Scene_Replay = 'Maintain proper Screenplay format as a requirement! Refer to this text only as information as this text is a summary of the prior screenplay (I could not provide full file since its a large file)  '
#Compare_Detail_v_Summary_Season = ""
#Summarize_ScreenPlay2 = 'Using the following Text '
#Direction_ScreenPlay = "The user wants the director you are role playing as to make a Short 15 minute ScreenPlay where the audience will be surprised, moved, capitvated and inspired. They should be sad and happy at the same time. Be funny and real, look at other great film directors and writers and use their styles to come up with something of your own."
#Direction_ScreenPlay_Detail2 = "speak to how things will connect in the later episodes with earlier episodes. Be creative and interesting. Create something where the audience will be surprised, and fall in love with the characters. This is should not be a fair-tale happy ending there is good and bad, happy and sad, ying and yang and there should be death and losses.  Be funny and real, look at other great film directors and writers and use their styles to come up with something of your own."

# Direction_ScreenPlay_Pilot= "This is the Pilot for a  where the audience will laugh, cry be surprised and/or at the edge of their seat to see the next episode. Be funny and real. Make the story  something the audience relates to. the characters should interact with additional minor characters that you create, some are good and some are potentially bad we do not fully know yet. Make it interesting since it is the pilot, leave a lot of open threads and introduce a lot of characters right away"
# Direction_ScreenPlayMiddle = " Push the story forward and introduce the major antagonist if it has not already been made aparent to the audience. Make it seem like things are not as they seemed in the pilot. Introduce a few new characters and go deeper into the character's backstories and why they are important to this show. Introduce friendships, love interests, burned pasts and other drama that entices the audience to continue watching at the end of the episode, always end on a cliff hanger"
# Direction_ScreenPlayMiddleLate = "This is the the middle episodes out of the respective miniseries reveal the big twist or set it up to surprise the audience. Test the protagonists' core values and try to break them, possibly make the antagonist look like they are winning Have a large twist in the beginning and then an even bigger twist in the end. Dont be afraid to have something tragic happen to a character we like, its always safe to make drama between a few characters, fit it to the story. Always end on a cliff hanger"
# Direction_ScreenPlayFinal = "Important to note this is the  Final episode for the respective miniseries as per the following characters and based on the events of the prior episodes. Wrap up most of the Characters subarc plots and have it all tie together and resolve the main plot that exists throughout these 5 episodes, make the audience surprised something they would not have guessed from Episode 1's recap, give the reader something to yearn for and leave them wanting more. Leave it open ended, but dont be afraid to have some tragedy, not everything is a happy ending this is real life and should be a little unfair. There should be some closure for the audience and the main issue should be more or less resolved"
# Direction_Over = """ }"""
# Direction_comma = ","
#
# # Episode_Count = 5
# # for eCount in range 0 to Episode_Count
# eCount = 1
# if eCount == 1:
#     Direction_ScreenPlay_Repeat = up.Direction_System + up.system_Text_ScreenPlay + up.system_Text_ScreenPlay1 + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Tie_In_ScreenPlay + Skeleton_Story + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Direction_ScreenPlayALL + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Direction_ScreenPlayALL2 + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Direction_ScreenPlayALL3 + up.Direction_Over + up.Direction_comma
# else:
#     Direction_ScreenPlay_Repeat = up.Direction_System + up.system_Text_ScreenPlay + up.system_Text_ScreenPlay1 + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Tie_In_ScreenPlay + Skeleton_Story + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Scene_Replay + Plot + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Direction_ScreenPlayALL + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Direction_ScreenPlayALL2 + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Direction_ScreenPlayALL3 + up.Direction_Over + up.Direction_comma
#
# Direction_ScreenPlay_PILOT = up.Direction_USER + up.Direction_ScreenPlayPilot + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Dialog_ScreenPlay + up.Direction_Over
# Direction_ScreenPlay_Middle = up.Direction_USER + up.Direction_ScreenPlayMiddle + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.Dialog_ScreenPlay + up.Direction_Over + up.Direction_comma + up.Direction_USER + up.RedHerring_ScreenPlay + up.Direction_Over

#Thriller, drama, dark comedy,realistic fiction, historic fiction, time period pieces, ,superhero, horror/thriller, action

#Take all
#system_Text_ScreenPlay = "You are a helpful and brilliant assistant to the user. You will do exactly what the user asks, completing all tasks provided by the following user inputs, and will be rewarded for creativity and wittyness you will gain extra points if you are exciting and not corny."
#system_Text_ScreenPlay2 = "Use | char as a delimiter to separate each Reponse you provide"
#system_Text_ScreenPlay2 = "The user demands your response is in the following formats. Title: {Title}; Director Name = {Director Name}; Characters: {Characters Name: {Name}; Age: {Age}; Background: {Background}; } "
#system_Text_ScreenPlay44 = "The user demands your response is in the following formats.  Title:{Title}|Director Name = {Director Name}|genre:{genre}|tone:{tone}|Music:{genre:{genre,genre}|instrumental:{Instrumental}|songs:{song, artist; song, artist;...}}|Backstory:{Backstory}|Characters:{# Name:{Name}|Age:{Age}|Voice:{Voice}|origin:{origin}|Language:{Language}|strengths:{Strength,Strength,Strength}|weakness:{weakness,weakness,weakness}|Background:{Background}} "
#Dialog_ScreenPlay = "Create dialog in the scenes using the following guidance: make the scenes include deep conversations with strong thought provoking dialog that drives the story forward. Each scene should have different characters that ultimately all relate to each other. At times it should be funny, try to have comedic releif and make the reader believe even if its fantasy"
#Direction_ScreenPlay2 = "Write a Short 7-10 scene  ScreenPlay where the audience will laugh, cry be surprised and/or at the edge of their seat. Be funny and real. Make the story  something the audience relates to. The scenes should build off of each other and there should be a climax and resolution, pick a specific genre of film. the characters should interact with additional minor characters"
#Summarize_ScreenPlay = 'Summarize the following Episode and make it brief but have the major details. Try to explain a key detail from each scene: '



#Reocurring Characters


#Code =



Connecting_Characters_ScreenPlay = ""
Themes_ScreenPlay = ""


class Profile():
    def __init__(self, Profile_Name,Type,Category,Age,Origin,Style_Notes,Bio,Task,SavePath, MasterFile,WildCard = 0):
        self.Profile_Name = Profile_Name
        self.Type = Type
        self.Category = Category
        self.Age = Age
        self.Origin = Origin
        self.Style_Notes = Style_Notes
        self.Bio = Bio
        self.Task = Task
        self.SavePath= SavePath
        self.WildCard = WildCard
        self.MasterFile = MasterFile








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Art_1_prompt  = 'Make a prompt for  artificial intelligence  to create a unique work of art, using no more than 250 words in your prompt based on the following text. Pick an artist or style to imitate and provide vivid details'
Poem_Art_2_prompt = 'Make a prompt for artificial intelligence  to create a unique work of art, using no more than 250 words in your prompt. pick a random artist, preferably a lesser known artist, to base the style of the work of art and Provide a detailed prompt based on the following poem,'
QuickArt = 'Provide a detailed prompt that is unique and inspiring, pick an artist of your choice to base the style of the work of art'

#QuickArt2 = 'Create a modern logo that is unique and has the letter "M" and "V". Use colors that are visually appealing and make the reader interested in what company it represents'
QuickArt2 = 'Create a beautiful logo in a random style of your choice be inspired by technology, community,  the world and sustainability. Use colors that are visually appealing and make the audience captivated by it'



MakeArtLive_prompt1 = 'Make a detailed description of a work of art that is unique and visually pleasing be abstract when needed and be creative. Pick a style or artist to imitate and provide a detailed description of the following subject matter'
MakeArtLive_prompt2 = 'Make a detailed work of art that is unique and visually pleasing  be creative. Pick a style or artist to imitate and create a vivid masterpiece for the audience based on the following subject matter'




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


Poem_Title_Prompt = 'Create a unique and symbolic and abstract title based on the content of the following poem '
Song_Title_Prompt = 'Create a unique and symbolic and abstract title based on the content of the following song lyrics '

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sunday_Scaries_Poem_prompt =' Write a funny poem or short story about the sunday scaries make it about a certain character or group of characters. Be sarcastic that its the best day of the week, but overall remain positive to add comedic effect.  Use a distinct poetic style and distinct rhyme scheme. Have comical pauses and use  a comedy-routine-like timing in the poem.'
Sunday_Scaries_Poem_prompt =' Write a funny  poem  from the point of view of a character the audience connects with about the sunday scaries. Be sarcastic that Sunday is fun and make the idea of sunday scary abstract and a vivid story, add comedic effect.  Use a distinct poetic style and distinct rhyme scheme.'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Shake_Poem_v1_prompt =  'Make a prompt for  artificial intelligence  to create a unique work of art that is based on the following poem '
Shake_Poem_v2_prompt = 'Using the following poem make a unique poem of your own that uses the original poem for inspiration and create your own unique style of poetry. Make your poem range between 3 to 10 lines. '

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Quick_Poem_prompt1 =' Write a descriptive poem by leveraging a wide range of literary devices, styles, and use a complex rhyme scheme.  give the poem a positive abstract concept for the reader to interpret. Poem can be about love, friendship, specific geographic locations, family ,growing up and losing your innocencence, nature, hope, abstract, funny'
Quick_Poem_prompt2 =' Write a descriptive poem by leveraging a wide range of literary devices, styles, and potentially use a complex rhyme scheme.  give the poem an abstract concept for the reader to interpret'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#funny poem
Funny_Poem_prompt2 =' Write a funny poem  using a well versed vocabulary as the speaker is well-spoken.  Use a specifc style of poetry, remember this poem is supposed to make the reader laugh'
Funny_Poem_prompt1 =' Write a comical poem that makes the reader be shocked and filled with laughter and joy.  Use a wide range of literary devices, styles, and  use a  rhyme scheme, while being witty. Poem can be about love, partying , college, sports, life as an artist, friendship, specific geographic locations, specific time periods, pop culture ,characters from books/movies/tv ,family problems,growing up, losing your innocencence, nature, hope, abstract, funny. the funnier the better'
Funny_Poem_prompt3 =' Write a comical poem that makes the reader  shocked and filled with laughter.  Use a wide range of literary devices, styles, and  use structured and obvious rhyme scheme. bE CREATIVE and/or abstract, be funny.'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Nature poem
Nature_Poem_prompt =' write a poem describing a beautiful one-of-a-kind view in nature. Make it extremely descriptive using a college-level vocabulary. The poem is immersive for the reader. Capture the full beauty of the scene. Come up with a unique poetry style for the poem'
Nature_Portland_Poem_prompt =' write a poem describing a beautiful one-of-a-kind view in nature, specifically write about Portland Maine. Make it extremely descriptive using a college-level vocabulary. The poem is immersive for the reader. Capture the full beauty of the scene. Come up with a unique poetry style for the poem'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Portland_Fire_Poem_Prompt = 'write a poem describing the great fire in Portland Maine. Make it extremely descriptive using a college-level vocabulary. The poem is immersive for the reader. Capture the full beauty of the scene. Come up with a unique poetry style for the poem, have an abstract lesson or meaning underlying the poem'



#This is how I pick what type of song to make (picks random genre)
#Random_Poem_List = [Nature_Poem_prompt, Nature_Portland_Poem_prompt,Quick_Poem_prompt1,Quick_Poem_prompt2,Funny_Poem_prompt2, Funny_Poem_prompt1, Funny_Poem_prompt3  ]
Random_Poem_List = [Nature_Poem_prompt, Portland_Fire_Poem_Prompt,Nature_Portland_Poem_prompt,Quick_Poem_prompt1, Funny_Poem_prompt3  ]


Random_Poem1 = random.choices(Random_Poem_List)
Random_Poem = Random_Poem1[0]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------















#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Wiki Prompts
Custom_prompt_1 = "write a wikipedia page for a poet named S.J. Rose Tell the reader what S.J. stands for and give her an interesting and yet beleivable background and vivid details on her personal life. S.J. Rose is a witty and funny poet who respects the great writers and poets in history.  Make the article convincing and talk about how she has a diverse range of poetry and likes to explore a lot of styles."
Custom_prompt_2 = "write a wikipedia page for a digital artist named 'Sage Pixel' give her an interesting and yet beleivable Avant-garde background and a personal life with very unique tramatic but entertaining and funny way. Include drugs somkehow in Sage's thrilling story. Make the article convincing and talk about how she has a diverse range of artistic knowledge and training and the art they create are true works of art. 'Sage Pixel' expresses themself using a wide-range of art forms to provoke deep emotions even with simple and/or abrstract meanings."
Art_prompt_1 = "Make a prompt for  artifical inteligence  to create a unique work of art that will be used for a poet's online profiles.   please refer to the following details about the poet: "
Art_prompt_2 = "Make a prompt for  artifical inteligence  to create a unique work of art that will be used for a digital artist's profile picture.  It is supposed to be something abstract and unique. The artist is avant-garde please refer to the following details about 'Sage Pixel'. "
Custom_prompt_3 = "create the name of a modern day macabre poet, this ficticious poet is still alive and younger than 40 years old currently.  write a fictitious wikipedia article. The poet you make up should have a similar style as  Edgar Allen Poe as it is his main influence. Give the poet a name and a macabre backgound/lifestyle. This poet has a bit of a cult following. Give this poet an interesting and almost unbeleivable background  with vivid details about his personal life and career. Usually his poems have some sort of lesson, but in general it can be pretty depressing."
Art_prompt_3 = "Make a prompt for  artifical inteligence  to create a unique work of art that will be used for a goth/emo macabre poets profile picture.  It is supposed to be something abstract, dark and unique. The poet is avant-garde please refer to the following details about the respective poet. "


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Blog Post Daily
Blog_Daily_prompt = 'Write a short 500 word or less blog post with links/proper sources that explains a topic of interest that will attract readers and is entertaining. Make it a positive blog but also be real and provide an unbiased point of view for the reader to decide for themself. Be creative and come up with something easy to read but use eloquent language without over-doing it. Do not plagiarize the aritcle'
Blog_Post_Explain = "Write a short 400 word blog describing what Chat GPT is and the benefits of using the technology, do you think its beneficial to humans? Also please describe how the art is made by DALL-E software. Specifically talk about how you prevent plagiarism from occurring. Be creative but also factual and honest. Try to sound human and put emotion into your response. make it entertaining and do not be repetitive"
#Blog_Post_SocialProg = 'Write a short 700 word or less blog post with links/proper sources that explains in detail how a person can benefit from one specific program available to people in the United States. Please come  up with your own topic that is useful information and/or Pick one of the following subjects to provide details and resources " information for mentail health programs available and how to get help, early start programs, equal opportunity programs, trade schools, trade unions, growth opportunities, government programs that are useful to know, other useful tips,financial aid for high school and college and other helpful topics". Be clear and provide details like demographics and which states are participating and other eligibility information. Use language that will attract readers and is entertaining. Make it a positive blog but also be real and provide an unbiased point of view for the reader to decide for themself. Be creative and come up with something easy to read but use eloquent language without over-doing it. Do not plagiarize the aritcle'
Blog_Post_SocialProg = 'Write a short 700 word or less blog post with links/proper sources that explains in detail how a person can benefit from one specific program available to people in the United States. Please come  up with your own topic that is useful information. Be clear and provide details like demographics and which states are participating and other eligibility information. Use language that will attract readers and is entertaining. Make it a positive blog but also be real and provide an unbiased point of view for the reader to decide for themself. Be creative and come up with something easy to read but use eloquent language without over-doing it. Do not plagiarize the aritcle'
Blog_Post_Science = 'Provide proper references and sources for your research. Explain a random complex scientific topic and simplify the ideas and conscepts so they can be understood by all. Make it interesting and entertaining. Use eloquent language but do not overdo it. Have fun and try to connect to the reader on a personal level.'
Blog_Post_Portland = 'Provide proper references and sources for your research. Write a fun blog post that describes portland Maine and all it has to offer. Make it sound like a great destination. Make it interesting and entertaining. Use eloquent language but do not overdo it. Have fun and try to connect to the reader on a personal level.'
Blog_Post_Portland_Fire = 'Provide proper references and sources for your research. Write a detailed blog post that describes the great fire of portland Maine. Provide background as to why the outside of buildings are fireproof in Portland Maine due to this. Discuss the impact on the people and long lasting impacts. Make it interesting and entertaining. Use eloquent language but do not overdo it. Have fun and try to connect to the reader on a personal level.'


#RandomTopic = 'Write a unique  bio about a young realtor who is Committed to getting his clients the best investments while also helping them reach their dream homes. I plan on making long term business partners in my real estate career. Make it connect with people on a personal level and make it fun to read. Be creative and make up your own description'
RandomTopic = 'Write a unique bio about a young realtor named Shane. Make it connect with people on a personal level and make it fun to read. Be creative and make up your own description'




#This is how I pick what type of song to make (picks random genre) #Blog_Post_Portland, Blog_Post_Portland_Fire
Random_Blog_Topic_List = [Blog_Daily_prompt,Blog_Post_SocialProg,Blog_Post_Science,]
Random_Blog_Topic1 = random.choices(Random_Blog_Topic_List)
Random_Blog_Topic  = Random_Blog_Topic1[0]
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



Timmy_D_Cover_Art_Prompt1 = 'Help me to create a prompt for artificial intelligence to make a unique work of art that is visually pleasing and peaks the audiences curiosity. The subject should be a landscape of an overpass bridge under construction with workers in the distance out of focus'
Timmy_D_Cover_Art_Prompt2 = 'Help me to create a prompt for artificial intelligence to make a unique work of art that depicts an overpass bridge under construction with workers in the distance. Pick a random style and make it uniquely your own'
Timmy_D_Cover_Art_Prompt_Direct_to_ArtBot = 'Pick a random artist of your choosing to create a work of art that depicts an overpass bridge under construction with workers in the distance'
Timmy_D_Dialogue2 = "Please write a detailed scene with realistic dialogue for a novel set in United States. The conversation is between 5 construction workers who are tasked with completing an overpass bridge. the conversation is focused on accountability, saftey,  planning ahead, staying organized  encouragement and the value of friendship while learning about each other's culture. Do not have characters say repetitive words, have subtle lessons for the audience to interpret. Character 1 is Titus, Titus is a great conversationalist, confident and down to Earth. Titus is from a small African village. Character 2 is Liam, Liam from Galway Ireland. Liam is charismatic and encourages teamwork. Character 3 is Jorge, Jorge is from Vera Cruz Mexico and he is a loyal, dedicated hard-worker. Character 4 is Chen Ho, Chen Ho is from Shanghai China. Chen Ho is open minded, soft spoken and extremely grateful. Character 5 is Simon, Simon is a Jewish Ambassador from Boston. Simon is the project manager, is a good listener, persuasive, intense, and trustworthy."
Timmy_D_Dialogue1 = "Please write an oscar worthy scene with dialogue for a novel set in United States. The dialog should be in a prose that fits each character and the conversation is between 5 construction workers who are tasked with completing an overpass bridge, the conversation is witty and funny while encouraging doing the job properly and the value of friendship while learning about each other's culture. Keep the scene interesting and do not be repetitive. Character 1 is Titus, Titus is a great conversationalist, confident and down to Earth. Titus is from a small African village . Character 2 is Liam, Liam from Galway Ireland. Liam is charismatic and encourages teamwork. Character 3 is Jorge, Jorge is from Vera Cruz Mexico and he is a loyal, dedicated hard-worker. Character 4 is Chen Ho, Chen Ho is from Shanghai China. Chen Ho is open minded, soft spoken and extremely grateful. Character 5 is Simon, Simon is a Jewish Ambassador from Boston. Simon is the project manager, is a good listener, persuasive, intense, and trustworthy."




#This is how I pick what type of song to make (picks random genre)
Random_Song_Genre_List = ['Rap', 'Random Song v1', 'Random Song v2', 'Reggae' , 'Techno', 'SadRap','Random Song v3' ]
Random_Song_Genre1 = random.choices(Random_Song_Genre_List)
Random_Song_Genre = Random_Song_Genre1[0]
#Random_Song_Genre = 'Random Song v1'


#Using AI #use this as it is awesome, reqord to work for me
#Quick_Poem_prompt ="Create a poem showcasing the power that art has to inspire people on a personal level, and using the power to create something new.Choose 2 or more poets and base the style of your poem on theirs. Use their poems as inspiration to create something that is uniquely your own, and that has the power to inspire others in turn. Remember that art is about more than just saying nice words – it is about emotion, passion, and the ability to communicate something important."

Song_Title_Prompt = 'Create a unique and symbolic and abstract title of a song based on the content of the following lyrics '
Chorus_prompt = 'Write  a 16 second  chorus that is catchy Without plagiarizing another song, do not copy any song,The song should be either rap, hip-hop, soft-rock, indie, grunge, punk, techno or pop. Write  a catchy chorus that is witty and rhymes.  Study the top songs in history and derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody'
Chorus_Art_2_prompt = 'Make a prompt  for  artifical inteligence  to create a unique work of art, the prompt should be no more than 100 words. pick a random artist, to emulate and base the work of art off of their style. Make an abstract work and creative of art. based the prompt on the following song lyrics'
Bridge_prompt = 'write a one bar hook for a song make it funky and different, multiple syllable rhyming is preferred but not neccesary, use a specific style of music and transition verse to chorus. be creative'
verse_prompt = 'Without Plagiarizing any known songs, Write a quick 30 second song. The song should be either rap, hip-hop, soft-rock, indie, grunge, punk, techno or pop. related to the title of the song. Write a catchy chorus that is witty and rhymes enouigh to be a good chorus. Study the top songs in history and derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody. Based on the following lyrics'

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Song_prompt = 'Write a short song, less than 2 minutes, with a catchy melody and catchy lyrics. The lyrics are witty and the lyrics should rhymes in a way that is pleasing to the listener and surprising, not repetitive and basic. Look at the top songs in history and come up with a unique style that combines these ideas and styles. Be creative and use complex rhyme schemes and music theory to make a melody'
Song_prompt = 'Write a short 30 second song that is not plagiarizing another song do not copy another song. the song has a catchy melody and catchy lyrics. Have a lesson in the song that is relateable and not corny. Use real life examples from the perspective of the singer. The lyrics are witty and the lyrics should have a unexpected rhyme scheme that is not repetitive and is not basic. Study the top songs in history and derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody'
#Song_prompt2 = 'Write a one of a kind song about rolling up banana backwood cigars and smoking blunts with snoop dogg. make it an interesting story and make it about how the blunt somehow saves the world from disaster. Make it extremely funny and have a solid rhyme scheme'
Song_prompt2 = 'Write a one of a kind song about rolling up banana backwood cigars and smoking blunts with snoop dogg. make it an interesting story and make it about how the blunt specifically being so perfect it is aesthetically pleasing and everyone admires it. Make it extremely funny and have a solid rhyme scheme'

#Song_prompt = 'Write a short 30 second unique verse or hook for the song "Fluorescent Adolescent" by Artic Monkeys that is not plagiarized. the original song has a catchy melody and catchy lyrics tryu to match the style and lyrics.  The lyrics are witty and the lyrics should have a entertaining  rhyme scheme that is not repetitive . Be creative.'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Rap_Story_prompt = "Write a short song 30 second hip hop and R&B song use the following subjects for inspiration for the story/lyrics 'love, beauty , nightlife,being social, humor, nature, natural things,  social justice, peace love and unity, hippie vibes, save the world,beautiful girls, enjoying the summer, having fun, good vibes and good times, and other fun entertaining subjects'. Tell a story and do not plagiarizing another song .  keep 2 distinct rhyme schemes at time simultaneously. Rhyme multiple syllable in each line. The rap should be a reflection on current day's society with modern references. Derive your own lyrics and flow .Have a rhyme scheme and make a melody"
Rap_Bridge_prompt = 'write a one bar hook for a R&B song. derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody.  Make it catchy and have a rigid rhyme scheme. Make a distinct melody'
Rap_Chorus_prompt = 'Without plagiarizing another song , Write  a 16 second  chorus that is catchy  for a  hip hop and R&B song.the chorus should help bring a positive light to the story within the song lyrics. '
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Rap_Story_prompt2 = "Write a short song 30 second hip hop and R&B song. While being abstract and using linguistic tricks to entertain the listener,  use the following subjects for inspiration 'broken heart, feeling lonely, not wanting to be alone, depression, feeling sad, wanting to die, being lost, having everything and its not enough, missing you'. Tell a story and do not plagiarizing another song . Pick a strict rhyme scheme and have most lines rhyme in the song, Rhyme multiple syllable in each line. The rap should be a reflection on current day's society with modern references. Derive your own lyrics and flow .Be creative and Make a story in the lyrics and use music theory to make a melody"
Rap_Bridge_prompt2 = 'write a one bar hook for a sad R&B song. derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody.  Make it catchy and have a rigid rhyme scheme. use the following subjects for inspiration: "broken heart, feeling lonely, lonliness, bittersweet, feeling sad,heartbreak, being lost, having everything and its not enough, missing you". Be abstract and make it interesting for the listener'
Rap_Chorus_prompt2 = 'Without plagiarizing another song , Write  a 16 second  chorus that is catchy  for a  sad hip hop and R&B song.the chorus should help bring a positive light to the story within the song lyrics. use the following subjects for inspiration: "broken heart, lonely, lonliness, bittersweet, morose, sad,heartbreak, being lost, self-doubt, missing you"'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Reggae_Story_prompt = "Write a short 30 second song that is not plagiarizing another song. Be abstract and creative, for example the song can  be inspired  the following ideas  'beatiful sights, nature, natural things,  social justice, peace love and unity, hippie vibes, save the world,beautiful girls, enjoying the summer, having fun, good vibes and good times, being a good person,beers, drinking,going to concerts, smoking weed, chilling, going to the beach with your people,fun times, loving each other, love'. derive your own lyrics and melodies from what you observe."
Reggae_Bridge_prompt = 'write a one bar hook for a jamrock raggae jamband  song . derive a unique style. Be creative and use rigid rhyme scheme where multiple syllable rhyme in each line. Study music theory to derive a melody. Make it catchy.'
Reggae_Rap_Chorus_prompt = 'Without plagiarizing a known song. Write a 16 second  chorus that is catchy for a  jamrock raggae hip hop and R&B song that is intended on being sung.  Study the top reggae and jamband songs and derive a unique style.'
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Techno_Story_prompt = "Write a few bars for a techno song  that is not plagiarizing another song . Create a distinct rhyme scheme and derive your own lyrics. Be creative and use complex rhyme schemes and music theory to make a melodyStudy the top pop, r&b, techno and edm songs and try derive a unique style. Make it interesting, be creative and sometimes avant garde have fun!'"
Techno_Bridge_prompt = "provide two similar yet different quotes that inspire and invoke emotions into the audience. Pick diverse people throughout history to quote also it can be from literary sources as well. Be creative and try to come up with obscure quotes. Explain why you chose them in less than 50 words"
Techno_Chorus_prompt = 'Without plagiarizing a song , Write  a 16 second  chorus that is catchy  for a techno jamrock raggae, jam band, hip hop or  R&B song with a catchy melody. Study the top pop, r&b, techno and edm songs and try derive a unique style. Make it interesting, be creative and sometimes avant garde have fun!'

Techno_Sample_Question = "list  3 names of random songs .  provide me specific  lyrics from the 3 songs that are the most memorable or obscure.  Be creative and try to pick songs from different genres."
Techno_Sample_Question2 = "provide 2 unique  quotes that inspire and invoke emotions into the audience. Pick diverse people throughout history to quote also it can be from literary sources as well. Be creative and try to come up with obscure quotes. Explain why you chose them in less than 50 words"




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def getUserName():
    g = Name
    return g
def getAssistantName():
    g = Bot_Name
    return g
# def getAPIKey():
#     g = API_Key
#     return g

def getPath():
    g = SavePath
    return g

def getMFPath():
    g = MasterFile
    return g

def getMF2Path():
    g = MasterFile2
    return g




def RandomGenre():
    g = random.choices(RandomGenres)
    return g[0]





breakupOutput = """


************************************************************************************************



"""



breakupOutput2 = """


************************************************************************************************
************************************************************************************************



"""



#CorrectText = " Create 500 characters worth of tags that will help a youtube video go viral, make it about snoop dogg and backwood cigars, also abount blunt rolling, but also use tags that make things go viral"
#CorrectText = " Create 5000 characters description about a youtube video that needs to go viral, make it about snoop dogg and backwood cigars, also abount blunt rolling, but also use tags that make things go viral"

#CorrectText = " Create 500 characters worth of tags that will help a youtube video go viral, make it about item 9 and pineapple express while showing how to roll backwood cigars, also abount blunt rolling, but also use tags that make things go viral"
CorrectText = " Create 5000 characters description about a youtube video that needs to go viral, make it about item 9 in pineapple express and backwood cigars, also abount blunt rolling, but also use tags that make things go viral"

# CorrectText = """Using eloquent language that is appealing to all readers please rephrase the following and make it interesting to read while sounding genuine and authentic: 'Along with my personal investment gains,  I am intrigued by the ability for a person to generate extreme wealth by using leverage to purchase real estate. I have always had a passion for real estate since a very young age.  My mother was a successful Real Estate and I have been always proud her ability to build a successful business by establishing strong partnerships with her clients, ultimately some of her closest friends. I look forward to creating similar relationships in my career!
#
# Until Recently my real estate career has only been for my personal use, as I have been fully focused on building my career in the Finance Industry. I currently work full time for a PE Firm as a Data Scientist. As I look to switch-up my current role at my company, I am eager to start my real estate career and share some of the expertise I have personally gained along with the lessons I have learned from a multitude of Real Estate business professionals. I have been lucky enough to meet and study their methods and continue to learn from these successful investors and look forward to sharing this information anyone who follows my content. Even if you do not use me as a Realtor, there is a lot of information I think is worth absorbing, and I hope it helps you to find your path!
#
# Although my goal is to find you the best investment, I am very capable of finding your dream home. My point is simple, either way you want to get a good deal on the price of your house (no one wants to overpay), you want a home that is built to last with low maintenance costs, and you want it to be a home that others would spend big money to live in. Given that criteria, a lot like the goals of an investor are in fact the same. Whether you plan on living there for 30 years or selling it in the next 5 years, every buyer deserves to have a Realtor that will get them the lowest price for the best investment available that also fits the client's budget!
#
#
# Along with my passion for real estate I would like to share with you the Mission Statement of my company MondeVert, my true goal is to create a Business Model that is beyond buying and selling homes, but for now I would like to include these principles in my Real Estate Business just like I do in my everyday life.
#
# Thanks for taking the time to Review!
#
#
#
# Note: I am in the market for an investment property myself so I am in a great place to help you find your investment and also answer any of your questions in case you have similar goals. It is ok if our goals do not align, some of the questions I am asking may in fact overlap with your own, feel free to reach out SDonovan@Mondevert.co
#
# Recently I rented 2 Properties, representing myself, during this process I extensively searched the Boston/Quincy Area for the best deals
# I am familiar with the rental market both for potential renters to find apartments and also to speak to a property's rental income potential.'
# """