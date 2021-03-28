from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    ## NASA Mars News
    # URL of page to be scraped
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    # Create Beautiful Soup object & select parser
    html = browser.html
    soup = bs(html, 'lxml')

    # Extract title text
    article = soup.find('div', class_="list_text")
    news_title = article.find('div', class_="content_title").text

    # Extract paragraph text
    news_p = article.find('div', class_="article_teaser_body").text

    ## Featured Image
    images_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html#'
    browser.visit(images_url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # Use splinter to navigate the site & find the image URL for the current featured mars image
    # assign url string to variable: featured_image_url
    find_img = soup.find('img', class_="headerimage fade-in")['src']

    # make sure to find the image url to the full size .jpg image
    # save complete url string for the image
    base_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    featured_image_url = base_url + find_img

    
    ## Mars Facts
    # define url of site to be scraped
    facts_url = 'https://space-facts.com/mars/'

    # use read_html function in pandas to scrape all tabular data
    tables = pd.read_html(facts_url)
    tables

    # slice off 1st dataframe
    marsfacts = tables[0]
    marsfacts.columns=['Category','Mars Profile']
    marsfacts.reset_index(drop=True, inplace=True)

    # generate html table from dataframe
    mars_html_table = marsfacts.to_html(index=False)

    # save directly to html file
    marsfacts.to_html('mars_facts_table.html')

    
    ## Mars Hemispheres
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)

    # establish base url variable to append links to for each image in loop
    base_url = 'https://astrogeology.usgs.gov'

    # Create empty list to store title & url info into a dictionary for each hemisphere
    mars_hemis = []

    # Iterate through all images
    #for i in range(0, 4):
    # HTML object
    html = browser.html

    # Parse HTML with beautiful soup
    soup = bs(html, 'html.parser')

    # Retrieve all elements that contain image info
    #results = soup.find('div', class_='result-list')
    images = soup.find_all('div', class_='description')

    for image in images:
        # Use BS's find() method to navigate main page to retrieve titles
        title = image.find('h3').text
        title = title.replace("Enhanced","")
        link = image.find('a')['href']
        hemi_link = base_url + link
        # Visit each page to retrieve full jpg url
        browser.visit(hemi_link)
        html = browser.html
        soup = bs(html, 'html.parser')
        wide_image = soup.find('img', class_='wide-image')
        img_url = wide_image['src']
        full_img_url = base_url + img_url
        mars_hemis.append({'Title': title, 'img_url': full_img_url})


    
    # Create single dictionary for all scraping outputs
    mars_dict = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_img': featured_image_url,
        'facts': mars_html_table, 
        'hemispheres': mars_hemis
    }

    # Quit the browser
    browser.quit()

    return mars_dict