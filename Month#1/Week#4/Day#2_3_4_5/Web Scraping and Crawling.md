# Web Scraping And Crawling 🕷️🕸️

Web Scraping refers to data extraction from websites up on the internet. For example, it can be used to get all the items listings on an online store. Or it can be used to get data about traffic on the webserver. This data can then be used to analyze and produce statistics, or be fed to a model which helps solves problems.

## Background

A website is made up of 3 basic elements:

* the structure 🧱
* the styling 🎨
* the brain 🧠

HTML is used to define the structure of a website, CSS is used to style the website and Javascript is the brain of a website. However, we'll only be focusing on the HTML and CSS files, since they contain the data we are interested in.

### How does it work? 🤔

HTML files have unique combinations of tags and classes for each type of object within the website. These tags and classes can be used to identify and selected the data field that we want to extract from.\
To retreive these tags and classes, we can inspect elements of a website. You can do this by right clicking on the any element on a brower, as shown.\
![Inspect prompt.](https://3fxtqy18kygf3on3bu39kh93-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/How-to-inspect-element-on-Mac.png)

This will take you to inspect window within the browser.\
![Inspect window in a browser.](https://images.ctfassets.net/lzny33ho1g45/6tl0bR7Iksg9zLxaLYQZKG/6cfa0dd7ac792105a2f219273e70268b/inspect-element-tutorial-00-hero.png)

Here we can select the tags and classes of data elements that we are interested in and feed that to our program. Then, the program will itself retreive this data and store it or display it according to your settings.

### What tools are available? ⚒️

Python has multiple libraries for web scraping, such as BeautifulSoup and Scrapy. We'll be using scrapy since it is fast, allows easy filtering and can directly store data into a local file or a database.

## Scrapy 🔪

Scrapy library makes web scraping a breeze by providing high level and efficient APIs. Every scrapy library has a particular structure.

```python
📦ScrapyProject
 ┣ 📂ScrapyProject
 ┃ ┣ 📂spiders
 ┃ ┃ ┣ 📜TestSpider.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜items.py
 ┃ ┣ 📜middlewares.py
 ┃ ┣ 📜pipelines.py
 ┃ ┣ 📜settings.py
 ┃ ┗ 📜__init__.py
 ┗ 📜scrapy.cfg
```

* Main Folder will have a `.cfg` file which holds the configurations for scrapy.
* Within a sub folder, there are:
  * `__init__.py` file, which is just there for the machine to know that this is a scrapy project.
  * `spiders` folder, which holds all the spiders that are used to crawl the websites and gather data.
  * `items.py` file, which is used to define item types, each with their features that are being extracted from websites.
  * `settings.py` file, which stores the settings for this project.
  * `middlewares.py` file, which is used to modify the functionality and mechanism of spiders.
  * `pipelines.py` file, which are used to preprocess the data before storing it into the database.

A **spider** is simply a web crawler which scrapes the data from websites.

### Basic Example

Let's suppose we wish to retrieve quotes, their authors and their tags from [this](https://quotes.toscrape.com) website. For this, we would need to create a spider first. In the subfolder named `spiders`, add a `.py` file with the following code:

```python
import scrapy

class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        # filter out the div tags with class "quote"
        # this will give us all the quote block on the website
        quote_blocks = response.css('div.quote')

        for quote in quote_blocks:

            # get the text out of span tags with class "text"
            text = quote.css('span.text::text').extract()

            # get the text out of small tag within a span tag
            author = quote.css('span small::text').extract()

            # get the text out of any tag with the class "tag"
            tags = quote.css('.tag::text').extract()

            # yield the data
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }
```

* Our custom spiders inherit from the `scrapy.Spider` class.
* `name` is used to give a name to the spider so that it can be referenced when it has to be called to crawl. However, the attribute name should not be changed.
* `start_urls` is a list of urls to crawl through. The attribute name should not be changed.
* `parse` function has to be overloaded from base class. This generator function is used to provide the filter context for our data.
  * `response` holds the html file of the website.
  * The string passed in the `css` method of `response` provides the filter context. The first word "div" refers to the type of html tag we need. After the period, "quote" is the class of the tag. This  filters out all the div tags with class "quote" and is stored in `quote_blocks`.
  * Within the for loop, we can go through each block of quote, further filter out the html tags, and finally, scrape off the quote itself, its author and tags.
  * `extract` function is used to extract the string out of the filtered html file generated by the `css` method call.

To crawl using the spider you just created, open the terminal in the subfolder with the project name (in this case Pratice/Practice). Then, run the following command:

```md
scrapy crawl test
```

* `test` is the name of the spider created in the example. You would replace it whatever name you chose to give to your spider.

This will print alot of information on the terminal as it crawls through the website, filters the response and extracts the data. The following is what was extracted after running the example project.

```md
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Albert Einstein'],
 'tags': ['change', 'deep-thoughts', 'thinking', 'world'],
 'text': ['“The world as we have created it is a process of our thinking. It '
          'cannot be changed without changing our thinking.”']}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['J.K. Rowling'],
 'tags': ['abilities', 'choices'],
 'text': ['“It is our choices, Harry, that show what we truly are, far more '
          'than our abilities.”']}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Albert Einstein'],
 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles'],
 'text': ['“There are only two ways to live your life. One is as though '
          'nothing is a miracle. The other is as though everything is a '
          'miracle.”']}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Jane Austen'],
 'tags': ['aliteracy', 'books', 'classic', 'humor'],
 'text': ['“The person, be it gentleman or lady, who has not pleasure in a '
          'good novel, must be intolerably stupid.”']}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Marilyn Monroe'],
 'tags': ['be-yourself', 'inspirational'],
 'text': ["“Imperfection is beauty, madness is genius and it's better to be "
          'absolutely ridiculous than absolutely boring.”']}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Albert Einstein'],
 'tags': ['adulthood', 'success', 'value'],
 'text': ['“Try not to become a man of success. Rather become a man of '
          'value.”']}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['André Gide'],
 'tags': ['life', 'love'],
 'text': ['“It is better to be hated for what you are than to be loved for '
          'what you are not.”']}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Thomas A. Edison'],
 'tags': ['edison', 'failure', 'inspirational', 'paraphrased'],
 'text': ["“I have not failed. I've just found 10,000 ways that won't work.”"]}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Eleanor Roosevelt'],
 'tags': ['misattributed-eleanor-roosevelt'],
 'text': ['“A woman is like a tea bag; you never know how strong it is until '
          "it's in hot water.”"]}
2022-09-23 20:13:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com>
{'author': ['Steve Martin'],
 'tags': ['humor', 'obvious', 'simile'],
 'text': ['“A day without sunshine is like, you know, night.”']}
2022-09-23 20:13:45 [scrapy.core.engine] INFO: Closing spider (finished)
```

### Item Containers 🧰

Items act as a dataframe for our data. They can have preset fields in which data will be stored. These act just like dictionaries in python but are more feature rich. To define an item type, go to the `items.py` file and add this code:

```python
class PracticeItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
```

* Our custom item type inherit from the `scrapy.Item` class.
* Fields can be defined for our items as demonstrated. `text`, `author` and `tags` are fields of the dataframe.

To use this item type, we can modify our spider like this:

```python
import scrapy
from ..items import PracticeItem


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        # our dataframe
        items = PracticeItem()

        # filter out the div tags with class "quote"
        # this will give us all the quote block on the website
        quote_blocks = response.css('div.quote')

        for quote in quote_blocks:

            # get the text out of span tags with class "text"
            text = quote.css('span.text::text').extract()

            # get the text out of small tag within a span tag
            author = quote.css('span small::text').extract()

            # get the text out of any tag with the class "tag"
            tags = quote.css('.tag::text').extract()

            # store the data in dataframe
            items['text'] = text
            items['author'] = author
            items['tags'] = tags

            yield items
```

This helps ensure that the field names between databases remain consistent and hence, solidifies collaboration efforts.

### Storing the Scraped Data into XML/JSON/CSV

To store the retrieved data into json, xml or csv file, you can simply run the following command on the terminal inside the project subfolder.

```md
scrapy crawl test -o output.json
```

* `test` is the name of the spider.
* `-o` can be thought of as a key of a keyword argument, and its value is the file name with extension (in this case `output.json`).

### Storing the Scraped Data into SQLite

To store the retrieved data into a SQLite database, add the following code into `pipelines.py` file in the project subfolder:

```python
import sqlite3

class PracticePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('quotes.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS quotes_table""")
        self.cursor.execute("""CREATE TABLE quotes_table(
            quote text,
            author text,
            tags text
        )""")

    def insert_values(self, item):
        self.cursor.execute("""INSERT INTO quotes_table VALUES (?,?,?)""",
                            (
                                item['text'][0],
                                item['author'][0],
                                item['tags'][0]
                            ))
        self.connection.commit()

    def process_item(self, item, spider):
        self.insert_values(item)
        return item
```

* `create_connection` function will connect to the database, or create it if it does not exist already.
* `create_table` function will create the table for quotes, and recreate it if it already exists.
* `insert_values` will store the values into the database.
* `process_item` is for all the preprocessing needed for the data. In this case, the data is only being stored to the database.
