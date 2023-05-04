import pandas as pd
import random


Name = 'Shane'
Bot_Name = 'Brick Top'
SavePath = r"A:\ShakeBot Testing"
AI_Art_Path = r"A:\AI Art"
AI_Poetry_Path = r"A:\AI Poetry"
AI_Blog_Path = r"A:\AI Blogs"
AI_Music_Path = r"A:\AI Song Lyrics"
AI_Live_Art_Path = r"A:\AI Live Art Path"
AI_Screen_Plays = r"A:\MondeVert Productions\ScreenPlays"
MasterFile = r"A:\Master Tracker Files\MondeVert Master Tracker.xlsx"
MasterFile2 = r"A:\Master Tracker Files\MondeVert Master Transcript.xlsx"
MasterFile3 = r"A:\Master Tracker Files\MondeVert Master Blog Poem and Song Lyrics.xlsx"


DownloadFolder = r"C:\Users\sdono\Downloads"

REData = r'A:\RE Data\MA 2022-2023 Data'
REDATAURL = 'https://idx.mlspin.com/idx.asp?user=2K7zB9ytn1MtTtUNFeBt92N7rZtjfWdyYmLtNzYRztDhtAnutnNK1mNRHrZhtFoE5A9t4c7vZmtatNxIteOL2ftNqO0oatxUyNt&proptype='

REDATAURL2 = 'https://idx.mlspin.com/idx.asp?userId=CN229354&user=2K7zB9ytn1MtTtUNFeBt92N7rZtjfWdyYmLtNzYRztDhtAnutnNK1mNRHrZhtFoE5A9t4c7vZmtatNxIteOL2ftNqO0oatxUyNt&filetype='



REURL_ADD = '&status=SLD'
MLSURL = 'https://h3i.mlspin.com/signin.asp'
MLSURL2 = 'https://h3y.mlspin.com/MLS.Pinergy/Home/Dashboard/Home'
REType = ['SF', 'LD', 'BU', 'CC', 'CI', 'MH', 'MF', 'RN', 'OH', 'VT']



RE_File_Names = ['idx_mh_sld.txt', 'idx_OH.txt', 'idx_rn.txt', 'idx_rn_sld.txt', 'idx_sf.txt', 'idx_sf_sld.txt', 'idx_VT.txt', 'idx_bu.txt', 'idx_bu_sld.txt', 'idx_cc.txt', 'idx_cc_sld.txt', 'idx_ci.txt', 'idx_ci_sld.txt', 'idx_ld.txt', 'idx_ld_sld.txt', 'idx_mf.txt', 'idx_mf_sld.txt', 'idx_mh.txt']


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


AI_ArtistName = 'Sage Pixels'
AI_Poet_Name = 'S. J. Rose'
AI_Blogger = "Brick Pulford"
Song_Writer = 'Bubba D'

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



GPT_Summary = 'Summarize the following Screenplay: '
GPT_90s_Summary = 'Summarize the following text. Make it sound like it is for a movie trailer in the 90s where it was monumental and extremely hyped up. "In a world...","This summer one man..." ,"Just when they thought...." draw inpiration from those previews on vhs tapes and come up with a preview for the following text: '



#ScreenPlay AI

