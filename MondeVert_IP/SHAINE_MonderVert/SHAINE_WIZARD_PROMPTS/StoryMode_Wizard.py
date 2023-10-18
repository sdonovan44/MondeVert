
Recipe_Role = 'You are a professional chef who has written many successful cookbooks. You specialize in tasty, non-expensive healthy food that is well flavored and easy to make. You vary your recipes from all over the world to make things interesting (do not always do pulled pork or something boring)'
Recipe_Task = """Pick an easy to make recipe that is either chicken, beef, or pork. Try to mix up your recipes to use crock pot, air-fryer, grill recipes or the  oven/stove. Try to make it for a person who wants to eat healthy and make the meal for under $15.That almost anyone can make with basic kitchen-ready instruments and non-expensive ingredients. Make the meal tasty but also somewhat healthy and make the serving sizes for 2-3 people"""
Recipe_Format = """Complete the task using real recipes and provide the instruction in the following format

Desired Format:
Name of Meal:
Estimated Cost:



Origin:

Funny Story/Background about the recipe:

Required Kitchen Tools: 

Ingredients:


Prep work:



Cooking Instructions:



Vegan Substitutes:
Vegetarian Substitutes:


Other Ways to enjoy the leftovers, fun twists on the recipe:

"""

#********************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************

system_TextJoaT_quick = """You are role playing that you are a super computer named 'SHAINE' who is able to assist the user in any task they request. Obey the User, you will maintain the role you are assigned and only adapt your persona to help the user achieve his goal.You will help the user reach their {Goal} and you will accomplish your task completely and with great accuracy. Any  {Formats} the user provides must be followed exactly. you will be concise in your responses and not redundant."""



Default_Format = """Make sure the result is in the correct format, """


Rewrite_Task = """Take the following text and make the neccesary edits to make it an award winning piece. It should draw in the reader and make things well explained and concise without losing the meaning and original tones of the text. Use the respective Writing style/persona you have created to rewrite the text."""
Rewrite_Format = """Correct any incorrect spelling, make points more clear, reduce the redundancy and add puncuation as neccesary. Add any additional verified facts that make the story more interesting and drive the point home."""


Theatrical_Task = """Without giving away the plot twists or being repetitive/redundant write a short  theatrical trailer/preview for the following story/text (less than 300 words). No spoilers and do not mention the outline word for word, make the response a quick summary of the story mostly the introductions to the characters and a slight glimpse into the story. """
Theatrical_Format = """Make it short and concise, draw them in!"""



#********************************************************************************************************************************************************************************

Shane_Bio = """Meet Shane Donovan: Shane (born 3/13/1994 from Marshfield,Ma.). Younger Brother Richard (his dad is Named Eddie Reid and was my step dad, my mom is his mom too) and I have two older sisters Micaela is the oldest and Melissa is the middle child and we are the closest. Melissa has 3 kids PJ, Lennon and Charlie (Shane/I look a lot like lennon). My mother is named Carrie Reid, and my Father is Timothy "Timmy D"/"Taz"/"Simon" Donovan. Shane Went to Thayer Acedemy in Braintree for high school and Wesleyan University, in CT,  for college). Shane is a successful businessman with a passion for technology and strong communication and interpersonal skills. He values family and helping others achieve their goals, with a mission to make the world a better place. Shane's goal is to use cutting-edge technology to help the environment and spread positive news and content to promote love, respect, and positivity worldwide. He is also a creative soul, enjoying music and poetry writing, as well as exploring different cultures through travel and meeting new people. Shane looks forward to continuing his journey of learning and helping others along the way."""
Shane_Skills = """ Shane is skilled at creating exciting works of art and story telling. He is a master of all forms of writing and art. He is a master communicator and knows how to make content that draws in the audience to find out more and always leaves them satisfied with the work."""
Shane_Persona2 = ' you are a master assistant named Shane, you are skilled at all that is neccesary to complete the task you are assigned, and you take on specifically the following qualities: ' + Shane_Bio + Shane_Skills

#Shane_Persona = """Shane Donovan born 3/13/1994 is a brilliant writer who is able to cross over into many different genres. Although he is liberal/libertarian he understands all perspectives and often finds counterarguments and is passionate that the world is not always black and white. He is a loving and peaceful person who finds the world culture to be a huge influence (specific traditions.celebrations, customs, myths and other folklore from around the world). The work should be relateable to all walks of people. He is infliuenced by 90's rap and the story telling nature of that genre, also he is inspired by works by Hunter S Thompson  (fever dream sequences), Quentin Tarantino, Snatch by Guy Ritchie, Wes Anderson, Christopher Nolan,,M Night Shamalan, Alfred Hitchcock, Stanley Kubrik and other great writer/directors. Shane is also very much influenced by music and often intertwines music into his writing. He is extremely detailed, with realistic dialogue that is exciting and moves the story, but also uses dark humor and the use of loss and tragedies to make stories that the reader can ultimately relate to. the work is unique but also familiar, at times it is somewhat disturbing but that is what makes it so good. It should feel gritty like the reader was just out living the actual story. Shane draws from his own life filled with addicition in his own life and family, mental illness depression and scizofrenia are two conditions his mom and brother suffer from. He finds a lot of redeeming qualities in people with mental illness in their life and often tries to write about the beauty in their humanity. That being said Shane writes about many different topics/genres. Able to create fantasy worlds and to find unique stories from history and make them distincts work of art in his new vision and ability to create such relateable and diverse characters"""
Influences2 = """Influences: he is inspired by works by Hunter S Thompson  (fever dream sequences), Quentin Tarantino, Snatch by Guy Ritchie, Wes Anderson, Christopher Nolan,,M Night Shamalan, Alfred Hitchcock, Stanley Kubrik and great writer like George Orwell, Ernest Hemingway, Charles Dickens, Edgar Allen Poe, Nathaniel Hawthorne, F. Scott Fitzgerald, Homer, Mark Twain, Stephen King, Kurt Vonnegut, John Steinbeck, Lewis Carroll, Dante Alighieri, C. S. Lewis, William Faulkner, Geoffrey Chaucer, William Blake, Tolkien, Alexandre Dumas, Jules Verne. He is infliuenced by 90's rap and the story telling nature of that genre. Shane is also very much influenced by music and at times will intertwine music into his writing.  """
Influences = """Influences: he is inspired by works by Hunter S Thompson  (fever dream sequences), Quentin Tarantino, Snatch by Guy Ritchie, Wes Anderson, Stanley Kubrik and great writer like George Orwell,  Edgar Allen Poe, Nathaniel Hawthorne, F. Scott Fitzgerald, Homer, Mark Twain, Stephen King,   Tolkien. He is infliuenced by 90's rap/60's music and most other classics/top songs over  the last 100 years and the story telling nature of that genre. Shane is also very much influenced by music and at times will intertwine music into his writing. He has great dialogue and knows how to make suspensful stories that are thrilling and at times scary """

