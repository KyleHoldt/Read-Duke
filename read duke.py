import bs4 as bs
import urllib.request
import numpy as np
source = urllib.request.urlopen('http://duke.fm/music/trackhistory/?page=1').read()
soup = bs.BeautifulSoup(source,'html.parser')

title = soup.find_all('span',{'class':'gmod-list-title'})
artist = soup.find_all('span',{'class':'gmod-list-metadata'})
time = soup.find_all('span',{'class':'gmod-list-time'})

titles = []
artists = []
times = []
def enlist(name, listname):
    for i in name:
        listname.append(i.string)
enlist(title,titles)
enlist(artist,artists)
enlist(time,times)
'''
List = open('play_info.txt','a')
for i in range(len(titles)):
    ii = times[i] + '\t' + titles[i] + '\t' + artists[i].replace('by ','') + '\n'
    List.write(ii)    
List.close()

'''
List = open('test.txt','a')
data = []
for i in range(len(titles)):
    row[i] = (times[i],titles[i],artists[i])
    data.append(row[i])
List.write(data)    
List.close()