system_Text_ScreenPlay = "The user wants you,the brilliant assistant, to role play that you are an award winning writer and director."
system_Text_ScreenPlay = "The user wants you,the brilliant assistant, to role play that you are an award winning writer and director. You will do exactly what the user asks with the goal being set to write a successful Screenplay, completing all tasks provided by the following user inputs, and will be rewarded for creativity and wittyness you will gain extra points if you make all of the arc plots connect to the main plot by the final episode. Follow the proper syntax for writing a screenplay, any spoken words should be surronded by double quotes, scene names should be single quotes. This show is intended for adults so there can be some rough language without going overboard."
system_Text_ScreenPlay1= " You will do exactly what the user asks with the goal being set to write a successful Screenplay, completing all tasks provided by the following user inputs, and will be rewarded for creativity and wittyness you will gain extra points if you make all of the arc plots connect to the main plot by the final episode. Follow the proper syntax for writing a screenplay, any spoken words should be surronded by double quotes, scene names should be single quotes. This show is intended for adults so there can be some rough language without going overboard."
system_Text_ScreenPlay2 = "The user demands your response is in the following formats.  Title:{Title}|Director Name = {Director Name}|settings: {setting}|TimePeriod:TimePeriod|genre:{genre}| tone:{tone}| Plot:{Plot}|Arc-Plot:{Arc-Plot, Arc-Plot}}|Summary:{Episode:{Summary by episode,...}}Music:{Opening Songs: {Episode 1, Episode 2, ...}|genres:{genre,genre}|songs:{song by  artist,song by  artist }}|Characters:{#Name:{Full Name}|Age:{Age}|Sex:{M or F or T}|Voice:{Voice}|Home:{Current: {City,State}| origin: {City,Country}}|Language:{Language}|Career: {Current:{Current}|Dream Job: {Dream Job}}|strengths:{Strength,Strength,Strength...}|weakness:{weakness,weakness,weakness...}|Background:{Background}} "
system_Text_ScreenPlay3 = "The user demands your response is in the following formats.  Title:{Title}|Episode:{Scene:{Summary by Scene}}"
system_Text_ScreenPlay4 = "The user demands your response is in the following formats.  Episode:{Scene: {Art Prompts: {'Art Prompt', 'Art Prompt'}}}"


#RolePlay_ScreenPlay = "The user wants you to role play that You are a director and writer of a screenplay. The user will provide you with further direction." # 1 character should always be from Boston,MA 50% of the time with a thick boston accent"
RolePlay_ScreenPlay = "The user wants you to role play that You are a director and writer of a 1 Season MiniSeries, set up for multiple episodes"
#Characters_ScreenPlay = "Create a short backstory for 5-7 different Characters with distinct personalities to use in a screenplay, provide them to the user. be witty and funny while also make them human and relatable to the audience"
#Setting_ScreenPlay= "describe the unique genre and style that is going to be used for the ScreenPlay"



Tie_In_ScreenPlay = "Draw inspiration from the following Summary of miniseries details you created with the user: "
Characters_ScreenPlay = "Create a short backstory for 7-10 different Characters with distinct personalities to use in a screenplay, provide them to the user. be witty and funny while also make them human and relatable to the audience. Pick a mix of common names, unique names, and names from international origins. Have a rich and diverse cast"
Setting_ScreenPlay= "describe the unique genre, style, tone and setting that is going to be used for the ScreenPlay"
Title_ScreenPlay= "Based on the ScreenPlay you have created, give the ScreenPlay an abstract or catchy title (Do not say Last), try to set up the name being said later in the film"
Theme_Song_ScreenPlay= "Based on the story you have created, pick 2-4 songs/artists/albums {Music} that fit the tone and style of the Screenplay pick an additional song that is an instrumental only"


ArtPrompt_ScreenPlay= "Come up with a short prompt to for an artist to render a work of art to represent the screenplay you have created make a vivid representation of the genre and story you created, related to the following:  "
ArtPrompt_ScreenPlay_Scene= "Based on the summary provided create 2 story boards for each scene and also create 1 unique work of art that is of a style that goes with the current scene "


Scene_Replay = 'Use the following last scenes to make up plot points for this episode: '
Summarize_ScreenPlay = 'Summarize the following Episode and make it brief but have the major details: '
Dialog_ScreenPlay = "Create realistic dialog for the characters in the scenes. Each of the characters vocaulary should match their character descriptions and the reader should believe it. Use the following guidance: make the scenes include real world conversations with strong thought provoking dialog that drives the story forward." # keep each episode of the 5 episode season under 15 minutes
#Direction_ScreenPlay = "The user wants the director you are role playing as to make a Short 15 minute ScreenPlay where the audience will be surprised, moved, capitvated and inspired. They should be sad and happy at the same time. Be funny and real, look at other great film directors and writers and use their styles to come up with something of your own."
Direction_ScreenPlay_Detail = "The user wants you, the director,  write a high level description {Summary} of a miniseries that is a series of 5 episodes 5-10 minutes long, with 7-11 scenes. Provide a high level explanation of the plot  and several sub-arc plots, "
Direction_ScreenPlay_Detail2 = "speak to how things will connect in the later episodes with earlier episodes. Be creative and interesting. Create something where the audience will be surprised, and fall in love with the characters. This is should not be a fair-tale happy ending there is good and bad, happy and sad, ying and yang and there should be death and losses.  Be funny and real, look at other great film directors and writers and use their styles to come up with something of your own."

