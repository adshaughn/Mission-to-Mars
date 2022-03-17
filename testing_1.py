# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url_list = [0]

def hemi_image_1(browser):

    # Visit URL
    url = 'https://marshemispheres.com/'
    browser.visit(url)  

        # Find and click the full image button
        full_image_elem_1 = browser.find_by_tag('itemLink product-item')[1]
        full_image_elem_1.click()

        # On new page, proceed with opening up full image
        full_image_elem_2 = browser.find_by_tag('_blank')[1]
        full_image_elem_2.click()

        # Parse the resulting html with soup
        html = browser.html
        img_soup = soup(html, 'html.parser')

        # Add try/except for error handling
        try:
            # Find the relative image url
            img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

        except AttributeError:
            return None

        # Use the base url to create an absolute url
        img_url = f'marshemispheres.com/images/full/{img_url_rel}'

        return img_url
    
        print(img_soup)
    