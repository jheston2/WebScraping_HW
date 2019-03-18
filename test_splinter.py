from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from splinter import Browser

executable_path = {'executable_path':'/Users/Jack/Desktop/DA_Files/splinter_test/chromedriver'}
browser = Browser('chrome', **executable_path)
url = 'https://mars.nasa.gov/news/'

try:
    browser.visit(url)
    # browser.fill('q', 'splinter - python acceptance testing for web applications')
    # button = browser.find_by_name('btnK')
    time.sleep(2)
    # button.click()
    # for x in range(3):
    #     links_found = browser.find_link_by_partial_text('Next')
    #     time.sleep(1)
    #     links_found[0].click()
    # print(browser.html[:100])
    with(open('mars.html','w')) as f:
        f.write(browser.html)
    
    soup = BeautifulSoup(browser.html,"html.parser")
    news_title = soup.find_all("div", {"class": "content-title"})
    print(news_title)
    
except Exception as e:
    print(e)
finally:
    browser.quit()