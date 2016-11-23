# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NYtimesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()

    category = scrapy.Field()

    title = scrapy.Field()

    author = scrapy.Field()

    date = scrapy.Field()

    article = scrapy.Field()
