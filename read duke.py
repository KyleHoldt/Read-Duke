import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://duke.fm/music/trackhistory/?page=1').read()
soup = bs.BeautifulSoup(source,'lxml')
'''
table = soup.table
# or table = soup.find('table')
table_rows = table.find_all('tr')
for tr in table_rows:
    rd = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
'''
'''
divs = soup.find_all('div')

for tr in divs.find('span'):
    print(tr.text)
'''

spans = soup.div.find_all('span')

for span in spans:
    print(span.text)
