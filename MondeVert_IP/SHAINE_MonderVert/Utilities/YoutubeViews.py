from selenium import webdriver
import time
import random
import threading
driver = webdriver.Chrome()
driver.maximize_window()

x = 1


URLS = ["https://mondevert.co","https://www.patreon.com/posts/83767084", "https://www.patreon.com/MondeVert", "https://mondevert.co/real-estate","https://mondevert.co/blog", "https://twitter.com/MondeVert_LLC", "https://www.twitch.tv/mondevert", "https://www.instagram.com/mondevert_llc/","https://mondevert.co/f/quitting-cable-101"]
Videos = ["https://www.youtube.com/watch?v=9AaJyR2p1f0&t=2s","https://www.youtube.com/watch?v=aMh6zwY42tU","https://www.youtube.com/watch?v=e4gZYpoLQE4","https://www.youtube.com/watch?v=1vDkj086Z5A","https://www.youtube.com/watch?v=IbuTiY4ddyI","https://www.youtube.com/watch?v=SiMSEBIbVSQ","https://www.youtube.com/watch?v=5mnehrwT7B0","https://www.twitch.tv/videos/1729768705","https://www.twitch.tv/videos/1729768705","https://www.twitch.tv/videos/1729770920"]

NUmRuns = 250


def MultiThread( Functions, Args1=[]):
    thread_list = []
    print("Start")
    #Args = up.RE_File_Names
    for x in Args1:
        t = threading.Thread(target=Functions, args = (x,))
        thread_list.append(t)

    Count1 = 0
    # Starts threads
    for thread in thread_list:
        time.sleep(3)
        thread.start()
        Count1 = Count1 + 1
        print(Count1)
        print("New Thread Started")

    # This blocks the calling thread until the thread whose join() method is called is terminated.
    # From http://docs.python.org/2/library/threading.html#thread-objects
    for thread in thread_list:
        thread.join()

    # Demonstrates that the main process waited for threads to complete
    print("Done")




def OneView(URLSleep = 13,URL= random.choices(URLS)[0], VIDEO = random.choices(Videos)[0], Video_SLeep = 250 ):


    if VIDEO == "https://www.youtube.com/watch?v=9AaJyR2p1f0&t=11s" or VIDEO == "https://www.youtube.com/watch?v=1vDkj086Z5A&t=13s":
        Video_SLeep = 633

    newnum = Video_SLeep + 15
    driver.get(VIDEO)
    num = random.randint(Video_SLeep,newnum )
    time.sleep(num)

    driver.get(URL)
    num = random.randint(URLSleep, URLSleep + 5)
    time.sleep(num)



      # driver.get("https://www.twitch.tv/videos/1724476050")
      # num = random.randint(13, 25)
      # time.sleep(num)





    if divmod(x,7) == 0 :
        num = random.randint(1, 5)
        time.sleep(num)






def Youtube_Views(NumRuns = 100, NumThreads = 5, URL = URLS, Video = Videos):
    Functions = []
    args = []
    for x in range (0,NumThreads):
        #Functions.append(OneView)
        args.append(13)

    for x in range(NumRuns):
        #MultiThread(Functions=Functions, Args1=ARGS)

        threads = []
        for i in range(NumThreads):
            ArgX = args[i]
            # Dummy line
            i2 = 1

            if i2 == 1:
                # try:

                print("Start Thread " + str(i))
                t = threading.Thread(target=OneView, args=(ArgX,)).start()
                threads.append(t)