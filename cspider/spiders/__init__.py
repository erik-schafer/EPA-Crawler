# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
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
        yield item
        #for url in response.xpath('//a/@href').extract():
        #    yield scrapy.Request(url, callback=self.parse)