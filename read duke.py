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

TitleCount = {}
ArtistCount = {}

#check if time is a repeat
history = open('test.txt','r').read()
for i in range(len(time)):
    person = '!' + artist[i].string
    person = person.replace('!by ','').replace('!','')
    row =[time[i].string,title[i].string,person]
    row_str = str(row).replace('[','').replace(']','')
    if row_str not in history:  
        times.append(time[i].string)
        titles.append(title[i].string)
        artists.append(artist[i].string)


#submit title and artist lists

#repopulate lists with new items





List = open('test.txt','a')
data = []
for i in range(len(titles)):
    person = '!' + artists[i].string
    person = person.replace('!by ','').replace('!','')
    data.append([times[i].string,titles[i].string,person])
    data_str = str(data[i]).replace('[','').replace(']','')
    List.write(data_str+'\n')
    
List.close()

print('%d lines added'%(len(titles)))
try:
    print('looking for format: %s \nwriting format: %s'%(row_str,data_str))
except NameError:
    print('looking for format: %s\nno new lines were written'%(row_str))







