# stockPriceSqlite
取得本月 2330 的股價並存至 sqlite

## run
```
(myenv11_02) PS D:\work\git\python_crawler\06-stockPriceSqlite> python .\stockPriceSqlite.py
取得本月台積電 (2330) 的股價 2022 11...
日期 開盤價 收盤價 成交筆數
111/11/01 388.50 391.50 29,780
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/01", 388.50, 391.50, 29,780)
111/11/02 391.00 395.00 22,285
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/02", 391.00, 395.00, 22,285)
111/11/03 385.00 384.00 52,660
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/03", 385.00, 384.00, 52,660)
111/11/04 381.00 382.00 26,895
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/04", 381.00, 382.00, 26,895)
111/11/07 390.00 390.00 30,880
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/07", 390.00, 390.00, 30,880)
111/11/08 395.00 399.00 35,956
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/08", 395.00, 399.00, 35,956)
111/11/09 403.50 417.00 67,569
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/09", 403.50, 417.00, 67,569)
111/11/10 409.00 407.50 36,464
command= INSERT INTO stockPrice (ID, 日期, 開盤價, 收盤價, 成交筆數) VALUES ("111/11/10", 409.00, 407.50, 36,464)
```