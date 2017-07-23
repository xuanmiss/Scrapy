#coding:utf-8
'''
Created on 2017年6月18日

@author: miss
'''

# # -*- coding: utf-8 -*-
# from scrapy import Request
# from scrapy.spiders import Spider
# from scrapy_splash import SplashRequest
# from scrapy_splash import SplashMiddleware
#
#
#
# class WeiXinSpider(Spider):
#     name = 'weixin'
#     # main address since it has the fun list of the products
#     start_urls = [
#         'http://weixin.sogou.com/weixin?page={}&type=2&query=%E4%B8%AD%E5%9B%BD'.format(a) for a in xrange(1,10)
#     ]
#
#     # allowed_domains = [
#     #     'sogou.com'
#     # ]
#
#     # def __init__(self, *args, **kwargs):
#     #      super(WeiXinSpider, self).__init__(*args, **kwargs)
#
#     def start_requests(self):
#         #text/html; charset=utf-8
#         for url in self.start_urls:
#             yield SplashRequest(url
#                                 ,self.parse
#                                 ,args={'wait':'0.5'}
#                                 #,endpoint='render.json'
#                                 )
#         pass
#
#     def parse(self, response):
#         self.logger.info('now you can see the url %s' % response.url)
#         div_results = response.xpath('//div[@class="results"]/div')
#         if not div_results:
#             self.logger.error(msg='there is not any body in the %s' % response.body)
#             return
#         for div_item in div_results:
#             title = div_item.xpath('descendant::div[@class="txt-box"]//h4//text()')
#             if title:
#                 txt = ''.join(title.extract())
#                 yield {'title':txt}
#


import scrapy
import re
from scrapy import Selector
from scrapy import Request
from sys import path
from weixin.config import key
from weixin.items import WeixinItem


class ArtWeixin(scrapy.Spider):
    name = "weixin"
    host = "http://weixin.sogou.com/weixin?type=2&query=key"
    start_urls = [
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=1",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=2",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=3",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=4",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=5",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=6",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=7",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=8",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=9",
        "http://weixin.sogou.com/weixin?query="+key+"&type=2&page=10"



    ]

    def start_requests(self):
        # sekey= raw_input("Enter your search key: ")
        for url in self.start_urls:
            # url.replace('key', '福大')
            # strinfo = re.compile('key')


            # url = strinfo.sub(sekey,url)
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        # time.sleep(3)
        selector = Selector(response)

        # for i in range(5):
        content_list = selector.xpath("//div[@class='txt-box']/h3/a")
        # xpath路径如果太复杂，检索效率低下，可能会是的进程中断

        # content_list2 = selector.xpath("//h3[@class='t c-gap-bottom-small']/a")
        # items=[]
        # for i in range(len(content_list)+len(content_list2)):
        #     item = BaiduItem()
        for content in content_list:
            item = WeixinItem()
            url = content.xpath('@href').extract_first()
            title = content.xpath('string(.)').extract_first()
            print url
            print title
            item['title'] = title
            item['url'] = url
            yield item
            # for content2 in content_list2:
            #     item = BaiduItem()
            #     url = content2.xpath('@href').extract_first()
            #     title = content2.xpath('string(.)').extract_first()
            #     item['title'] = title
            #     item['url'] = url
            #     print url
            #     print title
            #     yield item