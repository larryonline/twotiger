# -*- coding: utf-8 -*-

BOT_NAME = 'TwoTiger'

SPIDER_MODULES = ['twotiger.spiders']
NEWSPIDER_MODULE = 'twotiger.spiders'


# setup for crawlera
DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 300}
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = '743b2fd9b81841dfadced2d7217d5401'

CONCURRENT_REQUESTS = 32
CONCURRENT_REQEUSTS_PRE_DOMAIN = 32
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600

# cache and robots
ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True
