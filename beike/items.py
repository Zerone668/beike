# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangzuItem(scrapy.Item):
    name = scrapy.Field()
    quyu = scrapy.Field()
    zjia = scrapy.Field()
    dan1 = scrapy.Field()
    djia = scrapy.Field()
    dan2 = scrapy.Field()
    xxxx = scrapy.Field()
    star = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()