
# Import Splinter and beautiful soup

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#set up splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#visit mars news nasa site

url='https://redplanetscience.com'

browser.visit(url)

#Optional delay for loading the page

browser.is_element_present_by_css('div.list_text', wait_time = 1)

# convert the bowser htm to a soup object then quit browser
html = browser.html

news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')

# use the parent element to find the first tag and save it as news title

news_title = slide_elem.find('div', class_='content_title').get_text()

#use the parent element to find the paragraph text, save as news p
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()


# ### JPL space images Featured image


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# find and click the ful image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

#parse resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

#find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

#use the base url to create an absolute url
img_url=f'https://spaceimages-mars.com/{img_url_rel}'

# Mars facts
#convert html columns to data frame
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)

df.to_html()

browser.quit()
