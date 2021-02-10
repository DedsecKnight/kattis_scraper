# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KattisScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    letter = scrapy.Field()
    difficulty = scrapy.Field()

class AlertItem(scrapy.Item):
    notification = scrapy.Field()

class ContestID(scrapy.Item):
    cid = scrapy.Field()
