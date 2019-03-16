from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.naver.com')
bsObject = BeautifulSoup(html, 'html.parser')

print(bsObject)

'''
url을 일단 가져와서 beautifulsoup 파서로 파싱하면됨
'''