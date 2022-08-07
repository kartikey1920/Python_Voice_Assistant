import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 144)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def cmd():
    try:
        with sr.Microphone() as source:
            talk("Say Anything, I'm Listening to you.")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            talk(command)
            print(command)
    except:
        pass
    return cmd

def assist():
    command = cmd()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    else:
        talk('Please say the command again.')


while True:
    assist()

