
# IG login 抓圖檔 - 未完成(找不到進入 search button,似乎是會變動)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

# 出現以下錯誤, 增加 options mask
# [15856:11828:1225/110356.222:ERROR:device_event_log_impl.cc(215)]
# [11:03:56.222] USB: usb_device_handle_win.cc:1045 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# set browser not auto quit()
options.add_experimental_option('detach', True)

# auto install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

username.send_keys("")
password.send_keys("")

login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
login.click()

# dontcare_button = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_AA"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button'))
# )
# dontcare_button.click()


search_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, '_ab6-'))
)

import time
time.sleep(5)

searchs = driver.find_elements(By.CLASS_NAME, '_ab6-')
for search in searchs:
    print("======================")
    print(search.get_attribute('innerHTML'))
# search_button.click()

# search = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, '_aauy'))
# )
# search.send_keys('#cat')
# search.send_keys(Keys.ENTER)