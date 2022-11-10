import csv
import sqlite3
import os

def execute_sql(db, sql_cmd):
    cursor = db.cursor()
    cursor.execute(sql_cmd)
    db.commit()

STOCK_DB_FILE = 'stockPrice.db'
if os.path.isfile(STOCK_DB_FILE):
    os.remove(STOCK_DB_FILE)

db = sqlite3.connect(STOCK_DB_FILE)
# need add ID for sqlite3
execute_sql(db, f'CREATE TABLE stockPrice (ID INTEGER, 日期 TEXT, 開盤價 INTEGER, 收盤價 INTEGER, 成交筆數 INTEGER)')

with open('stockThisMonth.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    print('日期', '開盤價','收盤價','成交筆數')
    for info in reader:
        print(info['日期'],info['開盤價'],info['收盤價'],info['成交筆數'])
        # no add ID's value 
        command = f'INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("{info["日期"]}", {info["開盤價"]}, {info["收盤價"]}, {info["成交筆數"]})'
        print('command=', command)
        execute_sql(db, command)

db.close()
