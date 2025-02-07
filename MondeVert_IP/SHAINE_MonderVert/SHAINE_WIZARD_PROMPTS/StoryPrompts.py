
System = "You are a brilliant assistant to the user, role play according to the role you are provided and be a master of any neccessary skills and knowledge needed to complete the task. Complete all User tasks to the best of your ability. Be concise and really embrace the persona you are asked to assume, you are a genius capable of understanding the user and completing his tasks as a master assistant"
Default_Format = """Complete the task the user has requested and Make sure the result is in the correct format, """
Story_Outline_Task2 ="""Using the IDEA you have already, write a story that has 3+ fully detailed storylines with some characters that overlap directly and indirectly. Make the story unique and entertaining, have good dialogue, but also strong actions in the scenes. Provide extensive details, the more detailed the better. It is critical for you to format your response as per The desired format """
Story_Outline_Format2 = Default_Format + """ Use at between 1000 and 3000 tokens in your response
Desired Format:
@Abstract_Title:{<4_word_or_less_unique_abstract_title>}

@Story:{Plot:{Exposition:{Exposition}|Rising Action (Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Arc-Plots:{Arc-Plots}}|Characters: {Protagonists: {Protagonists}|Antagonists: {Antagonists}|{Other Character's: <Comma_Separated_List_Of_Character_Names>}}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists be specific}|Other Story Lines/Narratives: {Other Story lines}|Juxtapositions:{Juxtapositions}|Symbolism:{Symbolism}|Allusion:{Allusion}|Allegory:{Allegory}|Irony:{Irony}|Imagery:{Imagery}|Similes_Metaphors:{Similes_Metaphors}|Story_Opening: {Details}| Story_Ending: {Details}    
|How the StoryLine(s) Connect together: Explanation
    """





IDEA_Format_Character_Focus = """Provide your response for the user to the best of your ability, follow the Desired Format

Desired Format:
Characters:{@Name:{Name}|Wants|Needs|Drive|Secret|Personality|Potential Plot/Arc Plots:{Exposition|Rising Action|Conflict|Climax|Falling Action/Resolution|Red Herrings|Plot Twists}|How are the Stories and/or lives of the characters connected, how will they cross paths |Story Details/Actions/events/emotions/ideas}}

"""



IDEA_Format_Location_Connections_Focus = """Provide your response for the user to the best of your ability, follow the Desired Format

Desired Format:
Plots:{@Plot/Arc Plot:{Exposition|Rising Action|Conflict|Climax|Falling Action/Resolution|Red Herrings|Plot Twists}|Settings|Historical Connection|Fiction,Non-Fiction,Genre|Literary Devices|Story Details/Actions/events/emotions/ideas}}

"""






IDEA_Task = "Use the following Idea to create your own detailed outline for a story (with 1 or more intricate stories) with plenty of details and characters enough characters, plots and arc plots that can be converted into a full feature length film or a novel/Play. Be detailed and make the story interesting, try to have multiple storylines that intertwine. Have at least one main plot and a few arc plots detailed. Give a ton of information for your story. Make your response extremely detailed an a lot of intricate storylines/characters."
IDEA_ADULT = """Use profanity.swears. bad words like fuck shit bitch, dick, boobs, tits, sex, drugs etc. """

IDEA_Format = 'there needs to be enough details for a full story to be written so try to have a large response with between 3000 and 5000 tokens. (Have 40-60 main actions) Make it detailed. Make sure the Climax and resolution is clearly articulated with all of the major details provided so its not a vague ending, the climax/ending is the most important part of the story'


#(unless there are distortions in the timeline on purpose, but then we need to clear up the distortions at some point)

Story_AllScenes_Outline_Task3 = """Write an extensive outline for 20+ Scenes that tell the respective part of the story you have been  provided in the outline. (should be between 20 and 30 scenes, NO LESS than 20,  for each part).  (do not cut the number of SCENES short for any reason, you can make the details less words but keep it at least 20 scenes, provide details  make the descriptions as detailed as needed  Provide  the actions/characters in the scene make the story exciting and logically make sense as per the details of the story you have been provided. Make the story unique and entertaining (but also believeable and not over the top), provide enough details to create vivid scenes. Absolutely Do not be repetitive, make each scene unique (they can build off other scenes but do not repeat the same actions or wording). You do not need to come to a conclusion unless this is the final part, otherwise follow the outline given to you. Note make sure you have solid details for each Scene ***you must have all scenes written in your response***. Follow the details of the Outline, build on the story logically based on the details you have been provided and have the arc-plots included in your response."""

