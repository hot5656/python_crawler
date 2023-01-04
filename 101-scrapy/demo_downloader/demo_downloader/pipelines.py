# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class DemoDownloaderPipeline:
#     def process_item(self, item, spider):
#         return item



# from scrapy.pipelines.files import FilesPipeline
# import scrapy.pipelines.files as scrapy_file
from scrapy.pipelines.files import FilesPipeline


# class CustomFilePipeLines(scrapy_file.FilesPipeline):
class CustomFilePipeLines(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        print("CustomFilePipeLines　===========")
        print(item.get('Title'))
        return item.get('Title')
