import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
global Record
import sys

from dir import Dir
import selenium

Record = ''
import webbrowser
#make a transcript class that takes down all of my requests and saves to a text file
#have specific command for the assistant to save in a certain folder (always add date & time to the file
#create things like to do lists
#ideas
#stories and dialogue
#the key is being able to store it properly and sytemically access as well
#every program I create should be executeable through the assistant



#Urgent to do
#Make it a class
#have transcribe and also proofread (later) add method where in the middle of dictating you can add titles so it gets properly makred eventually
# bullets etc. parenthesis
#Have it so every pause puts a new line in between so its easy to pull out pauses etc.
#Most important is to have a mode where it callse poembot and reads the lines to me.
# .... also I would like for it to be a mini drama where I get multiple voices and characters that read
# the output etc eventually learn how to animate/make a nice script.
# create a series so eventually we might have a way to feed in characters to poem bot so its not just random like it is now lol

#12/18/2022 get the assistant able to open the respective web browsers
#set up mouse so it has shortcuts
#be able to run on both mac and also the pc
#import the site view bot
#update the youtube bot so it hides ips properly and also so it loops through videos to not draw attention
#    (make it so it starts off slow then has pockets of 100 here and there big days occasionally and find out how to make it work properly
#have assistant able to run those on command (buy wifi adapter so I can have it running whenever & get new monitor for that too




def Open_Web(url):
    new = 2  # open in a new tab, if possible
    url = url
    # open a public URL, in this case, the webbrowser docs


    webbrowser.open_new_tab(url)
    #webbrowser.get(using='google-chrome').open(url,new=new)


def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.8
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
            #Record += ('** ' + Query)



        except Exception as e:
            print(e)
            speak("In the words of the virgin mary, come again?")
            #speak("come again?")
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio + "")

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    # This method will give the time
    time = str(datetime.datetime.now())

    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak( "Yo man it is " + hour + "motha effing " + min + "Minootoes.... cheeeeeeeil broh")


def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("Yo Yo whats Gucci Shane D?")


def Take_query():
    # calling the Hello function for
    # making it more interactive
    Hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while (True):






        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = takeCommand().lower()
        if "company dashboard" in query or "open dashboard" in query :
            speak("Opening MondDay Vert's Dasboard, good luck with your work!")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            Mondevert = "http://mondeVert.co"
            godaddy = 'https://dashboard.godaddy.com/'
            Mail = 'https://outlook.office.com/mail/'
            Square_store = 'https://square.online/app/home/'
            Open_Web(Mail)
            Open_Web(Square_store)
            Open_Web(Mondevert)
            Open_Web(godaddy)

            continue

        elif "pay bills" in query or "pay credit cards" in query:
            speak("Bills Suck man, at least you are getting them done, Hope you have a nice day!")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            Liberty_Bay_CC = "https://www.myaccountaccess.com/onlineCard/login.do"
            Home_Depot_CC = 'https://citiretailservices.citibankonline.com/RSnextgen/svc/launch/index.action?siteId=PLCN_HOMEDEPOT#signon'
            Macys_CC = 'https://www.macys.com/my-credit/gateway/guest'
            Insurance = 'https://customer.concordgroupinsurance.com/ccp/login'
            National_Grid = 'https://login.nationalgridus.com/loginnationalgridus.onmicrosoft.com/oauth2/v2.0/authorize?cancel_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauth%2Fsso%2FNGP_SignIn_MA_Electric_Home&client_id=88d004b4-3d39-4599-b410-093849907ee5&customer_type=home&p=B2C_1A_UWP_NationalGrid_convert_merge_signin&redirect_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fservices%2Fauthcallback%2FNGP_SignIn_MA_Electric_Home&region=masselec&response_type=code&scope=https%3A%2F%2Flogin.nationalgridus.com%2Fapi%2Fread+openid+profile+email+offline_access&state=CAAAAYUokN2YMDAwMDAwMDAwMDAwMDAwAAAA8Iy1JaCJ8hTkDIfqZ5i6KE2oIrQFv5bPH9zBI_P-5wWki9riiDhgLKrNlnVD4FeR38QBEzYH17vRm_CbsR8msY3J3fEDKFqtBsup_Bp9KwM-Flb38WYF6YqeqejsI-Iuj-yWpXfajw6-QKG_DMoOBtkqcL8zubs4c8KgKiuF-yIk3yoa1_vp_KqVAuBw0DSopTJrDwsYAZN5qW9zaUmwyW-wk6zbTNddqu24EJObkHkfEGKHEKQwrqArl40WukP3dxbKBfj7sSMhdqjTPa0ido8%3D&switch_uri=https%3A%2F%2Fmyaccount.nationalgrid.com%2Fs%2Flogin'
            LLBean_CC = 'https://citiretailservices.citibankonline.com/RSauth/signon?pageName=signon&siteId=PLCN_LLBEAN&langId=en_US'
            Amazon_CC = 'https://secure07ea.chase.com/web/auth/#/logon/logon/chaseOnline'

            Open_Web(Liberty_Bay_CC)
            Open_Web(Home_Depot_CC)
            Open_Web(Macys_CC)
            Open_Web(Insurance)
            Open_Web(National_Grid)
            Open_Web(LLBean_CC)
            Open_Web(Amazon_CC)
            continue



        elif "get poetic" in query or "swoon me" in query:
            speak()

            x = Dir.PoemBot(1, 1, 1, 1, 40, 3)
            x.ReloadModel()
            Words = x.shakesbot_DA()
            speak(Words)
            continue

        elif "social media" in query or "marketing" in query:
            speak("Woohoo, I know you hate social media but its how you get known! Ayyy oooohh")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            Facebook = "https://www.facebook.com/"
            Insta = 'https://www.instagram.com/'
            TikTok = 'https://www.tiktok.com/'
            Twitter = 'https://twitter.com/home'

            Open_Web(Facebook)
            Open_Web(TikTok)
            Open_Web(Twitter)
            Open_Web(Insta)
            continue


        elif "open google" in query:
            speak("Opening Google ")
            url = "http://google.com"
            Open_Web(url)
            continue

        elif "s the date" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        # this will exit and terminate the program
        elif "bye" in query:
            speak("Peace Out!")
            exit()

        elif "from wikipedia" in query:

            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "stop" in query or "all set" in query or "quit" in query or "m done" in query or  "thank" in query or  "peace out"  in query:
            speak("Happy to help, Peace out brothah man")
            sys.exit()

        elif "tell me your name" in query or  "your name" in query or "introduce yourself" in query or "introduce your self" in query:
            speak("I am Big Master Funk the fourth also known as Brick top, AND i AM  Your personal desktop Assistant")

        else:
            continue



        #
        # elif "shut up" in query:
        #     speak("my bad I am tripping, I will leave you be Shane D")
        #     sys.exit()


if __name__ == '__main__':
    # main method for executing
    # the functions
    Record = ''
    Take_query()
