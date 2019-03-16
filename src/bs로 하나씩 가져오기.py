from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/about")
bsObject = BeautifulSoup(html, 'html.parser')

print(bsObject.head.find_all('meta'))
print(bsObject.head.find('meta', {}))
print(bsObject.head.find('meta', {'name': 'description'}))
