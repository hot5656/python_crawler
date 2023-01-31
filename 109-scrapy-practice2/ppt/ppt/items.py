# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class PptCategoryItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    counter = scrapy.Field()
    type = scrapy.Field()
    description = scrapy.Field()

class PptBeautyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    push_count = scrapy.Field()
    author = scrapy.Field()

class PptPostItem(scrapy.Item):
    # define the fields for your item here like:
    # title = scrapy.Field()
    # url = scrapy.Field()
    # push_count = scrapy.Field()
    # author = scrapy.Field()
    index = scrapy.Field(
        output_processor = TakeFirst()
    )
    image_urls = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()

