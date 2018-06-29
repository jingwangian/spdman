#!/usr/bin/env python3

import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import time


# class RandomSpider(CrawlSpider):

#     name = 'RandomSpider'
#     allowed_domains = ['random.com']
#     start_urls = [
#         'http://www.random.com'
#     ]

#     rules = (
#         Rule(SgmlLinkExtractor(allow=('some_regex_here')), callback='parse_item', follow=True),
#     )

#     def __init__(self):
#         CrawlSpider.__init__(self)
#         # use any browser you wish
#         self.browser = webdriver.Firefox()

#     def __del__(self):
#         self.browser.close()

#     def parse_item(self, response):
#         item = SomeItem()
#         self.browser.get(response.url)
#         # let JavaScript Load
#         time.sleep(3)

#         # scrape dynamically generated HTML
#         hxs = Selector(text=self.browser.page_source)
#         item['some_field'] = hxs.select('some_xpath')
#         return item


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
