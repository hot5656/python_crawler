from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# 出現以下錯誤, 增加 options mask
# [15856:11828:1225/110356.222:ERROR:device_event_log_impl.cc(215)]
# [11:03:56.222] USB: usb_device_handle_win.cc:1045 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# add argument headless - no open browser
options.add_argument('--headless')

# change executable_path to service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://duckduckgo.com")

search_input = driver.find_element(By.ID, "search_form_input_homepage")
search_input.send_keys("My User Agent")
# click button
# search_btn = driver.find_element(By.ID, "search_button_homepage")
# search_btn.click()

# press Enter
search_input.send_keys(Keys.ENTER)

# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")

print("======================================")
print(driver.page_source)
print("======================================")

# need close
driver.close()