import random

#MondeVert_Promo = "The following   Audio   is copyrighted by Monde  Vert  Studios.....  MondeVert_IP - because the world needs less stress and more success.         If you enjoy this content please subscribe and follow Monde Vert's Social Media Sites and check out our website at www.MondeVert_IP.co. The CEO, Shane Donovan has recently starting up a patreon with exclusive content and soon will be holding a contest for people to submit their own original work. Here at MondeVert_IP we are working with new talent to foster their brand and help them succeed. I hope you enjoy the following audiobook we have published for your entertainment. thanks for watching feel free to comment and suggest other types of content you would enjoy"
MondeVert_Promo = "The following   Audio   is copyrighted by Monde  Vert  Studios.....  MondeVert_IP - because the world needs less stress and more success.         If you enjoy this content please subscribe and follow Monde Vert's Social Media Sites and check out our website at www.MondeVert_IP.co. Our team has recently started up a patreon with exclusive content and soon will be holding several paid contest for people to submit their own original work Submissions as low as $1 to win $100. Additionally, Here at MondeVert_IP we are working with new talent to foster their brand and help them succeed. I hope you enjoy the following audiobook we have published for your entertainment; reach out to our team and you could have your content featured in the future. thanks for watching feel free to comment we look forward to hearing from you"




Text1="""Title: The Last Day of Summer

The sun was setting on the last day of summer. The air was warm and sticky, and the crickets chirped in the distance. Sofia and Diego sat on the edge of the dock, their feet dangling in the water. They had spent the entire day swimming, playing games, and eating ice cream. It had been the perfect day, but now it was coming to an end.

Sofia sighed and leaned her head on Diego's shoulder. ""I don't want summer to be over,"" she said.

""Me neither,"" Diego agreed. ""But we still have next summer to look forward to.""

Sofia nodded, but she knew it wouldn't be the same. Next summer, things would be different. They would be starting high school, and everything would change. She didn't know if she was ready for that.

As the sun disappeared below the horizon, Sofia and Diego sat in silence, watching the stars appear in the sky. They didn't need to talk. They were best friends, and they knew each other's thoughts without saying a word.

Finally, Diego stood up and held out his hand. ""Come on,"" he said. ""Let's make a wish on a shooting star.""

Sofia took his hand, and they walked back to the house, their hearts full of hope for the future.
"""

Text = """Title: The Weight of Grief

Grief is a heavy burden
That we all must bear
It weighs us down
And fills us with despair

It comes in waves
And knocks us off our feet
We struggle to stand
And find the strength to meet

The day with a smile
But sometimes it's too much
And we crumble and fall
And long for a gentle touch

To remind us that we're not alone
That others share our pain
And that we'll get through this
And find joy again

So hold on tight
To the ones you love
And know that time
Will heal the hurt above

And one day you'll look back
And see how far you've come
And know that the weight of grief
Can be overcome"""


Text2 = """Broken Dreams

INT. APARTMENT - DAY

Ana sits at the kitchen table, staring at a stack of bills. She picks up one and looks at the amount owed. Tears well up in her eyes.

ANA
(to herself)
How am I going to pay for all of this?

Diego enters the room and sees his mother's distress.

DIEGO
Mom, what's wrong?

ANA
(sighing)
We're in trouble, Diego. I can't pay the rent this month, and we're behind on all of our bills.

Diego's face falls.

DIEGO
What are we going to do?

ANA
(voice shaking)
I don't know. I thought I had everything under control, but everything's falling apart.

Diego puts his arm around his mother.

DIEGO
It's going to be okay, Mom. We'll figure something out.

ANA
(sighing)
I hope so. I just don't want you to have to give up your dreams because of my mistakes.

DIEGO
(shaking his head)
I won't give up, Mom. I'll find a way to make it work.

Ana looks at her son with pride and gratitude.

ANA
(hugging him)
I know you will, Diego. You're stronger than I ever was.

Diego smiles, but inside he feels the weight of his broken dreams. He knows he has to find a way to make things right, but he's not sure how.

"""



Translation_Languages_All = ['English','French', 'Italian','Spanish','Swahili','Chinese','Japanese','German']
Translation_Languages_Testing = ['English','French', 'Italian','Spanish', 'Swahili', 'Portuguese']
Translation_Languages_Testing2 = ['English','French', 'Italian']
Translation_Languages_Testing3 = ['English','French', 'Italian', 'Swahili']
Translation_Languages_Testing4 = ['English','French']
Translation_Languages_Testing5 = ['English','French', 'Swahili']


French_Voices = ['Gabrielle','Remi','Liam','Lea']
Spanish_Portuguese_Voices = ['Lucia','Sergio','Pedro', 'Mia', 'Ines', 'Vitoria','Lupe', 'Camila']
German_Voices = ['Daniel', 'Hannah', 'Vicki', 'Ola', 'Suvi']
Japanese_Voices = ['Tomoko', 'Takumi', 'Kazuha']
Chinese_Voices = ['Hiujin', 'Zhiyu']
Italian_Voices = ['Bianca','Adriano']



