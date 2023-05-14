import os
import sys
import threading
import time
import DoNotCommit  as DNC

import User_Prefs as up
from glob import glob
import ChatGPT as GPT

sys.path.append(os.path.join(sys.path[0], "../../"))
import schedule
from instabot import Bot, utils

import os
import glob

# importing the required package
from PIL import Image
import shutil

import cv2
import random

# Load .png image




def png2JPG(FilePath,NewPath,NewName = '',ArchivePath = up.PNGPath_Archive, Del = False ):
    try:
        # # open image in png format
        # img_png = Image.open(FilePath)
        # # The image object is used to save the image in jpg format
        #


        isExist = os.path.exists(NewPath)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(NewPath)

        isExist = os.path.exists(ArchivePath)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(ArchivePath)
    except:
        print('Error could not create file path)')


    try:
        image = cv2.imread(FilePath)
        NewFilePath = NewPath + '/' +  NewName + '.jpg'
        cv2.imwrite(NewFilePath, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

        ArchivePath2 = ArchivePath +  '' +NewName + '.png'
        try:
            print(FilePath)
            print(ArchivePath2)
            if Del == True:
                shutil.move(FilePath, ArchivePath2)
            else:
                shutil.copy(FilePath, ArchivePath2)
        except:
            print('Error could not move file from old to new directory')
    except:
        print('Error could not convert file')






def upload_pictures_error():
    bot = Bot()
    bot.login(username=DNC.Inst_username, password=DNC.Inst_password)
    bot.logger.info("ULTIMATE script. Safe to run 24/7!")

    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])

    posted_pic_list = utils.file(up.POSTED_PICS_FILE).list

    pics = sorted([os.path.basename(x) for x in glob(up.PICS_PATH + "/*.jpg")])

    try:
        for pic in glob.glob(up.PICS_PATH + '/**/*.jpg', recursive=True):

            if pic in posted_pic_list:
                continue

            # up.PICS_PATH + pic



            #Eventually have random mode to make 4 similar pics etc.
            x = GPT()
            print(up.breakupOutput)
            print('Getting Caption from ChatGPT')
            Caption = x.MondeVertAuto( Mode='AutoSocial')

            bot.logger.info("Uploading " + pic)
            bot.upload_photo(up.PICS_PATH + pic, caption=Caption)
            if bot.api.last_response.status_code != 200:
                bot.logger.error("Something went wrong, read the following ->\n")
                bot.logger.error(bot.api.last_response)
                break

            if pic not in posted_pic_list:
                posted_pic_list.append(pic)
                with open(up.POSTED_PICS_FILE, "a") as f:
                    f.write(pic + "\n")
                bot.logger.info("Succesfully uploaded: " + pic)
                break
    except Exception as e:
        bot.logger.error("Couldn't upload pic")
        bot.logger.error(str(e))

def run_threaded(job_fn):
    job_thread = threading.Thread(target=job_fn)
    job_thread.start()



def upload_pictures(Folder = up.PICS_PATH, Caption = ''):
    bot = Bot()
    time.sleep(15)
    bot.login(username=DNC.Inst_username, password=DNC.Inst_password)
    time.sleep(15)
    bot.logger.info("ULTIMATE script. Safe to run 24/7!")

    #cookie_del = glob.glob("config/*cookie.json")
    #os.remove(cookie_del[0])
    if os.path.isfile("path/to/config/file.json"):
        os.remove("path/to/config/file.json")


    pics = []
    #try:
    if Folder != '':
        for p in glob.glob(Folder+ '/**/*.jpg', recursive=True):
            pics.append(p)


        pic = random.choices(pics)
        print(pic)

        #Eventually have random mode to make 4 similar pics etc.
        x = GPT()
        Temp = pic.replace(Folder, "")
        Temp = Temp.replace('/', "")
        Details2 = Temp.replace(".jpg", "")

        print(Details2)

        if Caption == '':
            Caption = x.MondeVertAuto(Title = Details2, Mode='AutoSocial')
            print (Caption)
        bot.logger.info("Uploading " + pic)
        time.sleep(5)
        bot.upload_photo(up.PICS_PATH + pic, caption=Caption)
        time.sleep(10)
        if bot.api.last_response.status_code != 200:
            bot.logger.error("Something went wrong, read the following ->\n")
            bot.logger.error(bot.api.last_response)




    else:
    #except Exception as e:
        bot.logger.error("Couldn't upload pic")
        #bot.logger.error(str(e))



def onetimeClean():
    for f in glob.glob(up.PNGPath + '/**/*.png', recursive=True):
        try:
            print(f)




            if f.find(".png") == (len(f) - 4):

                Path1 = up.PNGPath

                print('Temp')
                Temp = f.replace(Path1, "")
                Temp = Temp.replace('/', "")
                print(Temp)
                print('Details')
                Details2 = Temp.replace(".png", "")
                print(Details2)



                #x = len(Details2)

                png2JPG(f, up.PICS_PATH, Details2)


                ddd = 1
            else:
                print("Did not Load a non-.png file - " + f)
        except:
            print('Error When Converting')




#
# schedule.every(5).hours.do(run_threaded, upload_pictures())
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#



if __name__ == '__main__':

    upload_pictures()

# onetimeClean()