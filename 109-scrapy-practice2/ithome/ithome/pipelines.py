# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
# import env


class IthomePipeline:
    def process_item(self, item, spider):
        return item

class PostgreSqlPipeline:
    def open_spider(self, spider):
        USER = 'postgres'
        PASSWORD = 'pg123456'
        host = 'localhost'
        user = USER
        password = PASSWORD
        dbname = 'ithome'
        conn_sting = f"host={host} user={user} dbname={dbname} password={password}"

        self.conn = psycopg2.connect(conn_sting)
        print('資料庫連線成功!')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        article = {
            'title': item.get('title'),
            'url': item.get('url'),
            'author': item.get('author'),
            'publish_time': item.get('publish_time'),
            'tags': item.get('tags'),
            'content': item.get('content'),
            'view_count': item.get('view_count')
        }

        # direct update
        # self.cursor.execute("""
        #     INSERT INTO articles(title, url, author, publish_time, tags, content, view_count)
        #     VALUES (%(title)s, %(url)s, %(author)s, %(publish_time)s, %(tags)s, %(content)s, %(view_count)s);
        #     """,
        #     article)

        # if len(article['title'])>100 or len(article['tags'])>100:
        #     print("---------->")
        #     print(f"({len(article['title'])}) {article['title']}")
        #     print(f"({len(article['tags'])}) {article['tags']}")

        # check update
        # current_timestamp : SQL current time
        self.cursor.execute("""
            INSERT INTO articles(title, url, author, publish_time, tags, content, view_count)
            VALUES (%(title)s, %(url)s, %(author)s, %(publish_time)s, %(tags)s, %(content)s, %(view_count)s)
            ON CONFLICT(url)
            DO UPDATE SET title=%(title)s,
                tags=%(tags)s,
                content=%(content)s,
                update_time=current_timestamp
            RETURNING id;
            """,
            article)
        self.conn.commit()
        article_id = self.cursor.fetchone()[0]

        article_responses = item.get('responses')
        for article_response in article_responses:
            response = {
                'id': article_response['resp_id'],
                'article_id': article_id,
                'author': article_response['author'],
                'publish_time': article_response['publish_time'],
                'content': article_response['content'],
            }

            # direct update
            # self.cursor.execute("""
            #     INSERT INTO public.response(article_id, author, publish_time, content)
            #     VALUES (%(article_id)s,%(author)s,%(publish_time)s,%(content)s);
            #     """,
            #     response)

            # check exist
            self.cursor.execute("""
                INSERT INTO public.response(id, article_id, author, publish_time, content)
                VALUES (%(id)s, %(article_id)s ,%(author)s, %(publish_time)s, %(content)s)
                ON CONFLICT(id) DO UPDATE
                SET content=%(content)s;
                """,
                response)
            self.conn.commit()

        # print(f"{item.get('index')}資料新增成功!")
        return item
