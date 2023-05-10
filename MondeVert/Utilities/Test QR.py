import segno

import User_Prefs as up

from segno import helpers




#This is for old people and their wifi set it up once and forget it (sell this to comcast)
#
# qrcode = helpers.make_wifi(ssid='Kabano 44', password='shaned313', security='WPA')
# qrcode.designator
# '3-M'
# qrcode.save('A:\MondeVert Productions\wifi-access.png', scale=10)
#
#






#"A:\MondeVert Productions\the-big-lebowski-the-dude ceiling.gif"
#"A:\MondeVert Productions\the-big-lebowski-coen-brothers.gif"
#"A:\MondeVert Productions\balls-polishing-dude-lebowski-jesus.gif"


import cv2
import base64


if __name__ == '__main__':
    img = cv2.imread(r"A:\MondeVert Productions\MondeVert Logo B & w.PNG")
    jpg_img = cv2.imencode('.jpg', img)
    x = base64.b64encode(jpg_img[1]).decode('utf-8')


    print(x)





    # Some params accept multiple values, like email, phone, url
    qrcode = helpers.make_vcard(nickname='Shane',
                                name = 'Donovan - MondeVert',
                                 displayname='Shane',
                                org=('MondeVert, CEO | SUCCESS! Real Estate, Realtor'),
                                    phone = '7819748735',
                                 email=('sdonovan@mondevert.co'),
                                 url=['http://www.mondevert.co/',  'Instagram.com/MondeVert_llc','Instagram.com/Shane_2Fames'],
                                photo_uri = (r"A:\MondeVert Productions\MondeVert Logo B & w.PNG"),
                                 memo = ('My Name is Shane Donovan,  I am CEO of my own company, MondeVert. I am also a Realtor in MA going for my license in South Carolina.')
                                 )


    qrcode.save('A:\MondeVert Productions\ShaneDonovan_MondeVert 5-9-2023.png', scale=4)





    #


    # #qrcode = segno.make('Big L - Contact', error='h')
    # qrcode.to_artistic(background=r"A:\MondeVert Productions\balls-polishing-dude-lebowski-jesus.gif",
    #                        target=r"A:\MondeVert Productions\Big_L_Contact3.gif", scale=45)
    #





    #qrcode = segno.make('Yellow Submarine', error='h')
    img = qrcode.to_pil(scale=4, dark='darkgreen', data_dark='green',
                       data_light='white')
    img.save('A:\MondeVert Productions\ShaneDonovan_MondeVert 5-9-2023_contact.png')






    qrcode = segno.make('https://mondevert.co/real-estate')
    img = qrcode.to_pil(scale=4, dark='darkgreen', data_dark='green',
                       data_light='lightblue')
    img.save('A:\MondeVert Productions\ShaneDonovan_MondeVert 5-9-2023_REpage.png')






#Generate QR codes to get people to my sight --> Tweet a new one everyday and alternate between my contact card and other websites of mine
#Find out how to sell this




