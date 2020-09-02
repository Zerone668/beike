# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from openpyxl import Workbook

name = 'wuhan' # 自定义数据表、集合、文件名
class MysqlPipeline(object):

    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root',
                                  password='6682835', db='mydata', charset='utf8')
        self.cursor = self.db.cursor()
        global name
        self.table = name

    def open_spider(self, spider):
        print('链接MySQL数据库...')

    def process_item(self, item, spider):
        name = item['name']
        quyu = item['quyu']
        pri = item['price']
        dan = item['dan']
        url = item['url']
        xxxx = item['xxxx']
        fuli = item['fuli']
        cf = item['cf']
        sql = f"insert into {self.table}(标题,区域,价格,单位,链接,详情,优势,跟进) values({repr(name)},{repr(quyu)},{repr(pri)},{repr(dan)},{repr(url)},{repr(xxxx)},{repr(fuli)},{repr(cf)})"
        #sql = f"insert into {self.table}(标题,区域,价格,单位,链接,详情,优势,跟进) values({repr(name)},{repr(quyu)},{repr(pri)},{repr(dan)},{repr(url)},{repr(xxxx)},{repr(fuli)},{repr(cf)})"
        self.cursor.execute(sql)  # 执行 SQL
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()
        print('断开MySQL数据库链接...')


class MongoPipeline:

    def __init__(self):
        global name
        self.db = pymongo.MongoClient(
            'mongodb://root:xxxxxx@localhost:27017/admin')
        self.ku = 'beike'     # 所在的数据库名
        self.jh = name        # 保存的集合名

    def open_spider(self, spider):
        print('链接MongoDB数据库...')
        self.db = self.db[self.ku]
        self.collection = self.db[self.jh]

    def process_item(self, item, spider):
        new = {
            '标题': item['name'],
            '区域': item['quyu'],
            '价格': item['price'],
            '单位': item['dan'],
            '链接': item['url'],
            '详情': item['xxxx'],
            '优势': item['fuli'],
            '跟进': item['cf']
        }
        self.collection.insert_one(new)
        return item

    def close_spider(self, spider):
        print('断开MongoDB数据库链接...')


class ExcelPipeline(object):
    def __init__(self):
        # 创建excel, 填写表头
        self.wb = Workbook()
        self.ws = self.wb.active
        # 设置表头
        self.ws.append(['标题', '区域', '价格', '单位', '链接', '详情', '优势', '跟进'])

    def process_item(self, item, spider):
        # 把数据的每一项整理出来
        line = [item['name'], item['quyu'], item['price'], item['dan'],
                item['url'], item['xxxx'], item['fuli'], item['cf']]
        # 将数据以行的形式添加到xlsx中
        self.ws.append(line)
        # 保存xlsx文件中
        global name
        self.wb.save(f'c:/Users/小白/Desktop/{name}.xlsx')
        return item
