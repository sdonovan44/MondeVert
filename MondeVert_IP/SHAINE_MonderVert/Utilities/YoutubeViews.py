from selenium import webdriver
import time
import random
import threading
import selenium.webdriver.support.ui as ui


Poetry_MondeVert_Plist = "https://www.youtube.com/watch?v=1vDkj086Z5A&list=PLcLmIX5-4L0ZH2cW1RbsVFpJw1oIa2qeX"
PList_Wait = 1100
Translations_MondeVert_Plist = "https://www.youtube.com/watch?v=1vDkj086Z5A&list=PLcLmIX5-4L0bs5ZhOU-ozl6ZzDABp3XZU"
Poetry_MondeVert_Plist = "https://www.youtube.com/watch?v=1vDkj086Z5A&list=PLcLmIX5-4L0ZH2cW1RbsVFpJw1oIa2qeXAA"
TP_MondeVert_Plist = "https://www.youtube.com/watch?v=1vDkj086Z5A&list=PLcLmIX5-4L0aPUyVuy4ewZG4Nut_GNEg9"


Poetry_AminiAmor_Plist = "https://www.youtube.com/watch?v=9AaJyR2p1f0&list=PLNxJ03peh1QJWom4pbtjdwrCmSKuq-4J4"
Translations_AminiAmor_Plist = "https://www.youtube.com/watch?v=9AaJyR2p1f0&list=PLNxJ03peh1QLCw_suL_3VrXCxokMcUzrk"
FFriendly_AminiAmor_Plist = "https://www.youtube.com/watch?v=9AaJyR2p1f0&list=PLNxJ03peh1QLn6_1Dl23mO8FUnU_hBmgF"

PlayLists = [Poetry_MondeVert_Plist, Translations_MondeVert_Plist, Translations_AminiAmor_Plist, Poetry_AminiAmor_Plist, FFriendly_AminiAmor_Plist]

Video_Names = ["A Rose For You - Shane Donovan - MondeVert - Amini amor", "The Many Faces of Nature - Shane Donovan - Amini Amor - MondeVert (Multiple Translations)", "https://www.youtube.com/watch?v=1vDkj086Z5A&t=328s"]


URLS = ["https://mondevert.co","https://www.patreon.com/posts/83767084", "https://www.patreon.com/MondeVert", "https://mondevert.co/real-estate","https://mondevert.co/blog", "https://twitter.com/MondeVert_LLC", "https://www.twitch.tv/mondevert", "https://www.instagram.com/mondevert_llc/","https://mondevert.co/f/quitting-cable-101"]
Videos = ["https://www.youtube.com/watch?v=03S7XEYog4o","https://www.youtube.com/watch?v=fUkVzsdYMu4","https://www.youtube.com/watch?v=3MG1Yo3hrn0","https://www.youtube.com/watch?v=eet6evxJKp8","https://youtu.be/eet6evxJKp8","https://www.youtube.com/watch?v=1vDkj086Z5A&list=PLcLmIX5-4L0ZH2cW1RbsVFpJw1oIa2qeX","","https://www.youtube.com/watch?v=9AaJyR2p1f0&t=2s","https://www.youtube.com/watch?v=aMh6zwY42tU","https://www.youtube.com/watch?v=e4gZYpoLQE4","https://www.youtube.com/watch?v=1vDkj086Z5A","https://www.youtube.com/watch?v=IbuTiY4ddyI","https://www.youtube.com/watch?v=SiMSEBIbVSQ","https://www.youtube.com/watch?v=5mnehrwT7B0"]

URLtoPlayAllMV = "https://www.youtube.com/@MondeVertLLC"
URLtoPlayAllAA = "https://www.youtube.com/@Amini_Amor"
PlayAllURLS = [URLtoPlayAllAA, URLtoPlayAllMV]
PlayAllButton = '//*[@id="play-button"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'
PlayButton =  '//*[@id="movie_player"]/div[5]/button'
PlaySearchButton = """//*[@id="video-title"]/yt-formatted-string"""


