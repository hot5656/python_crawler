import scrapy
from scrapy.selector import Selector
import json
import re
# add splash
from scrapy_splash import SplashRequest
# add for splash user+password(run Aquarium)
from w3lib.http import basic_auth_header


class ListingSpider(scrapy.Spider):
    name = 'listing'
    allowed_domains = ['www.centris.ca']

    position = {
        "startPosition": 0
    }
    index = 0

    # add splash
    # script = '''
    #     function main(splash, args)
    #         assert(splash:go(args.url))
    #         assert(splash:wait(0.5))
    #         return splash:html()
    #     end
    # '''
    # add splash - add some condition
    script = '''
        function main(splash, args)
            splash:on_request(function(request)
                if request.url:find('css') then
                    request.abort()
                end
            end)
            splash.images_enabled = false
            splash.js_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()
        end
    '''


    def start_requests(self):
        query = {
            "query": {
                "UseGeographyShapes": 0,
                "Filters": [
                    {
                        "MatchType": "CityDistrictAll",
                        "Text": "Montréal (All boroughs)",
                        "Id": 5
                    }
                ],
                "FieldsValues": [
                    {
                        "fieldId": "CityDistrictAll",
                        "value": 5,
                        "fieldConditionId": "",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "Category",
                        "value": "Residential",
                        "fieldConditionId": "",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "SellingType",
                        "value": "Rent",
                        "fieldConditionId": "",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "LandArea",
                        "value": "SquareFeet",
                        "fieldConditionId": "IsLandArea",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "RentPrice",
                        "value": 0,
                        "fieldConditionId": "ForRent",
                        "valueConditionId": ""
                    },
                    {
                        "fieldId": "RentPrice",
                        "value": 1500,
                        "fieldConditionId": "ForRent",
                        "valueConditionId": ""
                    }
                ]
            },
            "isHomePage": True
        }
        yield scrapy.Request(
            url="https://www.centris.ca/property/UpdateQuery",
            method="POST",
            body=json.dumps(query),
            headers={
                'content-type': 'application/json; charset=utf-8',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
            },
            callback=self.update_query
        )

    def update_query(self, response):
        yield scrapy.Request(
            url="https://www.centris.ca/Property/GetInscriptions",
            method="POST",
            body=json.dumps(self.position),
            headers={
                'content-type': 'application/json; charset=utf-8',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
            },
            callback=self.parse
        )

    def parse(self, response):
        resp_dict = json.loads(response.body)

        # resp_dict['d']['Result']['html'] - same as below
        html = resp_dict.get('d').get('Result').get('html')
        sel = Selector(text=html)
        listings = sel.xpath("//div[@class='shell']")

        print(f"------------> index {self.position['startPosition']}")
        for listing in listings:
            category = listing.xpath("normalize-space(.//span[@class='category']/div/text())").get()
            # some room not include bed
            bedrooms = listing.xpath(".//div[@class='cac']/text()").get()
            bathrooms =  listing.xpath(".//div[@class='sdb']/text()").get()
            if bedrooms:
                features = f"{bedrooms} Bed, {bathrooms} Bath"
            else:
                features = f"{bathrooms} Bath"

            # remove character "," space and $
            price_str =  listing.xpath(".//div[@class='price']/span/text()").get()
            price = price_str[-1] + " " + re.sub("[^0-9]", "",  price_str)
            city = listing.xpath("(.//span[@class='address']/div)[2]/text()").get()
            url = listing.xpath(".//a[@class='property-thumbnail-summary-link']/@href").get()
            abs_url = response.urljoin(url)

            self.index += 1
            # yield {
            #     'index': self.index,
            #     'category': category,
            #     'features': features,
            #     'price': price,
            #     'city': city,
            #     'url': response.urljoin(url)
            # }
            yield SplashRequest(
                url= abs_url,
                endpoint='execute',
                callback= self.parse_summary,
                args = {
                    'lua_source': self.script
                },
                meta = {
                    'cat': category,
                    'fea': features,
                    'pri': price,
                    'city': city,
                    'url': abs_url,
                    'index': self.index,
                },
                # add for splash user+password(run Aquarium)
                splash_headers={
                    'Authorization': basic_auth_header('user', 'userpass')
                }
            )

        count = resp_dict.get('d').get('Result').get('count')
        increment_number = resp_dict.get('d').get('Result').get('inscNumberPerPage')

        if self.position['startPosition']+increment_number <  count:
            self.position['startPosition'] += increment_number

            yield scrapy.Request(
                url="https://www.centris.ca/Property/GetInscriptions",
                method="POST",
                body=json.dumps(self.position),
                headers={
                    'content-type': 'application/json; charset=utf-8',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
                },
                callback=self.parse
            )

    def parse_summary(self, response):
        address = response.xpath("//h2[@itemprop='address']/text()").get()
        description = response.xpath("normalize-space(//div[@itemprop='description']/text())").get()
        category = response.request.meta['cat']
        features = response.request.meta['fea']
        price = response.request.meta['pri']
        city = response.request.meta['city']
        url = response.request.meta['url']
        yield {
            'address': address,
            'description': description,
            'category': category,
            'features': features,
            'price': price,
            'city': city,
            'url': url,
            'index': response.request.meta['index']
        }


