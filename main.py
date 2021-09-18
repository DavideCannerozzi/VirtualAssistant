import speech_recognition as sr
import webbrowser

r = sr.Recognizer()


with sr.Microphone() as source:
        print("Hi I am Davide...Talk To Me")
        # convert voice to text
        audio = r.listen(source)
        try:
            data = r.recognize_google(audio)
            if "Davide" in audio:
                print("How Can I Help You?")
            if "Location" in audio:
                location = print("What is the Location?")
                print("Location is: " + location)
                webbrowser.open_new_tab('https://google/maps/place' + location)
            if "Search" in audio:
                webbrowser.open_new_tab('https://google.com/search')
            else:
                print('Error')
        except sr.UnknownValueError:
                print("Can't understand, Try Again")