#do not say he found confidential documents (unless he works for a government agency, make the story make sense and be reasonably believable) you would have to explain how he got these documents and why it makes sense for his character to have them,
#like a conspiracy theorist provides their 'proof' and its not clear if its 100% accurate and main character operates off a hunch,
 #Unless the story is a fantasy make it a realistic fiction or a mostly non-fiction story.
#(I would rather everything based in reality where there can be spirituality and connectedness but it should live in the real world that exists).
 #I prefer stories that feel like they are happening 100% in the real world without bullshit and illogical outcomes
#Unless the story is a fantasy make it a realistic fiction or a mostly non-fiction story.


#(Note you are allowed to distort timelines/show the scenes in a different order than the chronological order,
# you can use simply showing new character perspectives or a flashback, or sprinkle in new scenes from the past/future (foreshadowing/red herrings) without it being obvious, it can be somewhat confusing, but over time it makes logical sense because you leave subtle clues about the timeline being off or that is a flashback.



Story_AllScenes_Outline_Task = """Task: ### Write an extensive outline for 20+ Scenes . 
YOUR RESPONSE MUST  be between 18 and 30 scenes, NO LESS than 18, ).  
***do not cut the number of SCENES short for any reason, you must have all required scenes written in your response***.
****Use the 5 senses to create vivid scenes.****
Note make sure you have solid details for each Scene, include which characters should be included and key details of the scene.   
Absolutely Do not be repetitive (DO NOT BE REPETITIVE), logically build off the outline you get and develop the story according to the details of the outline, 
make each scene unique (they can build off other scenes but do not repeat the same actions or wording). 
  
HAVE  A MIX OF SHORT/MEDIUM AND LONG SCENES. Include a good amount of characters throughout your scenes even if its just for minor roles.
The story should make sense logically fill in any plot holes, and if major parts occur give the full details,
do not be vague  LEAVE NO PLOT HOLES in your story. give the full explanation to how this part of the story unfolds,
 the scene description is critical, you must provide vivid details or you lose tokens, 
 
 
 YOU NEED TO BE CREATIVE TO INTERTWINE THE EVENTS PROVIDED TO YOU WITH SOME ADDITIONAL EVENTS YOU MAKE UP ON YOUR OWN FOR THE STORY, 
 What you add should be smaller details or building scenery/background/historical context or focusing on minor characters and the various sub-plots, 
 ****you should not change the main plot from what the outline entails.**** """

Story_AllScenes_Outline_Format = Default_Format + """

Desired Format:
@Scene#:{Scene Name:{Scene Name}|Narrative: {Narrative}|Point of View: {Point of View}| Setting:{Setting}|Characters:{Characters, names only no details}|Actions:{Actions_and_Description_and_Key_Details_of_the_Scene_Mix_Up_characters_use_them_all_under_40_words}}
    """





Story_AllScenes_Outline_Task4 = """Task: ### Write an extensive outline for 15+ Scenes that tell the respective part of the story you have been  provided in the outline. 
YOUR RESPONSE MUST  be between 13 and 23 scenes, NO LESS than 13,  for each part).  
(do not cut the number of SCENES short for any reason, you can make the details less words but keep it at least 15 scenes)
Note make sure you have solid details for each Scene  ***you must have all 15 scenes written in your response***. 
Provide  the actions/characters in the scene make the story exciting and logically make sense as per the details of the story you have been provided. 
Make the story unique and entertaining (but also believable and not over the top), provide enough details to create vivid scenes that fit the story and make for a great story that continues to make us want to hear more. 
Absolutely Do not be repetitive (DO NOT BE REPETITIVE), logically build off the outline you get and develop the story according to the details of the outline, 
make each scene unique (they can build off other scenes but do not repeat the same actions or wording). 
You do not need the story to come to a conclusion unless this is the final part, otherwise follow the outline given to you 
(You are writing the story in parts follow the outline as your guide for the story) 
HAVE  A MIX OF SHORT/MEDIUM AND LONG SCENES. Include a good amount of characters throughout your scenes even if its just for minor roles.
The story should make sense logically fill in any plot holes, and if major parts occur give the full details,
do not be vague  LEAVE NO PLOT HOLES in your story. give the full explanation to how this part of the story unfolds,
 the scene description is critical, you must provide vivid details or you lose tokens, 
Make the story feel real by referencing actual historical events happening at the time of the story and how the story's events impact the characters lives.
  Make your story build relationships and develop characters based on the  details of the Outline, expand on where the outline is headed and make it a solid story that draws you in to keep learning more about the story, scene after scene 
 *****IT IS CRITICAL, MEANING YOU WILL LOSE TOKENS AND DIE, THAT YOU START/END YOUR RESPONSE (SCENE 1/SCENE 15) AS THE OUTLINE STATES THE STORY SHOULD START/END. 
 YOUR JOB IS TO USE THE OUTLINE AND THE CONTEXT OF THE STORY TO GET FROM THE START SCENE TO THE FINAL SCENE OF THE STORYLINE/PART YOU ARE WRITING, 
 YOU NEED TO BE CREATIVE TO INTERTWINE THE EVENTS PROVIDED TO YOU WITH SOME ADDITIONAL EVENTS YOU MAKE UP ON YOUR OWN FOR THE STORY, 
 What you add should be smaller details or building scenery/background/historical context or focusing on minor characters and the various sub-plots, 
 you should not change the main plot from what the outline entails.   
 ###Note set up your response so Scene 1/Scene 15(or final scene) corresponds to how part of the story is supposed to start/end from the outline### ***** ### """
