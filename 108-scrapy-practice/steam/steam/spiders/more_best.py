import scrapy
from scrapy.selector import Selector
import json
from ..items import SteamItem
from w3lib.html import remove_tags


class MoreBestSpider(scrapy.Spider):
    name = 'more_best'
    allowed_domains = ['store.steampowered.com']
    offset_index = 0
    INCREASEMENT_COUNT = 50
    ITEM_MAX = 230
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

    def get_platforms(self, list_classes):
        platforms = []
        for item in list_classes:
            platform = item.split(' ')[-1]
            if platform == 'win':
                platforms.append('Windows')
            if platform == 'mac':
                platforms.append('Mac os')
            if platform == 'linux':
                platforms.append('Linux')
            if platform == 'vr_supported':
                platforms.append('VR supported')
        return platforms

    def remove_html(self, review_summary):
        cleaned_review_summary = ''
        try:
            cleaned_review_summary = remove_tags(review_summary)
        except TypeError:
            cleaned_review_summary = 'No reviews'
        return cleaned_review_summary

    def clean_discount_rate(self, discount_rate):
        if discount_rate:
            return discount_rate.lstrip('-')
        return discount_rate

    def get_original_price(self, selector_obj):
        original_price = ''
        div_with_discount = selector_obj.xpath(".//div[contains(@class, 'discounted')]")
        if div_with_discount:
            original_price = selector_obj.xpath(".//span/strike/text()").get()
        else:
            original_price = selector_obj.xpath("normalize-space(.//div[contains(@class, 'search_price')]/text())").get()
        return original_price

    def clean_discounted_price(self, discounted_price):
        if discounted_price:
            return discounted_price.strip()
        return discounted_price

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
            steam_item['game_url'] = game.xpath(".//@href").get()
            steam_item['img_url'] = game.xpath(".//div[@class='col search_capsule']/img/@src").get()
            steam_item['game_name'] = game.xpath(".//span[@class='title']/text()").get()
            steam_item['release_date'] = game.xpath(".//div[@class='col search_released responsive_secondrow']/text()").get()
            steam_item['platforms'] = self.get_platforms(game.xpath(".//span[contains(@class,'platform_img') or @class='VR Supported']/@class").getall())
            steam_item['reviews_summary'] = self.remove_html(game.xpath(".//span[contains(@class,'search_review_summary')]/@data-tooltip-html").get())
            steam_item['discount_rate'] = self.clean_discount_rate(game.xpath(".//div[contains(@class,'search_discount')]/span/text()").get())
            steam_item['original_price'] = self.get_original_price(game.xpath(".//div[contains(@class,'search_price_discount_combined')]"))
            steam_item['discounted_price'] = self.clean_discounted_price(game.xpath("(.//div[contains(@class, 'search_price discounted')]/text())[2]").get())
            steam_item['index'] = self.item_index

            # print game_name + release_date
            # print(f"({self.item_index}) : {steam_item['game_name']} -  {steam_item['release_date']}")
            self.item_index += 1

            # output
            yield steam_item

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


