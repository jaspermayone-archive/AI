import pyttsx3
import speech_recognition as sr
import socket
import getpass

USERNAME = getpass.getuser()

def Offline():
    HOST = socket.gethostname()
    IP = socket.gethostbyname(HOST)
    if "127.0.0.1" in IP:
        print("You're Offline, Service can't Provide")
    else:
        pass

def Speech_Core():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recognizing...")
        listener.adjust_for_ambient_noise(source)
        InputFromUser = listener.listen(source, None, 10)
        command = listener.recognize_google(InputFromUser, language="en-US").lower()
        return command

def Chat(user_name, SOURCE=None):
    if "how are you" in Speech_Core():
        print(Speech_Core())
        pyttsx3.speak(f"I'm fine, what about you {user_name}")
        if "fine" in Speech_Core():
            pyttsx3.speak(f"if you need any help just call me {user_name}")


Offline()
Chat(USERNAME, None)