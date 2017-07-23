#coding:utf-8
'''
Created on 2017年6月20

@author: miss
'''
import scrapy
import re
from scrapy import Selector
from scrapy import Request
import json
from weibo.items import WeiboItem
from weibo.config import key
class Weibo(scrapy.Spider):
    name="weiboseh"
    # host="http://s.weibo.com/weibo/key&typeall=1&suball=1&Refer=g"
    host = "https://m.weibo.cn/status/"#+id
    start_urls={
        # "http://s.weibo.com/weibo/台风苗柏&typeall=1&suball=1&Refer=g",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=1",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=2",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=3",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=4",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=5",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=6",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=7",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=8",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=9",
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type=60%26q="+key+"&title=热门-"+key+"&cardid=weibo_page&page=10",
    }

    def parse(self,response):
        jdict = json.loads(response.body)
        jcontent = jdict["cards"]
        jpresult = jcontent[0]
        jresult = jpresult["card_group"]
        urls=[]


        for each in jresult:
            #print each['positionId']
            #                 item = LagouItem()
            item = WeiboItem()
            # print each['positionName']
            blog = each["mblog"]
            name = blog['user']['screen_name'].encode('utf-8')
            content = blog['text'].encode('utf-8')
            time=blog["created_at"].encode('utf8')
            item['name'] = name
            item['content'] = content
            item['time'] = time
            yield item
            print name
            print content
            # print time
            print ''

            # print each['companyFullName']
            # url="https://www.lagou.com/jobs/"+str(each['positionId'])+".html"
            # urls.append(url)
            # item['url']=url
            #
            # print url


