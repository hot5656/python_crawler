import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser
from ..items import ZillowItem
import json

class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            # this site not need cookie, just try put cookie
            cookies=cookie_parser()
        )

    def parse(self, response):
        # with open('initial_response.json', 'wb') as f:
        #     f.write(response.body)
        json_resp = json.loads(response.body)
        # print(type(json_resp))
        houses = json_resp['cat1']['searchResults']['listResults']
        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', house['id'])
            loader.add_value('img_url', house['imgSrc'])
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
            yield loader.load_item()
