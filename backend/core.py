#The core.py file contains all commands for jarvis but some commands are also present in app.py
from speak import speak
from search import search
from location import location
from weather import weather
from news import news
import webbrowser
import pyjokes
import datetime
import YouTubeMusicAPI as ytm



#commands for introduction
commandA='who are you'
commandB='what is your name'
commandC='who is jarvis'
commandD='jarvis who is jarvis'
commandE='jarvis introduce yourself'
#commands for telling jokes
commandF='jarvis tell me a joke'
commandG='jarvis make me laugh'
#commands for telling time
commandH='jarvis what is the time'
commandI='jarvis tell me the time'
#commands for telling location
commandJ='jarvis where am i'
commandK='jarvis tell me my location'
#commands for telling weather of the current city
commandL='jarvis how is the weather'
commandM='jarvis tell me about the weather'
#commands for telling weather of the required city
commandL='how is the weather in'
commandM='tell me about the weather of'
#commands for greeting
commandN='jarvis how are you'
#commands for news
commandO='jarvis what happened today'
commandP='jarvis tell me about the news'

def core(query):
    q=query.lower()
    q=query.replace(".","")

    #for 0 input
    if q.replace(" ","")=="":
        text="Sorry about that I didn't hear anything"
        

    #for introduction
    elif q.replace(" ","") in commandA.replace(" ","") or q.replace(" ","") in commandB.replace(" ","") or q.replace(" ","") in commandC.replace(" ","") or q.replace(" ","") in commandD.replace(" ","") or q.replace(" ","") in commandE.replace(" ",""):
        text="Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week"
        

    #for greeting
    elif q.replace(" ","") in commandN.replace(" ",""):
        text="I am fine how may I help you"
        

    #for telling joke
    elif q.replace(" ","") in commandF.replace(" ","") or q.replace(" ","") in commandG.replace(" ",""):
        text=pyjokes.get_joke(language='en', category= 'all')
        

    #for telling time
    elif q.replace(" ","") in commandH.replace(" ","") or q.replace(" ","") in commandI.replace(" ",""):
        time=datetime.datetime.now().strftime('%I:%M %p')
        text=f'now it is {time}'
        

    #for telling news
    elif q.replace(" ","") in commandO.replace(" ","") or q.replace(" ","") in commandP.replace(" ","") or q.replace(" ","") == "news":
        try:
            
            text=news()
            
        except:
            text="Sorry about that but I couldn't access the server"
            

    #for telling weather of the current city
    elif q.replace(" ","") in commandL.replace(" ","") or q.replace(" ","") in commandM.replace(" ",""):
        try:
            locate=location()
            locate=str(locate)
            locate=locate.split(",")
            city=locate[2]
            text=f'In {city} {weather(city)}'
            
        except:
            text="Sorry about that but I couldn't access the server"
            

    #for telling weather of the required city
    elif commandL.replace(" ","") in q.replace("jarvis","").replace("j.a.r.v.i.s","").replace(" ","") or commandM.replace(" ","") in q.replace("jarvis","").replace("j.a.r.v.i.s","").replace(" ",""):
        try:
            city=q.replace("jarvis","").replace("j.a.r.v.i.s","").replace(" ","")
            city=city.replace(commandL.replace(" ",""),"")
            text=weather(city)
        except:
            text="Sorry about that but I couldn't access the server"
            

    #for playing music
    elif q.find("play")==0 or q.replace(" ","").find("jarvisplay")==0:
        query=q.replace("play","")
        query=q.replace("jarvis","")
        try:
            text="here is what i found on the internet"
            if query.replace(" ","")=='play':
                webbrowser.open('https://www.google.com/search?q=play')
            elif query.replace(" ","")=='playmeaning':
                webbrowser.open('https://www.google.com/search?q=play+meaning')
            else:
                ytm.play(query)
        except:
            text="Sorry about that but I couldn't understand which music to play"
                

    #for opening url
    elif q.find("open")==0 or q.replace(" ","").find("jarvisopen")==0 :
        try:
            text="here is what i found on the internet"
            if q.replace(' ','')=='open':
                webbrowser.open('https://www.google.com/search?q=open') 
            if q.replace(' ','')=='openmeaning':#open meaning
                webbrowser.open('https://www.google.com/search?q=open+meaning') 
            else:
                query=q.replace("open","")
                query=q.replace("jarvis","")
                results=search(query)
                webbrowser.open(results)
        except:
            text="Sorry about that but I couldn't understand what to open"
            
    #searching the web if can't answer question
    else:
        text="here is what i found on the internet"
        webbrowser.open(f'https://www.google.com/search?q={query}') 
    

    speak(text)


a=input()
core(a)
