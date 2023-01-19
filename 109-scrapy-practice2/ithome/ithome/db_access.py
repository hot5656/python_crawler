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
    'title': '前言',
    'url': 'https://ithelp.ithome.com.tw/articles?tab=tech',
    'author': 'Robert',
    'publish_time': datetime.now(),
    'tags': 'scrapy,postgresql',
    'content': 'Test DB...............'
}


# cursor.execute("""
#     INSERT INTO public.article(title, url, author, publish_time, tags, content)
#     VALUES (%(title)s, %(url)s, %(author)s, %(publish_time)s, %(tags), %(content)s)
#     """
#     ,
#     article)

# cur.execute("""
#     INSERT INTO some_table (an_int, a_date, another_date, a_string)
#     VALUES (%(int)s, %(date)s, %(date)s, %(str)s);
#     """,
#     {'int': 10, 'str': "O'Reilly", 'date': datetime.date(2005, 11, 18)})
cursor.execute("""
    INSERT INTO public.article (title, url, author, publish_time, tags, content)
    VALUES (%(title)s, %(url)s, %(author)s, %(publish_time)s, %(tags), %(content)s);
    """,
    article)

print('資料新增成功!')

conn.commit()
cursor.close()
conn.close()
