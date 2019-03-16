from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://naver.com')
bsObject = BeautifulSoup(html,'html.parser')

print(bsObject.head.title)