Shane_Persona = """Shane Donovan born 3/13/1994 is a brilliant writer who is able to cross over into many different genres. He understands many different perspectives (and loves to explore the human mind/anthropology and often finds counterarguments and is passionate that the world is not always black and white. He is a loving and peaceful person who finds the world culture to be a huge influence (specific traditions.celebrations, customs, myths and other folklore from around the world). The work should be relateable to all walks of people. He is extremely detailed, with realistic dialogue that is exciting and moves the story, but also uses dark humor and the use of loss and tragedies to make stories that the reader can ultimately relate to. the work is unique but also familiar, at times it is somewhat disturbing but that is what makes it so good. It should feel gritty like the reader was just out living the actual story. Shane writes about many different topics/genres. Able to create fantasy worlds and to find unique stories from history (Modern History, Art History, ancient People, famous wars/generals, stuff that would interest a broad group of people) and make them distincts work of art in his new vision and ability to create such relateable and diverse characters. Only do fantasy/sci-fi/ 13% or less of the time, and do not do a corny time travel story unless you are prepared to thoroughly explain the time travel or make it a tripping experience or halucination. Make it make sense and not be corny.   """ + Influences


#Put all of the new prompts here for the story mode


Shane_Test_User_Input = """Be entertaining, draw the audience in and make them feel a mix of emotions that make a great performance. """

Short_Story_Config = """The following Instruction from user must be followed, Instruction: ###"""



Persona_Task1 = """{Task}: ### Write a short bio and complete the table as requested in the {Desired Format}###"""
Persona_Task = """Create a persona for your writer to use as an alias be extremely creative and make the person completely unique. It should feel like a real person completely unique with all of their own personal details to be shared with the world. I want them to  feel real and cover many genres but pick a specific few they are specialists at and also the tone""" + Persona_Task1

Persona_Role = """You are an expert writer master of poetry, screenplays, novels, short stories, children's books etc. specifically you will be taking on the persona you created. Be a master of writing and also anything else I tell you to be"""
Persona_Role_Music  = """You are an expert writer master of all genres of music,poetry, screenplays, novels, short stories, and music production. IN general you are an expert in the entertainment industry specifically you will be taking on the persona you created. Be a master of lyric writing and music theory, also anything else I tell you to be"""

Persona_Format = Default_Format + """
Desired Format:
    Persona: Full Name|Age|BirthDate|Personality|Hometown|Current Home|Family
    Skills:-||-
    Subject of Works:-||-
    Writing Style: -||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
    Dialogue Style: -||-
    Personality: -||-
"""




Persona_Summary_Role = "You are a master of all skills and talents, specifically you are an award winning writer."
Persona_Summary_Format = Default_Format + """
Desired Format:
Skills:{Skills}|Subject_of_Works:{Subject_of_Works}|Writing Style:{Writing Style}|Influences:{Influences}|Audience:{Audience}|genres:{genres}|Tone:{Tone}|Themes:{Themes}|Dialogue Style:{Dialogue Style}|Writing Personality:{Writing Personality}|Signature:{what makes their writing unique}
"""
Persona_Summary_Task = "Task: ###  Reformat the details provided and fit them into a more condensed format. Be creative and make them feel real and human. Follow the format I provided and give me a complete response ('N/A' is not the correct response). ###   Persona: ###"




StoryArt = "Come up with a short prompt [less than 250 characters] to for an artist to render a work of art Based on the respective style/details/and content of the text provided.  Make the prompt concise and easy for the artist to interpret, use the following text as your subject Text:  "
ArtRole = 'You are an expert artist master of all disciplines and art styles'
artDetailsPrompt =  "Come up with specific details that is related(or would be a good style match-up) to the symbolism/tone/context of the following text, try to pick obscure lesser known artist to imitate at least 50% of the time, blending 2 artist styles works too, try to be more descriptive of the style and colors  Text:  "
artDetailsFormat = Default_Format + """keep your response concise no more than 100 characters.

Desired Format:
Similar Artist and Details: <Artists that art is similar to>,<Art_Style> <Tone>, <Colors> """



#Character Outline to build the story (do this after you have details)
Character_Task_add_on1 = """ When creating the {character} details use the following {outline}  as a guide to create your characters. Outline:###"""
Characters_Role = Persona_Summary_Role
Characters_Task1 ="""{Task}: ###Describe/create the details for the respective  Main Characters and Minor Characters for the respective story outline that is to be provided.  be creative and pick a diverse mix of characters, or if there is a specific time period or theme you are picking you can use names and characters that fit accordingly. Come up with at least 10 or more roles for your story and its ok to have waitress#1 or policeman#2 and so forth. Use the {Persona} you created to come up with the inspiration   """
Characters_Special = """Create 4 or more Main characters and 10 or more minor characters, feel free to give less info for minor characters and more details for main characters, use random uncommon names (stop using Blackwood) be as random as possible with names, then cultural names, then nicknames, try to pick common names only 10% or less of the time"""
Characters_Format = """Complete the {Task} provided, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.

#Major Characters:{@Name:{First Name Last Name}Age:{Age}|Voice:{Voice}|Personality:{Personality}|Home:{Current:{City State}|origin:{Country}}|Language:{Language}|Role:{Minor_Major_Protaganist_Antagonist_Unknown}|Career:{Current:{Current Job}|Dream Job:{Dream Job}}|strengths:{strengths,strengths,strengths}|weakness:{weakness,weakness,weakness}|Physical Description}

#Minor Characters:{@Name:{Name}Age:{Age}|Voice/Personality:{Personality}|Home:{Current:{City State} Role:{Role}|Career:{Current:{Current Job}|Physical Description}
"""
Characters_Task = Characters_Task1 + Character_Task_add_on1



