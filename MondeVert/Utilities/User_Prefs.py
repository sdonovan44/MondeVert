import pandas as pd
import random


Name = 'Shane'
Bot_Name = 'Brick Top'
SavePath = r"A:\ShakeBot Testing"
AI_Art_Path = r"A:\AI Art"
AI_Poetry_Path = r"A:\AI Poetry"
AI_Blog_Path = r"A:\AI Blogs"
AI_Music_Path = r"A:\AI Song Lyrics"
MasterFile = r"A:\Master Tracker Files\MondeVert Master Tracker.xlsx"
MasterFile2 = r"A:\Master Tracker Files\MondeVert Master Transcript.xlsx"
MasterFile3 = r"A:\Master Tracker Files\MondeVert Master Blog Poem and Song Lyrics.xlsx"

#API_Key = "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"
AI_ArtistName = 'Sage Pixels'
AI_Poet_Name = 'S. J. Rose'
AI_Blogger = "Brick 'Top' Pulford"
Song_Writer = "Mr Pulford"

Poem_Title_Prompt = 'Create a unique and symbolic and abstract title based on the content of the following poem '
Song_Title_Prompt = 'Create a unique and symbolic and abstract title based on the content of the following song lyrics '
Shake_Poem_v1_prompt =  'Make a prompt for  artificial intelligence  to create a unique work of art that is based on the following poem '
Shake_Poem_v2_prompt = 'Using the following poem make a unique poem of your own that uses the original poem for inspiration and create your own unique style of poetry. Make your poem range between 3 to 10 lines. '

Art_1_prompt  = 'Make a prompt for  artificial intelligence  to create a unique work of art, using no more than 250 words in your prompt.  Provide a detailed prompt to make a unique, creative work of art to be used for to capture readers attention based on the following text'
Poem_Art_2_prompt = 'Make a prompt for artificial intelligence  to create a unique work of art, using no more than 250 words in your prompt. pick a random artist, preferably a lesser known artist, to base the style of the work of art and Provide a detailed prompt based on the following poem,'

#Quick_Poem_prompt =' Write a descriptive poem by leveraging a wide range of literary devices, styles, and potentially use a complex rhyme scheme.  give the poem an positive concept for the reader to interpret. Poem can be about love, friendship, specific geographic locations, family ,growing up and losing your innocencence, nature, hope, abstract, funny'
#Quick_Poem_prompt2 =' Write a descriptive poem by leveraging a wide range of literary devices, styles, and potentially use a complex rhyme scheme.  give the poem an abstract concept for the reader to interpret'
#Quick_Poem_prompt =' Write a comical poem with a positive vibe that makes the reader be shocked and filled with laughter and joy.  Use a wide range of literary devices, styles, and  use a  rhyme scheme, while being witty. Poem can be about love, partying , college, sports, life as an artist, friendship, specific geographic locations, specific time periods, pop culture ,characters from books/movies/tv ,family problems,growing up, losing your innocencence, nature, hope, abstract, funny. the funnier the better'
#funny poem
#Quick_Poem_prompt =' Write a funny poem  using a well versed vocabulary as the speaker is well-spoken.  Use a specifc style of poetry, remember this poem is supposed to make the reader laugh'



#Nature poem
#Quick_Poem_prompt =' write a poem describing a beautiful one-of-a-kind view in nature. Make it extremely descriptive using a college-level vocabulary. The poem is immersive for the reader. Capture the full beauty of the scene. Come up with a unique poetry style for the poem'
Quick_Poem_prompt =' write a poem describing a beautiful one-of-a-kind view in nature, specifically write about Portland Maine. Make it extremely descriptive using a college-level vocabulary. The poem is immersive for the reader. Capture the full beauty of the scene. Come up with a unique poetry style for the poem'

#Using AI #use this as it is awesome, reqord to work for me
#Quick_Poem_prompt ="Create a poem showcasing the power that art has to inspire people on a personal level, and using the power to create something new.Choose 2 or more poets and base the style of your poem on theirs. Use their poems as inspiration to create something that is uniquely your own, and that has the power to inspire others in turn. Remember that art is about more than just saying nice words – it is about emotion, passion, and the ability to communicate something important."

