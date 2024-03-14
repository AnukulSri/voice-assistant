import speech_recognition as sr
import pyttsx3
import datetime


# Initialize the speech recognizer and text-to-speech converter
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")

    speak("I'm your voice assistant.")

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "what is your name" in command:
        speak("My name is Python Assistant.")
    elif "good bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    wishme()
    # speak("Hello! I'm your voice assistant.")
    while True:
        command = listen()
        if command:
            process_command(command)
