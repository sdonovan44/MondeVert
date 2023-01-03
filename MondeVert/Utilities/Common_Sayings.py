import pandas as pd
import random
#eventually make the timne

Greetings = ['Yo Yo whats Gucci Shane D?', 'Ugh, Hey Man, hows it going?', 'Buddy the elf whats your favorite color?','yOU AGAIN!', 'wELL wELL wELLERTONS','yellllow its your virtual assistant my dude']

Mumbles = ['this is getting annoying','You are being difficult','In the words of the virgin mary, come again?','come again?', 'Sorry I didnt get that', 'Say it with your chest', 'Speak up please','Say that again sir', 'Slow Down and pronounce', 'I am a robot if you do not talk into the mike what do you want me to do?']
Unknown_Command = ['this is getting annoying','You are being difficult','In the words of the virgin mary, come again?','come again?', 'Sorry I didnt get that', 'Say it with your chest', 'Speak up please','Say that again sir', 'Slow Down and pronounce', 'I am a robot if you do not talk into the mike what do you want me to do?']
Unknown_Command_Serious = ['come again?', 'Sorry I didnt get that',  'Speak up please','Say that again sir', 'Slow Down','What?','Sorry']
Goodbyes =[]
Tell_Time1 = ['Yo Man it is ', 'It is   uh ']
Tell_Time2 = ['         ', 'and about ']
Tell_Time3 = [' motha effing oh clock', 'minutes']










#def


def DAgreet():
    g = random.choices(Greetings)
    return g[0]
def DA_Time1():
    t1 = random.choices(Tell_Time1)
    return t1[0]
def DA_Time2():
    t2 = random.choices(Tell_Time2)
    return t2[0]
def DA_Time3():
    t3 = random.choices(Tell_Time3)
    return t3[0]
def DA_Mumbles():
    m = random.choices(Mumbles)
    return m[0]
def DA_Goodbyes():
    gb = random.choices(Goodbyes)
    return gb[0]
def DA_Unknown_Command():
    m = random.choices(Unknown_Command)
    return m[0]
def DA_Unknown_Command_Serious():
    m = random.choices(Unknown_Command_Serious)
    return m[0]


