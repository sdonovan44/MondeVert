import segno

from segno import helpers

import URI_Codes as URI
import io
from PIL import Image
import segno
import glob
import time
import datetime
import qrcode as qr
import random

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

import io
from urllib.request import urlopen

#This is for old people and their wifi set it up once and forget it (sell this to comcast)
#
# qrcode = helpers.make_wifi(ssid='Kabano 44', password='shaned313', security='WPA')
# qrcode.designator
# '3-M'
# qrcode.save('A:\MondeVert_IP Productions\wifi-access.png', scale=10)
#
#






#"A:\MondeVert_IP Productions\the-big-lebowski-the-dude ceiling.gif"
#"A:\MondeVert_IP Productions\the-big-lebowski-coen-brothers.gif"
#"A:\MondeVert_IP Productions\balls-polishing-dude-lebowski-jesus.gif"


import cv2
import base64
from MondeVert_IP.SHAINE_MonderVert import Instagram_Posts as IP

if __name__ == '__main__':



    Folder = r"A:\Amini Amor\QR Code and ads\QR Testing\Add Contact"
    Mode = "Add Shane Contact"
    bio = 'Thanks for adding me I look forward to working with You! Founder of MondeVert where "WE DO IT ALL!"'

    # Some params accept multiple values, like email, phone, url
    qrcode = helpers.make_vcard(nickname='Shane D - Realtor & Solar Guy',
                                name = 'Shane Donovan',
                                 displayname='Shane Donovan',
                                title='CEO: MondeVert | LoveYourLawn.Care ',
                                org=('REALTOR: BRG Real Estate (SC) | SUCCESS! Real Estate (MA)'),
                                    phone = '7819748735',
                                 email=('sdonovan@mondevert.co'),
                                 url=['http://www.mondevert.co/','http://www.loveyourlawn.care/',  'Instagram.com/MondeVert_llc','Instagram.com/Shanedthatsme'],
                                photo_uri = '',
                                 memo = (bio)
                                 )

    # dColor = 'darkgreen'
    # dDataColor = 'green'
    # dLight = 'lightgreen'
    #
    # dColor = 'lightgreen'
    # dDataColor = 'lightblue'
    # dLight = 'white'
    #
    #
    #
    # dColor = 'purple'
    # dDataColor = 'red'
    #
    # dDataColor= 'orange'
    # dColor= 'red'
    #
    # dColor = 'purple'
    # dDataColor = 'darkred'
    # dLight = 'lightgray'


    DarkColors = ['red','orange','blue','purple','darkblue','darkgray','gray','darkred','darkgreen','darkorange']
    LightColors = ['pink','orange','yellow','lightblue','lightgray', 'lightgreen']

    RunNum = 10
    for i in range(0,RunNum):

        current_time1 = datetime.datetime.now()
        current_time = current_time1.strftime('%m-%d-%Y_%H.%M.%S.%f')

        dColor = random.choices(DarkColors)[0]
        dDataColor = dColor
        dLight= dColor
        while dColor == dDataColor:
            dDataColor = random.choices(DarkColors)[0]
        while dColor == dLight or dLight == dDataColor:
            dLight = random.choices(LightColors)[0]

        print(dColor)
        print(dDataColor)
        print(dLight)



        SaveLoc = Folder + r"/QR_" + Mode + "_" + current_time + ".png"
        #qrcode = segno.make('http://www.LoveYourLawn.care')
        img = qrcode.to_pil(dark=dColor, data_dark=dDataColor,
                            data_light=dLight, scale = 8)
        img.save(SaveLoc)


    # pcount = 0
    # for p in glob.glob(Folder + '/**/*.png', recursive=True):
    #     pcount += 1
    #
    #     SaveLoc = Folder + r"/QR_" + Mode + "_"+ str(pcount) + "_" + current_time + ".jpg"
    #     qrcode.to_artistic(background=p,target=SaveLoc, scale = 8)

        # qrcode = segno.make('http://www.LoveYourLawn.care')
        # img = qrcode.to_pil(dark='darkgreen', data_dark='green',
        #                     data_light='lightgreen')
        # img.save('A:\Amini Amor\SHAINE\Marketing\LoveyourLawnQR.png')
        #
        # # qrcode = segno.make('Big L - Contact', error='h')
        # qrcode.to_artistic(background=r"A:\Amini Amor\SHAINE\Marketing\LoveyourLawn.care logo.JPG",
        #                    target=r"A:\Amini Amor\SHAINE\Marketing\LoveyourLawnQR2.png", scale=10)
        #












    # bround = r"C:\Users\sdono\Downloads\Facetune-11-04-2023-17-54-23.jpg"
    # logo1 = r"A:\Amini Amor\QR Code and ads\Logo 3.PNG"
    # logo2 = r"A:\Amini Amor\SHAINE\Marketing\SHAINE - Art\End of Broadcast_Amini Amor_Portuguese_Gabrielle_Chunk_1.png"
    # logo2 = r"A:\Amini Amor\SHAINE\Requests\Beta\AI Art\ expressive brushstrokes to capture the tension trust and commitment in their eyes as they symbolize the financial and emotional bond between them.png"
    # logo2 = r"A:\Amini Amor\SHAINE\Requests\Beta\AI Art\ from his flask The artwork should convey the unreliable narrative caused by drugs and alcohol blurring the lines between reality and hallucination.png"

    # img = qrcode.to_pil( dark='darkgreen', data_dark='lightGreen',
    #                    data_light='white', scale=4)
    # qrcode2 = img
    # img.save('A:\Amini Amor\SHAINE\Marketing\ShaneContactQR.png')
    #
    #
    # qrcode.to_artistic(background=logo2,
    #                        target=r"A:\Amini Amor\SHAINE\Marketing\ShaneContactQR23.png")
    #
    # qrcode.to_artistic(background=logo1,
    #                        target=r"A:\Amini Amor\SHAINE\Marketing\ShaneContactQR2.png")



    # img = qrcode.to_pil( dark='darkgreen', data_dark='lightGreen',
    #                    data_light='white')
    # img.save('A:\Amini Amor\SHAINE\Marketing\ShaneContactQR.png')

    data = '''BEGIN:VCARD

    VERSION:3.0

    N:Donovan;Shane

    FN:Shane Donovan - Add Contact

    ORG:MondeVert, CEO | SUCCESS! Real Estate, Realtor

    URL:'http://www.mondevert.co/'

    EMAIL:sdonovan@mondevert.co

    TEL;TYPE=voice,work,pref:+7819748735

    END:VCARD'''

    # # img = qr.make_image(fill_color="black", back_color="white")
    # #
    # # qr2 = qr.QRCode(
    # #     version=1,
    # #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    # #     box_size=10,
    # #     border=4,
    # # )
    # # qr2.add_data(data)
    # # qr2.make(fit=True)
    #
    #
    #
    # qr2 = qr.QRCode(error_correction=qr.constants.ERROR_CORRECT_L)
    # qr2.add_data(data)
    #
    # img_1 = qr2.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    # img_2 = qr2.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
    # img_3 = qr2.make_image(image_factory=StyledPilImage, embeded_image_path=bround)
    #
    #
    # # #
    # # url = r"C:\Users\sdono\Downloads\Facetune-11-04-2023-17-54-23.jpg"
    # # bg_file = urlopen(url)
    # # out = io.BytesIO()
    # # qrcode.to_artistic(background=bg_file, target=out, kind='png')
    # #
    # #
    # #
    # # # Nothing special here, let Segno generate the QR code and save it as PNG in a buffer
    # #
    # #
    # # out.seek(0)  # Important to let Pillow load the PNG
    # img = Image.open(r'A:\Amini Amor\SHAINE\Marketing\ShaneContactQR.png')
    # img = img.convert('RGB')  # Ensure colors for the output
    # img_width, img_height = img.size
    # logo_max_size = img_height // 3  # May use a fixed value as well
    # logo_img = Image.open(r'C:\Users\sdono\Downloads\Facetune-11-04-2023-17-54-23.jpg')  # The logo'
    # # Resize the logo to logo_max_size
    # logo_img.thumbnail((logo_max_size, logo_max_size))
    # # Calculate the center of the QR code
    # box = ((img_width - logo_img.size[0]) // 2, (img_height - logo_img.size[1]) // 2)
    # img.paste(logo_img, box)
    # img.save('A:\Amini Amor\SHAINE\Marketing\ShaneContactQR3.png')
    # #
    # #
    #
    # #
    # #
    # #
    # #
    # #
    # #
    #
    #
    # # #qrcode = segno.make('Big L - Contact', error='h')
    # # qrcode.to_artistic(background=r"A:\MondeVert_IP Productions\balls-polishing-dude-lebowski-jesus.gif",
    # #                        target=r"A:\MondeVert_IP Productions\Big_L_Contact3.gif", scale=45)
    # #
    #
    #
    #
    #
    #
    # #qrcode = segno.make('Yellow Submarine', error='h')
    # img = qrcode.to_pil(scale=4, dark='darkgreen', data_dark='green',
    #                    data_light='white')
    # img.save('A:\MondeVert Productions\ShaneDonovan_MondeVert 5-9-2023_contact.png')
    #
    #







    # img = cv2.imread(r"A:\MondeVert Productions\MondeVert Logo B & w.PNG")
    # jpg_img = cv2.imencode('.jpg', img)
    # x = base64.b64encode(jpg_img[1]).decode('utf-8')
    #
    #
    # print(x)


    #
    #



# IP.onetimeClean(FilePath=r"C:\Users\sdono\Downloads\Facetune-11-04-2023-17-54-23.jpg", Destination=r'A:\Amini Amor\SHAINE\Marketing')
#
#r"A:\Amini Amor\QR Code and ads\MondevertlOGOuri2.txt"



#Generate QR codes to get people to my sight --> Tweet a new one everyday and alternate between my contact card and other websites of mine
#Find out how to sell this




