from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from splinter import Browser

def scrape():
    #NEWS
    url = 'https://mars.nasa.gov/api/v1/news_items/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    resp = requests.get(url)
    news_title = resp.json().get('items')[0].get('title')
    news_p = resp.json().get('items')[0].get('description')

    #IMAGE
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content,"html.parser")

    x = soup.find("div", {"class": "carousel_items"}).find('article').find("a", {"class":"button fancybox"}).get('data-fancybox-href')
    featured_image_url='https://www.jpl.nasa.gov'+ x

    #WEATHER
    url = 'https://twitter.com/marswxreport?lang=en'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content,"html.parser")

    mars_weather = soup.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}).get_text()

    #SPACE FACTS TABLE
    url = 'https://space-facts.com/mars/'
    df = pd.read_html(url)[0]
    df.columns = ['thing','value']
    data = df.to_html()

    #HEMISPHERES
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    executable_path = {'executable_path':'C:/Users/jhest/Desktop/DA_Files/WebScraping_HW/chromedriver'}
    browser = Browser('chrome', **executable_path)

    try:
        browser.visit(url)
        link = browser.find_link_by_partial_text('Cerberus')
        link.click()
        soup1 = BeautifulSoup(browser.html,"html.parser")
        browser.back()
        
        link = browser.find_link_by_partial_text('Schiaparelli')
        link.click()
        soup2 = BeautifulSoup(browser.html,"html.parser")
        browser.back()
        
        link = browser.find_link_by_partial_text('Syrtis')
        link.click()
        soup3 = BeautifulSoup(browser.html,"html.parser")
        browser.back()
        
        link = browser.find_link_by_partial_text('Valles Marineris')
        link.click()
        soup4 = BeautifulSoup(browser.html,"html.parser")
        browser.back()
        
    except Exception as e:
        print(e)
    finally:
        browser.quit()
        
    soup_list = [soup1,soup2,soup3,soup4]
    title_list = []
    href_list = []
    hemisphere_image_urls = []

    for soup in soup_list:
        title_list.append(soup.find('h2', {'class':'title'}).get_text())
        href_list.append(soup.find('a', {'target':'_blank'})['href'])

    for title, href in zip(title_list, href_list):
        hemisphere_image_urls.append({"title": title, "img_url": href})

    mars = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url, 
        'mars_weather': mars_weather,  
        'hemisphere_image_urls': hemisphere_image_urls,
        'data': data
    }

    return mars
    