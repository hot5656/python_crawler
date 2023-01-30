# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from pymongo import MongoClient
from datetime import datetime
import ithome2.items as items
import ithome2.env as env
# save item to json
import json

class Ithome2Pipeline:
    def process_item(self, item, spider):
        if type(item).__name__ == 'IthomeArticleItem':
            if item['view_count'] < 100:
                raise DropItem(f'[{item["title"]}] 瀏覽數小於 100')

        return item


class MongoPipeline:
    collection_article = 'articles'
    collection_response = 'response'

    def open_spider(self, spider):
        dbname = 'ithome2'
        user = env.MONGO_USER
        password = env.MONGO_PASSWORD
        host = 'localhost'
        port =  27017
        MONGO_URI = f'mongodb://{user}:{password}@{host}:{port}/'
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[dbname]
        # save item to json
        self.file1 = open('art.json', 'w', encoding='utf-8')
        self.file2 = open('resp.json', 'w', encoding='utf-8')
        self.file1.write('[\n')
        self.file2.write('[\n')

    def close_spider(self, spider):
        self.client.close()
        # save item to json
        self.file1.write(']')
        self.file2.write(']')
        self.file1.close()
        self.file2.close()

    def process_item(self, item, spider):
        # if type(item).__name__ == 'IthomeArticleItem':
        if type(item) is items.IthomeArticleItem:
            # 查詢資料庫中是否有相同網址的資料存在
            doc = self.db[self.collection_article].find_one({'url': item['url']})
            item['update_time'] = datetime.now()

            if not doc:
                # 沒有就新增
                item['_id'] = str(self.db[self.collection_article].insert_one(dict(item)).inserted_id)
            else:
                # 已存在則更新
                self.db[self.collection_article].update_one(
                    {'_id': doc['_id']},
                    {'$set': dict(item)}
                )
                item['_id'] = str(doc['_id'])

            # save item to json
            values = dict(item)
            values['update_time'] = values['update_time'].strftime("%Y-%m-%d %H:%M:%S")
            line = json.dumps(values, ensure_ascii=False) + ",\n"
            self.file1.write(line)

        # if type(item).__name__ == 'IthomeReplyItem':
        if type(item) is items.IthomeReplyItem:
            # save item to json
            values = dict(item)
            del values['_id']
            values['publish_time'] = values['publish_time'].strftime("%Y-%m-%d %H:%M:%S")
            values['article_id'] = str(values['article_id'])
            line = json.dumps(values, ensure_ascii=False) + ",\n"
            self.file2.write(line)

            document = self.db[self.collection_response].find_one(item['_id'])
            if not document:
                insert_result = self.db[self.collection_response].insert_one(dict(item))
            else:
                del item['_id']
                self.db[self.collection_response].update_one(
                    {'_id': document['_id']},
                    {'$set': dict(item)},
                    upsert=True
                )

        return item

