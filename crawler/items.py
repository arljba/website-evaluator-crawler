# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WebCheckScraperItem(scrapy.Item):
    url_src = scrapy.Field()
    url_dest = scrapy.Field()
    status = scrapy.Field()