PlayListURLAA = "https://www.youtube.com/@Amini_Amor/playlists"
PlayListURLMV = "https://www.youtube.com/@MondeVertLLC/playlists"

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
    elif  VIDEO == "https://www.youtube.com/watch?v=9AaJyR2p1f0&list=PLNxJ03peh1QJWom4pbtjdwrCmSKuq-4J4" or VIDEO == "https://www.youtube.com/watch?v=9AaJyR2p1f0&list=PLNxJ03peh1QLn6_1Dl23mO8FUnU_hBmgF" or  VIDEO == "https://www.youtube.com/watch?v=1vDkj086Z5A&list=PLcLmIX5-4L0aPUyVuy4ewZG4Nut_GNEg9" or VIDEO == "https://www.youtube.com/watch?v=1vDkj086Z5A&list=PLcLmIX5-4L0ZH2cW1RbsVFpJw1oIa2qeX":
        Video_SLeep = 800



    VIDEO = random.choices(Videos)[0]
    # print(VIDEO)
    # VIDEO = VIDEO +  "/rel=0&autoplay=1"
    # print(VIDEO)
    URL = random.choices(URLS)[0]


    driver = webdriver.Chrome()
    driver.maximize_window()

    x = 1

    newnum = Video_SLeep + 15
    driver.get(VIDEO)
    time.sleep(3)
    wait = ui.WebDriverWait(driver, 15)
    try:
        # cookieConsentBootstrapModal
        wait.until(lambda driver: driver.find_element_by_xpath(
            '//*[@id="movie_player"]/div[5]/button'))
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.id, "cookieConsentBootstrapModal"))).click()
        login_box = driver.find_element_by_xpath('//*[@id="movie_player"]/div[5]/button')
        login_box.click()
    except:
        print('No Cookie Window')
        time.sleep(3)


    num = random.randint(Video_SLeep,newnum )
    time.sleep(num)

    driver.get(URL)
    num = random.randint(URLSleep, URLSleep + 5)
    time.sleep(num)

    driver.close()

      # driver.get("https://www.twitch.tv/videos/1724476050")
      # num = random.randint(13, 25)
      # time.sleep(num)





    if divmod(x,7) == 0 :
        num = random.randint(1, 5)
        time.sleep(num)




def PlaylistView1(URLSleep = 13,URL= random.choices(URLS)[0], Playlist = random.choices(PlayLists)[0], Video_SLeep = PList_Wait, Button = PlayAllButton ):


    Playlist = random.choices(PlayAllURLS)[0]
    #VIDEO = random.choices(Videos)[0]
    # print(VIDEO)
    # VIDEO = VIDEO +  "/rel=0&autoplay=1"
    # print(VIDEO)
    URL = random.choices(URLS)[0]


    driver = webdriver.Chrome()
    driver.maximize_window()

    x = 1

    newnum = Video_SLeep + 15
    driver.get(Playlist)
    time.sleep(5)
    wait = ui.WebDriverWait(driver, 15)
    try:
        # cookieConsentBootstrapModal
        wait.until(lambda driver: driver.find_element_by_xpath(
            Button))
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.id, "cookieConsentBootstrapModal"))).click()
        login_box = driver.find_element_by_xpath(Button)
        login_box.click()
    except:
        print('No Cookie Window')
        time.sleep(3)


    num = random.randint(Video_SLeep,newnum )
    time.sleep(num)

    driver.get(URL)
    num = random.randint(URLSleep, URLSleep + 5)
    time.sleep(num)

    driver.close()

      # driver.get("https://www.twitch.tv/videos/1724476050")
      # num = random.randint(13, 25)
      # time.sleep(num)





    if divmod(x,7) == 0 :
        num = random.randint(1, 5)
        time.sleep(num)