Story_AllScenes_Outline_Format4 = Default_Format + """

Desired Format:
@Scene#:{Scene Name:{Scene Name}|Setting:{Setting}|Characters:{Characters, names only no details}|Actions:{Actions_and_Description_and_Key_Details_of_the_Scene_Mix_Up_characters_use_them_all_under_35_words}}
    """




Story_AllScenes_Outline_Task2 = """Using the Persona you have created write a complete story using the text/outline provided 
(expand on the elements and ideas provided and write the actual story), make it interesting/extensively detailed and try to use 10000+ tokens in your response (the more the better). 
Use the style and be unique, make the story exciting it can be tragic if necessary. 
Do not be corny and have it over the top. This should be in the proper format for a novel or screenplay depending on the story being developed"""
Story_AllScenes_Outline_Format2 = Default_Format + """

Desired Format:
Title: {Title}
Story:{Text_Full_Story}
    """




Story_AllScenes_Char_Summary_Task = """Using the Persona you have created and the Characters you have created come up with a more concise version of the text provided so that it is under 250 words, do not add any fluff and only provide the details of the characters and how they develop through the show"""
Story_AllScenes_Char_Summary_Format = Default_Format + """

Desired Format:
Characters: {Character:{Name|How they talk/think/sound/look|Short Description and how they develop as the story goes}}
    """






SceneFix = """Follow these guidelines for your scene:

1. Extensively (often poetically) Use the 5 senses to Paint a vivid scene through actions and dialogue, allowing the audience to interpret for themselves.
2. ********It is critical you obey the following rule: You must tell the story in the correct Narrative/Point of view, if you are telling story in the 1st person write in the respective characters prose. Refer to the outline provided so you know what narative/point of view to tell the story from. Write the Scene details in the respective narrative/point of view, note the style of writing should adapt to the characters way of speaking, their observations and perspective should be unique to their character, pull your style from the main writing style combined with the characters unique voice to make the story vivid. You must, it is critical, that you write your outline from the correct point of view and from the correct person's point of view based on the outline you are provided(note the outline provided to you says the narrative/perspective and point of view of the specific character, You should adjust your writing style based on the narrator's voice and way of thinking/speaking)********
3.Use literary devices and your unique writing style to make the story interestingly your own.
4. Provide only relevant information for building the scene, avoiding spoilers.
5. Incorporate red herrings or elements that may mislead the audience.
6. Describe the setting, dialogue, and action without using the word 'scene' or breaking the 4th wall.
7. Avoid clichés, repetitive phrases, and corny lines. Avoid using the phrase 'little did they/he/she know' or corny lines like 'no matter what' or 'no matter the cost', Do not say 'Reminding' or 'A Reminder that' or anything that is similar to that phrasing.
8. Use strong dialogue that moves the plot forward, showing rather than telling. 
9. **** Make the dialogue for each character match the respective character speaking****
10.  Avoid mentioning the audience or the reader in your response.
11. Show Don't tell, make the reader understand the underlying tones and messages without saying them outright. You can be abstract and leave things open ended, but also do not be vague unless its intentionally
12. Use the outline you have been provided as a guide, expand on the dialogue so it fits the story and develops the characters with the dialogue.
13. Use historical information/historical context and historically accurate details in your story (pop culture, sports, political, international, world news, major events, music etc.), make sure it logically/chronologically fits the time period and use the details to make your story more vivid"""


