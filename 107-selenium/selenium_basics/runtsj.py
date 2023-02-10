# ActionChains 模擬遊戲操作

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

# 出現以下錯誤, 增加 options mask
# [15856:11828:1225/110356.222:ERROR:device_event_log_impl.cc(215)]
# [11:03:56.222] USB: usb_device_handle_win.cc:1045 Failed to read descriptor from node connection: 連結到系統的某個裝置失去作用。 (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# set browser not auto quit()
# options.add_experimental_option('detach', True)

# add argument headless - no open browser
# options.add_argument('--headless')

# auto install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://tsj.tw/")

blow = driver.find_element(By.ID, 'click')
blow_count = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
click_count= driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/h4[1]')
items = []
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
items.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
prices = []
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))


actions = ActionChains(driver)

for i in range(10000):
    actions.click(blow)
    actions.perform()
    count=int(blow_count.text.replace("您目前擁有","").replace("技術點",""))
    count_all = click_count.text
    for j in range(3):
        # print(prices[j].text)
        # try:
        price = int(prices[j].text.replace("技術點",""))
        # except:
        #     break
        if price <= count:
            print(f"({i}) ({j}){count} {price} -{count_all}")
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(items[j])
            upgrade_actions.click()
            upgrade_actions.perform()
            break

    # time.sleep(0.5)