import bs4 as bs
import urllib.request
from time import sleep
from datetime import datetime
prev_t = []
titles = {}
artists = {}

def send_to_dict(element,Dict):
    if element not in Dict:
        Dict[element] = 1
    else:
        Dict[element] += 1

while True:
    source = urllib.request.urlopen('http://duke.fm/music/trackhistory/?page=1').read()
    soup = bs.BeautifulSoup(source,'html.parser')
    title = soup.find_all('span',{'class':'gmod-list-title'})
    artist = soup.find_all('span',{'class':'gmod-list-metadata'})
    time = soup.find_all('span',{'class':'gmod-list-time'})
    newtitles = 0
    for i in range(len(title)):
        title_s = title[i].string
        artist_s = '!' + artist[i].string
        if title_s not in prev_t:
            send_to_dict(title_s,titles)
            send_to_dict(artist_s.replace('!by ','').replace('!',''),artists)
            newtitles +=1
    prev_t = []
    for titl in title:
        prev_t.append(titl.string)

    def SortByCount(Dict):
        Ordered = sorted(Dict.items(), key = lambda t:t[1], reverse=True)
        return Ordered

    OrderedT = SortByCount(titles)
    OrderedA = SortByCount(artists)
    
    titlefile = open('Titles.txt','w')
    for i in range(len(titles)):
        line = '%s : %s\n'%(OrderedT[i][0],OrderedT[i][1])
        titlefile.write(line)
    titlefile.close()
    artistfile = open('Artists.txt','w')
    for i in range(len(artists)):
        line = '%s : %s\n'%(OrderedA[i][0],OrderedA[i][1])
        artistfile.write(line)
    artistfile.close()
    print('last read at %s'%(datetime.now().strftime('%m-%d %H:%M:%S')))
    print('%s titles added'%(newtitles))
    print('Totals: %s songs, %s artists'%(len(titles),len(artists)))
    sleep( 1800 )