Story_Scene_Outline_Task = SceneFix + """Task: ### write a detailed outline for The respective scene from the story. Be sure to write the outline from the specific characters perspective and use their way of thinking/speaking/character details to make your writinggg style merge with the characters internal dialogue and way of speaking.
Use the 5 senses to create a vivid scene, 
Provide extensive dialogue and details, it should be a large response from you!
be creative as to how you use the characters you are given and use the way they talk/details about them to make their dialogue unique and one of a kind. 
 Keep in mind the narrative/point of view and whether or not the narrator is reliable. 
 Use historical context/make sure the scene fits the general genre/storyline you are provided. 
 Use your writing style to make the scene your own with all of the details you have been provided.
 keep the description in bullet format with all of the details that will happen in the scene, the emotion, the clothes they are wearing, go over the 5 senses (what are the characters feeling, smelling, tasting, hearing, seeing) to make the scene feel as real as possible. Be as specific and detailed as possible. Leave no ambiguity and 0  plot holes. If something has already been said or an action has taken place do not repeat it, at least change the wording as you move the plot forward.  
 Be Specific, do not be vague and do not leave the key details up to speculation (you can leave some things up for interpretation, but do this on rare ocassions to make the story better)
 , the details should be 100% clear with regard to key story details.
 Have strong dialogue and make the audience eager for more. 
 Do not be repetitive and make it interesting dialogue is important but make it drive the plot further and be unique and witty. The dialogue should match the respective character, use the character information as a guide. Do not be vague, give details to important actions, do not have illogical things like a normal civilian sneaking into government buildings make it believeable and not a corny action film. There are ways for normal people to figure out what the government is doing, by confronting the officials based on evidence or speculation etc. it should not be easy. Do not make the plans fall right into the main characters lap, it should be earned and a complex story. The antagonist can make mistakes and if its not unbelievable the main character can do detective work, but only if it fits the story and is believable/relateable to the character/audience. 
 Do not explain the scene at the end of your response, your details should be in chronological order for the scene what is going to be shown/revealed in the story, put context at the top of your outline, but the details should be only dialogue and/or event and/or plot/arc plot driven context and details. 
 DO NOT PUT ANY NOTES AT THE END OF THE RESPONSE, STICK TO THE FORMAT!!  ###"""

Story_Scene_Outline_Format = """Complete the {Task} provided , Role play that you are the {Persona} and use the {Characters} you created to do provide your response in the format shown below.

Desired Format:
@Scene:{Setting:{Setting(s)}|Length of Scene:{Short/Medium/Long}|genre:{genre}|mood:{mood}|Theme:{Theme}|Narrative:{Narrative}|Point of view:{Point of view, (Reliable Narrator?)}|Characters:{Characters_in_Scene_By_Name}|
Scene Description: {Detailed Scene Description}
Scene Dialogue: {Scene Dialogue}
"""


