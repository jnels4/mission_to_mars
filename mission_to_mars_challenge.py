#!/usr/bin/env python
# coding: utf-8

# In[82]:


# Import Splinter and beautiful soup

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


# In[83]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


#visit mars news nasa site

url='https://redplanetscience.com'

browser.visit(url)

#Optional delay for loading the page

browser.is_element_present_by_css('div.list_text', wait_time = 1)


# In[5]:


html = browser.html

news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[6]:


slide_elem.find('div', class_='content_title')


# In[7]:


news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

news_p


# ### Featured Imagines
# 

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# find and click the ful image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')


img_url_rel


# In[13]:


img_url=f'https://spaceimages-mars.com/{img_url_rel}'


# In[14]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)

df


# In[15]:


df.to_html()


# In[ ]:





# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[84]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

browser.is_element_present_by_css('div.list_text', wait_time = 1)


# In[147]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

html = browser.html
hq_img_soup = soup(html, 'html.parser')

hq_img_url_rel = hq_img_soup.find('div', class_='result-list')#.all()#.get('src')

all_img = hq_img_url_rel.find_all('img')

all_title = hq_img_url_rel.find_all('h3')

for x in range (0,len(all_img)):
    hemispheres = {}
    hq_title = all_title[x].text.strip()
    hq_img = all_img[x].get('src')
    hq_img_url=f'https://marshemispheres.com/{hq_img}'
    
    
    
    
    #get full image link
    full_image_elem = browser.find_by_tag('img')[x+3]
    full_image_elem.click()
    
    html = browser.html
    full_img_soup = soup(html, 'html.parser')
    full_img_url_rel = full_img_soup.find('div', class_='downloads')
    find_full_img = full_img_url_rel.find_all('a')
    full_img_loc = find_full_img[0].get('href')
    full_img_url = f'https://marshemispheres.com/{full_img_loc}'
    hemispheres ={'img_url': full_img_url,
                 'title':hq_title}
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()







# In[141]:


#hq_img_url_rel

len(all_img)


# In[148]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[149]:


browser.quit()


# In[133]:


#testing and notes below this cell

full_image_elem = browser.find_by_tag('img')[4]
full_image_elem.click()


# In[135]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[136]:


img_url_rel = img_soup.find('div', class_='downloads')

img_url_rel


# In[137]:


find_img = img_url_rel.find_all('a')
find_img


# In[138]:


find_img[0].get('href')


# In[118]:


browser.back()


# In[132]:


img_url_rel = img_soup.find('div', class_='wide_image_wrapper')

print(img_url_rel)


# In[ ]:




