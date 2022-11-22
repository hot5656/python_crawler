# dcardTop10

## install
```
pip install fake_useragent

pip install selenium

x pip install lxml : no

x pip install pandas

x pip install requests_html : no
x pip install cloudscraper : free version not support

pip install pandas
```

## dcardGetError.py
```
(myenv11_02) D:\work\run\python_crawler\13-dcardTop10>python dcardGetError.py
=================
<Response [403]>
=================
Invalid url: https://www.dcard.tw/f
=================
<Response [403]>
=================
Invalid url: https://www.dcard.tw/service/api/v2/posts
```

## dcardTop10.py
```
(myenv11_02) D:\work\run\python_crawler\13-dcardTop10>python dcardGetTop10.py

DevTools listening on ws://127.0.0.1:56683/devtools/browser/9842f823-d095-4af3-9178-d22972287ef2
[7028:296:1122/164538.915:ERROR:device_event_log_impl.cc(215)] [16:45:38.915] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
[7028:296:1122/164538.918:ERROR:device_event_log_impl.cc(215)] [16:45:38.918] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
[7028:296:1122/164538.919:ERROR:device_event_log_impl.cc(215)] [16:45:38.920] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
[7028:296:1122/164538.922:ERROR:device_event_log_impl.cc(215)] [16:45:38.923] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
[%] Scrolling down.
0
1
length=7
=======================
post-240580531
(1) #贈品 #贈品 星巴克飲品券==
=======================
post-240577753
(2) 家教老師與學生家長竟然......==
=======================
post-240574152
(3) 一個國小特教老師的故事==
=======================
post-240575426
(4) #閒聊 小說都不敢這麼寫的田柾國人生履歷==
=======================
post-240580141
(5) #開箱 雙11給妳11,000要買什麼？雅詩蘭黛/契爾氏/資生堂/ELEMIS/蘿拉蜜思/Momo揪團==
=======================
post-240578549
(6) 發明這項運動的人是天才==
=======================
post-240579487
(7) #分享 TWICE 要回歸了嗎？2022年回歸盤點回顧🍭==
=======================
['post-240580531', 'post-240577753', 'post-240574152', 'post-240575426', 'post-240580141', 'post-240578549', 'post-240579487']
[%] Scrolling down.
0
1
length=8
=======================
post-240578549
*1* 發明這項運動的人是天才==
=======================
post-240579487
*2* #分享 TWICE 要回歸了嗎？2022年回歸盤點回顧🍭==
=======================
post-240572914
(3) （更）媽媽到底怎麼養活我的==
=======================
post-240580098
(4) 老公已經半年沒碰我了==
=======================
post-240579730
(5) #詢問 以為女生都是穿成套內衣==
=======================
post-240578711
(6) #情報 2022 MMA最終出席陣容==
=======================
post-240579385
(7) 感謝上天讓我遇到天使系女友==
=======================
post-240580415
(8) #討論 想當個快樂的胖子錯了嗎？==
=======================
['post-240580531', 'post-240577753', 'post-240574152', 'post-240575426', 'post-240580141', 'post-240578549', 'post-240579487', 'post-240572914', 'post-240580098', 'post-240579730', 'post-240578711', 'post-240579385', 'post-240580415']
```

