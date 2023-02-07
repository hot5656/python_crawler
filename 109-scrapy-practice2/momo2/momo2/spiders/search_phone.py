# ok 選擇正確網址與payload
import scrapy
import json


class SearchPhoneSpider(scrapy.Spider):
    name = "search_phone"
    allowed_domains = ["apisearch.momoshop.com.tw"]
    # start_urls = ["http://apisearch.momoshop.com.tw/"]
    URL_ENTRY = 'https://apisearch.momoshop.com.tw/momoSearchCloud/moec/textSearch'
    payload = {
        "host": "momoshop",
        "flag": "searchEngine",
        "data": {
            "specialGoodsType": "",
            "isBrandSeriesPage": False,
            "authorNo": "",
            "searchValue": "iphone 14 pro",
            "cateCode": "",
            "cateLevel": "-1",
            "cp": "N",
            "NAM": "N",
            "first": "N",
            "freeze": "N",
            "superstore": "N",
            "tvshop": "N",
            "china": "N",
            "tomorrow": "N",
            "stockYN": "N",
            "prefere": "N",
            "threeHours": "N",
            "video": "N",
            "cycle": "N",
            "cod": "N",
            "superstorePay": "N",
            "showType": "chessboardType",
            "curPage": "1",
            "priceS": "0",
            "priceE": "9999999",
            "searchType": "1",
            "reduceKeyword": "",
            "isFuzzy": "0",
            "rtnCateDatainfo": {
                "cateCode": "",
                "cateLv": "-1",
                "keyword": "iphone 14 pro",
                "curPage": "1",
                "historyDoPush": False,
                "timestamp": 1675674197375
            },
            "flag": 2018
        }
    }


    def start_requests(self):
        dumpjson = json.dumps(self.payload)
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/json; charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        yield scrapy.Request(url = self.URL_ENTRY,
                              method = 'POST',
                              headers = headers,
                              body = dumpjson,
                              callback=self.parse,
                              dont_filter=True,
                              errback=self.errback
                              )

    def parse(self, response):
        print("===========================")
        # print(response.body)
        resp_data = json.loads(response.body)
        products =  resp_data['rtnSearchData']['goodsInfoList']
        for product in products:
        # print(resp_data['rtnSearchData']['goodsInfoList'])
            print(f"{product['goodsName']} {product['goodsPrice']}")
        # print(resp_data['rtnSearchData']['goodsInfoList'])
        print("===========================")

    def errback(self, failure):
        print(failure)
