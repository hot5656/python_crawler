import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser, parse_new_url
from ..items import ZillowItem
import json

class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']
    index = 1

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            # this site not need cookie, just try put cookie
            cookies=cookie_parser(),
            meta = {
                'currentPage': 1
            }
        )

    def parse(self, response):
        # with open('initial_response.json', 'wb') as f:
        #     f.write(response.body)
        current_page = response.meta['currentPage']
        json_resp = json.loads(response.body)
        # print(type(json_resp))
        houses = json_resp['cat1']['searchResults']['listResults']
        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', house['id'])
            # download images
            loader.add_value('image_urls', house['imgSrc'])
            loader.add_value('detail_url', house['detailUrl'])
            loader.add_value('status_type', house['statusType'])
            loader.add_value('status_text', house['statusText'])
            loader.add_value('price', house['price'])
            loader.add_value('address', house['address'])
            loader.add_value('beds', house['beds'])
            loader.add_value('baths', house['baths'])
            loader.add_value('area_sqft', house['area'])
            # dict field 某些地方一定要用 get()
            loader.add_value('latitude', house.get('latLong').get('latitude'))
            loader.add_value('longitude', house.get('latLong').get('longitude'))
            loader.add_value('broker_name', house.get('brokerName'))
            loader.add_value('index', self.index)
            self.index += 1
            yield loader.load_item()

        total_pages = json_resp.get('cat1').get('searchList').get('totalPages')
        if current_page< total_pages:
            current_page += 1
            print(f"----> {current_page}")
            # yield scrapy.Request(
            #     url=parse_new_url(URL, current_page),
            #     callback=self.parse,
            #     cookies=cookie_parser(),
            #     meta = {
            #         'currentPage': current_page
            #     }
            # )
