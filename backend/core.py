#The core.py file contains all commands for jarvis but some commands are also present in app.py
from .search import *
from .location import *
from .weather import *
from .news import *
from .password import *
from .chat import *
from pysimilar import compare
from word2number import w2n
from PyDictionary import PyDictionary
import screen_brightness_control as sbc
import wikipedia  
import webbrowser
import pyjokes
import datetime
from youtubesearchpython import VideosSearch


#commands for introduction
commandA='who are you'
commandB='what is your name'
commandC='who is jarvis'
commandD='jarvis who is jarvis'
commandE='introduce yourself'
#commands for telling jokes
commandF='tell me a joke'
commandG='make me laugh'
#commands for telling time
commandH='what is the time'
commandI='tell me the time'
#commands for telling location
commandJ='where am i'
commandK='tell me my location'
#commands for telling weather of the current city
commandL='how is the weather'
commandM='tell me about the weather'
#commands for telling weather of the required city
commandL2='how is the weather in'
commandM2='tell me about the weather of'
#commands for greeting
commandN='how are you'
#commands for news
commandO='what happened today'
commandP='tell me about the news'
#commands for asking question
commandQ='who is'
commandR='what is'
#commands for reducing brightness
commandS='reduce the brightness'
commandT='reduce the screen brightness'
commandU='reduce screen brightness'
commandV='reduce brightness'
#commands for increasing brightness
commandW='increase the brightness'
commandX='increase the screen brightness'
commandY='increase screen brightness'
commandZ='increase brightness'
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
#commands for telling meaning
commandAH="what is the meaning of"
commandAI="meaning of"
#bit of chat
chatA="are you there"
chatB="are you up"