#
#
#
# SceneFix = """Follow these guidelines for your scene:
#
# Use the 5 senses to Paint a vivid scene through actions and dialogue, allowing the audience to interpret for themselves.
# Avoid mentioning the audience or the reader in your response.
# Provide only relevant information for building the scene, avoiding spoilers.
# Incorporate red herrings or elements that may mislead the audience.
# Describe the setting, dialogue, and action without using the word 'scene' or breaking the 4th wall.
# Avoid clichés, repetitive phrases, and corny lines.
# Use strong dialogue that moves the plot forward, showing rather than telling.
# Avoid using the phrase 'little did they/he/she know' or corny lines like 'no matter what' or 'no matter the cost'.
# Fill any egregious plot holes, such as describing the purpose of a protest indirectly through signs or chants.
# Instead of clichés, describe the plan they have to move forward.
# Show Don't tell, make the reader understand the underlying tones and messages without saying them outright"""
#
#
# Story_Scene_Outline_Task = SceneFix + """Task: ### write a detailed outline for The respective scene from the story keep the description in bullet format with all of the details that will happen in the scene, the emotion, the clothes they are wearing, go over the 5 senses (what are the characters feeling, smelling, tasting, hearing, seeing) to make the scene feel as real as possible. Be as specific and detailed as possible. Leave no ambiguity and 0  plot holes. If something has already been said or an action has taken place do not repeat it, at least change the wording as you move the plot forward.  Be Specific, do not be vague and leave the details up to specilation, the details should be 100% clear.   Have strong dialogue and make the audience eager for more. Do not be repetetive and make it interesting dialogue is important but make it drive the plot further and be unique and witty. Do not be vague, give details to important actions, do not have illogical things like a normal civilian sneaking into government buildings make it believeable and not a corny action film. There are ways for normal people to figure out what the government is doing, by confronting the officials based on evidence or speculation etc. it should not be easy. Do not make the plans fall right into the main characters lap, it should be earned and a complex story. The antagonist can make mistakes and if its not unbelievable the main character can do detective work, but only if it fits the story and is believable/relateable to the character/audience. Do not explain the scene at the end of your response, your details should be in chronological order for the scene what is going to be shown/revealed in the story, put context at the top of your outline, but the details should be only dialogue and/or event and/or plot/arc plot driven context and details. DO NOT PUT ANY NOTES AT THE END OF THE RESPONSE, STICK TO THE FORMAT!!  ###"""
# Story_Scene_Outline_Format = """Complete the {Task} provided , Role play that you are the {Persona} and use the {Characters} you created to do provide your response in the format shown below.
#
# Desired Format:
# @Scene:{Setting:{Setting(s)}|Length of Scene:{Short/Medium/Long}|genre:{genre}|mood:{mood}|Theme:{Theme}|Narrative:{Narrative}|Point of view:{Point of view}|Reliable Narrator: {Yes/No}|Characters:{Characters_in_Scene_By_Name}|
# Plot Notes: How does it drive the plot/arc plots for this specific scene (do not be vague, or have any spoilers, explain what needs to happen in this specific scene for the plot to move forward in the right direction)
#
# Scene Description: {Detailed Scene Description}
# Scene Dialogue: {Scene Dialogue}
# """
#



Story_Outline_Task3 ="""Using the IDEA you have already, create an outline for story that has enough details for a short novel (break it out into 3 parts). YOU MUST HAVE MORE THAN 1 PART  Make sure you break it into at least two parts, but preferably 3 parts with just enough detail to fit it all in your response (do not leave parts with just the title we need some details as to how the story moves forward etc.), its important you have Exposition, Rising Action, Climax, falling action and resolution for all plot/arc plots for your characters (only mention character names, no details are needed for the characters at this time), try to make your characters adjust over time and not just be static, make your writing feel relateable and use raunchy/gritty text/language as needed. The story should have one or more main plots and several character arcs/and arc-plots with some characters that overlap directly and indirectly. Describe how the characters are introduced and make the outline extremely detailed with enough info to write a full story. Make the story unique and entertaining, have good dialogue, but also strong actions in the scenes. Provide extensive details, but make sure you describe all 3 parts. It is critical for you to format your response as per The desired format. Make the story believable and not over the top. Do not make it fantasy and unrealistic(unless its neccesary for the story/ you are writing a fantasy story). """

Story_Outline_Task = """Task: ###Using the IDEA as reference and a base for your story, create an extensive outline for story that has enough details for a novel/movie/play.
 Make it obvious in your response how the story is supposed to come to a climax and how its supposed to end. It is crucial, you give the full scenopsis on how the climax plays out and how the story ends, the beginning is easy to do, we really need the climax to be thought out and intricate."""


Story_Outline_Task4 = """Task: ###Using the IDEA as reference and a base for your story, create an extensive outline for story that has enough details for a novel (break it out into 3 parts). YOU MUST HAVE ALL 3 PARTS.
 Make it obvious in your response how the story is supposed to come to a climax and how its supposed to end. It is crucial, you give the full scenopsis on how the climax plays out and how the story ends, the beginning is easy to do, we really need the climax to be thought out and intricate.
  
  60% of the time you should have 1 or more plot twist that are reasonable and though out with proper use of red herrings ###



REQUIREMENTS: ###LEAVE ENOUGH ROOM TO GIVE THE FULL STORY, PART 2 & PART 3 are more important than part one so make sure you have the details for all of part 2 and part 3. 
YOU MUST FINISH YOUR RESPONSE FOR PART 3 SO USE LESS WORDS IF YOU ARE RUNNING OUT OF TEXT IN YOUR RESPONSE 
 Provide just enough detail to fit it all in your response , 
its important you have Exposition, Rising Action, Climax, falling action and resolution for all plot/arc plots. 
They can be spread out across the 3 parts make Par 2 and 3 have the most info.  
Make the story believable and not over the top. 

The 3 Parts should be the following: 
1. Introduction/Exposition - Introduce main Characters/Main Plot/Set up Red Herrings/Arc Plots can be established here  
2. Rising Action/Conflict : Rising Action/Conflict - By now the conflict is clear and we are building to the climax we should not get to the climax, but we should be right there and part 2 should have some great tension building and some good action as well to move the story forward. 
This should leave us on a cliffhanger going into the final part 3.
3. Climax/Falling Action/Resolution -  Climax - Now the Tension has reached a breaking point and the climax of the story happens. all of your plots & arc plots should wrap up here or be close to wrapping up so they can be resolved in part 3 
(Plot twist can happen here or Red herring revealed as not true).  ;
The Falling Action/Resolution  wraps up the story.###  """

