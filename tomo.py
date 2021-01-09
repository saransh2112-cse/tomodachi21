#ai project grp 2
import pyttsx3  # text - speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

# microsoft speech api - for voice acceptance, uses inbuilt Windows voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # set the voice

print(voices[1].id)
engine.setProperty('voices', voices[1].id)
# 0 = male | 1= female


def speak(audio):  # defining speak function
    engine.say(audio)
    engine.runAndWait()  # assistant waiting time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
    elif hour >= 18:
        speak("Good Evening !")

    speak("Hello, My name is Tomodachi. How can i help you!")


def takeCommand():
    # It takes Speech input form the user and returns string output of that
    print("Speak Something")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("<<<<<<<<<<  Listening   >>>>>>>>")
        r.pause_threshold = 0.8 # pause in two word or phases
        audio = r.listen(source)
        try:
            print("***** Analysing the voice *****")
            query = r.recognize_google(audio)  # google audio is being used
            print(query)
        except Exception as e:  # return none string if problem will come
            print(e)
            print("Please Repeat Your Query, Your voice not Recognized by the Program")
            speak('Please Repeat, I am unable to hear your voice')
            return "None"

        return query


if __name__ == "__main__":
    speak('I am  your virtual assistant')
    speak('I have been made by Group 2')
    wishMe()

    while True:
        query = takeCommand().lower()
    # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching the Wikipedia.......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to the Wikipedia")
            print(results)
            speak(results)

           # webbrowser.open("wikipedia.com")

        elif 'youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'google' in query:
            webbrowser.open("Google.com")

        elif 'geeks for geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'music' in query:
            speak('Which type of music  you  would  like  beatles , rock,chill,romance')
            music = takeCommand().lower()
            if 'beatles' in music:
                 speak("Playing something from the beatles")
                 webbrowser.open("https://www.youtube.com/watch?v=UelDrZ1aFeY")

            elif 'rock' in music:
                 speak("Playing Rock")
                 webbrowser.open("https://www.youtube.com/watch?v=nYh-n7EOtMA")

            elif 'chill' in music:
                 speak("Finding something chill")
                 webbrowser.open("https://www.youtube.com/watch?v=uJbooOYyBCA")

            elif 'romance' in music:
                 speak("Playing romantic songs")
                 webbrowser.open("https://www.youtube.com/watch?v=J4_XiSN3AM8")

        elif 'class' in query:
             speak('Opening class')
             speak("all your assignments are submitted!!")
             webbrowser.open( "https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fcourse")

        elif 'time' in query:
             strtime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The time is {strtime}")

        elif 'myntra' in query:
             speak("opening myntra")
             webbrowser.open("https://www.myntra.com/shop/men")
        elif 'quit' in query:
             speak('Bye buddy ! see you soon>>')
             quit()
