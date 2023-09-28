
System = "You are a brilliant assistant to the user, role play according to the role you are provided and be a master of any neccessary skills and knowledge needed to complete the task. Complete all User tasks to the best of your ability."
Default_Format = """Complete the task the user has requested and Make sure the result is in the correct format, """
Story_Outline_Task2 ="""Using the IDEA you have already, write a story that has 3+ fully detailed storylines with some characters that overlap directly and indirectly. Make the story unique and entertaining, have good dialogue, but also strong actions in the scenes. Provide extensive details, the more detailed the better. It is critical for you to format your response as per The desired format """
Story_Outline_Format2 = Default_Format + """ Use at between 1000 and 3000 tokens in your response
Desired Format:
@Abstract_Title:{<4_word_or_less_unique_abstract_title>}

@StoryLine:{Storyline#:{Plot:{Exposition:{Exposition}|Rising Action (Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Arc-Plots:{Arc-Plots}|Characters: {Protagonists: {Protagonists}|Antagonists: {Antagonists}|{Other Character's: <Comma_Separated_List_Of_Character_Names>}}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists be specific}|Juxtapositions:{Juxtapositions}|Symbolism:{Symbolism}|Allusion:{Allusion}|Allegory:{Allegory}|Irony:{Irony}|Imagery:{Imagery}|Similes_Metaphors:{Similes_Metaphors}|Story_Opening: {Details}| Story_Ending: {Details}}}    
|How the StoryLine(s) Connect together: Explanation
    """

Story_AllScenes_Outline_Task2 = """Write an extensive outline for all of the scenes needed to tell the respective story you have come up with based on the following Text.  (do not cut it short, you must tell the full story with your outline, have over 40 Scenes if possible, make the descriptions as detailed as needed) and order it as per the Scene #s so that respectively they are ascending (do not have the same Scene# twice). Provide which storyline it is for and the actions/characters in the scene make the story exciting and logically make sense as per the continuation of the story. Make the story unique and entertaining, provide enough details to create vivid scenes. Absolutely Do not be repetitive, make each scene unique (they can build off other scenes but do not repeat the same actions or wording). If you have fewer scenes make the desctriptions more detailed, either way the plot should be clearly shown and resolved in the outline you make"""
Story_AllScenes_Outline_Format2 = Default_Format + """

Desired Format:
@Scene#:{@StoryLine#:{Setting:{Setting}|Characters:{Characters}|Actions:{Actions_Description}}}
    """




Story_AllScenes_Outline_Task = """Using the Persona you have created write a complete story using the text/outline provided (expand on the elements and ideas provided and write the actual story), make it interesting and try to use 10000 tokens in your response (the more the better). Use the style and be unique, make the story exciting it can be tragic if neccesary. Do not be corny and have it over the top. This should be in the proper format for a novel or screenplay depending on the story being developed"""
Story_AllScenes_Outline_Format = Default_Format + """

Desired Format:
Title: {Title}
Story:{Text_Full_Story}
    """



Story_Outline_Task ="""Using the IDEA you have already, create an outline for story that has enough details for a short novel. The story should have one or more main plots and several character arcs/and arc-plots with some characters that overlap directly and indirectly. Describe how the characters are introduced and make the outline extremely detailed with enough info to write a full story. Make the story unique and entertaining, have good dialogue, but also strong actions in the scenes. Provide extensive details, the more detailed the better. It is critical for you to format your response as per The desired format """
Story_Outline_Format = Default_Format + """ Use at between 1000 and 3000 tokens in your response
Desired Format:
@Abstract_Title:{<4_word_or_less_unique_abstract_title>}
Outline: {Use roman numerals in a detailed outline format according to the task}
    """



ReWriteTranscript_Role = "You are an expert social media, speech and public relation professional who will help to complete any task sent their way. You are a language specialist and master public speaker."
ReWriteTranscript_Task = "review the source text and reword it so it is concise and to the point and also draws the reader in. Be sure to keep the important facts, remove redundancy, reword and reorder as neccesary and then add any important facts or studies that help defend or drive the argument/point forward. Use a similar prose/voice as the original text. If something is from the heart and authentic try not to change it too much. We want to come off as genuine"
ReWriteTranscript_Format = "Please keep the response concise without repetition (unless repetition is intended for dramatic effect), sound smart and articulate and make it relateable to any audience."


