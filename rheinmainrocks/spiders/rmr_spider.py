from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from rheinmainrocks.items import RheinmainrocksItem

class RmrSpider(BaseSpider):
    name = "rmr"
    allowed_domains = ["rheinmainrocks.de"]
    start_urls = [
        "http://rheinmainrocks.de/usergroups/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        ugs = hxs.select('//table/tbody/tr')
        items = []
        for ug in ugs:
            if not ug.select('td[1]/a/text()').extract():
                continue
            item = RheinmainrocksItem()
            item["name"] = ug.select('td[1]/a/text()').extract()[0]
            item["url"] = ug.select('td[1]/a/@href').extract()[0]
            item["subject"] = ug.select('td[2]/text()').extract()[0]
            item["location"] = ug.select('td[3]/text()').extract()[0]
            items.append(item)
        return items        

