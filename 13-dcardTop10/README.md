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
# 有時會錯誤如下
===== query api falure =====
Dcard 在某些情況下會需要驗證請求是真實的人類，而非機器人。

如果您符合以下行為，這可能是正常的現象：
1. 您操作的頻率過快
2. 您的瀏覽器版本過老舊或安裝的擴充程式異常
3. 您使用公共網路或受監控的網路環境
4. 您使用 VPN 或 Proxy 服務
5. 您使用的網路曾經有異常行為
```

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

## dcardApi.py(有時會錯誤)
```
(myenv11_02) D:\work\run\python_crawler\13-dcardTop10>python dcardApi.py

DevTools listening on ws://127.0.0.1:57660/devtools/browser/0d4db1a1-361f-44de-ac83-b48460857ee4
[16776:11508:1123/114040.163:ERROR:device_event_log_impl.cc(215)] [11:40:40.162] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
[16776:11508:1123/114040.166:ERROR:device_event_log_impl.cc(215)] [11:40:40.166] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
[16776:11508:1123/114040.167:ERROR:device_event_log_impl.cc(215)] [11:40:40.167] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
[16776:11508:1123/114040.171:ERROR:device_event_log_impl.cc(215)] [11:40:40.171] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
(1) 推薦的英文教學資源網站(聖誕節)
(2) 配哪雙鞋
(3) 迪卡密碼忘記怎麼辦？😭😭
(4) 女生真的能跟不喜歡的人在ㄧ起嗎？
(5) 莫拉隊伍
(6) #討論 每日一問，勤業今天要發實習通知了嗎
(7) 對於保守理財者的策略
(8) 月老幫你促
(9) 11月合庫金庫存
(10) 求租（或出）二手木棒🥺🥺
(11) 韓國偶像中，最常見的MBTI性格類型大公開
(12) 符號請益
(13) 淘寶轉帳
(14) 請益「雪薇－躺平記多益單字：45天強迫取分」評價
(15) #請益 Costco現在還有賣Diptyque香水嗎？🥺
(16) #鑑定 出現在宿舍廁所的小傢伙
(17) 案例分享
(18) #找鞋 請問台灣哪裡買得到這雙呢？
(19) #問卷 AI 面試大調查✨
(20) 只要$299的超大容量水壺*⸜( •ᴗ• )⸝*
(21) 有人會做自己沒興趣的運動？
(22) 📄請幫我填寫一下問卷📄
(23) 沖繩花費詢問
(24) #贈品 二手衣物
(25) 世足能串關嗎到底
(26) #分享 隱翅蟲講座
(27) #分享 耳朵終於解放了 眼睛近視雷射分享
(28) 表弟加盟海神？一月底來台
(29) #發問 你對 AI 面試的看法如何呢？🤩
(30) 投給黃珊珊的理由
get from dcard api....

(myenv11_02) D:\work\run\python_crawler\13-dcardTop10>
```

