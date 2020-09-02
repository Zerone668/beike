# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangzuItem(scrapy.Item):
    name = scrapy.Field()
    quyu = scrapy.Field()
    price = scrapy.Field()
    dan = scrapy.Field()
    url = scrapy.Field()
    xxxx = scrapy.Field()
    fuli = scrapy.Field()
    cf = scrapy.Field()