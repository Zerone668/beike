# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo, os
from openpyxl import Workbook

name = 'beijing' # 自定义数据表、集合、文件名
class MysqlPipeline(object):

    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='xxxxx',
                                  password='xxxxx', db='mydata', charset='utf8')
        self.cursor = self.db.cursor()
        global name
        self.table = name

    def open_spider(self, spider):
        print('链接MySQL数据库...')

    def process_item(self, item, spider):
        name = item['name']
        quyu = item['quyu']
        zjia = item['zjia']
        dan1 = item['dan1']
        djia = item['djia']
        dan2 = item['dan2']
        xxxx = item['xxxx']
        star = item['star']
        tag  = item['tag']
        url  = item['url']
        sql = f"insert into {self.table}(标题,小区,总价,单位 万,单价,元/平米,详情,star,标签,链接) values({repr(name)},{repr(quyu)},{repr(zjia)},{repr(dan1)},{repr(djia)},{repr(dan2)}{repr(xxxx)},{repr(star)},{repr(tag)},{repr(url)})"
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
            '小区': item['quyu'],
            '总价': item['zjia'],
            '单位 万': item['dan1'],
            '单价': item['djia'],
            '万/平米': item['dan2'],
            '详情': item['xxxx'],
            'star': item['star'],
            '标签': item['tag'],
            '链接': item['url']
        }
        self.collection.insert_one(new)
        return item

    def close_spider(self, spider):
        print('断开MongoDB数据库链接...')


class ExcelPipeline(object):
    def __init__(self):
        global name
        self.path = f'c:/Users/小白/Desktop/{name}.xlsx'
        if os.path.exists(self.path):
            os.remove(self.path)
        # 创建excel, 填写表头
        self.wb = Workbook()
        self.ws = self.wb.active
        # 设置表头
        self.ws.append(['标题', '小区', '总价', '万', '单价', '元/平米', '详情', 'star', '标签', '链接'])

    def process_item(self, item, spider):
        # 把数据的每一项整理出来
        line = [item['name'], item['quyu'], item['zjia'], item['dan1'],
                item['djia'], item['dan2'], item['xxxx'], item['star'], item['tag'], item['url']]
        # 将数据以行的形式添加到xlsx中
        self.ws.append(line)
        # 保存xlsx文件中
        self.wb.save(self.path)
        return item
