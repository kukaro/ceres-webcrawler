from selenium import webdriver
from bs4 import BeautifulSoup
import platform

driver = None
os_type = platform.platform()

if os_type.find('Darwin') == 0:
    driver = webdriver.Chrome('../chromedriver_mac64')
else:
    driver = webdriver.Chrome('../chromedriver_linux64')
driver.implicitly_wait(3)

find_url = 'https://search.naver.com/search.naver?where=article&query={{}}&ie=utf8&st=rel&date_option=2&date_from=&date_to=&board=&srchby=text&dup_remove=1&cafe_url=&without_cafe_url=&sm=tab_opt&nso=so%3Ar%2Cp%3A1w%2Ca%3Aall&t=0&mson=0&prdtype=0'
find_keyworld = '파이어 레드'


def find(url, keworld):
    url = url.replace('{{}}', keworld)
    driver.get(url)
    html = BeautifulSoup(driver.page_source, 'html.parser')
    items = html.select('ul#elThumbnailResultArea > li > dl > dd.sh_cafe_passage ')
    for key, value in enumerate(items):
        print("%i: %s" % (key, value.text))
    driver.close()


find(find_url, find_keyworld)