Direction_ScreenPlayALL = "Write a Short Screenplay for 1 episode of a miniseries, the episode duration is 7-11 minutes, with 7-11 scenes that are either packed with dialog and/or solid action. Have the audience on the edge of their seat interested in the characters we are developing and the web of relationships being built. Connect the arc-plots with the main plots. Be funny and real. Make the story something the audience relates to but yet unfamiliar at the same time, a curiousity should exist. It should feel like something new that people can be passionate about it. "
Direction_ScreenPlayALL2 = "Develop an arc story and have intricate storylines developing, don't be afraid to have bad things happen to the main characters. Feel free to use literary devices at your will and try to make it a true drama that teaches people and inspires without feeling fake"
Direction_ScreenPlayALL3 = "The scenes and episodes should build off of each other no interaction should be boring, all dialog should have a meaning later on, even if its not used yet set something up for later."


Direction_ScreenPlayPilot = "This is the Pilot for a  where the audience will laugh, cry be surprised and/or at the edge of their seat to see prior episode. Be funny and real. Make the story  something the audience relates to. the characters should interact with additional minor characters that you create, some are good and some are potentially bad we do not fully know yet. Make it interesting since it is the pilot, leave a lot of open threads and introduce a lot of characters right away"
Direction_ScreenPlayMiddle = " Push the story forward and introduce the major antagonist if it has not already been made aparent to the audience. Make it seem like things are not as they seemed in the pilot. Introduce a few new characters and go deeper into the character's backstories and why they are important to this show. Introduce friendships, love interests, burned pasts and other drama that entices the audience to continue watching at the end of the episode, always end on a cliff hanger"
Direction_ScreenPlayMiddleLate = "This is the the middle episodes out of the respective miniseries as per events of the prior episodes create a twist or new dilemna that is major for the protagonists and make the antagonist look like they are winning Have a large twist in the beginning and then an even bigger twist in the end (have something tragic happen to a character we like), make drama between a few characters. Potentially reveal there has been an unreliable narrator or some other major twist, always end on a cliff hanger"
Direction_ScreenPlayFinal = "Important to note this is the  Final episode for the respective miniseries as per the following characters and based on the events of the prior episodes. Wrap up most of the Characters subarc plots and have it all tie together and resolve the main plot that exists throughout these 5 episodes, make the audience surprised something they would not have guessed from Episode 1's recap, give the reader something to yearn for and leave them wanting more. Leave it open ended, but dont be afraid to have some tragedy, not everything is a happy ending this is real life and should be a little unfair. There should be some closure for the audience and the main issue should be more or less resolved"








#Literary Tricks
Twist_ScreenPlay= "Based on the characters you have created and the prior Episodes create an eloborate twist that was not obvious yet is believable based on prior events in the story, there should be a red herring set up do not fall into that, be creative and trick the reader into a wow factor that leaves them wanting more"
RedHerring_ScreenPlay= "Based on the characters you have created and the prior Episodes create an eloborate red Herring that seems to be where the show is going based on prior events in the story. Note a red herring is a literary device that leads readers or audiences toward a false conclusion"
Mystery_Character_Past = "Choose the most mysterious character and create a flashback that fits their backstory, persona and general events of the story so far. Make it somehow impact someone else in the story whether they know it or not already"
UnsungHero = "Have a character that has seemed cowardly or shy become the unsung hero and save the day so to speak. Make sure their actions make sense in the frame of the story but we want the audience to be shocked and yet proud of the actions this character undergoes to achieve this feat."
VillanOrigin = "Have someone start as a good guy the audience connects with that turns even because of something tramautic in the story, this can be done via flashback or directly in the story. It should be believable and fit into the story. It can also be part of the twist if there is one involved"




Character_Art1 = "Come up with a Prompt for someone to create a unique portrait of the character based on the description provided, be creative and give the reader an idea of what the character looks like. Make sure to match the style with the genre of show"
Character_Art2 = "give the AI a prompt to make a work of art inspired by their character and their description the art type should be an illistration of the characters concept art  based on the description provided, be creative and give the reader an idea of what the character looks like. Make sure to match the style with the genre of show"
#Character_Art3 - give the AI a prompt to make a work of art inspired by their character and their description feel free to be creative and have them in action, give the AI a prompt to make a work of art

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