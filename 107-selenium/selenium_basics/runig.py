
# IG login 抓圖檔

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

import os
import wget

import env

# 出現以下錯誤, 增加 options mask
# [15856:11828:1225/110356.222:ERROR:device_event_log_impl.cc(215)]
# [11:03:56.222] USB: usb_device_handle_win.cc:1045 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# set browser not auto quit()
options.add_experimental_option('detach', True)

# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# add argument headless - no open browser
# options.add_argument('--headless')

# auto install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

keyword = '#dog'
username.send_keys(env.USER_NAME)
password.send_keys(env.PASSWORD)

login = driver.find_element(By.XPATH, "//button[@class='_acan _acap _acas _aj1-']")
login.click()

search_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[local-name() = 'svg'][contains(@aria-label, '搜尋')]"))
)
search_button.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, '搜尋輸入')]"))
)
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(1)
search.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='_aagv']/img"))
)

for i in range(5) :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

# generate dirctory
path = os.path.join(keyword)
os.mkdir(path)

pics = driver.find_elements(By.XPATH, "//div[@class='_aagv']/img")
count = 1
for pic in pics:
    save_as = os.path.join(path, f"{keyword}{count}.jpg")
    # print(pic.get_attribute('src'))
    wget.download(pic.get_attribute('src'), save_as)
    count += 1

driver.close()