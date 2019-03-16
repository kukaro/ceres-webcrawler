from selenium import webdriver
import platform

driver = None
os_type = platform.platform()

if os_type.find('Darwin')==0:
    driver = webdriver.Chrome('../chromedriver_mac64')
else:
    driver = webdriver.Chrome('../chromedriver_linux64')
# driver = webdriver.PhantomJS('../phantomjs-2.1.1-macosx/bin/phantomjs')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)
driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('mypassword1234')
driver.implicitly_wait(3)
driver.close()