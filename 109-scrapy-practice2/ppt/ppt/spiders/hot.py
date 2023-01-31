import scrapy
import ppt.items as items


class HotSpider(scrapy.Spider):
    name = 'hot'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/index.html']

    def parse(self, response):
        categories = response.xpath("//div[@class='b-ent']")
        for category in categories:
            category_item = items.PptCategoryItem()
            category_item['title'] = category.xpath(".//div[@class='board-name']/text()").get()
            category_item['counter'] = category.xpath(".//div[@class='board-nuser']/span/text()").get()
            category_item['type'] = category.xpath(".//div[@class='board-class']/text()").get()
            category_item['description'] = category.xpath(".//div[@class='board-title']/text()").get()

            yield category_item

