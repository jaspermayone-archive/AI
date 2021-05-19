import speech_recognition as sr
import pyttsx3

def JARVIS_COMMANDS():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        InputFromUser = listener.listen(source, None, 10)
        command = listener.recognize_google(InputFromUser)
        command = command.lower()
        if "jarvis" in command:
            command = command.replace("jarvis", "")                
            if "solve" in command:
                command - command.replace("solve", "")
                sum =  eval(command.replace("plus", "+"))
                pyttsx3.speak(sum)
