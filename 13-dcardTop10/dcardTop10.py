from bs4 import BeautifulSoup
from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def find_top10_hot_title(soup, post_list, key_pattern):
  top_ten_topic = soup.find_all('div', {'data-key': re.compile(key_pattern)})
  i = 1
  print('length=' + str(len(top_ten_topic)))
  print('=======================')
  for topic in top_ten_topic:
    key = topic['data-key']
    print(key)
    if key in post_list:
      # if get already show * n *
      print('*'+str(i)+'* '+topic.find('h2').text.strip()+'==')
      # pass
    else:
      print('('+str(i)+') '+topic.find('h2').text.strip()+'==')
      post_list.append(topic['data-key'])
    print('=======================')
    i += 1

def page_down(element, times, sec):
  print("[%] Scrolling down.")
  for i in range(times):
    print(i)
    element.send_keys(Keys.PAGE_DOWN)
    sleep(sec)  # bot id protection

# save post - it check get post already
post_list = list()

if __name__ == '__main__':
  browser = webdriver.Chrome()
  browser.get('https://www.dcard.tw/f')
  sleep(2)

  # element for press page down
  element = browser.find_element(By.TAG_NAME, "body")

  # loop break when get >= 10 post
  count=0
  for count in range(10):
    page_down(element, 2, 0.5)
    html = browser.page_source
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    find_top10_hot_title(soup, post_list, 'post-*')
    print(post_list)
    if (len(post_list)>=10):
      break

  # # html write to file
  # # Opening the existing HTML file
  # Func = open("t1.html","w",encoding='utf-8')
  # # Adding input data to the HTML file
  # Func.write(html)
  # # Saving the data into the HTML file
  # Func.close()

  # exit browser
  browser.quit()