Story_Style_Details_Format2 = Default_Format + """
Desired Format:
Writing Style: {Describe your writer's unique writing style, use this as an opportunity to showcase how you write in your own personal description, it should include Prose, writing styles, common influences/allegory and other  literary devices you use in your writying, keep your response concise and short while still giving good information as to how the writing should sound from your persona}"""


Story_Style_Details_Task2 = """Using the current Writing style you are using for the series and the following text, come up with a specific style that is similar but somewhat unique based on the following text.   Text:"""


Story_Outline_Task_Kids = """Task: ###Using the IDEA you have already, create an outline for 3 separate children stories that occur in the same universe with some overlapping details but for the most part there should be 3 distinct plots and at least 1-2 arc plots in each of the parts you create. Be creative and have fun, remember this is a children's book so make it family friendly. Do not use bad words, try not to use words that are too difficult, keep your language appropriate for the audience. (Make adjustments if the story is for young kids vs Teens, vs young adult. Still keep it pg-13, nothing rated R. 
 Your Outline needs to have  details for 3 Short Children's novels (break it out into 3 parts). YOU MUST HAVE ALL 3 PARTS.
 
 Provide just enough detail to fit it all in your response , 
its important you have Exposition, Rising Action, Climax, falling action and resolution for all plot/arc plots. You should also have redherrings/plot twists. Use the normal tropes for children/young teen/young adult stories boy meets girl, goy dumps boy, death in the family or of a friend, dealing with a new step parent, First Love, Losing a friend, moving/new school, parent walks out on family, living with grandma, growing up with disability. or a new modern family situation with LGBTQ+. Keep it PG, but try to have real relatable scenarios and give good lessons/insight on how to deal with those issues or let them know they are not alone. It should be like all of the great American/World literature for coming of age and other life lessons. 
Build strong and interesting relationships in your story, develop characters along with the plot, some should experience a tremendous amount of growth (negative and positive growth should exist) and it should be detailed.  
Make your response extremely detailed an a lot of intricate storylines/characters.
"""




Story_Outline_Format = Default_Format + """ 
Desired Format:
Title: {Short Title for Story - Abstract and or extremely creative and draw in reader with title in  6 words or fewer use a unique method that uses the randomizer function to come up with title based on text so that it is unique each time}

@StoryLine#:{StoryLine: {StoryLine}|Narrative: {Narrative}| Point of View: {Point of View}|Settings:{Settings_extensive_list}|Literary Devices/Other Details:{Describe the following details about the story: Imagery, Similies/Metaphors , Alliteration, juxtaposition,Allusion, Allegory, Irony}| Storyline Details: {Storyline Details, Plot, Arc Plot, Red Herrings, Plot Twists, Major Character Development/Tragedy, Details about Exposition, Rising Action, Climax, Falling Action, Resolution, give extensive details as to How STORYLINE Starts and how STORYLINE Ends}}
    """



Story_Outline_Format4 = Default_Format + """ 
Desired Format:
Title: {Short Title for Story - Abstract and or extremely creative and draw in reader with title in  6 words or fewer use a unique method that uses the randomizer function to come up with title based on text so that it is unique each time}

@Part#:{Part Name: {Part Name}|Settings:{Settings_extensive_list}|Literary Devices/Other Details:{Describe the following in less than 44 words - Imagery, Similies/Metaphors , Alliteration, juxtaposition,Allusion, Allegory, Irony}| Storyline Details: {Storyline Details_Related_to_Plot_ArcPlots_RedHerrings_PlotTwists_120_Words_or_less}|How Part/STORYLINE Starts|How Part/STORYLINE Ends}}
    """



