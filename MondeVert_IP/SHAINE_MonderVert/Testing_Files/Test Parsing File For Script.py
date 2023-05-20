import ChatGPT as GPT



def FixActorsLines_and_Action(FilePath):
    FilePath = r"A:\MondeVert Productions\SHAINE - MondeVert AI Assistant\AI Tasks\MondeVert_Audio_Video_Story\Echoes of the Heart_Miniseries.txt"
    with open(FilePath) as file:
        numlines = len(file.readlines())
        lines = file.readlines()
        for x in range (0,numlines):
            Text2Send = ''
            line = line[x]
            #re.sub(r'\([^)]*\)', '', filename)
            line = line.replace('(voiceover)','')
            line = line.replace('(in person)', '')
            line = line.replace('(on the phone)', '')
            line = line.replace('(INT)', 'Setting: The Scene is Inside ')
            line = line.replace('(EXT)', 'Setting: The Scene is Outside ')
            line = line.replace('(int)', 'Setting: The Scene is Inside ')
            line = line.replace('(ext)', 'Setting: The Scene is Outside ')
            line = line.replace('(CUT TO:)', 'CUT TO')
            line = line.replace('(CUT TO:)', 'CUT TO')
            line = line.replace('(FADE IN:)', 'FADE IN')
            line = line.replace('(Fade In:)', 'Fade In')
            line = line.replace('(FADE OUT:)', """FADE OUT
            
            
            """)
            line = line.replace('(Fade Out:)', """Fade Out
            
            
            
            
            .....
            """)

            if line[0] =='' or line[0] ==' ':
                ignore = True
            elif line[0:6] =='Episode' or line[0:6] =='EPISODE'
                Actor_Voice = 'Narrator'
                Actor_Lines = line
            elif ':' not in line:
                ignore = True
            elif 'Music:' or 'Setting:' in line:
                BlankLine = False
                Text2Send += line
                countConsecutive = 1
                while BlankLine ==False:
                    line2 = lines[x+countConsecutive]
                    if line2[0]!='' or line2[0]!=' ':
                        line = line+line2
                        countConsecutive+=1
                    else:
                        BlankLine= True

                Actor_Lines = GPT.MondeVert.Basic_GPT_Query(Line2_Role='You are an expert director and story board creator', Line4_Task=""" you are narrating a short story your task is to create the scene using the following information, if its music explain how the scenery is in juxtaposition or in sync with the music. For your reference here is the text:### """ + line + """###""", Line3_Format="Keep it short and sweet make it something that can be spoken in under 15 seconds, make it almost poetic, you can also say a quote that relates to the Text")
                Actor_Voice = 'Narrator'
                ignoreXFix = x+countConsecutive
            else:
                #this means it has to be someone speaking, and we already started to cover speaking
                ignore = True

            #Create 2 variables
            # -Actors_Line
            # -Actors_Voice