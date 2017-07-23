#coding:utf-8
'''
Created on 2017年6月18日

@author: miss
'''
import pprint

import scrapy
import re
from scrapy import Selector
from scrapy import Request
import newsbaidu.settings
from newsbaidu.items import NewsbaiduItem,logsItem
from newsbaidu.config import key
from newsbaidu.config import id
import json
# import logging
# from scrapy.xlib.pydispatch import dispatcher
# from scrapy.linkextractors import LinkExtractor
# from scrapy import signals
from newsbaidu.statscolle import StatsCollector
from datetime import datetime
import time
class NewsBaidu(scrapy.Spider):
    # statsco = StatsCollector(StatsCollector,crawler=settings)

    # itemlog = logsItem()
    #
    # def __init__(self,rule):
    #     #spider启动信号和spider_opened函数绑定
    #     dispatcher.connect(self.spider_opened, signals.spider_opened)
    #     #spider关闭信号和spider_spider_closed函数绑定
    #     dispatcher.connect(self.spider_closed, signals.spider_closed)
    # #spider关闭时的逻辑
    # def spider_closed(self, spider):
    #     print "spider is closed!"
    #     self.itemlog['count'] = self.count
    #     self.itemlog['endTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     yield logsItem
    #
    # #spider启动时的逻辑
    # def spider_opened(self, spider):
    #     print "spider is running!"
    #     self.itemlog['startTime']=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = "newsb"
    startTime =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    id = id
    count = 0
    isend = 0
    runresult = 1
    # starInfoUrl = "http://localhost:8089/rest/restJob/jobStart?jobId=10004"
    host = "http://www.baidu.com/s?wd=key&rsv_bp=0&rsv_spt=3&rsv_n=2&inputT=6391"
    start_urls = [
        "http://localhost:8089/rest/restJob/jobStart?jobId="+str(id),
        "http://news.baidu.com/ns?word="+key+"&pn=0&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",
        "http://news.baidu.com/ns?word="+key+"&pn=50&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",
        "http://news.baidu.com/ns?word="+key+"&pn=100&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",
        "http://news.baidu.com/ns?word="+key+"&pn=150&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",
        "http://news.baidu.com/ns?word="+key+"&pn=200&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",
        "http://news.baidu.com/ns?word="+key+"&pn=250&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",
        "http://news.baidu.com/ns?word="+key+"&pn=300&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",
        "http://news.baidu.com/ns?word="+key+"&pn=350&cl=2&ct=0&tn=news&rn=50&ie=utf-8&bt=0&et=0",


    ]
    def start_requests(self):
        # Request(url=self.starInfoUrl,callback= self.parseId)
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse_page)

    # def parseId(self,response):
    #     content = json.load(response)
    #     self.id = content['message']
    def parse_page(self,response):
        self.isend = self.isend + 1
        if(self.isend == 1):
            content = json.loads(response.body)
            self.id = content['message']
        else:
            selector = Selector(response)
            content_list = selector.xpath("//div[@class='result']/h3/a")
            content_list2 = selector.xpath("//div[@class='result']//p[@class='c-author']")
            i = 0
            for content in content_list:
                item = NewsbaiduItem()
                url = content.xpath('@href').extract_first()
                title = content.xpath('string(.)').extract_first()
                content2 = content_list2[i].xpath('string(.)').extract_first()
                author = content2.encode('utf8')
                i = i+1
                #print url
                #print title
                # print author
                item['url'] = url
                item['title'] = title
                item['author'] = content2
                self.count = self.count+1
                yield item
            if(self.isend >=9 ):
                eid = self.id
                if(self.count<400):
                    self.runresult=0
                else:
                    self.runresult=1
                cocount = self.count
                time.sleep(5)
                endurl = "http://localhost:8089/rest/restJob/jobEnd?id="+str(eid)+"&runResult="+str(self.runresult)+"&collectionCount="+str(cocount)
                yield Request(url=endurl)

        # info = self.statsco.get_stats(StatsCollector,spider=NewsBaidu)
        # pprint.pformat(info)

    # def closed(self):
    #
		#
    # def CollectStats(self):
    #     print self.start
    #     print self.count
    #     endTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     print endTime


        # for content2 in content_list2:
        #     content2 = content2.xpath('string(.)').extract_first()
        #     content1 = content2.encode('utf8')
        #     print content1
    # # start_urls = [
    #
    #      "http://news.baidu.com/ns?word=郑州大专&tn=newsfcu&from=news&cl=2&rn=50&ct=0"
    #
    #
    # ]
    #
    # def start_requests(self):
    #     # sekey= raw_input("Enter your search key: ")
    #     for url in self.start_urls:
    #         # url.replace('key', '福大')
    #         # strinfo = re.compile('key')
    #
    #
    #         # url = strinfo.sub(sekey,url)
    #         yield Request(url=url, callback=self.parse_page)
    #
    # def parse_page(self, response):
    #     # time.sleep(3)
    #     selector = Selector(response)
    #
    #     # for i in range(5):
    #     content_list = selector.xpath("/html/body/div[@class='baidu']/a")
    #     # content_list2 = selector.xpath("//h3[@class='t c-gap-bottom-small']/a")
    #     # items=[]
    #     # for i in range(len(content_list)+len(content_list2)):
    #     #     item = BaiduItem()
    #     for content in content_list:
    #         item = NewsbaiduItem()
    #         url = content.xpath('@href').extract_first()
    #         title = content.xpath('string(.)').extract_first()
    #         print url
    #         print title
    #         item['title'] = title
    #         item['url'] = url
    #         yield item
        # for content2 in content_list2:
        #     item = BaiduItem()
        #     url = content2.xpath('@href').extract_first()
        #     title = content2.xpath('string(.)').extract_first()
        #     item['title'] = title
        #     item['url'] = url
        #     print url
        #     print title
        #     yield item