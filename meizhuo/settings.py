# -*- coding: utf-8 -*-
from fake_useragent import UserAgent

# Scrapy settings for meizhuo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meizhuo'

SPIDER_MODULES = ['meizhuo.spiders']
NEWSPIDER_MODULE = 'meizhuo.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'meizhuo.pipelines.MeizhuoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400
}
# 下载路径
IMAGES_STORE = '/Users/mac/Documents/ttt'
# 下载延迟
DOWNLOAD_DELAY = 0.3

# 这个是需要手动加上的，通过scrapy-redis自带的pipeline将item存入redis中

# 启动redis自带的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 启用调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否在关闭spider的时候保存记录
SCHEDULER_PERSIST = True
# 使用优先级调度请求队列（默认使用）
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# 指定redis的地址和端口，有密码的需要加上密码
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
# 如果你的redis设了密码就需要加上密码，


# USER_AGENT = UserAgent(verify_ssl=False).chrome()
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'meizhuo (+http://www.yourdomain.com)'

# Obey robots.txt rules


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'meizhuo.middlewares.MeizhuoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'meizhuo.middlewares.MeizhuoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
