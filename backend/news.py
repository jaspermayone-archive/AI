import bs4
from urllib.request import urlopen

def news():
    url = "https://news.google.com/news/rss"
    client = urlopen(url)
    xml_page = client.read()
    client.close()
    page = bs4.BeautifulSoup(xml_page, 'xml')
    news_list = page.findAll("item")
    headlines=""
    for news in news_list:
        headlines+=news.title.text
    return headlines                   