Song_Title_Prompt = 'Create a unique and symbolic and abstract title of a song based on the content of the following lyrics '
Chorus_prompt = 'Write  a 16 second  chorus that is catchy Without plagiarizing another song, do not copy any song,The song should be either rap, hip-hop, soft-rock, indie, grunge, punk, techno or pop. Write  a catchy chorus that is witty and rhymes.  Study the top songs in history and derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody'
Chorus_Art_2_prompt = 'Make a prompt  for  artifical inteligence  to create a unique work of art, the prompt should be no more than 100 words. pick a random artist, to emulate and base the work of art off of their style. Make an abstract work and creative of art. based the prompt on the following song lyrics'
Bridge_prompt = 'write a one bar hook for a song make it funky and different, multiple syllable rhyming is preferred but not neccesary, use a specific style of music and transition verse to chorus. be creative'
verse_prompt = 'Without Plagiarizing any known songs, Write a quick 30 second song. The song should be either rap, hip-hop, soft-rock, indie, grunge, punk, techno or pop. related to the title of the song. Write a catchy chorus that is witty and rhymes enouigh to be a good chorus. Study the top songs in history and derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody. Based on the following lyrics'


#Song_prompt = 'Write a short song, less than 2 minutes, with a catchy melody and catchy lyrics. The lyrics are witty and the lyrics should rhymes in a way that is pleasing to the listener and surprising, not repetitive and basic. Look at the top songs in history and come up with a unique style that combines these ideas and styles. Be creative and use complex rhyme schemes and music theory to make a melody'
Song_prompt = 'Write a short 30 second song that is not plagiarizing another song do not copy another song. the song has a catchy melody and catchy lyrics. Have a lesson in the song that is relateable and not corny. Use real life examples from the perspective of the singer. The lyrics are witty and the lyrics should have a unexpected rhyme scheme that is not repetitive and is not basic. Study the top songs in history and derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody'

Rap_Story_prompt = "Write a short song 30 second hip hop and R&B song use the following subjects for inspiration for the story/lyrics 'love, beauty , nightlife,being social, humor, nature, natural things,  social justice, peace love and unity, hippie vibes, save the world,beautiful girls, enjoying the summer, having fun, good vibes and good times, and other fun entertaining subjects'. Tell a story and do not plagiarizing another song .  keep 2 distinct rhyme schemes at time simultaneously. Rhyme multiple syllable in each line. The rap should be a reflection on current day's society with modern references. Derive your own lyrics and flow .Have a rhyme scheme and make a melody"
Rap_Bridge_prompt = 'write a one bar hook for a R&B song. derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody.  Make it catchy and have a rigid rhyme scheme. Make a distinct melody'
Rap_Chorus_prompt = 'Without plagiarizing another song , Write  a 16 second  chorus that is catchy  for a  hip hop and R&B song.the chorus should help bring a positive light to the story within the song lyrics. '

Rap_Story_prompt2 = "Write a short song 30 second hip hop and R&B song. While being abstract and using linguistic tricks to entertain the listener,  use the following subjects for inspiration 'broken heart, feeling lonely, not wanting to be alone, depression, feeling sad, wanting to die, being lost, having everything and its not enough, missing you'. Tell a story and do not plagiarizing another song . Pick a strict rhyme scheme and have most lines rhyme in the song, Rhyme multiple syllable in each line. The rap should be a reflection on current day's society with modern references. Derive your own lyrics and flow .Be creative and Make a story in the lyrics and use music theory to make a melody"
Rap_Bridge_prompt2 = 'write a one bar hook for a sad R&B song. derive a unique style. Be creative and use complex rhyme schemes and music theory to make a melody.  Make it catchy and have a rigid rhyme scheme. use the following subjects for inspiration: "broken heart, feeling lonely, lonliness, bittersweet, feeling sad,heartbreak, being lost, having everything and its not enough, missing you". Be abstract and make it interesting for the listener'
Rap_Chorus_prompt2 = 'Without plagiarizing another song , Write  a 16 second  chorus that is catchy  for a  sad hip hop and R&B song.the chorus should help bring a positive light to the story within the song lyrics. use the following subjects for inspiration: "broken heart, lonely, lonliness, bittersweet, morose, sad,heartbreak, being lost, self-doubt, missing you"'



Reggae_Story_prompt = "Write a short 30 second song that is not plagiarizing another song. Be abstract and creative, for example the song can  be inspired  the following ideas  'beatiful sights, nature, natural things,  social justice, peace love and unity, hippie vibes, save the world,beautiful girls, enjoying the summer, having fun, good vibes and good times, being a good person,beers, drinking,going to concerts, smoking weed, chilling, going to the beach with your people,fun times, loving each other, love'. derive your own lyrics and melodies from what you observe."
Reggae_Bridge_prompt = 'write a one bar hook for a jamrock raggae jamband  song . derive a unique style. Be creative and use rigid rhyme scheme where multiple syllable rhyme in each line. Study music theory to derive a melody. Make it catchy.'
Reggae_Rap_Chorus_prompt = 'Without plagiarizing a known song. Write a 16 second  chorus that is catchy for a  jamrock raggae hip hop and R&B song that is intended on being sung.  Study the top reggae and jamband songs and derive a unique style.'


