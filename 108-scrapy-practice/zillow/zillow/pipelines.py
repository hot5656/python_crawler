# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# change download image name
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request



class ZillowPipeline(ImagesPipeline):
    # change download image name
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, meta={'houseID': item.get('id')}) for u in urls]

    # change download image name
    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.meta['houseID']
        return f'full/{image_name}.jpg'
