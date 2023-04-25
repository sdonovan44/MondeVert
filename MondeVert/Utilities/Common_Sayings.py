import pandas as pd
import random
#eventually make the timne

#Greetings = ['Yo Yo whats Gucci Shane D?', 'Ugh, Hey Man, hows it going?', 'Buddy the elf whats your favorite color?','yOU AGAIN!', 'wELL wELL wELLERTONS','yellllow its your virtual assistant my dude']
#Greetings = ["Hi there", "Hey", "Howdy", "Greetings", "Salutations", "Hiya", "Hello there", "Yo", "What's up", "How are you", "Good morning", "Good afternoon", "Good evening", "How's it going", "Hey there", "Hi there!", "Hey there!", "Good day", "Howdy-doody", "Hi-ya", "Hola", "Bonjour", "Hey-yo", "Ahoy", "How's everything", "Hey-oh", "How's life", "What's new", "How's it hanging", "What's shaking", "Howdy-do", "Howdy-ho", "Hi-de-ho", "Hi-dee-ho", "Hi ho", "Hi-diddly-ho", "Hi-diddly-dee", "Hi-diddly-doo", "Hi-dee-do", "Hi-dee-dee", "Hi-dee-doo", "Hey y'all", "Hi-ya-all", "Hi-ya-ya", "Hi-ya-yo", "Hi-ya-do", "Hi-ya-dee", "Hi-ya-doo", "Hi-ya-ho", "Hey-o", "How's tricks", "Howdy-doo", "Howdy-hey", "Hey-diddle-diddle", "Hey-diddle-dee", "Hey-diddle-do", "Hey-diddle-ho", "Hey-diddle-yo", "Hey-diddle-doo", "Howdy-diddle", "Howdy-dee", "Hey-diddly-dee", "Hey-diddly-doo", "Hey-diddly-ho", "Hey-diddly-yo", "Hey-diddly-diddle", "Hey-diddly-hey", "Hi-diddly-yo", "Hi-diddly-diddle", "Hi-diddly-hey", "Hey-doodly-dee", "Hey-doodly-doo", "Hey-doodly-ho", "Hey-doodly-yo", "Hey-doodly-diddle", "Hey-doodly-hey", "Howdy-doodly-dee", "Howdy-doodly-doo", "Howdy-doodly-ho", "Howdy-doodly-yo", "Howdy-doodly-diddle", "Howdy-doodly-hey", "Hey-doodle-dee", "Hey-doodle-doo", "Hey-doodle-ho", "Hey-doodle-yo", "Hey-doodle-diddle", "Hey-doodle-hey", "Hi-doodle-dee", "Hi-doodle-doo", "Hi-doodle-ho", "Hi-doodle-yo", "Hi-doodle-diddle", "Hi-doodle-hey", "Howdy-doodle-dee", "Howdy-doodle-doo", "Howdy-doodle-ho", "Howdy-doodle-yo", "Howdy-doodle-diddle", "Howdy-doodle-hey", "Welcome", "Hiya-ho", "Hiya-dee", "Hiya-doo", "Hiya-yo", "Hiya-diddle", "Hiya-hey", "Hey-ya-ho", "Hey-ya-dee", "Hey-ya-doo", "Hey-ya-yo", "Hey-ya-diddle", "Hey-ya-hey", "Howdy-ya-ho", "Howdy-ya-dee", "Howdy-ya-doo", "Howdy-ya-yo", "Howdy-ya-diddle", "Howdy-ya-hey", "Hi-ya-diddle", "Hi-ya-hey", "Hey-yo-ho", "Hey-yo-dee", "Hey-yo-doo", "Hey-yo-yo", "Hey-yo-diddle", "Hey-yo-hey", "Howdy-yo-ho", "Howdy-yo-dee", "Howdy-yo-doo", "Howdy-yo-yo", "Howdy-yo-diddle", "Howdy-yo-hey", "Hi-yo-ho", "Hi-yo-dee", "Hi-yo-doo", "Hi-yo-yo", "Hi-yo-diddle", "Hi-yo-hey", "Hey-y'all", "Hi-y'all", "Howdy-y'all", "Welcome!", "Glad to see you!", "What's going on?", "How have you been?", "How's it hanging?", "What's shakin'?", "Doc?", "Glad to have you here", "Good to see you", "Glad you're here", "Long time no see", "Great to see you", "Looking good!", "How have you been doing?", "Howdy-hoo", "Hi-hoo", "Hey-hoo", "Howdy-hoo-hoo", "Hi-hoo-hoo", "Hey-hoo-hoo", "Howdy-hoo-dee", "Hi-hoo-dee", "Hey-hoo-dee", "Howdy-hoo-doo", "Hi-hoo-doo", "Hey-hoo-doo", "Howdy-hoo-ho", "Hi-hoo-ho", "Hey-hoo-ho", "Howdy-hoo-yo", "Hi-hoo-yo", "Hey-hoo-yo", "Howdy-hoo-diddle", "Hi-hoo-diddle", "Hey-hoo-diddle", "Howdy-hoo-hey", "Hi-hoo-hey", "Hey-hoo-hey", "Hi-de-dee", "Hi-de-doo", "Hi-de-yo", "Hi-de-diddle", "Hi-de-hey", "Hey-de-dee", "Hey-de-doo", "Hey-de-ho", "Hey-de-yo", "Hey-de-diddle", "Hey-de-hey", "Howdy-de-dee", "Howdy-de-doo", "Howdy-de-ho", "Howdy-de-yo", "Howdy-de-diddle", "Howdy-de-hey", "Hi-do-dee", "Hi-do-doo", "Hi-do-ho", "Hi-do-yo", "Hi-do-diddle", "Hi-do-hey", "Hey-do-dee", "Hey-do-doo", "Hey-do-ho", "Hey-do-yo", "Hey-do-diddle", "Hey-do-hey", "Howdy-do-dee", "Howdy-do-doo", "Howdy-do-ho", "Howdy-do-yo", "Howdy-do-diddle", "Howdy-do-hey", "Hi-ho-dee", "Hi-ho-doo", "Hi-ho-ho", "Hi-ho-yo", "Hi-ho-diddle", "Hi-ho-hey", "Hey-ho-dee", "Hey-ho-doo", "Hey-ho-ho", "Hey-ho-yo", "Hey-ho-diddle", "Hey-ho-hey", "Howdy-ho-dee", "Howdy-ho-doo", "Howdy-ho-ho", "Howdy-ho-yo", "Howdy-ho-diddle", "Howdy-ho-hey", "Hi"]
Greetings = ["Hi there", "Hey", "Howdy", "Greetings", "Salutations", "Hiya", "Hello there", "Yo", "What's up", "How are you", "Good morning", "Good afternoon", "Good evening", "How's it going", "Hey there", "Hi there!", "Hey there!", "Good day", "Howdy-doody", "Hi-ya", "Hola", "Bonjour", "Hey-yo", "Ahoy", "How's everything", "Hey-oh", "How's life", "What's new", "How's it hanging", "What's shaking",  "Hi"]
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


