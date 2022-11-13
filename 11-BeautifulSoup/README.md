# beautifulSoup

## run

```
PS D:\work\git\python_crawler\11-BeautifulSoup> python .\beautifulSoup_01.py
===============================
First soup.h4 :
<h4 class="card-title">
<a href="http://www.pycone.com/blogs#pablo">Mac使用者</a>
</h4>
===============================
First soup.h4.a.text :
Mac使用者
===============================
ALL soup.h4.a.text :
Mac使用者
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
===============================
ALL soup.h4.a.text for class="card-title" :
Mac使用者
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
給初學者的 Python 網頁爬蟲與資料分析
===============================
soup.find(id="mac-p").text.strip() :
-在Mac環境下安裝Python與Sublime Text3 Read More-
===============================
[]
===============================
<< blog list >>
開發環境設定 Mac使用者 在Mac環境下安裝Python與Sublime Text3 Read More
資料科學 給初學者的 Python 網頁爬蟲與資料分析 (1) 前言 Read More
資料科學 給初學者的 Python 網頁爬蟲與資料分析 (2) 套件安裝與啟動網頁爬蟲 Read More
資料科學 給初學者的 Python 網頁爬蟲與資料分析 (3) 解構並擷取網頁資料 Read More
<< blog list 2nd way>>
['開發環境設定', 'Mac使用者', '在Mac環境下安裝Python與Sublime Text3', 'Read More']
['資料科學', '給初學者的 Python 網頁爬蟲與資料分析', '(1) 前言', 'Read More']
['資料科學', '給初學者的 Python 網頁爬蟲與資料分析', '(2) 套件安裝與啟動網頁爬蟲', 'Read More']
['資料科學', '給初學者的 Python 網頁爬蟲與資料分析', '(3) 解構並擷取網頁資料', 'Read More']
['資料科學', '給初學者的 Python 網頁爬蟲與資料分析', '(4) 擷取資料及下載圖片', 'Read More']
['資料科學', '給初學者的 Python 網頁爬蟲與資料分析', '(5) 資料分析及展示', 'Read More']
```

```
PS D:\work\git\python_crawler\11-BeautifulSoup> python .\beautifulSoup_02.py
Total clouse count: 6
1490
1890
1890
1890
1890
1890
Average courage price: 1823.3333333333333

1490
1890
1890
1890
1890
1890
Average courage price: 1823.3333333333333

初心者 - Python入門 初學者 1490 http://www.pycone.com img/python-logo.png
Python 網頁爬蟲入門實戰 有程式基礎的初學者 1890 http://www.pycone.com img/python-logo.png
Python 機器學習入門實戰 (預計) 有程式基礎的初學者 1890 http://www.pycone.com img/python-logo.png
Python 資料科學入門實戰 (預計) 有程式基礎的初學者 1890 http://www.pycone.com img/python-logo.png
Python 資料視覺化入門實戰 (預計) 有程式基礎的初學者 1890 http://www.pycone.com img/python-logo.png
Python 網站架設入門實戰 (預計) 有程式基礎的初學者 1890 None img/python-logo.png
=============
```
