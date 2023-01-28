# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from pymongo import MongoClient
from datetime import datetime

class Ithome2Pipeline:
    def process_item(self, item, spider):
        if item['view_count'] < 100:
            raise DropItem(f'[{item["title"]}] 瀏覽數小於 100')

        return item


class MongoPipeline:
    collection_name = 'articles'

    def open_spider(self, spider):
        # DB 不用先建也 ok
        host = 'localhost'
        dbname = 'ithome2'

        self.client = MongoClient('mongodb://%s:%s@%s:%s/' % (
            'mongoadmin',   # 資料庫帳號
            'mg123456',     # 資料庫密碼
            'localhost',    # 資料庫位址
            '27017'         # 資料庫埠號
        ))
        print('資料庫連線成功！')


        self.db = self.client[dbname]
        # self.article_collection = self.db.articles
        # self.response_collection = self.db.response

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # article_id = self.db[self.collection_name].insert_one(dict(item)).inserted_id

        # 查詢資料庫中是否有相同網址的資料存在
        doc = self.db[self.collection_name].find_one({'url': item['url']})
        item['update_time'] = datetime.now()

        if not doc:
            # 沒有就新增
            article_id = self.db[self.collection_name].insert_one(dict(item)).inserted_id
        else:
            # 已存在則更新
            self.db[self.collection_name].update_one(
                {'_id': doc['_id']},
                {'$set': dict(item)}
            )
            article_id = doc['_id']
        return item