Techno_Story_prompt = "Write a few bars for a techno song  that is not plagiarizing another song . Create a distinct rhyme scheme and derive your own lyrics. Be creative and use complex rhyme schemes and music theory to make a melodyStudy the top pop, r&b, techno and edm songs and try derive a unique style. Make it interesting, be creative and sometimes avant garde have fun!'"
Techno_Bridge_prompt = "provide two similar yet different quotes that inspire and invoke emotions into the audience. Pick diverse people throughout history to quote also it can be from literary sources as well. Be creative and try to come up with obscure quotes. Explain why you chose them in less than 50 words"
Techno_Chorus_prompt = 'Without plagiarizing a song , Write  a 16 second  chorus that is catchy  for a techno jamrock raggae, jam band, hip hop or  R&B song with a catchy melody. Study the top pop, r&b, techno and edm songs and try derive a unique style. Make it interesting, be creative and sometimes avant garde have fun!'

Techno_Sample_Question = "list  3 names of random songs .  provide me specific  lyrics from the 3 songs that are the most memorable or obscure.  Be creative and try to pick songs from different genres."
Techno_Sample_Question2 = "provide 2 unique  quotes that inspire and invoke emotions into the audience. Pick diverse people throughout history to quote also it can be from literary sources as well. Be creative and try to come up with obscure quotes. Explain why you chose them in less than 50 words"


#Sunday_Scaries_Poem_prompt =' Write a funny poem or short story about the sunday scaries make it about a certain character or group of characters. Be sarcastic that its the best day of the week, but overall remain positive to add comedic effect.  Use a distinct poetic style and distinct rhyme scheme. Have comical pauses and use  a comedy-routine-like timing in the poem.'
Sunday_Scaries_Poem_prompt =' Write a funny  poem  from the point of view of a character the audience connects with about the sunday scaries. Be sarcastic that Sunday is fun and make the idea of sunday scary abstract and a vivid story, add comedic effect.  Use a distinct poetic style and distinct rhyme scheme.'



#Wiki Prompts
Custom_prompt_1 = "write a wikipedia page for a poet named S.J. Rose Tell the reader what S.J. stands for and give her an interesting and yet beleivable background and vivid details on her personal life. S.J. Rose is a witty and funny poet who respects the great writers and poets in history.  Make the article convincing and talk about how she has a diverse range of poetry and likes to explore a lot of styles."
Custom_prompt_2 = "write a wikipedia page for a digital artist named 'Sage Pixel' give her an interesting and yet beleivable Avant-garde background and a personal life with very unique tramatic but entertaining and funny way. Include drugs somkehow in Sage's thrilling story. Make the article convincing and talk about how she has a diverse range of artistic knowledge and training and the art they create are true works of art. 'Sage Pixel' expresses themself using a wide-range of art forms to provoke deep emotions even with simple and/or abrstract meanings."
Art_prompt_1 = "Make a prompt for  artifical inteligence  to create a unique work of art that will be used for a poet's online profiles.   please refer to the following details about the poet: "
Art_prompt_2 = "Make a prompt for  artifical inteligence  to create a unique work of art that will be used for a digital artist's profile picture.  It is supposed to be something abstract and unique. The artist is avant-garde please refer to the following details about 'Sage Pixel'. "
Custom_prompt_3 = "create the name of a modern day macabre poet, this ficticious poet is still alive and younger than 40 years old currently.  write a fictitious wikipedia article. The poet you make up should have a similar style as  Edgar Allen Poe as it is his main influence. Give the poet a name and a macabre backgound/lifestyle. This poet has a bit of a cult following. Give this poet an interesting and almost unbeleivable background  with vivid details about his personal life and career. Usually his poems have some sort of lesson, but in general it can be pretty depressing."
Art_prompt_3 = "Make a prompt for  artifical inteligence  to create a unique work of art that will be used for a goth/emo macabre poets profile picture.  It is supposed to be something abstract, dark and unique. The poet is avant-garde please refer to the following details about the respective poet. "



#Blog Post Daily
Blog_Daily_prompt = 'Write a short 500 word or less blog post with links/proper sources that explains a topic of interest that will attract readers and is entertaining. Make it a positive blog but also be real and provide an unbiased point of view for the reader to decide for themself. Be creative and come up with something easy to read but use eloquent language without over-doing it. Do not plagiarize the aritcle'
Blog_Post_Explain = "Write a short 400 word blog describing what Chat GPT is and the benefits of using the technology, do you think its beneficial to humans? Also please describe how the art is made by DALL-E software. Specifically talk about how you prevent plagiarism from occurring. Be creative but also factual and honest. Try to sound human and put emotion into your response. make it entertaining and do not be repetitive"
Blog_Post_SocialProg = 'Write a short 700 word or less blog post with links/proper sources that explains in detail how a person can benefit from various programs available to people in the United States. Please come  up with your own topic that is useful information and/or Pick one of the following subjects to provide details and resources " information for mentail health programs available and how to get help, early start programs, equal opportunity programs, trade schools, trade unions, growth opportunities, government programs that are useful to know, other useful tips,financial aid for high school and college and other helpful topics". Be clear and provide details like demographics and which states are participating and other eligibility information. Use language that will attract readers and is entertaining. Make it a positive blog but also be real and provide an unbiased point of view for the reader to decide for themself. Be creative and come up with something easy to read but use eloquent language without over-doing it. Do not plagiarize the aritcle'
Blog_Post_Science = 'Provide proper references and sources for your research. Explain a random complex scientific topic and simplify the ideas and conscepts so they can be understood by all. Make it interesting and entertaining. Use eloquent language but do not overdo it. Have fun and try to connect to the reader on a personal level.'
Blog_Post_Portland = 'Provide proper references and sources for your research. Write a fun blog post that describes portland Maine and all it has to offer. Make it sound like a great destination. Make it interesting and entertaining. Use eloquent language but do not overdo it. Have fun and try to connect to the reader on a personal level.'



Timmy_D_Cover_Art_Prompt1 = 'Help me to create a prompt for artificial intelligence to make a unique work of art that is visually pleasing and peaks the audiences curiosity. The subject should be a landscape of an overpass bridge under construction with workers in the distance out of focus'
Timmy_D_Cover_Art_Prompt2 = 'Help me to create a prompt for artificial intelligence to make a unique work of art that depicts an overpass bridge under construction with workers in the distance. Pick a random style and make it uniquely your own'
Timmy_D_Cover_Art_Prompt_Direct_to_ArtBot = 'Pick a random artist of your choosing to create a work of art that depicts an overpass bridge under construction with workers in the distance'
Timmy_D_Dialogue2 = "Please write a detailed scene with realistic dialogue for a novel set in United States. The conversation is between 5 construction workers who are tasked with completing an overpass bridge. the conversation is focused on accountability, saftey,  planning ahead, staying organized  encouragement and the value of friendship while learning about each other's culture. Do not have characters say repetitive words, have subtle lessons for the audience to interpret. Character 1 is Titus, Titus is a great conversationalist, confident and down to Earth. Titus is from a small African village. Character 2 is Liam, Liam from Galway Ireland. Liam is charismatic and encourages teamwork. Character 3 is Jorge, Jorge is from Vera Cruz Mexico and he is a loyal, dedicated hard-worker. Character 4 is Chen Ho, Chen Ho is from Shanghai China. Chen Ho is open minded, soft spoken and extremely grateful. Character 5 is Simon, Simon is a Jewish Ambassador from Boston. Simon is the project manager, is a good listener, persuasive, intense, and trustworthy."
Timmy_D_Dialogue1 = "Please write an oscar worthy scene with dialogue for a novel set in United States. The dialog should be in a prose that fits each character and the conversation is between 5 construction workers who are tasked with completing an overpass bridge, the conversation is witty and funny while encouraging doing the job properly and the value of friendship while learning about each other's culture. Keep the scene interesting and do not be repetitive. Character 1 is Titus, Titus is a great conversationalist, confident and down to Earth. Titus is from a small African village . Character 2 is Liam, Liam from Galway Ireland. Liam is charismatic and encourages teamwork. Character 3 is Jorge, Jorge is from Vera Cruz Mexico and he is a loyal, dedicated hard-worker. Character 4 is Chen Ho, Chen Ho is from Shanghai China. Chen Ho is open minded, soft spoken and extremely grateful. Character 5 is Simon, Simon is a Jewish Ambassador from Boston. Simon is the project manager, is a good listener, persuasive, intense, and trustworthy."

def getUserName():
    g = Name
    return g
def getAssistantName():
    g = Bot_Name
    return g
def getAPIKey():
    g = API_Key
    return g

def getPath():
    g = SavePath
    return g

def getMFPath():
    g = MasterFile
    return g

def getMF2Path():
    g = MasterFile2
    return g