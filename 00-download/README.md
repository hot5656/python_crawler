# download
download "Pycone 松果城市" page

## install requests
```
PS D:\work\git\python_crawler\00-download> pip3 install requests  
Collecting requests
  Using cached requests-2.28.1-py3-none-any.whl (62 kB)
Requirement already satisfied: charset-normalizer<3,>=2 in d:\app\python_env\myenv11_02\lib\site-packages (from requests) (2.1.1)
Requirement already satisfied: idna<4,>=2.5 in d:\app\python_env\myenv11_02\lib\site-packages (from requests) (3.4)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in d:\app\python_env\myenv11_02\lib\site-packages (from requests) (1.26.12)
Requirement already satisfied: certifi>=2017.4.17 in d:\app\python_env\myenv11_02\lib\site-packages (from requests) (2022.9.24)
Installing collected packages: requests
Successfully installed requests-2.28.1
PS D:\work\git\python_crawler\00-download>
PS D:\work\git\python_crawler\00-download> pip3 list
Package            Version
------------------ ---------
certifi            2022.9.24
charset-normalizer 2.1.1
idna               3.4
pip                22.3
requests           2.28.1
setuptools         65.5.0
urllib3            1.26.12
wheel              0.37.1
```

## run

```
D:\work\git\python_crawler\00-download> python .\download.py

status_code= 200
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Pycone 松果城市</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="http://getbootstrap.com/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="http://getbootstrap.com/examples/sticky-footer/sticky-footer.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="http://getbootstrap.com/assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <!-- Begin page content -->
    <div class="container">
      <div class="page-header">
        <h1>歡迎來到 Pycone 松果城市！</h1>
      </div>
      <p class="lead">Python是非常強的的程式語言, 簡潔友好的語法特別容易上手, 又有許多第三方函式庫的支援。Python是完全物件導向的語言, 有益於減少程式碼的重複性。Python的設計哲學是優雅, 明確, 簡單。 Python的設計風格,  
使其成為易讀, 易維護且具有廣泛用途的程式語言。Python的應用範圍相當廣泛, 例如web後端開發, 機器學習, 資料分析, 自然語言處理, 網頁爬蟲與遊戲等等。如果自己常常翻閱書籍卻無法掌握重點, 上網收集資料卻覺得太過片段, 想要自己 
動手寫寫看卻不知道如何開始。 這們課會從最基本的環境架設開始教起, 讓所有同學都可以深入淺出一窺Python的奧妙,更透過實務專題練習的方式,使學生可以應用課堂所學來完成一個Python軟體。</p>
      <p><a href="http://www.pycone.com/">了解更多</a></p>
    </div>

    <footer class="footer">
      <div class="container">
        <p class="text-muted">Pycone (c) 2017</p>
      </div>
    </footer>


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
```