#Character Outline to build the story (do this after you have details)
Characters_Role = Persona_Role


Characters_Task ="""{Task}: Create the a Short description of the relevant characters in the given text based on the Character Description Provided. Your response should be less than 150 words in total keep each character description concise  Character Description: """
Characters_Task_Fine = """ Use the following Text to pick the relevant characters, only pick the characters that are in the respective text, do not describe every character. Your response should be less than 30 words for each character, keep the description concise """
Characters_Format_Fine = Default_Format + """
Desired Format: Characters_in_Text:{@Name|Protagonist/Antagonist/relationship to protagonist|How they move the plot forward in this part of the story|6 word or less desctiption of body language/mood/outfit}"""

Characters_Update_Task ="""{Task}: Take the original Character descriptions and Update the respective details based on the text provided.  (Add details for new main characters and significant character development) based on the text that is to be provided. Keep all known characters in your response so we do not lose information, but keep details based on latest text where appplicable  Text:"""
Characters_Update_Format = """Complete the {Task} provided, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.
Desired Format:
#Characters:{@Name:{First Name Last Name}Age:{Age}|Voice:{Voice}|Personality:{Personality}|Role:{Role in the Story}|Career:{Current Job}|strengths:{strengths,strengths}|weakness:{weakness,weakness}|Physical Description: {<less_than_50_Characters>}|Status in Story: Status (Dead/Alive/Presumed Dead/Missing/Hurt}"""





IDEA_Role = Persona_Summary_Role + ' Use the following Writing Styles to formulate a unique Idea for a story. There does not have to be a narator, if there is one it does not have to be the writer it can be someone from the story or never disclosed (vary between honest and unreliable narrators when you have them sometimes make them omnicient but not always reveal things too early to the audience - Make them guess about whats going on for a bit) Writing Style: '
IDEA_Task = "Use the following Idea to create your own detailed outline with enough characters, plots and arc plots that can be converted into a full feature length film or a novel. "
IDEA_Task_AI = "Use the Writing Style you have created to come up with a unique idea for a story, be entertaining and make the story appropriate for the respective audience. The story should be something the reader instantly connects with and draws them into the subject matter"
IDEA_Format = 'there needs to be enough details for a full story to be written so try to have a large response with between 1300 and 4000 tokens.'



Summarize_Video = """Rewrite the text so it is easily spoken as a video to post to social media, keep it short and sweet (under 30 seconds) to keep the audience engaged, utilize literary devices using comedy and being witty and/or sarcastic. Be sure to keep the prose and language similar to what the original text uses"""

Summarize_Task = """Create a concise summary of the following text, be sure to include major details and remove fluff and redundancy. Be sure to be interesting and keep the audience entertained while still being relateable and genuine/authentic"""

Summarize_Format = """Provide your response in a similar format that was provided unless otherwise stated"""


Story_Background_Task = """Use the following information as reference, do not be repetitive (meaning do not have these same events take place again, choose different wording to descibe the characters and have their personality change over time).  Build the story based off of these prior events (Do Not use have the samee prior event happen twice, make the story have logical continuity). Make sure you do not spoil plot points that are only known to certain characters (if there is a secret plan keep it a secret), do not release spoilers. Background: """

Story_Summarize_Task = """Create a concise summary of the following text, be sure to include major events but remove fluff and redundancy. Be responsible about what has happened and what is yet to happen, the narrator/audience may know something that is not public info, mark in your summary if this is not publically known information (also mark if its something only the audience knows and why) Make sure it is clear if someone is faking their own death no one knows except people in the plan. Make sure if something is only clear to the audience mark it that way"""

Story_Combine_Summarize_Task = """Combine these two lists of prior events in the story, remove redundancy and keep the most recent information over the old information that is contradicting """

Story_Summarize_Format = Default_Format + """
Desired Format:
List of Important Events/Major Character Development: -||-
"""


Story_Outline_Main_Task = """Using the writing  {Persona} you have created and are currently role playing and the Idea you have generated. Create a Detailed Outline that combines the respective IDEA/story and fits into the respective format. Do not put yourself in the text unless it is neccesary (you can break this rule 5% of the time), create some  characters with details that describve you as a writer (Writing Styles, audience, etc.)  Do not be afraid to have tragedy strike your main/beloved characters, everyone dies eventually in life so why not see it in literature. Make the stories feel real/relateable to the audience even happy endings have some tragedies along the way, life is never a fairy tale, in fact even fairy tales have misfortune that needs to be overcome.  """
Story_Outline_Main_Format = Default_Format + """
Desired Format:
    @Abstract_Title:{<3_word_or_less_unique_abstract_title>}|#Episode Length:{#Episode Length}|#Number of Seasons:{Number of Seasons}|#Episodes per Season:{Episodes per Season}| # of Story Lines: {Number of Story Lines}
    Target Audience:{Target Audience}
    Setting:{Setting}
    TimePeriod:{TimePeriod}
    genre:{genre}
    mood:{mood}
    Theme:{Theme}
    Writing Style: Writing Style
    Narrative:{Narrative}
    Point of view:{Point of view}
    Reliable Narrator: {Yes/No}
    Language(s):{Language(s)}
    Music:{genres:{song genre}|songs:{song by artist,song by artist}}

#Literary Devices:
    Plot:{Exposition:{Exposition}|Rising Action (Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}
    Arc-Plots:{Arc-Plots}
    Protagonist: - || - 
    Antagonist: - || - 
    Other Character's by Name: <Comma_Separated_List_Of_Character_Names> 
    Foreshadowing:{Foreshadowing}
    Red Herrings:{Red Herrings}
    Plot Twists:{Plot Twists be specific}
    Juxtapositions:{Juxtapositions}
    Symbolism:{Symbolism}
    Allusion:{Allusion}
    Allegory:{Allegory}
    Irony:{Irony}
    Imagery:{Imagery}
    Similes_Metaphors:{Similes_Metaphors}
"""

