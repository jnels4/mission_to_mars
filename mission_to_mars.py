#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Import Splinter and beautiful soup

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[10]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


#visit mars news nasa site

url='https://redplanetscience.com'

browser.visit(url)

#Optional delay for loading the page

browser.is_element_present_by_css('div.list_text', wait_time = 1)


# In[20]:


html = browser.html

news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[21]:


slide_elem.find('div', class_='content_title')


# In[22]:


news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[24]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

news_p


# ### Featured Imagines
# 

# In[25]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[26]:


# find and click the ful image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[29]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[32]:


img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')


img_url_rel


# In[33]:


img_url=f'https://spaceimages-mars.com/{img_url_rel}'


# In[35]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)

df


# In[36]:


df.to_html()


# In[37]:


browser.quit()


# In[ ]:




