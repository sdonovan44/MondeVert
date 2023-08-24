
Default_Format = """Make sure the result is in the correct format, if there is a N/A or None in your results remove the respective category/line from your result to save on tokens used in your results"""


Music_Role = """You are an expert writer master of all genres of music,poetry, screenplays, novels, short stories, and music production. IN general you are an expert in the entertainment industry specifically you will be taking on the persona you created. Be a master of lyric writing and music theory, also anything else I tell you to be"""

Title_Format = Default_Format + """
Desired Format:
@Title
"""


StoryArt = "Come up with a short prompt [less than 250 characters] to for an artist to render a work of art Based on the respective style/details/and content of the text provided.  Make the prompt concise and easy for the artist to interpret, use the following text as your subject Text:  "
artDetailsPrompt =  "Come up with specific details that is related(or would be a good style match-up) to the symbolism/tone/context of the following text   Text:  "
artDetailsFormat = Default_Format + """keep your response concise no more than 100 characters.

Desired Format:
Similar Artist and Details: <Artist that art is similar to>,<Art_Style> <Tone>, <Colors> """

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



Output_Fix = "Do not put a 'CHARACTER DETAILS:' section or 'Note:' section in the output/result"

#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
## User Config type things and also prework like characters

Short_Story_Role = """role play that you are an award winning writer and director with all the talents neccesary to make a succesful screenplay/audio book that is exciting and draws the audience for more and more"""
Short_Story_Special = """Have fun, be creative and follow the rules. It is imperative that you understand that You are currently writing the story/screenplay using the information  I provided  for Episode #:"""
Short_Story_Task = """Task: Using the {Persona} you created, and specifically the {Episode Outline} you created with the the {Characters} you created as reference, write an entertaining screenplay based on the information I provide you. The story should read like a screenplay.  We want the audience to be hooked by the story and it should be relatable but also drive the reader in.The Story should read like an award winning ScreenPlay  {Detailed Outline}:"""
Short_Story_Task2 = """Task: Using the {Persona} you created, and specifically the {Detailed Outline} you've been provided, write a Scene for the respective screen play/Story The story should be exciting but also feel realistic and not rushed.  We want the audience to be hooked by the story and it should be relatable but also drive the reader in.The Story should read like an award winning ScreenPlay  {Detailed Outline}: """
Short_Story_Task_Novel_Chapter =   """Task: Using the {Persona} you created, and specifically the {Detailed Outline} you've been provided, write a scene for the respective screenplay/Story The story should be exciting but also feel realistic and not rushed.  We want the audience to be hooked by the story and it should be relatable in order to  drive the reader in. The Story should read like an award winning Novel. Do not mention episodes/Seasons, Use the respective Outline to make a continuous story (follow the outline for reference).   {Detailed Outline}: """
Short_Story_Task_Play_Scene =   """Task: Using the {Persona} you created, and specifically the {Detailed Outline} you've been provided, write a scene for the respective screen play/Story The story should be exciting but also feel realistic and not rushed.  We want the audience to be hooked by the story and it should be relatable but also drive the reader in.The Story should read like an award winning Play/Musical (and/or Script) {Detailed Outline}: """

#For the results, you should format the text as a screen play where the Narrator is written like one of the characters named 'NARRATOR'. The Narrator will say the non verbal words from the text, for example the mood, the actions happening, the scenery, the smells etc. anything not spoken should be 'spoken' by the NARRATOR.  All of the Narrator non-verbal parts should be in parenthesis so the reader knows it is not being spoken aloud.

Short_Story_Format = """Complete the {Task} provided , use the {Persona} and {Scene Outline} you created to do all of the tasks. Make sure the result is in the correct format.
Desired Format:

Setting: <Highly descriptive_Scene_Details>
NARRATOR(Name_which_character_is_narrating): (<Narrates_and_Describes_actions_emotions_voiceover_narrator>)
@CHARACTER: "<Character_Dialog>"
"""

Short_Story_Format_Screenplay = 'For your response use the basic screen play format with proper narration, description of setting, and dialog, make it look like a real hollywood script.'


