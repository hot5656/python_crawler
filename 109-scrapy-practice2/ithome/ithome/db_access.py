import psycopg2
from datetime import datetime
import env

host = 'localhost'
user = env.USER
password = env.PASSWORD
dbname = 'ithome'

conn_sting = f"host={host} user={user} dbname={dbname} password={password}"
conn = psycopg2.connect(conn_sting)
print('資料庫連線成功!')
cursor = conn.cursor()

article = {
    'title': '前言3',
    'url': 'https://ithelp.ithome.com.tw/articles?tab=tech',
    'author': 'Robert',
    'publish_time': datetime.now(),
    'tags': 'scrapy,postgresql,#3',
    'content': 'Test DB3...............'
}

# ok command 1
# postgres_insert_query = '''
#         INSERT INTO articles(title, url, author, publish_time, tags, content)
#         VALUES (%s, %s ,%s, %s, %s, %s)
#     '''
# cursor.execute(postgres_insert_query, (article['title'], article['url'], article['author'], article['publish_time'], article['tags'], article['content']) )

# ok command 2
cursor.execute("""
    INSERT INTO articles(title, url, author, publish_time, tags, content)
    VALUES (%(title)s, %(url)s, %(author)s, %(publish_time)s, %(tags)s, %(content)s);
    """,
    article)


print('資料新增成功!')

conn.commit()
cursor.close()
conn.close()
