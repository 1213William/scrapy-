# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from fake_useragent import UserAgent
from meizhuo.items import MeizhuoItem

headers = {
    'user-agent': UserAgent(verify_ssl=False).chrome
}


class MzSpider(scrapy.Spider):
    name = 'mz'
    allowed_domains = ['www.win4000.com']
    start_urls = [
        # 'http://www.win4000.com/wallpaper_2285_0_0_1.html',
        # 'http://www.win4000.com/wallpaper_204_0_0_1.html',
        # 'http://www.win4000.com/wallpaper_205_0_0_1.html'
    ]

    def parse(self, response):
        sel = Selector(response)
        list = sel.xpath('//*[@class="list_cont Left_list_cont"]/div/div/div/ul/li/a')

        for img in list:
            # 这个是每个图集得到的url
            url = img.xpath('@href').extract_first()
            title = img.xpath('@title').extract_first()
            # 对我的每一个URL进行解析
            yield scrapy.Request(url, callback=self.get_all_img, meta={'title': title})
        # 对于下一页进行定位，如果存在就进行跳转
        next_url = sel.xpath('//*[@class="next"]/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)

    def get_all_img(self, response):
        item = MeizhuoItem()

        container = []
        sel = Selector(response)
        # 这个是所有照片的所有的总共的页数
        img_list = sel.xpath('//*[@class="scroll-img-cont"]/ul')
        for img in img_list:
            img_url = img.xpath('li/a/img/@data-original').extract()
            for url in img_url:
                # 这个url还是需要经过处理的，所以要循环出来挨个进行修改
                cmp_url = url.split('_')[0] + '.jpg'
                container.append(cmp_url)
            item['url'] = container
            item['title'] = response.meta['title']
            # print(container)

            yield item
            container.clear()

