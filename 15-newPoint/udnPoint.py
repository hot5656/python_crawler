from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

udn_url = 'https://udn.com/news/breaknews/1'


def page_down(element, times, sec):
  print("page_down...")
  for i in range(times):
    # print(i)
    element.send_keys(Keys.PAGE_DOWN)
    sleep(sec)  # bot id protection

def main():
  browser = webdriver.Chrome()
  browser.get(udn_url)
  sleep(2)

  element = browser.find_element(By.TAG_NAME, "body")
  # press page down
  count=0
  for count in range(2):
    page_down(element, 1, 0.5)

  # get news
  print('\n\n聯合報今日即時')
  news =  browser.find_elements(By.CLASS_NAME, "story-list__news")
  i = 1
  for new in news:
    new_html =  new.get_attribute('innerHTML')
    soup = BeautifulSoup(new_html, 'html5lib')
    title = soup.find('div', {'class' : 'story-list__text'}).find('a').text
    time_tag = soup.find('div', {'class' : 'story-list__info'})
    if time_tag:
      time_tag = time_tag.text.strip().split('\n')[1].strip()
    else:
      time_tag = ""

    # check no title mean not exist
    if len(title) != 0:
      print(f'{i:02d} {time_tag:16s} {title}')
      i += 1

  # exit browser
  browser.quit()

if __name__ == '__main__':
  main()
