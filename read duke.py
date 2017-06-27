import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://duke.fm/music/trackhistory/?page=1').read()
soup = bs.BeautifulSoup(source,'lxml')

for div in soup.find_all('div', class_='body'):
    print(div.text)



