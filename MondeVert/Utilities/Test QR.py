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


#
#
# # Some params accept multiple values, like email, phone, url
# qrcode = helpers.make_vcard(name='Shane Donovan',
#                              displayname='Shane Donovan',
#                             org=('MondeVert, CEO | SUCCESS! Real Estate, Realtor'),
#                                 phone = '7819748735',
#                              email=('sdonovan@mondevert.co'),
#                              url=['http://www.mondevert.co/',  'Instagram.com/MondeVert_llc','Instagram.com/Shane_2Fames'],
#                             photo_uri = (r"C:\Users\sdono\Downloads\Facetune-11-04-2023-17-54-23.jpg"),
#                              memo = ('My Name is Shane Donovan,  I am CEO of my own company, MondeVert. We do a lot of different things, I like to say I build solutions, even the QR code you scanned was coded by me. If you are looking for a reliable real estate professional who is passionate about helping you find the best investment, I am here to help!')
#                              )
#
#
# qrcode.save('A:\MondeVert Productions\ShaneDonovan_MondeVert.png', scale=5)
#




qrcode = segno.make('https://mondevert.co/real-estate')


#qrcode = segno.make('Big L - Contact', error='h')
qrcode.to_artistic(background=r"A:\MondeVert Productions\balls-polishing-dude-lebowski-jesus.gif",
                       target=r"A:\MondeVert Productions\Big_L_Contact3.gif", scale=45)






#Generate QR codes to get people to my sight --> Tweet a new one everyday and alternate between my contact card and other websites of mine
#Find out how to sell this