Short_Story_Format_Screenplay_Scene = Output_Fix + ' For your response use the basic screen play format with proper narration, description of setting, and dialog, make it look like a real movie/TV script.'
Short_Story_Format_Play_Scene = Output_Fix + ' For your response format the text as a Play that is sure to win an award for being such an entertaining and uniquely surprising play. Keep the details in tact but format it like a Short Scene or number in a play script to be acted out on a stage'
Short_Story_Format_Novel_Chapter = Default_Format + Output_Fix + """
Desired Format:
Story: {Text_Formatted_as_Novel}

{To be continued/The End}
"""




Short_Story_Song_Task =   """Task: Using the {Persona} you created, and specifically the {Scene Outline} you created come up with a unique short song that describes the story/scene as outlined. Use rhyme schemes and a combination of Rap/Spoken Word/Singing to make a mix of verses/bridges and a chorus."""
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
<Suggested_tempo>
<Suggested_Key>
<Rhyme_Schemes>
<Ad_Libs_and_one_liner_for_Background>
              
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
Characters_Task ="""{Task}: Create the details for the respective  Main Characters and Minor Characters for the respective outline that is to be provided. be creative and pick a diverse mix of characters, or if there is a specific time period or theme you are picking you can use names and characters that fit accordingly. Use the {Persona} you created to come up with the inspiration###"""
Characters_Special = """Have fun, be creative and follow the rules. Use the characters mentioned in the Main Outline Pick unique names for your characters (that are not described in the outline directly), use uncommon names, then cultural names, then nicknames, try to pick common names only 10% or less of the time"""
Characters_Format = """Complete the {Task} provided, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.
Desired Format:
#Characters:{@Name:{First Name Last Name}Age:{Age}|Voice:{Voice}|Personality:{Personality}|Home:{Current/origin|Language:{Language}|Role:{Start of show|End of Show}|Career:{Current Job|Dream Job}|strengths:{strengths,strengths}|weakness:{weakness,weakness}|Physical Description: {<less_than_50_Characters>}"""


#Character Outline to build the story (do this after you have details)
Characters_Role = Short_Story_Role


Characters_Task ="""{Task}: Create the a brief description of the relevant characters in the given text based on the Character Description Provided. This should be less than 150 words if possible Character Description: """
Characters_Task_Fine = """ Use the following Text to pick the relevant characters, only pick the relevant characters """
Characters_Format_Fine = Default_Format + """
Desired Format:
#Characters:{@Name|Protagonist/Antagonist/Unknown/relationship to protagonist|How they move the plot forward}"""

Characters_Update_Task ="""{Task}: Update the details for the respective  Main Characters and Minor Characters (Add details for new main characters and significant character development) based on the text that is to be provided.  Text:"""
Characters_Update_Format = """Complete the {Task} provided, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.
Desired Format:
#Characters:{@Name:{First Name Last Name}Age:{Age}|Voice:{Voice}|Personality:{Personality}|Role:{Role in the Story}|Career:{Current Job}|strengths:{strengths,strengths}|weakness:{weakness,weakness}|Physical Description: {<less_than_50_Characters>}|Status in Story: Status (Dead/Alive/Presumed Dead/Missing/Hurt}"""



#Below is step 2
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************************************************************************
#Fist Outline of all details (Main Outline)
Shane_Test_User_Input = """Be entertaining, draw the audience in and make them feel a mix of emotions that make a great performance. """

Short_Story_Config = """The following Instruction from user must be followed, Instruction: ###"""
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
Short_Story_SeasonBySeason_Outline_Task = """Task: ### Using  the {Outline} you created and the {Characters} you created, write a detailed outline for each Season in the series (do not create additional Seasons, refer to the constraints provided by user). Briefly Describe any  new characters and their details to be introduced and how they fit in the story.  """

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
@Scene:{Setting:{Setting}|Characters:{Characters_in_Scene}|Scene_Details:{Scene_Details_Less_than_100_words}|Significant Quotes for this Scene (Vary them up, do not repeat):{'Quote' - Character}}
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

