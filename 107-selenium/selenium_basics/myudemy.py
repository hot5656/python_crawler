# udemy 還是有 cloudflare protect 問題
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import env
import time

# 出現以下錯誤, 增加 options mask
# [15856:11828:1225/110356.222:ERROR:device_event_log_impl.cc(215)]
# [11:03:56.222] USB: usb_device_handle_win.cc:1045 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# set browser not auto quit()
options.add_experimental_option('detach', True)

# add argument headless - no open browser
# options.add_argument('--headless')

# auto install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.udemy.com/")

time.sleep(2)

# login_entry = driver.find_element(By.XPATH, "//a[@data-purpose='header-login']")
login_entry = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@data-purpose='header-login']"))
)
login_entry.click()

# print("reset driver")
# handle = driver.current_window_handle
# driver.service.stop()
# time.sleep(7)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.switch_to.window(handle)
# print("continue")
# time.sleep(3)


# username = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "email"))
# )
# password = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "password"))
# )
# username.send_keys(env.UDEMY_USERNAME)
# password.send_keys(env.UDEMY_PASSWORD)

# login = driver.find_element(By.XPATH, "//form[@data-disable-loader='true']/button")
# login.click()

# # import time
time.sleep(3)
# print(driver.get_cookies())

# save page to image
# driver.save_screenshot("datacamp.png")

# mycourse = driver.find_element('//a[@data-purpose="my-courses"]')
# print(mycourse)

# import codecs
# import os
# #open file in write mode with encoding
# name = os.path.join("", "index.html")
# file = codecs.open(name, "w", "utf−8")
# #obtain page source
# h = driver.page_source
# #write page source content to file
# file.write(h)

# save page to image
# driver.save_screenshot("index.png")


# driver.quit()
