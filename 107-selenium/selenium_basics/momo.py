# selenium 抓 iphone 14 pro

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapy.selector import Selector

import time


# 出現以下錯誤, 增加 options mask
# [15856:11828:1225/110356.222:ERROR:device_event_log_impl.cc(215)]
# [11:03:56.222] USB: usb_device_handle_win.cc:1045 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# set browser not auto quit()
options.add_experimental_option('detach', True)

# add argument headless - no open browser
options.add_argument('--headless')

# auto install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.momoshop.com.tw/search/searchShop.jsp")

search_input = driver.find_element(By.ID, "keyword")

# input string
search_input.send_keys('iphone 14 pro')

# input special key
search_input.send_keys(Keys.ENTER)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "toothUl"))
    )
finally:
    # driver.quit()
    pass

products = driver.find_elements(By.XPATH, "//div[@class='listArea']/ul/li")
for product in products:
    # element to Selector
    product_sel = Selector(text=product.get_attribute('innerHTML'))
    title = product_sel.xpath(".//h3[@class='prdName']/text()").get()
    print(title)


# quit browser
driver.quit()