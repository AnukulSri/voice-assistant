import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
print(voices[1].id)


def speak (audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis Sir")
     

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please....")
        return "None"
    return query
if __name__=="__main__":
    # speak("this is an apple")
    wishme()
    while True:
      query =takeCommand().lower()
      if 'wikipedia' in query:
          speak("searching wikipedia...")
          query= query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

      elif 'open youtube' in query:
          webbrowser.open("https://www.youtube.com")

      elif 'open google' in query:
          webbrowser.open("https://www.google.com")

    #   elif 'play music' in query:
    #       music_dir = "music path"
    #       songs =os.listdir(music_dir)
    #       print(songs)
    #       os.startfile(os.path.join(music_dir,songs[0]))
          
      elif 'what\'s time now' in query:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak("The current time is " + current_time)
