import speech_recognition as sr
import pyttsx3

r = sr.Recognizer

try:
    with sr.Microphone() as source:
        print("Hi I am Davide...Talk To Me")
        # convert voice to text
        audio = r.listen(source)
        if 'dave' in audio:
            print(audio)
        else:
            print('Hey! My Name Is Dave')
except:
    pass