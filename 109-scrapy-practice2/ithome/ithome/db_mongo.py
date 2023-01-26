from pymongo import MongoClient
from datetime import datetime


# DB 不用先建也 ok
host = 'localhost'
dbname = 'ithome'

client = MongoClient('mongodb://%s:%s@%s:%s/' % (
    'mongoadmin',   # 資料庫帳號
    'mg123456',     # 資料庫密碼
    'localhost',    # 資料庫位址
    '27017'         # 資料庫埠號
))
print('資料庫連線成功！')


db = client[dbname]
article_collection = db.articles

article = {
    'title': '前言3',
    'url': 'https://ithelp.ithome.com.tw/articles?tab=tech',
    'author': 'Robert',
    'publish_time': datetime.now(),
    'tags': 'scrapy,postgresql,#3',
    'content': 'Test DB3...............'
}
article_id = article_collection.insert_one(article).inserted_id

print(f'資料新增成功！ID: {article_id}')

client.close()
