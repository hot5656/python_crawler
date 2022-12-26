import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class CoinSpiderSeleniunm(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20200116052415/https://www.livecoin.net/en']

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # add argument headless - no open browser
        options.add_argument('--headless')

        # change executable_path to service
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # set windows size(width, height)
        driver.set_window_size(1920, 1080)
        driver.get("https://web.archive.org/web/20200116052415/https://www.livecoin.net/en")

        print("=======================")
        # get by class then click - not ok
        # rur_tab_class = driver.find_element(By.CLASS_NAME, "filterPanelItem___2z5Gb ")
        # rur_tab_class[4].click()

        # get by xpath then click - ok
        rur_tab = driver.find_element(By.XPATH,"//div[@class='filterPanelItem___2z5Gb '][4]")

        # add deleay, then click ok
        time.sleep(5)

        # print("=======================")
        # print(rur_tab)
        # print(rur_tab.text)
        print("=======================")
        # get by xpath then click - ok
        rur_tab.click()
        print("=======================")

        # time.sleep(200)

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)

        # print(resp)
        for currency in resp.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }