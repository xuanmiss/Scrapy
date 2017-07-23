# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime

class NewsbaiduPipeline(object):
    def process_item(self, item, spider):
        return item

    def open_spider(self,spider):
      spider.logger.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
