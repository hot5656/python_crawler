# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class ZillowItem(scrapy.Item):
    index = scrapy.Field(
        output_processor = TakeFirst()
    )
    id = scrapy.Field(
        output_processor = TakeFirst()
    )
    # img_url = scrapy.Field(
    #     output_processor = TakeFirst()
    # )
    # download images
    image_urls = scrapy.Field()
    images = scrapy.Field()
    detail_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    status_type = scrapy.Field(
        output_processor = TakeFirst()
    )
    status_text = scrapy.Field(
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        output_processor = TakeFirst()
    )
    address = scrapy.Field(
        output_processor = TakeFirst()
    )
    beds = scrapy.Field(
        output_processor = TakeFirst()
    )
    baths = scrapy.Field(
        output_processor = TakeFirst()
    )
    area_sqft = scrapy.Field(
        output_processor = TakeFirst()
    )
    latitude = scrapy.Field(
        output_processor = TakeFirst()
    )
    longitude = scrapy.Field(
        output_processor = TakeFirst()
    )
    broker_name = scrapy.Field(
        output_processor = TakeFirst()
    )
