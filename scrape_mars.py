# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser

import os
from bs4 import BeautifulSoup
import requests
import splinter
from splinter import Browser
browser = Browser("chrome", headless=False)


get_ipython().system('which chromedriver')



exectuable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser("chrome", headless=False)



# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'



# Retrieve page with the requests module
browser.visit(url)



# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
print(soup)




# Examine the results, then determine element that contains sought info
#print(soup.prettify())



news_div = soup.find('ul', class_="item_list")
news_panels = news_div.find_all("div", class_="list_text")

for panel in news_panels:
    
    title = panel.find('a').text
    text = panel.find('div', class_="article_teaser_body").text
    print(title)
    print(text)
#for title in news_titles:
    #print(title.text)




news_p = soup.find_all('div', class_="rollover_description_inner")
#for p in news_p:
    #print(p.text)



###





get_ipython().system('which chromedriver')




executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)




jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)




featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA16729_ip.jpg'
browser.visit(featured_image_url)




### Mars Weather




Mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(Mars_twitter_url)



tweet_response = requests.get(Mars_twitter_url)


tweet_soup = BeautifulSoup(tweet_response.text, 'html.parser')



#print(tweet_soup.prettify())



mars_weather = tweet_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
print("Latest Mars weather tweet is:  \n" +mars_weather.text)




### Mars Facts





#We can use the read_html function in Pandas to automatically 
#scrape any tabular data from a page.
import pandas as pd



facts_url = 'https://space-facts.com/mars/'




tables = pd.read_html(facts_url)
tables
#What we get in return is a list of 
#dataframes for any tabular data that Pandas found.




df = tables[0]
df.columns = ['Measure' , 'Value']
df.head()





df.set_index('Measure', inplace=True)
df.head()




html_table = df.to_html()
#html_table




#html_table.replace('\n', '')



df.to_html('table.html')




get_ipython().system('open table.html')



### Mars Hemisperes




# Setting url for access and scraping. 
hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hem_url)
hem_html = browser.html
hemisoup = BeautifulSoup(hem_html, 'html.parser')



# Identifying parent div's for reference in for loop
ParentDiv = hemisoup.find('div', class_='collapsible results')
results = ParentDiv.find_all('div', class_='item')




# Creating for loop to loop through four hemispheres in page and scrape date from each hemisphere
for result in results:
    # Creating empty object to house scraped data
    hemisphere = {}




# Scraping the title, descriptive blurb, and image url for each instance
title = result.find('h3').text
paragraph = result.find('p').text
imageUrl = result.find('a')['href']
imageUrl = imageUrl[11:]



# Building url for database
img_url_base = 'https://astropedia.astrogeology.usgs.gov/download'
img_url_tail = '.tif/full.jpg'
imageUrl = img_url_base + imageUrl + img_url_tail




# Appending each title, descriptive blurb, and image url for each hemisphere into the 'Hemisphere' object
hemisphere['title'] = title
hemisphere['paragraph'] = paragraph
hemisphere['imageUrl'] = imageUrl
print(hemisphere)
print("---------------------")