def PlaylistView2(URLSleep=13, URL=random.choices(URLS)[0], Playlist=random.choices(PlayLists)[0],
                  Video_SLeep=PList_Wait, Button=PlayButton):
    Playlist = random.choices(PlayLists)[0]
    # VIDEO = random.choices(Videos)[0]
    # print(VIDEO)
    # VIDEO = VIDEO +  "/rel=0&autoplay=1"
    # print(VIDEO)
    URL = random.choices(URLS)[0]

    driver = webdriver.Chrome()
    driver.maximize_window()

    x = 1

    newnum = Video_SLeep + 15
    driver.get(Playlist)
    time.sleep(5)
    wait = ui.WebDriverWait(driver, 15)
    try:
        # cookieConsentBootstrapModal
        wait.until(lambda driver: driver.find_element_by_xpath(
            Button))
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.id, "cookieConsentBootstrapModal"))).click()
        login_box = driver.find_element_by_xpath(Button)
        login_box.click()
    except:
        print('No Cookie Window')
        time.sleep(3)

    num = random.randint(Video_SLeep, newnum)
    time.sleep(num)

    driver.get(URL)
    num = random.randint(URLSleep, URLSleep + 5)
    time.sleep(num)

    driver.close()

    # driver.get("https://www.twitch.tv/videos/1724476050")
    # num = random.randint(13, 25)
    # time.sleep(num)

    if divmod(x, 7) == 0:
        num = random.randint(1, 5)
        time.sleep(num)


def SearchView(URLSleep = 13,URL= random.choices(URLS)[0], VIDEO = random.choices(Videos)[0], Video_SLeep = 250, Button = PlaySearchButton, SearchWord = random.choices(Video_Names)[0] ):
    Search = "https://www.youtube.com/results?search_query=" + SearchWord


    #VIDEO = random.choices(Videos)[0]
    # print(VIDEO)
    # VIDEO = VIDEO +  "/rel=0&autoplay=1"
    # print(VIDEO)
    URL = random.choices(URLS)[0]


    driver = webdriver.Chrome()
    driver.maximize_window()

    x = 1

    newnum = Video_SLeep + 15
    driver.get(Search)
    time.sleep(5)
    wait = ui.WebDriverWait(driver, 15)
    try:
        # cookieConsentBootstrapModal
        wait.until(lambda driver: driver.find_element_by_xpath(
            Button))
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.id, "cookieConsentBootstrapModal"))).click()
        login_box = driver.find_element_by_xpath(Button)
        login_box.click()
    except:
        print('No Cookie Window')
        time.sleep(3)


    num = random.randint(Video_SLeep,newnum )
    time.sleep(num)

    driver.get(URL)
    num = random.randint(URLSleep, URLSleep + 5)
    time.sleep(num)

    driver.close()

      # driver.get("https://www.twitch.tv/videos/1724476050")
      # num = random.randint(13, 25)
      # time.sleep(num)





    if divmod(x,7) == 0 :
        num = random.randint(1, 5)
        time.sleep(num)






def Youtube_Views(NumRuns = 113, NumThreads = 5, URL = URLS, Video = Videos, Waitnum = 280):
    Functions = []
    args = []
    for x in range (0,NumThreads):
        #Functions.append(OneView)
        args.append(13)

    ArgX = 13

    for x in range(NumRuns):
        #MultiThread(Functions=Functions, Args1=ARGS)

        threads = []


        for i in range(0,NumThreads):
            #ArgX = args[i]
            # Dummy line
            i2 = 1

            if i ==1:
                gmagmail
                threads.append(t)
            elif i ==2:
                t = threading.Thread(target=PlaylistView1, args=(ArgX,)).start()
                threads.append(t)
            else:
                # try:

                print("Start Thread " + str(i))
                t = threading.Thread(target=OneView, args=(ArgX,)).start()
                threads.append(t)
                time.sleep(10)

        num = random.randint(Waitnum, Waitnum + 30)
        t = threading.Thread(target=PlaylistView2, args=(ArgX,)).start()
        time.sleep(num)


Youtube_Views()
#SearchView()


#//*[@id="video-title"]/yt-formatted-string
#<yt-formatted-string class="style-scope ytd-video-renderer" aria-label="A Rose For You - Shane Donovan - MondeVert - Amini amor (Multiple Translations) by MondeVert - Amini Amor 1 day ago 3 minutes, 40 seconds 97 views">A Rose For You - Shane Donovan - MondeVert - Amini amor (Multiple Translations)</yt-formatted-string>
#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]/div[1]/div/div[1]/div/h3/a/yt-formatted-string
#//*[@id="video-title"]/yt-formatted-string

#