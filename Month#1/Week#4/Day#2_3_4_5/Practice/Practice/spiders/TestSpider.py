import scrapy
from ..items import PracticeItem


class TestSpider(scrapy.Spider):
    name = 'test'
    page_number = 1
    start_urls = [f"https://quotes.toscrape.com/page/{page_number}/"]

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

        # the last page of the website is 10, so it page number should not be larger
        if TestSpider.page_number < 10:

            # increment the page number so spider can crawl to the next page
            TestSpider.page_number += 1

            # address of the next page is defined
            next_page = f'https://quotes.toscrape.com/page/{TestSpider.page_number}/'

            # spider crawls to the next page and starts scraping
            yield response.follow(next_page, callback=self.parse)
