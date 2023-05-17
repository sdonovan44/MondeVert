import speech_recognition as sr
import DoNotCommit as DNC
r = sr.Recognizer()

audio = 'trial.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio)
    print (text)

except Exception as e:
    print (e)