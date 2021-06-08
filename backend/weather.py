from bs4 import BeautifulSoup
import requests

def weather(city):    
    url = f"https://www.google.com/search?q=weather{city}" 
    html = requests.get(url).content
    soup = BeautifulSoup(html,"lxml")
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    pos = strd.find('Wind')
    other_data = strd[pos:]
    result = f'The temperature is currently {temp.replace("C", "celcius")} and the sky is now {sky}'
    return result

    