# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)

# HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text') # directly points to div tag and class list_text with all elements within it


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_= 'content_title').get_text()
news_title

# summary of paragraph
news_summary = slide_elem.find('div', class_ = 'article_teaser_body').get_text()
news_summary

# ### Featured Images

# visit url
url = 'https://spaceimages-mars.com/'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
# splinter will click image to full size
full_image_elem.click()

# parsing the automated html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# relative image url 
img_url_rel = img_soup.find('img', class_ = 'fancybox-image').get('src')
img_url_rel

# absolute img url 
img_url_abs = f'https://spaceimages-mars.com/{img_url_rel}'
img_url_abs

# grab Tables
df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace= True)
df

df.to_html()

# end 
browser.quit()




