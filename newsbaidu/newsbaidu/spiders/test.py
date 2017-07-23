import scrapy
from scrapy import Request
class testSpider(scrapy.Spider):
    name = "test"
    start_urls=[
        "http://localhost:8089/rest/restJob/jobStart?jobId=10004"
    ]
    def parse(self,response):
        pass
