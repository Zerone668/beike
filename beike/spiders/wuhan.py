# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from beike.items import FangzuItem


class FangSpider(CrawlSpider):
    name = 'wuhan'
    allowed_domains = ['wh.zu.ke.com']
    # redis_key="spider_key"
    start_urls = ['https://wh.zu.ke.com/zufang/']

    rules = (Rule(LinkExtractor(allow='.+/pg\d'), callback='parse_item', follow=True),)

    def parse_item(self, response):
        res = response.css('.content__list>div')
        for re in res:
            name = re.css(
                '.content__list--item--title a::text').get().strip()      # 标题
            url = re.css('.content__list--item--title a::attr(href)').get()
            # 链接
            url = response.urljoin(url)
            l1 = re.css('.content__list--item--des a::text').getall()
            l2 = ''.join(re.css('.content__list--item--des::text').getall())
            l2 = l2.replace('-', '').split()
            l3 = ''.join(re.css('.content__list--item--des span::text').getall())
            l3 = l3.replace('\n', '').split()
            ls1 = l1 + l2 + l3
            # quyu
            ls0 = ls1[0]
            # xxxx
            ls1 = ' '.join(ls1)
            ls2 = re.css('.content__list--item--bottom i::text').getall()
            # fuli
            ls2 = ' '.join(ls2)
            ls3 = ''.join(
                re.css('.content__list--item--brand span::text').getall())
            ls3 = ls3.replace('\n', '').split()
            # cf
            ls3 = ' '.join(ls3)
            pri = int(re.css('.content__list--item-price em::text').get())
            dan = re.css('.content__list--item-price::text').get()
            item = FangzuItem(
                name=name, quyu=ls0, price=pri, dan=dan, url=url, xxxx=ls1, fuli=ls2, cf=ls3)
            yield item
