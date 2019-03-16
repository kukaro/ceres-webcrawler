from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://naver.com')
bsObject = BeautifulSoup(html, 'html.parser')

div_list = bsObject.select('div > div > h3')

for key, value in enumerate(div_list):
    print('%i:%s' % (key, value))
