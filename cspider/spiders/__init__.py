# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from cspider.items import CspiderItem

class MySpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['epa.gov']
    start_urls = ['http://www.epa.gov/cromerr/']

    rules = [Rule(LinkExtractor(allow='cromerr'), follow=True, callback='parse_item')]
        #Rule(LinkExtractor(allow=(r'cromerr/(\w+/?)+')))]
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        #Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
        

    def parse_item(self, response):
        item = CspiderItem()
        item['url'] = response.url
        item['content'] = response.css('div#content').extract()
        #item['keyw'] = response.css('meta[name="DC.description"]').extract()
        #item['descr'] = response.css('meta[name="Keyword"]').extract()
        #item['title'] = response.css('meta[name="DC.title"]').extract()
        #item['subj'] = response.css('meta[name="DC.Subject.epabrm"]').extract()
        #item['ptype'] = response.css('meta[name="DC.type"]').extract()
        item['descr'] = response.xpath('//meta[@name="DC.description"]/@content').extract()
        item['keyw'] = response.xpath('//meta[@name="Keywords"]/@content').extract()
        item['title'] = response.xpath('//meta[@name="DC.title"]/@content').extract()
        item['subj'] = response.xpath('//meta[@name="DC.Subject.epabrm"]/@content').extract()
        item['ptype'] = response.xpath('//meta[@name="DC.type"]/@content').extract()
        yield item
        #for url in response.xpath('//a/@href').extract():
        #    yield scrapy.Request(url, callback=self.parse)