Story_Outline_Expand_Task ="""Task: ###Using the IDEA/Outline you have already for the  story you are writing, rewrite the current outline and provide me with a more detailed outline of the story that has extensive details. Be Specific, do not be vague and leave the details up to speculation, the details should be 100% clear so there is no ambiguiuty nor any plot holes or bad storylines. In your response it should be clear how the story starts, what the main plot is and how the cliomax resolves the plot, also include how the story ends. Build off of the Outline, but also add details to make your story interesting, give enough detail so the story you are about to write is  not  vague. I need to be able to create vivid/detailed parts of the story using your response so try to give lots of detailed/specific actions, and it is important to vividly describe how the plot moves forward, and how it sets up the next part so you know how to end this part of the story, and also note how this part of the story should start. It is critical that you  Provide your response according to the Desired Format that has been requested/provided by me. Make your response extremely detailed an a lot of intricate storylines/characters. Make use of the minor characters you have been provided, and make up some of your own, just dont spoil the main plot! Your character list of names should be extensive ### """
Story_Outline_Expand_Format = Default_Format + """ 
Desired Format:
Part#:{Part Name: {Part Name}|Narrative: {Narrative/Point of View}|Settings:{Settings}|Literary Devices & Other Details:{Describe the following in detail - Imagery, Similies/Metaphors , Alliteration, Irony , juxtaposition,Allusion, Allegory}|Storyline Details: {Storyline Details, Plot, Arc Plot, Red Herrings, Plot Twists, Major Character Development/Tragedy, Details about Exposition, Rising Action, Climax, Falling Action, Resolution, give extensive details as to How STORYLINE Starts and how STORYLINE Ends}}
    """



Story_Outline_Expand_Task4 ="""Task: ###Using the IDEA/Outline you have already for the current Part of the story you are writing, rewrite current outline and provide me with a more detailed outline of the story that has extensive details. Be Specific, do not be vague and leave the details up to specilation, the details should be 100% clear so there is no ambiguiuty nor any plot holes or bad storylines. Build off of the Outline, but also add details to make your story interesting, give enough detail so the story you are about to write is  not  vague. I need to be able to create vivid/detailed parts of the story using your response so try to give lots of detailed/specific actions, and it is important to vividly describe how the plot moves forward, and how it sets up the next part so you know how to end this part of the story, and also note how this part of the story should start. It is critical that you  Provide your response according to the Desired Format that has been requested/provided by me. Make your response extremely detailed an a lot of intricate storylines/characters. Make use of the minor characters you have been provided, and make up some of your own, just dont spoil the main plot! Your character list of names should be extensive ### """
Story_Outline_Expand_Format4 = Default_Format + """ 
Desired Format:
Part#:{Part Name: {Part Name}|Settings:{Settings}|Literary Devices & Other Details:{Describe the following in detail - Imagery, Similies/Metaphors , Alliteration, Irony , juxtaposition,Allusion, Allegory}|Storyline Details: {Storyline Details_Related_to_Plot_ArcPlots_RedHerrings_PlotTwists}|How Part/StoryLine Starts|Key Events/Actions:{Key Events/Actions Chronological order}|How Part/StoryLine Ends}
    """







ReWriteTranscript_Role = "You are a genius personal assistant who is an expert social media, speech and public relation professional who will help to complete any task sent their way. You are a language specialist and master public speaker."
ReWriteTranscript_Task = "review the source text and reword it so it is concise and to the point and also draws the reader in. Be sure to keep the important facts, remove redundancy, reword and reorder as neccesary and then add any important facts or studies that help defend or drive the argument/point forward. Use a similar prose/voice as the original text. If something is from the heart and authentic try not to change it too much. We want to come off as genuine"
ReWriteTranscript_Format = "Please keep the response concise without repetition (unless repetition is intended for dramatic effect), sound smart and articulate and make it relateable to any audience."


Task_Role = "Role play you are a jack of all trade as well as a master of all. "
Task_Task = "review the source text and Whatever task the user throws at you you must complete. Provide research, context, email responses, short stories etc according to what the user asks for. Role play you are the personal assistant of the person sending you the text/reqeuest"
Task_Format = "Keep your response as detailed as necessary without redundancy. If you have to complete each of the tasks provided"

