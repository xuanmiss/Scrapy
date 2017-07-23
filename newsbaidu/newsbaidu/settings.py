# -*- coding: utf-8 -*-

# Scrapy settings for newsbaidu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'newsbaidu'

SPIDER_MODULES = ['newsbaidu.spiders']
NEWSPIDER_MODULE = 'newsbaidu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsbaidu (+http://www.yourdomain.com)'
LOG_FILE="log2.json"
LOG_LEVEL="INFO"
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
from scrapy.exporters import JsonLinesItemExporter  , CsvItemExporter
class CustomJsonLinesItemExporter(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super(CustomJsonLinesItemExporter, self).__init__(file, ensure_ascii=False, **kwargs)

#这里只需要将超类的ensure_ascii属性设置为False即可
#同时要在setting文件中启用新的Exporter类
class customcsvLinesItemExporter(CsvItemExporter):
    def __init__(self, file,  **kwargs):
        super(CsvItemExporter, self).__init__(file, ensure_ascii=False,**kwargs)
FEED_EXPORTERS = {
    'json': 'newsbaidu.settings.CustomJsonLinesItemExporter',
    'csv': 'newsbaidu.settings.CustomJsonLinesItemExporter',
}
ITEM_PIPELINES = {
    'newsbaidu.pipelines.NewsbaiduPipeline': 1,
}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8'
    # 'Cookie': 'BAIDUID=F5D2B350CD4C8CF318A6C7996E1D4985:FG=1; BIDUPSID=F5D2B350CD4C8CF318A6C7996E1D4985; PSTM=1488978570; __cfduid=d401c041644b30ae82d3ffcbd7ffe8f791495390048; BDUSS=WdVN0VGeU9ielp3T1Q5b2l5SzBzckNiem9lRE5IRUJiWXdCU0tOTlZkWkM3bUZaSVFBQUFBJCQAAAAAAAAAAAEAAADwv4sk0PltaW5lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEJhOllCYTpZT; LOCALGX=%u798F%u5DDE%7C%33%33%37%33%7C%u798F%u5DDE%7C%33%33%37%33; locale=zh; BDRCVFR[V-PzB8QWBwm]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[yVI6aa0RE20]=mk3SLVN4HKm; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_e9e114d958ea263de46e080563e254c4=1497606263,1497757169; Hm_lpvt_e9e114d958ea263de46e080563e254c4=1497757169; BD_CK_SAM=1; PSINO=3; BDSVRTM=113; H_PS_PSSID=',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'newsbaidu.middlewares.NewsbaiduSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'newsbaidu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'newsbaidu.pipelines.NewsbaiduPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
