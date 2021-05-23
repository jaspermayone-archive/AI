#The core.py file contains all commands for jarvis but some commands are also present in app.py
from speak import speak
from search import search
from location import location
from weather import weather
from news import news
from password import password
from story import story
from word2number import w2n
import screen_brightness_control as sbc
import wikipedia  
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
#commands for asking question
commandQ='who is'
commandR='what is'
#commands for reducing brightness
commandS='jarvis reduce the brightness'
commandT='jarvis reduce the screen brightness'
commandU='jarvis reduce screen brightness'
commandV='jarvis reduce brightness'
#commands for increasing brightness
commandW='jarvis increase the brightness'
commandX='jarvis increase the screen brightness'
commandY='jarvis increase screen brightness'
commandZ='jarvis increase brightness'
#commands for setting brightness
commandAA='set screen brightness to'
#commands for setting password
commandAB='create a password'
commandAC='generate a password'
commandAD='jarvis create a password'
commandAE='jarvis generate a password'
#commands for generaing text
commandAF="jarvis write something about"
commandAG="write something about"



def core(query):
    q=query.lower()
    q=query.replace(".","")

    #for 0 input
    if q.replace(" ","")=="":
        text="Sorry about that I didn't hear anything"
        

    #for introduction
    elif q.replace(" ","") in commandA.replace(" ","") or q.replace(" ","") in commandB.replace(" ","") or q.replace(" ","") in commandC.replace(" ","") or q.replace(" ","") in commandD.replace(" ","") or q.replace(" ","") in commandE.replace(" ",""):
        if q.replace(" ","")=="whois" or q.replace(" ","")=="whatis" or q.replace(" ","")=="jarviswhois" or q.replace(" ","")=="jarviswhatis":
            text="Please tell me what do you want to know about"
        else:
            text="Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week"
        

    #for greeting
    elif q.replace(" ","") in commandN.replace(" ",""):
        text="I am fine how may I help you"
        
    #for asking question
    elif commandQ.replace(" ","") in q.replace(" ","") or commandR.replace(" ","") in q.replace(" ",""):
        q=q.replace(" ","")
        q=q.replace("jarvis","")
        q=q.replace("whois","")
        q=q.replace("whatis","")
        if q=="":
            text="Please tell me what do you want to know about"
        else:
            try:
                text=f"According to wikipedia {wikipedia.summary(query, sentences = 5)}"
            except:
                try:
                    text="here is what i found on the internet"
                    results=search(query)
                    webbrowser.open(results)
                except:
                    text="Sorry about that but I can't find the answer to your question"

    #for generaing text
    elif commandAF.replace(" ","") in q.replace(" ","") or  commandAG.replace(" ","")in q.replace(" ",""):
        quaryA=q.replace(commandAF,"")
        quaryB=quaryA.replace(commandAG,"")
        if quaryB.replace(" ","")=="":
            text="sorry about that but i couldn't hear about what i should write"
        else:
            try:
                written=story(quaryB,char=1000)
                if written==quaryB:
                    text=f"sorry about that but i don't anything about this"
                else:
                    text=f"here is what i have written {written}"
            except:
                text=f"sorry about that but i don't anything about this"
             
    #for creating passwords
    elif q.replace(" ","") == commandAB.replace(" ","") or q.replace(" ","") == commandAC.replace(" ","") or q.replace(" ","") == commandAD.replace(" ","") or q.replace(" ","") == commandAE.replace(" ",""):
        result=password()
        text=f"you can use {result} as your password"


    #for telling joke
    elif q.replace(" ","") in commandF.replace(" ","") or q.replace(" ","") in commandG.replace(" ",""):
        text=pyjokes.get_joke(language='en', category= 'all')
        

    #for telling time
    elif q.replace(" ","") in commandH.replace(" ","") or q.replace(" ","") in commandI.replace(" ",""):
        time=datetime.datetime.now().strftime('%I:%M %p')
        text=f'now it is {time}'

    #for reducing brightness
    elif q.replace(" ","") in commandS.replace(" ","") or q.replace(" ","") in commandT.replace(" ","") or q.replace(" ","") in commandU.replace(" ","") or q.replace(" ","") in commandV.replace(" ",""):
        try:
            current_brightness = sbc.get_brightness()
            if current_brightness==0:
                text="your screen brightness is already at it's lowest level"
            else:
                text="okay"
                sbc.set_brightness(current_brightness-10)
        except:
            text="looks like I don't have the permission to reduce your screen brightness"

    #for increasing brightness
    elif q.replace(" ","") in commandW.replace(" ","") or q.replace(" ","") in commandX.replace(" ","") or q.replace(" ","") in commandY.replace(" ","") or q.replace(" ","") in commandZ.replace(" ",""):
        try:
            current_brightness = sbc.get_brightness()
            if current_brightness==100:
                text="your screen brightness is already at it's highest level"
            else:
                text="okay"
                sbc.set_brightness(current_brightness+10)
        except:
            text="looks like I don't have the permission to increase your screen brightness"
        

    #for setting brightness   
    elif commandAA.replace(" ","") in q.replace(" ",""):
        q=q.replace("set",'')
        q=q.replace("screen",'')
        q=q.replace("brightness",'')
        q=q.replace("to",'')
        q=q.replace("jarvis",'')
        if q.replace(" ","")=="":
            text="Sorry about that but I couldn't understand what should be the screen brightness"
        else:
            try:
                try:
                    q=int(q.replace(" ",''))
                    if q<0:
                        text="Sorry about that but screen brightness can't be less than 0" 
                    elif q>100:
                        text="Sorry about that but screen brightness can't be more than 100"
                    else:
                        text="okay"
                        sbc.set_brightness(q)
                except ValueError:
                    try:
                        q=int(w2n.word_to_num(q))
                        if q<0:
                            text="Sorry about that but screen brightness can't be less than 0" 
                        elif q>100:
                            text="Sorry about that but screen brightness can't be more than 100"
                        else:
                            text="okay"
                            sbc.set_brightness(q)
                    except:
                        text="Sorry about that but I couldn't understand what should be the screen brightness"

            except:
                text="looks like I don't have the permission to increase your screen brightness"

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
    
    print(text)
    speak(text)


a=input()
core(a)