from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/about")
bsObject = BeautifulSoup(html, 'html.parser')

for meta in bsObject.head.find_all('meta'):
    print(meta)
    print(meta.get('content'))

'''
get메소드를 사용해서 속성으로 가져온다
'''