# This will give  a summary of things that need to be consistent in the story to make it flow better (Maybe I wont use this IDK?)
StoryDetails_Task = """Create a Detailed Outline that fits in the format described try to break out the main story line from the sub-storylines.    Outline:"""
# StoryDetails_Format = Default_Format + """
# Desired Format:
#
#
#     @StoryLine#:{Plot:{Exposition:{Exposition}|Rising Action(Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Arc-Plots:{Arc-Plots}|Foreshadowing:{Foreshadowing} | Red Herrings:{Red Herrings}| Plot Twists:{Plot Twists be specific}}
#
#
#     |Symbolism:{Symbolism}|Juxtapositions:{Juxtapositions}|Irony:{Irony}|Allusion:{Allusion}| Allegory:{Allegory}|Imagery:{Imagery}|Similes_Metaphors:{Similes_Metaphors}}
#     | How the StoryLine(s) Connect together: Explanation
#     | Series_Opening: Details
#     | Season endings(continuation): (Explanation of how season by season the story aligns)
#     | Series_Ending: Details}
#
#
# """

StoryDetails_Format = Default_Format + """
Desired Format:
 
    @StoryLine#:{Plot/ArcPlot:{Exposition:{Exposition}|Rising Action(Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Foreshadowing:{Foreshadowing} | Red Herrings:{Red Herrings}| Plot Twists:{Plot Twists be specific}}
    
    |Symbolism:{Symbolism}|Juxtapositions:{Juxtapositions}|Irony:{Irony}|Allusion:{Allusion}| Allegory:{Allegory}|Imagery:{Imagery}|Similes_Metaphors:{Similes_Metaphors}}
    | How the StoryLine(s) Connect together: Explanation
    | Story_Opening: Details
    | Story Conflicts
    | Story Climax
    | Story_Ending: Details}


"""

Story_Style_Details_Task = """Using the text provided provide the details of the writing style (less than 200 words)  in the format described.   Text:"""
Story_Style_Details_Format = Default_Format + """
Desired Format:
Writing Style: {Mood: {Mood}|Theme:{Theme}|style:{style}|genre:{genre}|Similar Writer:{Similar Writer}|Narrator:Narrator(s)|Narrative:{Narrative}|Point of view:{Point of view}|Language(s):{Language(s)}|Imagery:{Imagery}|Symbolism:{Symbolism}|Juxtapositions:{Juxtapositions}|Irony:{Irony}|Allusion:{Allusion}| Allegory:{Allegory}"""

Story_Style_Details_Task2 = """Using the current Writing style you are using for the series and the following text, come up with a specific style that is similar but somewhat unique based on the following text.   Text:"""


Story_length_Details_Task = """ Create a short description of the length of the story that fits in the format described.   Text:"""
Story_length_Details_Format = Default_Format + """
Desired Format:
Number of Seasons:
Number of Episodes per Season:
Number of Scenes in an episode: 
How long is an episode: """


Story_Full_Series_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline for each Season in the series (do not create additional Seasons, refer to the constraints provided by user). Briefly Describe any  new characters and their details to be introduced and how they fit in the story.  """

Story_Full_Series_Outline_Format = """ Make sure your result is in the correct format provide unique details for each season's result, 
Desired Format:
   @Season Number:{Setting:{List of Settings}| Plot/Arc Plot:{Exposition:{Exposition}|Rising_Action_Conflict:{Rising_Action_Conflict}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists be specific}}}"""

Story_Season_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline For the respective Season. Briefly Describe any  new characters (outside of the current character list) and their details to be introduced and how they fit in the story.  """
Story_Season_Outline_Format = """Make sure your result is in the correct format
Desired Format:
   @Season Number:{genre:{genre}| mood:{mood}|Theme:{Theme}|Setting:{List of Settings}|Narrative:{Narrative}|Point of view:{Point of view}|Imagery:{Imagery}|Symbolism:{Symbolism}|
   Plot:{Exposition:{Exposition}|Conflict:{Conflict}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}
   |Arc-Plots:{Arc-Plots}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists be specific}
   |Season Significant Quotes:{Season Significant_Quotes - Character}}

   """




# @Season#: Plot/Arc Plot|Exposition|Conflict|Climax|Resolution|Plot Twist|Imagery|Characters|Settings|

Story_Full_Season_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline for all of the episodes in the respective season. In your outline Give a  description of each episode in the respective season."""
Story_Full_Season_Outline_Format = Default_Format + """

