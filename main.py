import speech_recognition as sr
import webbrowser
import playsound
from gtts import gTTS
import os



def speak(text):
    tts = gTTS(text=text)
    audio_file = "dave.mp4"
    tts.save(audio_file)
    playsound.playsound(audio_file)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            data = r.recognize_google(audio)
            print(data)
            if "Hey Dave" in audio:
                speak('How are you?')
            if "Search" in audio:
                webbrowser.open_new_tab('https://google.com')
            if "Stackoverflow" in audio:
                webbrowser.open_new_tab('https://stackoverflow.com/')
            if "Youtube" in audio:
                webbrowser.open_new_tab('https://youtube.com/')
        except sr.UnknownValueError:
                speak("Can't understand, Try Again")


data = get_audio()








