import bs4 as bs
import urllib.request
import numpy as np

source = urllib.request.urlopen('http://duke.fm/music/trackhistory/?page=1').read()
soup = bs.BeautifulSoup(source,'html.parser')

title = soup.find_all('span',{'class':'gmod-list-title'})
artist = soup.find_all('span',{'class':'gmod-list-metadata'})
time = soup.find_all('span',{'class':'gmod-list-time'})

prev_t = []
titles = {}
artists = {}

def send_to_dict(element,Dict):
    if element not in Dict:
        Dict[element] = 1
    else:
        Dict[element] = Dict[element] + 1

while True:
    for i in range(len(title)):
        title_s = title[i].string
        artist_s = '!' + artist[i].string
        if title_s not in prev_t:
            send_to_dict(title_s,titles)
            send_to_dict(artist_s.replace('!by ','').replace('!',''),artists)
    prev_t = []
    for titl in title:
        prev_t.append(titl.string)
    