def core(query):
    q=query.lower()
    q=query.replace(".","")

    #for 0 input
    if q.replace(" ","")=="":
        text="Sorry about that I didn't hear anything"
        

    #for introduction
    elif compare(commandA,q)>0.65 or compare(commandB,q)>0.65  or compare(commandC,q)>0.65 or compare(commandD,q)>0.65 or compare(commandE,q)>0.65 or commandA.replace(" ","") in q.replace(" ","") or commandB.replace(" ","") in q.replace(" ","") or commandC.replace(" ","") in q.replace(" ","") or commandD.replace(" ","") in q.replace(" ","") or commandE.replace(" ","") in q.replace(" ",""):
        if q.replace(" ","")=="whois" or q.replace(" ","")=="whatis" or q.replace(" ","")=="jarviswhois" or q.replace(" ","")=="jarviswhatis":
            text="Please tell me what do you want to know about"
        else:
            text="Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week"
        

    #for greeting
    elif compare(commandN,q)>0.65 or commandN.replace(" ","") in q.replace(" ",""):
        text="I am fine, how may I help you"

    #for telling meaning
    elif commandAH.replace(" ","") in q.replace(" ","") or commandAI.replace(" ","") in q.replace(" ",""):
        q=q.replace(commandAH,"")
        q=q.replace(commandAI,"")
        q=q.replace('jarvis',"")
        if q.replace(" ","")=="":
            text="Sorry about that but I could not hear which word's meaning you want to know"
        else:
            dictionary=PyDictionary()
            dic=dictionary.meaning(q)
            try:
                text=dic['Noun'][0]
                text=f"The meaning of the word {q} is {text}"
            except:
                try:
                    text=dic['Verb'][0]
                    text=f"The meaning of the word {q} is {text}"
                except:
                    try:
                        text=dic['Adjective'][0]
                        text=f"The meaning of the word {q} is {text}"
                    except:
                        text=f"Sorry about that but I don't know the meaning of {q}"
            

    #bit of chat 
    elif compare(chatA,q)>0.65 or compare(chatB,q)>0.65 or chatA.replace(" ","") in q.replace(" ","") or chatB.replace(" ","") in q.replace(" ",""):
        text="For you always"

    #for telling time
    elif compare(commandH,q)>0.65  or compare(commandI,q)>0.65 or commandH.replace(" ","") in q.replace(" ","") or commandI.replace(" ","") in q.replace(" ",""):
        time=datetime.datetime.now().strftime('%I:%M %p')
        text=f'Now it is {time}'  

         
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
                text=f"According to wikipedia {wikipedia.summary(q, sentences = 5)}"
            except:
                try:
                    text="Here is what i found on the internet"
                    results=search(query.replace("jarvis",""))
                    webbrowser.open(results)
                except:
                    text="Sorry about that but I can't find the answer to your question"

    #for generaing text
    elif commandAF.replace(" ","") in q.replace(" ","") or  commandAG.replace(" ","")in q.replace(" ",""):
        quaryA=q.replace(commandAF,"")
        quaryB=quaryA.replace(commandAG,"")
        if quaryB.replace(" ","")=="":
            text="Sorry about that but i couldn't hear about what i should write"
        else:
            try:
                from .story import story
                written=story(quaryB,char=1000)
                if written==quaryB:
                    text=f"Sorry about that but i don't anything about this"
                else:
                    text=f"Here is what i have written, {written}"
            except:
                text=f"Sorry about that but i don't anything about this"
             
    #for creating passwords
    elif compare(commandAB,q)>0.65 or compare(commandAC,q)>0.65 or compare(commandAD,q)>0.65 or compare(commandAE,q)>0.65 or commandAB.replace(" ","") in q.replace(" ","") or commandAC.replace(" ","") in q.replace(" ","") or commandAD.replace(" ","") in q.replace(" ","") or commandAE.replace(" ","") in q.replace(" ",""):
        result=password()
        text=f"You can use {result} as your password"


    #for telling joke
    elif compare(commandF,q)>0.65 or commandF.replace(" ","") in q.replace(" ","") or compare(commandG,q)>0.65 or commandG.replace(" ","") in q.replace(" ","") :
        text=pyjokes.get_joke(language='en', category= 'all')
        

    #for reducing brightness
    elif compare(commandS,q)>0.65 or compare(commandT,q)>0.65 or compare(commandU,q)>0.65 or compare(commandV,q)>0.65 or commandS.replace(" ","") in q.replace(" ","") or commandT.replace(" ","") in q.replace(" ","") or commandU.replace(" ","") in q.replace(" ","") or commandV.replace(" ","") in q.replace(" ",""):
        try:
            current_brightness = sbc.get_brightness()
            if current_brightness==0:
                text="Your screen brightness is already at it's lowest level"
            else:
                text="Okay"
                sbc.set_brightness(current_brightness-10)
        except:
            text="Looks like I don't have the permission to reduce your screen brightness"

    #for increasing brightness
    elif compare(commandW,q)>0.65 or compare(commandX,q)>0.65 or compare(commandY,q)>0.65 or compare(commandZ,q)>0.65 or commandW.replace(" ","") in q.replace(" ","") or commandX.replace(" ","") in q.replace(" ","") or commandY.replace(" ","") in q.replace(" ","") or commandZ.replace(" ","") in q.replace(" ",""):
        try:
            current_brightness = sbc.get_brightness()
            if current_brightness==100:
                text="Your screen brightness is already at it's highest level"
            else:
                text="Okay"
                sbc.set_brightness(current_brightness+10)
        except:
            text="Looks like I don't have the permission to increase your screen brightness"
        

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
                        text="Okay"
                        sbc.set_brightness(q)
                except ValueError:
                    try:
                        q=int(w2n.word_to_num(q))
                        if q<0:
                            text="Sorry about that but screen brightness can't be less than 0" 
                        elif q>100:
                            text="Sorry about that but screen brightness can't be more than 100"
                        else:
                            text="Okay"
                            sbc.set_brightness(q)
                    except:
                        text="Sorry about that but I couldn't understand what should be the screen brightness"

            except:
                text="Looks like I don't have the permission to increase your screen brightness"

    #for telling news
    elif commandO.replace(" ","") in q.replace(" ","") or commandP.replace(" ","") in q.replace(" ","") or q.replace(" ","") == "news":
        try:
            
            text=news()
            
        except:
            text="Sorry about that but I couldn't access the server"
            
    
    #for telling location
    elif compare(commandJ,q)>0.65 or  compare(commandK,q)>0.65 or commandJ.replace(" ","") in q.replace(" ","") or commandK.replace(" ","") in q.replace(" ",""):
        try:
            locate=location()
            locate=str(locate)
            text=f'You are currently in {locate}'
        except:
            text="Sorry about that but I couldn't access the server"

    #for telling weather of the required city
    elif commandL2.replace(" ","") in q.replace(" ","") or commandM2.replace(" ","") in q.replace(" ",""):
        try:
            city=q.replace("jarvis","").replace(" ","")
            city=city.replace(commandL2.replace(" ",""),"")
            city=city.replace(commandM2.replace(" ",""),"")
            if city.replace(" ","")=="":
                text="Which city's weather you want to know"
            else:
                text=weather(city)
        except:
            text="Sorry about that but I couldn't access the server"

    #for telling weather of the current city
    elif compare(commandL,q)>0.65 or compare(commandM,q)>0.65 or commandL.replace(" ","") in q.replace(" ","") or commandM.replace(" ","") in q.replace(" ",""):
        try:
            locate=location()
            locate=str(locate)
            locate=locate.split(",")
            city=locate[2]
            text=f'In {city} {weather(city)}'
            
        except:
            text="Sorry about that but I couldn't access the server"          

    #for playing video
    elif q.find("play")==0 or q.replace(" ","").find("jarvisplay")==0:
        q=q.replace("jarvis","")
        try:
            text="Here is what i found on the internet"
            if q.replace(" ","")=='play':
                webbrowser.open('https://www.google.com/search?q=play')
            elif q.replace(" ","")=='playmeaning':
                webbrowser.open('https://www.google.com/search?q=play+meaning')
            else:
                q=q.replace("play","")
                videosSearch = VideosSearch(q, limit = 1)
                a=videosSearch.result()
                a=a['result']
                a=str(a[0]['link'])
                webbrowser.open(a)
        except:
            text="Sorry about that but I couldn't understand which video to play"
                

    #for opening url
    elif q.find("open")==0 or q.replace(" ","").find("jarvisopen")==0:
        try:
            text="Here is what i found on the internet"
            if q.replace(' ','')=='open' or q.replace(' ','')=='jarvisopen':
                webbrowser.open('https://www.google.com/search?q=open') 
            if q.replace(' ','')=='openmeaning' or q.replace(' ','')=='jarvisopenmeaning':
                webbrowser.open('https://www.google.com/search?q=open+meaning') 
            else:
                q=q.replace("open","")
                q=q.replace("jarvis","")
                results=search(q)
                webbrowser.open(results)
        except:
            text="Sorry about that but I couldn't understand what to open"
            
    #chatting or searching the web if can't answer question
    else:
        if q.replace(" ","")=='jarvis':
            text="Hello, I am jarvis how may I help you"
        else:
            try:
                text=chat(query)
                if text=="":
                    text="Here is what i found on the internet"
                    webbrowser.open(f'https://www.google.com/search?q={query}')
                else:
                    text=text
            except:
                text="Here is what i found on the internet"
                webbrowser.open(f'https://www.google.com/search?q={query}') 
    
    print(text)
    return text