Translate_Sys = 'You must translate the text I provide in my conversation I will tell you Translate[] you must translate what is between the Text: []'
Translate_Line2 = "You are a master translator and children's writer able to take an english text and translate to [ "
Translate_Line4 = "Translate the following Text: ["
Translate_Line3 = "The text being translated is a [short story], use appropriate words that are descriptive and accurate translations, try to translate the meaning more than the actual word for word translation so the respective language sounds like someone speaking and not just reading."

Original_List_of_Voices_English = ['Joanna','Kendra','Kimberly','Salli','Ruth','Olivia','Kajal','Amy','Emma','Aria','Ayanda','Ivy','Joey','Matthew','Stephen','Brian','Arthur','Justin','Kevin']
Original_List_of_Voices_ESL= ['Lupe','Hiujin','Zhiyu','Lea','Gabrielle','Bianca','Ida','Ola','Camila','Vitoria/Vitoria','Ines','Lucia','Mia','Hala','Arlet','Laura','Suvi','Vicki','Hannah','Kazuha','Tomoko','Seoyeon','Elin','Pedro','Remi','Liam','Adriano','Thiago','Sergio','Andres','Daniel','Takumi']
Original_List_of_Voices = ['Joanna','Kendra','Kimberly','Salli','Ruth','Olivia','Kajal','Amy','Emma','Aria','Ayanda','Ivy','Joey','Matthew','Stephen','Brian','Arthur','Justin','Kevin','Lupe','Hiujin','Zhiyu','Lea','Gabrielle','Bianca','Ida','Ola','Camila','Vitoria','Ines','Lucia','Mia','Hala','Arlet','Laura','Suvi','Vicki','Hannah','Kazuha','Tomoko','Seoyeon','Elin','Pedro','Remi','Liam','Adriano','Thiago','Sergio','Andrés','Daniel','Takumi']

def Pick_Voice(Language = 'English'):
    if Language == 'English':
        Language_Base= Original_List_of_Voices_English
    elif Language == 'French':
        Language_Base = French_Voices
    elif Language == 'Italian':
        Language_Base = Italian_Voices + Italian_Voices + Italian_Voices + French_Voices
    elif Language == 'Spanish':
        Language_Base = Spanish_Portuguese_Voices
    elif Language == 'Swahili':
        Language_Base = French_Voices + Original_List_of_Voices_English
    elif Language == 'Chinese':
        Language_Base = Chinese_Voices
    elif Language == 'Japanese':
        Language_Base = Japanese_Voices
    elif Language == 'German':
        Language_Base = German_Voices
    elif Language == 'Portuguese':
        Language_Base = Spanish_Portuguese_Voices
    else:
        Language_Base = Original_List_of_Voices

    Voice = random.choices(Language_Base)[0]

    return Voice



Audio_Voice_Table = """Language and language variants,Rarity Weight (Higher the % means its more likely to be picked),Name/ID,Gender
English (US),90%,Joanna,Female
English (US),90%,Kendra,Female
English (US),90%,Kimberly,Female
English (US),90%,Salli,Female
English (US),90%,Ruth,Female
English (Australian),50%,Olivia,Female
English (Indian),40%,Kajal,Female
English (British),30%,Amy,Female
English (British),30%,Emma,Female
English (New Zealand),30%,Aria,Female
English (South African),30%,Ayanda,Female
English (US),90%,Ivy,Female (child)
English (US),90%,Joey,Male
English (US),90%,Matthew,Male
English (US),90%,Stephen,Male
English (British),30%,Brian,Male
English (British),30%,Arthur,Male
English (US),90%,Justin,Male (child)
English (US),90%,Kevin,Male (child)
Spanish (US),30%,Lupe,Female
Chinese (Cantonese),20%,Hiujin,Female  
Chinese (Mandarin),20%,Zhiyu,Female
French,20%,Léa,Female
French (Canadian),20%,Gabrielle,Female
Italian,20%,Bianca,Female
Norwegian,20%,Ida,Female
Polish,20%,Ola,Female
Portuguese (Brazilian),15%,Camila,Female
Portuguese (Brazilian),15%,Vitoria/Vitoria,Female
Portuguese (European),15%,Ines/Ines,Female
Spanish (European),15%,Lucia,Female
Spanish (Mexican),15%,Mia,Female
Arabic (Gulf),5%,Hala,Female
Catalan,5%,Arlet,Female
Dutch,5%,Laura,Female
Finnish,5%,Suvi,Female
German,5%,Vicki,Female
German (Austrian),5%,Hannah,Female
Japanese,5%,Kazuha,Female
Japanese,5%,Tomoko,Female
Korean,5%,Seoyeon,Female
Swedish,5%,Elin,Female
Spanish (US),30%,Pedro,Male
French,20%,Remi,Male
French (Canadian),20%,Liam,Male
Italian,20%,Adriano,Male
Portuguese (Brazilian),15%,Thiago,Male
Spanish (European),15%,Sergio,Male
Spanish (Mexican),15%,Andres,Male
German,5%,Daniel,Male
Japanese,5%,Takumi,Male"""

