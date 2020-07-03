import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


print("Initializing Dailey....")

MASTER = "Danji"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

    
    speak("Hello " + MASTER + " This is Daily. How may i help you?..")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<12:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("I am Dailey. how may i help you?")              


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-uk')
        print(f"user said: {query}\n")

    except Exception as e:
        print("sorry, say that again please")
        query = None
    return query    

speak("Initializing Dailey....")
wishMe()
takeCommand() 


if 'wikipedia' in query.lower():
    speak('searching online....')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentence =2)
    speak(results)


elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
    url = "youtube.com"


elif 'open Google' in query.lower():
    webbrowser.open("Google.com")
    url = "Google.com"

