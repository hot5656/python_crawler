import scrapy
from scrapy.selector import Selector
# add Itemloader
from scrapy.loader import ItemLoader
import json
from ..items import SteamItem


class MoreBestSpider(scrapy.Spider):
    name = 'more_best'
    allowed_domains = ['store.steampowered.com']
    offset_index = 0
    INCREASEMENT_COUNT = 50
    ITEM_MAX = 500
    # print game_name + release_date
    item_index = 1

    def start_requests(self):
        page_condition = f"query&start={self.offset_index}&count=50&dynamic_data=&sort_by=_ASC&supportedlang=english&snr=1_7_7_7000_7&filter=topsellers&infinite=1"
        url = f"https://store.steampowered.com/search/results/?{page_condition}"

        yield scrapy.Request(
            url = url,
            method = "GET",
            callback=self.update_query
        )

    def update_query(self, response):
        steam_item = SteamItem()

        resp_dict = json.loads(response.body)
        html = resp_dict['results_html']
        start_index = resp_dict['start']
        print("==================")
        print(f"start={start_index}, total_count={resp_dict['total_count']} ")
        # print(html)
        # print("==================")
        # with open('index.html', 'w', encoding='utf-8') as f:
        #     f.write(html)

        sel = Selector(text=html)
        games = sel.xpath("//a")
        for game in games:
            # add Itemloader
            loader = ItemLoader(item=SteamItem(), selector=game, response=response)
            # loader.add_css()
            # loader.add_value()
            loader.add_xpath('game_url', ".//@href")
            loader.add_xpath('img_url', ".//div[@class='col search_capsule']/img/@src")
            loader.add_xpath('game_name', ".//span[@class='title']/text()")
            loader.add_xpath('release_date', ".//div[@class='col search_released responsive_secondrow']/text()")
            loader.add_xpath('platforms', ".//span[contains(@class,'platform_img') or @class='VR Supported']/@class")
            loader.add_xpath('reviews_summary', ".//span[contains(@class,'search_review_summary')]/@data-tooltip-html")
            loader.add_xpath('discount_rate', ".//div[contains(@class,'search_discount')]/span/text()")
            loader.add_xpath('original_price', ".//div[contains(@class,'search_price_discount_combined')]")
            loader.add_xpath('discounted_price', "(.//div[contains(@class, 'search_price discounted')]/text())[2]")
            loader.add_value('index', self.item_index)
            self.item_index += 1

            # add Itemloader
            # output
            yield loader.load_item()

        if (start_index + self.INCREASEMENT_COUNT) < self.ITEM_MAX:
            offset_index = start_index + self.INCREASEMENT_COUNT
            print("2 ==================")
            print(f"next offset_index={offset_index}")

            page_condition = f"query&start={offset_index}&count=50&dynamic_data=&sort_by=_ASC&supportedlang=english&snr=1_7_7_7000_7&filter=topsellers&infinite=1"
            url = f"https://store.steampowered.com/search/results/?{page_condition}"
            yield scrapy.Request(
                url = url,
                method = "GET",
                callback=self.update_query
            )


