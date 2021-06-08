from bs4 import BeautifulSoup
import requests

def search(query):
    USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36/10csO9CgK-99'
    query=query
    URL= f'https://www.google.com/search?q={query}&num=1'
    headers={"user-agent":USER_AGENT}
    requests_session = requests.Session()
    resp=requests_session.get(URL,headers=headers)
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,"lxml")
        results=[]
        for g in soup.find_all('div',class_="yuRUbf"):
            anchors=g.find_all('a')
            if anchors:
                link=anchors[0]['href']
                results=link
        return results
