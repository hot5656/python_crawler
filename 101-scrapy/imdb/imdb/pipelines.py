# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# for MongoDB
import pymongo
# for SQlite
import sqlite3
# for mongodb client link
import mongodb_altas

# for MongoDB - changhe name
class MongodbPipeline:
    collection_name = "best_movies"

    def open_spider(self, spider):
        # for MongoDB
        # for mongodb client link
        self.client = pymongo.MongoClient(mongodb_altas.mogodb_link)
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        # for MongoDB
        self.client.close()

    def process_item(self, item, spider):
        # for MongoDB
        self.db[self.collection_name].insert_one(item)
        return item

# for SQlite
class SQLitePipeline:

    def open_spider(self, spider):
        self.connection = sqlite3.connect("imdb.db")
        self.c = self.connection.cursor()
        self.c.execute('''
            CREATE TABLE best_movies(
                title TEXT,
                year TEXT,
                duration TEXT,
                genre TEXT,
                rating TEXT,
                movie_url TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        print("=============")
        print(item.get('title'))
        print("*************")
        self.c.execute('''
            INSERT INTO best_movies (title,year,duration,genre,rating,movie_url) VALUES(?,?,?,?,?,?)
        ''', (
            item.get('title'),
            item.get('year'),
            item.get('duration'),
            item.get('genre'),
            item.get('rating'),
            item.get('movie_url')
        ))
        self.connection.commit()
        return item

        # self.c.execute('''
        #     INSERT INTO best_movies (title, year, duration, genre, rating, movie_url) VALUES(?,?,?,?,?,?)

        # ''', (
        #     item.get('title'),
        #     item.get('year'),
        #     item.get('duration'),
        #     item.get('genre'),
        #     item.get('rating'),
        #     item.get('movie_url')
        # ))
