#!/usr/bin/env python
# coding: utf-8

# In[223]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re


# In[224]:


# Set up splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[225]:


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles¶


# In[226]:


## Hemispheres¶


# In[227]:


# Step One Visit the mars nasa news site
url = 'https://marshemispheres.com/'
browser.visit(url)

base_url = 'https://marshemispheres.com/'
# Optional delay for loading the page
# browser.is_element_present_by_css('div.list_text', wait_time=1)

# scrape pages
html=browser.html
html_soup = soup(html, 'html.parser')
#html_soup

divs=html_soup.select('div.item > a')
for link in divs:
    print(link.get('href'))


# In[228]:


# Step Two - create list to hold .jpg image URL and title for each hemisphere image
hemisphere_image_urls = []


# In[229]:


# Step 3, write code to retrieve the full-resolution image URL and title for each hemisphere image. 
# The full-resolution image will have the .jpg extension
# scrape the four urls that contain links to the full images

for link in divs:
    hemispheres={}
    url=base_url + link['href']
    browser.visit(url)
    html=browser.html
    html_soup = soup(html, 'html.parser')
    img_url = html_soup.find_all(href=re.compile(".jpg"))
    #print(img_url)
    for img_link in img_url:
        img_link = base_url + img_link.get('href')
    #print(img_link)
    img_title = html_soup.find('h2').text
    #print(img_title)
    hemispheres={'img_url': img_link, "title" : img_title}
    #print(hemispheres)
    hemisphere_image_urls.append(hemispheres) 


# In[230]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[231]:


# 5. Quit the browser
browser.quit()


# In[6]:


slide_elem.find('div',class_='content_title')


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


df.to_html()


# In[15]:


browser.quit()


# In[ ]:





# In[ ]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:





# Visit the NASA Mars News Site

# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[ ]:


# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')


# In[ ]:


slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# JPL Space Images Featured Image

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[ ]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# In[ ]:





# In[ ]:





# In[ ]:




