#coding:utf-8
'''
Created on 2017年6月28日

@author:miss
'''
import scrapy
from scrapy import Selector
from scrapy import Request
from tieba.items import TiebaItem
from tieba.config import key
class Tieba(scrapy.Spider):
    name = "tiebac"
    host = "http://tieba.baidu.com/"
    start_urls = [
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=1',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=2',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=3',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=4',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=5',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=6',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=7',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=8',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=9',
        'http://tieba.baidu.com/f/search/res?ie=utf-8&qw='+key+'&rn=50&sm=1&pn=10',

      ]
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url = url,callback=self.parsePage)


    def parsePage(self,response):

        selector = Selector(response)
        # content_list3 = selector.xpath("/html/body//div[@class='s_post_list']/div[@class='s_post']")
        content_list = selector.xpath("/html/body//div[@class='s_post_list']/div[@class='s_post']/span[@class='p_title']/a")
        content_list_2 = selector.xpath("/html/body//div[@class='s_post_list']/div[@class='s_post']/div[@class='p_content']")
        i = 0
        for content in content_list:
            item = TiebaItem()
            title = content.xpath("string(.)").extract_first()
            url = content.xpath('@href').extract_first()
            content2 = content_list_2[i].xpath("string(.)").extract_first()
            i = i+1
            url = str(self.host + url)
            item['url']=url
            item['title']=title
            item['content']= content2
            print url
            print title
            yield item

        # for content2 in content_list_2:
        #     # item = TiebaItem()
        #     contents2 = content2.xpath("string(.)").extract_first()
        #     item['content']=contents2
        #     print contents2
        #     yield item
        # for content in content_list:
        #      conts = content.xpath("/span[@class='p_title']/a")
        #     # url = conts.xpath('@href').extract_first()
        #     # title = conts.xpath('string(.)').extract_first()
        #     #
        #     # # cont = content.xpath("/div[@class='p_content']")
        #     # # con = cont.xpath('string(.)').extract_first()
        #     # print url
        #     # print title
        #     # print con
        #      print conts
