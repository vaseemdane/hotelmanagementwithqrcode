import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greetme():
    time=int(datetime.datetime.now().hour)
    if time>0 and time<11:
        speak("good morning")
    elif time>11 and time<=16:
        speak("good afternoon")
    else:
        speak("good evening")
def takecommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        speak("recognizing")
        query = r.recognize_google(audio, language='en-in')
        speak(f"the user said {query}")
        print(f"{query}")
    except Exception as e:
        speak("can you say that again please")
        return 'none'
    return query
if __name__ == '__main__':
    greetme()
    while True:
    # if 1:
        query = takecommands().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:

            webbrowser.open("stackoverflow.com")


        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")



        elif 'ok bye' in query:
            print("bye bye")
            speak("bye bye have  a nice day ahead")
            exit()
        else:
            print(query)