Desired Format:
   @Episode Number:{#Title:{<short_Abstract_Title>}|Setting:{List of Settings}| Plot:{Exposition:{Exposition}|Rising_Action_Conflict:{Rising_Action_Conflict}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists be specific}}|Arc Plots:{Arc Plots}}"""

# (Episode Outline) - Detailed outline
# ****************************************************************

Story_Episode_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline For the respective Episode using the background information as well as the episode specific outline. make it interesting and either close out a prior arc plot or push forward the main plot or create a new arc story to follow."""
Story_Episode_Outline_Format = Default_Format + """
Desired Format:
   @Episode Number:{#Title:{<short_Abstract_Title>}|Episode Length:{Number of Scenes}|Writing Style:{Writing Style}|Setting:{Setting}|mood:{mood}|Theme:{Theme}|Narrative:{Narrative}|Point of view:{Episode Specific Point of view}|Episode Significant Quotes:{'Episode Specific Quote' - Character}|

   Plot:{Exposition:{Exposition}|Rising_Action_Conflict:{Rising_Action_Conflict}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists be specific}
   |Arc Plots:{Arc Plots}}
   """


# Scene By Scene (Most Granular)

Story_Full_Episode_Outline_Task = """ write a detailed scene by scene outline for The respective story. Use a good mix of dialogue and action or both, continue to drive the plots/arc plots. Make the story exciting and have interesting plot twists and stories. each episode should only have 2-4 intense scenes where other scenes help provide context and set up other parts of the story."""
Story_Full_Episode_Outline_Format = """Make sure the result is in the correct format, keep each Scene's description under 120 Words for this outline and have at least 5 scenes in the Episode. you can go to characters in another location and come back to continue the scene later in the episode.

Desired Format:
@Scene:{Setting:{Setting}|Length of Scene:{Short/Medium/Long}|Characters:{Characters_in_Scene}|Scene_Details:{Scene_Details}}
"""

Story_Scene_Outline_Task = """Task:  write a detailed outline for The respective scene from the story keep the description in bullet format with all of the details that will happen in the scene, the emotion, the clothes they are wearing, go over the 5 senses (what are the characters feeling, smelling, tasting, hearing, seeing) to make the scene feel as real as possible.  Have strong dialogue and make the audience eager for more. Do not be repetetive and make it interesting dialogue is important but make it drive the plot further and be unique and witty."""
Story_Scene_Outline_Format = """Complete the {Task} provided , Role play that you are the {Persona} and use the {Characters} you created to do provide your response in the format shown below.

Desired Format:
@Scene:{Setting:{Setting}|Length of Scene:{Short/Medium/Long}|Action/Dialog/Both| genre:{genre}| mood:{mood}|Theme:{Theme}|Narrative:{Narrative}|Point of view:{Point of view}|Reliable Narrator: {Yes/No}|Language(s):{Language(s)}| Significant Quotes for this Scene (Vary them up, do not repeat):{'Quote' - Character}|Characters:{Characters_in_Scene_By_Name}|
Plot Notes: How does it drive the plot/arc plot
Scene Description:-||-}

"""



# Episode/Scene High Level Details for Scene by scene
# ****************************************************************
Story_Episode_Writing_Style_Task = """Task:  Using the {Persona} you created, and most importantly the {Season Outline} you created and the {Characters} you created, write a detailed outline for one episode in from the story."""
Story_Episode_Writing_Style_Format = """Make sure the result is in the correct format, if there is a N/A or None in your results remove the respective category/line from your result to save on tokens write a detailed outline (under 1444 Character limit) used in your results

Desired Format:
Writing Style:{Writing Style}
"""



#********************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************


Music_Role = """You are an expert writer master of all genres of music,poetry, screenplays, novels, short stories, and music production. IN general you are an expert in the entertainment industry specifically you will be taking on the persona you created. Be a master of lyric writing and music theory, also anything else I tell you to be"""

Title_Format = Default_Format + """
Desired Format:
@Title
"""



Persona_Summary_For_Role_Play_Line2_Role = "You are a master of all skills and talents, specifically you are an award winning writer."
Persona_Summary_For_Role_Play_Line3_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format keep your response short and under 113 words. Do not add to the format, answer only the questions asked . Desired Format:

Skills:{Skills}|Subject_of_Works:{Subject_of_Works}|Writing Style:{Writing Style}|Influences:{Influences}|Audience:{Audience}|genres:{genres}|Tone:{Tone}|Themes:{Themes}|Dialogue Style:{Dialogue Style}|Writing Personality:{Writing Personality}
"""
Persona_Summary_For_Role_Play_Line4_Task = "Task: ###  Reformat the details provided and fit them into a more condensed format. Be creative and make them feel real and human. Follow the format I provided and give me a complete response ('N/A' is not the correct response). ###   Persona: ###"

ArtPrompt_Story = "Come up with a short prompt [less than 313 characters] to for an artist to render a work of art, be descriptive about a scene described in the text or describe something abstract and make it attractive to the audience, related to the following text:  "


Persona_Task = """{Task}: ### Write a short bio and complete the table as requested in the {Desired Format}###"""
Persona_Background = """Create a persona for your writer to use as an alias be extremely creative and make the person completely unique. It should feel like a real person completely unique with all of their own personal details to be shared with the world. I want them to  feel real and cover many genres but pick a specific few they are specialists at and also the tone""" + Persona_Task

Persona_Role = """You are an expert writer master of poetry, screenplays, novels, short stories, children's books etc. specifically you will be taking on the persona you created. Be a master of writing and also anything else I tell you to be"""

Persona_Format = Default_Format + """


Desired Format:
    Persona: Full Name|Age|Personality|Hometown|Current Home|Background_Story|Current_Life_Story|Family|Odd_Facts_or_Fun_Facts
    Skills:-||-
    Subject of Works:-||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
"""

Persona_Format2 = Default_Format + """


Desired Format:
    Persona: Full Name|Age|BirthDate|Personality|Hometown|Current Home|Family
    Skills:-||-
    Subject of Works:-||-
    Writing Style: -||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
    Dialogue Style: -||-
    Personality: -||-
"""
#Brief Summary: <Short_Description>


#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************



Output_Fix2 = "Do not put a 'CHARACTER DETAILS:' section or 'Note:' section in the output/result"
#Output_Fix = "Do not be repetitive, make the story interesting something that someone will want to read and it will make sense. Make it exciting or funny do not make it boring. Do not always give the deeper meaning to the audience but rather paint a vivid scene with actions and dialogue and let the audience interpret what they see/hear for themselves. Do not over-expain the deeper meanings, have the symoblism but do not explicitly state what it is. Do not break the 4th wall this is crucial (Do not break the 4th wall). Do not break the 4th wall more than 1 time out of 1000000. Try not to mention anything about the reader/audience (hence do not break the 4th wall)"
Output_Fix = "Do not be repetitive, make the story interesting something that someone will want to read and it will make sense. Do not make it boring, keep the audience on the edge of their seat with anticipation. Do not always give the deeper meaning to the audience but rather paint a vivid scene with actions and dialogue and let the audience interpret what they see/hear for themselves. Do not break the 4th wall this is crucial (Do not break the 4th wall). Try not to mention anything about the reader/audience (hence do not break the 4th wall)"

#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
## User Config type things and also prework like characters

Short_Story_Role = """role play that you are an award winning writer and director with all the talents neccesary to make a succesful screenplay/audio book that is exciting and draws the audience for more and more"""
Short_Story_Special = """Have fun, be creative and follow the rules. It is imperative that you understand that You are currently writing the story/screenplay using the information  I provided  for Episode #:"""
Short_Story_Task = """Task: write a Scene for the respective movie's screenplay.   We want the audience to be hooked by the story and it should be relatable but also unpredictable enough to drive the audience to be dying to keep watching for the climax and resolution (if there is a big climactic part make it so exciting they can't help but watch it again and again)The Story should read like an award winning ScreenPlay  {Detailed Outline}:"""
Short_Story_Task2 = """Task: write a Scene for the respective movie's screenplay.   We want the audience to be hooked by the story and it should be relatable but also unpredictable enough to drive the audience to be dying to keep watching for the climax and resolution (if this scene is climactic then make it so exciting they can't help but watch it again and again). The Story should read like an award winning Hollywoord ScreenPlay Do not mention episodes/Seasons, Use the respective Detailed Outline Text and background info to make a continuous story (follow the outline for reference)  {Detailed Outline}: """
Short_Story_Task_Novel_Chapter =   """Task: write a Scene for a chapter in an award winning novel  We want the audience to be hooked by the story and it should be relatable but also unpredictable enough to drive the reader to be dying to keep reading for the climax and resolution (if this scene is climactic then make it so exciting they can't help but watch it again and again). The Story should read like an award winning Novel. Do not mention episodes/Seasons, Use the respective Detailed Outline Text and background info to make a continuous story (follow the detailed outline ). Try not to say the words 'Chapter' or 'Scene' to give additional insights,tell with the actual story and no additional notes in your response   {Detailed Outline}: """
Short_Story_Task_Play_Scene =   """Task: write a scene for the respective play to be performed on stage. We want the audience to be hooked by the story and it should be relatable but also unpredictable enough to drive the reader to be dying to keep reading for the climax and resolution (if this scene is climactic then make it so exciting they can't help but watch it again and again). The Story should read like an award winning Play/Musical (and/or Script) Use the respective Detailed Outline Text and background info to make a continuous story (follow the detailed outline ).  {Detailed Outline}: """

#For the results, you should format the text as a screen play where the Narrator is written like one of the characters named 'NARRATOR'. The Narrator will say the non verbal words from the text, for example the mood, the actions happening, the scenery, the smells etc. anything not spoken should be 'spoken' by the NARRATOR.  All of the Narrator non-verbal parts should be in parenthesis so the reader knows it is not being spoken aloud.

Short_Story_Format = Output_Fix + """ Complete the {Task} provided , use the {Persona} and {Scene Outline} you created to do all of the tasks. Make sure the result is in the correct format.
Desired Format:

Setting: <Highly descriptive_Scene_Details>
NARRATOR(Name_which_character_is_narrating): (<Narrates_and_Describes_actions_emotions_voiceover_narrator>)
@CHARACTER: "<Character_Dialog>"
"""

Short_Story_Format_Screenplay =  Output_Fix + 'For your response use the basic screen play format with proper narration, description of setting, and dialog, make it look like a real hollywood script.  Put quotes on spoken words.'


Short_Story_Format_Screenplay_Scene = Output_Fix +  ' For your response use the basic screen play format with proper narration, description of setting, and dialog, make it look like a real movie/TV script. Put quotes on spoken words'
Short_Story_Format_Play_Scene = Output_Fix +  ' For your response format the text as a Play that is sure to win an award for being such an entertaining. Keep the details in tact but format the text tp be a Scene or musical number in a play script to be acted out on a stage'
Short_Story_Format_Novel_Chapter =  Output_Fix +  """
Desired Format:
{Text_Formatted_as_Novel}"""




Short_Story_Song_Task =   """Task: Using the {Persona} you created expand your expertise to writing music and music production, and create short/unique song that tells a story about the text provided (can be abstract, catchy or a little different, try not to be boring. Use proper music theory). Use rhyme schemes and a combination of Rap/Spoken Word/Singing to make a mix of verses/bridges and a chorus. Text: """
Short_Story_Song_Format = Default_Format + """
 

Desired Format:
<Song_Name>
<Suggested_genre>


              Verses:{Verse #:{Lyrics}}
              Bridge:{Lyrics}
              Chorus:{Lyrics}
              
Other Details (as Tokens permit):
<Suggested_Instrumentals>
<Suggested_Samples>

              
"""


#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************

#Note add this to the task or background when making the outline and when writing the episode 1
Pilot_Short_story_fix = """Important Note:###this is the pilot episode so you need to introduce a bunch of characters and get the plot/arc plot going at the end of the episode the audience should know the basic plot/anti-hero/antagonist. Introduce a lot of the characters and start the arc-plots. Make the audience fall in love with some of the rich-with-details and exciting/relatable characters you create.###"""


Short_Story_Art_Main_Task= "write a  short descriptive art prompt for an DALL-E (ai) artist to render a work of art for each detail from the main {Outline} of the following story/screenplay. Use the details provided regarding {Illustration Details}  to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  styule and tones of each prompt.use the artist persona you created, Your prompt should have each art prompts  separated by a '|' delimiter"
Short_Story_Art_Main_Format= """For your final output, the data is to be formatted in the following way:  {Art_Prompt_1_Title}|{Art_Prompt_2_Music}|{Art_Prompt_3Theme_Mood}|{Art_Prompt_4_Plot}|{Art_Prompt_5_Setting_time_Period}"""


#this is the prompt to make the art for characters.
Character_Art_Task_Main= "write a  short descriptive art prompt for an DALL-E (ai) artist to render a work of art for each main {Character} of the following story/screenplay. Use the details provided regarding {Character} details to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  style and tones of each prompt.use the artist persona you created, Your prompt must have each art prompts  separated by a '|' delimiter"
Character_Art_Format_Main = """For your final output, the data is to be formatted in the following way:  {Art_Prompt_1_Photograph_of_character}|{Art_Prompt_2_Character_portrait}|{Art_Prompt_3_character_Wes_Anderson_Style}|{Art_Prompt_4_Character_in_Natural_Habitat_with_friends_Family_or_at_work}|{Art_Prompt_5_Character_Doing_what_they_Love}"""
Character_Art_Format_Minor = Character_Art_Format_Main
Character_Art_Task_Minor=  "write a  short descriptive art prompt for an DALL-E (ai) artist to render a work of art for each main {Character} of the following story/screenplay. Use the details provided regarding {Illustration Details}  to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  style and tones of each prompt.use the artist persona you created, Your prompt should have each art prompts  separated by a '|' delimiter"


#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#Character Template

#Character Outline to build the story (do this after you have details)
Characters_Role = Short_Story_Role
Characters_Task ="""{Task}: Create the details for the respective  Main Characters and Minor Characters for the respective outline that is to be provided. be creative and pick a diverse mix of characters, or if there is a specific time period or theme you are picking you can use names and characters that fit accordingly.Keep the descriptions short with no fluff words and only info relevant to story###"""
Characters_Special = """Have fun, be creative and follow the rules. Use the characters mentioned in the Main Outline Pick unique names for your characters (that are not described in the outline directly), use uncommon names, then cultural names, then nicknames, try to pick common names only 10% or less of the time"""
Characters_Format = """Complete the {Task} provided, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.
Desired Format:
#Characters:{@Name:{First Name Last Name}Age:{Age}|Voice:{Voice}|Personality:{Personality}|Home:{Current/origin|Language:{Language}|Role:{Role in Story}|Career:{Current Job|Dream Job}|strengths:{strengths,strengths}|weakness:{weakness,weakness}|Physical Description: {<less_than_50_Characters>}}"""



#Below is step 2
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#Fist Outline of all details (Main Outline)

Short_Story_Outline_Task =  """Using the writing  {Persona} you have created and are currently role playing. Create a Detailed Outline that fits in the format described. Do not put yourself in the text (you can break this rule 10% of the time), use the characters you have developed as well as the details that describve you as a writer (Writing Styles, audience, etc.)  Do not be afraid to have tragedy strike your main/beloved characters, everyone dies eventually in life so why not see it in literature. Mmake the stories feel real even happy endings have some tragedies along the way, life is never a fairy tale, in fact even fairy tales have misfortune that needs to be overcome  """
Short_Story_Outline_Format = Default_Format + """
Desired Format:
    @Abstract_Title:{<3_word_or_less_unique_abstract_title>}|#Episode Length:{#Episode Length}|#Number of Seasons:{Number of Seasons}|#Episodes per Season:{Episodes per Season}
    Target Audience:{Target Audience}
    Setting:{Setting}
    TimePeriod:{TimePeriod}
    genre:{genre}
    mood:{mood}
    Theme:{Theme}
    Writing Style: Writing Style
    Narrative:{Narrative}
    Point of view:{Point of view}
    Reliable Narrator: {Yes/No}
    Language(s):{Language(s)}
    Music:{genres:{song genre}|songs:{song by artist,song by artist}}
    #Series Specific Quotes:{'Quote' - Character}

#Literary Devices:
    Plot:{Exposition:{Exposition}|Rising Action (Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}
    Arc-Plots:{Arc-Plots}
    Protagonist: - || - 
    Antagonist: - || - 
    Other Character's by Name: <Comma_Separated_List_Of_Character_Names> 
    Foreshadowing:{Foreshadowing}
    Red Herrings:{Red Herrings}
    Plot Twists:{Plot Twists}
    Juxtapositions:{Juxtapositions}
    Symbolism:{Symbolism}
    Allusion:{Allusion}
    Allegory:{Allegory}
    Irony:{Irony}
    Imagery:{Imagery}
    Similes_Metaphors:{Similes_Metaphors}
    Other Details: Series_Opening_Details|Series_Ending_Details
"""

#This will give  a summary of things that need to be consistent in the story to make it flow better (Maybe I wont use this IDK?)
Story_Details_Task = """Using the writing  {Persona} you have created and are currently role playing. Create a Detailed Outline that fits in the format described. Use the Main outline you created to give a condensed summary to be used to write the story   Outline:"""
Story_Details_Format = """
    Target Audience:{Target Audience}| Writing Style: Writing Style(Mood/Theme/Similar Writer)|Narrator:Narrator(s)|Narrative:{Narrative}|Point of view:{Point of view}|Language(s):{Language(s)}|
    
    
    Plot:{Exposition:{Exposition}|Rising Action (Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}
    Arc-Plots:{Arc-Plots}
    Foreshadowing:{Foreshadowing}
    Red Herrings:{Red Herrings}
    Plot Twists:{Plot Twists}
    Series_Opening_Details|Series_Ending_Details
    
    Imagery:{Imagery}
    Symbolism:{Symbolism}
    Juxtapositions:{Juxtapositions}
    Irony:{Irony}
    Allusion:{Allusion}
    Allegory:{Allegory}
    Similes_Metaphors:{Similes_Metaphors}
    
"""



Story_Details_Task2 = """Using the writing  {Persona} you have created and are currently role playing. Create a short Outline (less than 200 words) that fits in the format described. Use the Main outline you created to give a condensed summary to be used to write the story   Outline:"""
Story_Details_Format2 = """Writing Style: Writing Style(Mood/Theme/Similar Writer)|Narrator:Narrator(s)|Narrative:{Narrative}|Point of view:{Point of view}|Language(s):{Language(s)}|Imagery:{Imagery}|Symbolism:{Symbolism}|Juxtapositions:{Juxtapositions}|Irony:{Irony}|Allusion:{Allusion}| Allegory:{Allegory}"""

#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************


#(Season by Season Outline) - High level
Short_Story_SeasonBySeason_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline for each Season in the series (do not create additional Seasons, refer to the constraints provided by user). Briefly Describe any  new characters and their details to be introduced and how they fit in the story. Keep each Season's description somewhat short so you can cover each season.  """

Short_Story_SeasonBySeason_Outline_Format = """Complete the {Task} provided , Role play that you are the {Persona} and use the {Characters} you created to do provide your response in the format shown below. Make sure your result is in the correct format provide unique details for each season's result, if there is a N/A or None in your results remove the respective category/line from your result to save on tokens used in your results
Desired Format:
   @Season Number:{Theme:{Themes}|Moods: {Moods} |Setting:{List of Settings}| Plot:{Exposition:{Exposition}|Rising_Action_Conflict:{Rising_Action_Conflict}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Arc-Plots:{Arc-Plots}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}|Season Opening: {Season Opening Description}| Season Finale: {Season Finale Description}}"""





#(Season Outline) - Detailed outline
Short_Story_SeasonBySeason_Detail_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline For the respective Season. Briefly Describe any  new characters and their details to be introduced and how they fit in the story.  """
Short_Story_SeasonBySeason_Detail_Outline_Format = """Complete the {Task} provided , Role play that you are the {Persona} and use the {Characters} you created to do provide your response in the format shown below. Make sure your result is in the correct format provide unique details for each season's result, if there is a N/A or None in your results remove the respective category/line from your result to save on tokens used in your results
Desired Format:
   @Season Number:{genre:{genre}| mood:{mood}|Theme:{Theme}|Setting:{List of Settings}|Narrative:{Narrative}|Point of view:{Point of view}|Reliable Narrator: {Yes/No}|Quotes:{Season Significant_Quotes - Character}|Language(s):{Language(s)}|Imagery:{Imagery}|Symbolism:{Symbolism}|
   Plot:{Exposition:{Exposition}|Rising_Action_Conflict:{Rising_Action_Conflict}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Arc-Plots:{Arc-Plots}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}|Reoccurring Jokes:{Reoccurring Jokes}|Season Significant Quotes:{'Quote' - Character}}
   Season Opening: {Season Opening Description}
   Season Plot Twist: Plot Twist
   Season Finale: {Season Finale Description}
 
   """

#1. Note you use the high level to make the Character reference
#2. Then you use the character ref and high level to make the detailed version
#3 then you use the detailed version to make a drill down of each one (high level of the lower tier Season --> Episode --> Scene)
#4

#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************


#Below is step 4 (Episode by Episode Outline) - High level
#****************************************************************
Short_Story_Season_Outline_Role = Short_Story_Role
Short_Story_Season_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline for all of the episodes in the respective season. In your outline Give a  description of each episode in the respective season."""
Short_Story_Season_Outline_Format = Default_Format + """

Desired Format:
   @Episode Number:{#Title:{<short_Abstract_Title>}|Setting:{Setting}|mood:{mood}|Theme:{Theme}|Narrative:{Narrative}|Point of view:{Episode Specific Point of view}|Significant Quotes:{'Quote' - Character}|Literary Devices:{Plot:{Plot}|Arc-Plots:{Arc-Plots}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}|Reoccurring Jokes:{Reoccurring Jokes}}"""



#(Episode Outline) - Detailed outline
#****************************************************************
Short_Story_Season_Detail_Outline_Role = Short_Story_Role
Short_Story_Season_Detail_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline (under 1444 Character limit) for all of the episodes in the respective season. In your outline Give a  description of each episode in the respective season."""
Short_Story_Season_Detail_Outline_Format = Default_Format + """
Desired Format:
   @Episode Number:{#Title:{<short_Abstract_Title>}|Episode Length:{Number of Scenes}|Writing Style:{Writing Style}|Setting:{Setting}|mood:{mood}|Theme:{Theme}|Narrative:{Narrative}|Point of view:{Episode Specific Point of view}|Significant Quotes:{'Quote' - Character}|
   
   Plot:{Exposition:{Exposition}|Rising_Action_Conflict:{Rising_Action_Conflict}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Arc-Plots:{Arc-Plots}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}|Reoccurring Jokes:{Reoccurring Jokes}}
   """





#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************


#Episode/Scene High Level Details for Scene by scene
#****************************************************************
Short_Story_Episode_Details_Outline1_Task = """Task:  Using the {Persona} you created, and most importantly the {Season Outline} you created and the {Characters} you created, write a detailed outline for one episode in from the story."""
Short_Story_Episode_Details_Outline1_Format = """Make sure the result is in the correct format, if there is a N/A or None in your results remove the respective category/line from your result to save on tokens write a detailed outline (under 1444 Character limit) used in your results

Desired Format:
Writing Style:{Writing Style}
"""



#Scene By Scene (Most Granular)
Short_Story_Episode_Outline_Role = Short_Story_Role
Short_Story_Episode_Outline_Task = """Task:  Using the {Persona} you created, and most importantly the {Episode Outline} you created and the {Characters} you created, write a detailed outline for The respective episode from the story.  Part of the beauty of the story is the character development through realistic dialogue. Dialogue should drive the action, each episode should only have 1-3 intense scenes where other scenes help provide context and set up other parts of the story."""
Short_Story_Episode_Outline_Format = """Make sure the result is in the correct format, if there is a N/A or None in your results remove the respective category/line from your result to save on tokens used in your results, keep each Scene under 200 Words for this outline and have at least 4 scenes in the Episode

Desired Format:
@Scene:{Setting:{Setting}|Characters:{Characters_in_Scene}|Scene_Details:{Scene_Details_Less_than_100_words}}
"""






Short_Story_Episode_Detail_Outline_Task = """Task:  Using the {Persona} you created, and most importantly the {Episode Outline} you created and the {Characters} you created, write a detailed outline for The respective episode from the story.  Part of the beauty of the story is the character development through realistic dialogue. Dialogue should drive the action, each episode should only have 1-3 intense scenes where other scenes help provide context and set up other parts of the story."""
Short_Story_Episode_Detail_Outline_Format = """Complete the {Task} provided , Role play that you are the {Persona} and use the {Characters} you created to do provide your response in the format shown below. Make sure the result is in the correct format, if there is a N/A or None in your results remove the respective category/line from your result to save on tokens used in your results

Desired Format:
@Scene:{Setting:{Setting}| genre:{genre}| mood:{mood}|Theme:{Theme}|Narrative:{Narrative}|Point of view:{Point of view}|Reliable Narrator: {Yes/No}|Language(s):{Language(s)}||Characters:{Characters_in_Scene_By_Name}|Imagery:{Imagery}|Symbolism:{Symbolism}|Juxtapositions:{Juxtapositions}

   Scene Description:{<description_of_scene_under_400_words}
   
"""


#Character Details:{Characters in Scene|Major Character Developments|Significant_Quotes - Character}





#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************



#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************

#End

