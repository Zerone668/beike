# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from beike.items import FangzuItem


class FangSpider(CrawlSpider):
    name = 'beijing'
    allowed_domains = ['bj.ke.com']
    start_urls = ['https://bj.ke.com/ershoufang/']

    rules = (Rule(LinkExtractor(allow=r'https://bj.ke.com/ershoufang/.*/?'), callback='parse_item', follow=True),)

    def parse_item(self, response):
        res = response.css('.sellListContent li.clear')
        for rs in res:
            name = rs.css('.title a::text').get()          # 标题
            url = rs.css('.title a::attr(href)').get()     # 链接
            quyu = rs.css('.positionInfo a::text').get()   # 区域，小区
            zjia = rs.css('.totalPrice span::text').get()  # 总价
            jia1 = rs.css('.totalPrice::text').get()       # 万
            djia = rs.css('.unitPrice span::text').get()
            jia2 = djia[-4:]                               # 元/平米
            djia = djia[2:-4]                              # 单价
            xxxx = rs.css('.houseInfo').get().replace(' ','').split('\n')[2:-1]
            xxxx = ''.join([i for i in xxxx if i != ''])   # 详细信息
            star = rs.css('.followInfo').get().replace(' ','').split('\n')[2:-1]
            star = ''.join([i for i in xxxx if i != ''])   # star
            tag  = rs.css('.tag').get()
            tag = '_'.join(re.findall('<.+>(.+)<.+>',tag)) # tag
            print('-'*30)
            item = FangzuItem(
                name=name, quyu=quyu, zjia=zjia, dan1=jia1, djia=djia, dan2=jia2, xxxx=xxxx, star=star, tag=tag, url=url)
            yield item