# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ithome2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IthomeArticleItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    publish_time = scrapy.Field()
    view_count = scrapy.Field()
    title = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
    update_time = scrapy.Field()

class IthomeReplyItem(scrapy.Item):
    _id = scrapy.Field()
    article_id = scrapy.Field()
    author = scrapy.Field()
    publish_time = scrapy.Field()
    content = scrapy.Field()