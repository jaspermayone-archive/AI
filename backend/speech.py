import speech_recognition as sr

def speech():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language='en-US')
    return command

a=speech()
print(a)