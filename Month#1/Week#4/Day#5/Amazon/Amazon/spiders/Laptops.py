from nturl2path import url2pathname
import scrapy
from ..items import AmazonItem


class LaptopsSpider(scrapy.Spider):
    name = 'Laptops'
    page_number = 1
    start_urls = [
        f'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108&dc&page={page_number}&qid=1664284454&rnid=13896617011&ref=sr_pg_2']

    def parse(self, response):

        laptops = AmazonItem()

        laptop_divs = response.css('.s-widget-spacing-small .sg-col-inner')

        total_pages = 43

        for laptop in laptop_divs:

            name = laptop.css('.a-size-base-plus::text').extract_first()
            price_dollar = laptop.css(
                'span.a-price-whole::text').extract_first()
            price_cent = laptop.css(
                'span.a-price-fraction::text').extract_first()
            rating = laptop.css(
                '.aok-align-bottom').css('::text').extract_first()
            if rating is not None:
                rating = rating.split()[0]

            laptops['name'] = name
            laptops['price_dollar'] = price_dollar
            laptops['price_cent'] = price_cent
            laptops['rating'] = rating

            yield laptops

        print('AAAAAAAAAAAAAAAAAAA', LaptopsSpider.page_number,
              'AAAAAAAAAAAAAAAAAAAAA')

        if LaptopsSpider.page_number < total_pages:
            LaptopsSpider.page_number += 1
            next_page = f'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108&dc&page={LaptopsSpider.page_number}&qid=1664284454&rnid=13896617011&ref=sr_pg_2'
            yield response.follow(next_page, callback=self.parse)
