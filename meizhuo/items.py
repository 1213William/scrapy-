# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizhuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图集的标题
    title = scrapy.Field()
    # 图片的url，需要来进行图片的抓取
    url = scrapy.Field()
    pass
