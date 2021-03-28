# Web Scraping Homework - Mission to Mars

In this assignment, I was tasked with building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.


## Step 1 - Scraping

Initial scraping was done using Jupyter Notebook, BeautifulSoup, Pandas & Requests/Splinter:

### NASA Mars News
* I scraped the NASA Mars News Site & collected the latest news title & paragraph text.

### JPL Mars Space Images - Featured Image

* I visited the url for JPL Featured Space Image & used splinter to navigate the site and find the image url for the current Featured Mars Image.


### Mars Facts

* I went to the Mars Facts Webpage & used Pandas to scrape the table containing facts about the planet including diameter, mass, etc. & convert the data to an HTML table string.

### Mars Hemispheres

* I visited the USGS Astrogeology site to obtain high resolution images for each of Mars' hemispheres.

* I created a loop to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* I saved both the image url string for above image & title containing corresponding hemisphere name using a Python dictionary & appended the dictionary with the image url string & corresponding title to a list; the list contained one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application

Once the initial scraping was completed, I used MongoDB w/ Flask templating to create a new HTML page displaying all the information that was obtained.

* First, I converted my Jupyter notebook into a Python script called "scrape_mars.py" with a function called "scrape" that executed all of hte scraping code from above & returned a single Python Dictionary containing all of the scraped data.

* Next, I created a route called '/scrape' that imported the 'scrape_mars.py' script & called the 'scrape' function.  I stored this return value in Mongo as a Python dictionary.

* I also created a root route '/' that queried the new Mongo database & passed the data innto an HTML template to display the data.

* Finally, I created a template HTML file called 'index.html' that takes the mars data dictionary & displays all of that data in appropriate HTML elements.
