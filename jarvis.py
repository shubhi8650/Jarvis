import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  # used to take voice
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning!')

    elif hour >= 12 and hour < 18:
        speak('good afternoon!')

    else:
        speak('good evening!')

    speak('I am Jarvis Sir. Please tell me how may I help you')


def takeCommand():
    ''' it takes microphone input from user and returns strings output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('say that again please....')
        return 'None'
    return query


if __name__ == "__main__":

    wishme()

    while True:

        query = takeCommand().lower()  # will convert in lower case string and match the query

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')  # removing the word wikipedia from the query
            results = wikipedia.summary(query, sentences=2)  # will serch the query on wikipedia
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'play music' in query:
            music_dir = 'E:\\music\\music '
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))