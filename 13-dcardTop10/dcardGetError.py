import requests
# from fake_useragent import UserAgent
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep

url = 'https://www.dcard.tw/f'
url_api = 'https://www.dcard.tw/service/api/v2/posts'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}


def main():
  current_page = get_web_page(url)
  if current_page:
    print(current_page)

  current_page = get_web_page(url_api)
  if current_page:
    print(current_page)
  # return
  # if current_page:
  #   print(current_page)
  #   soup = BeautifulSoup(current_page, 'html.parser')
  #   topic_entry_pattern = '^PostEntry_container_'
  #   topic_title_pattern = 'strong'
  #   find_top10_hot_title(soup, topic_entry_pattern, topic_title_pattern)


def get_web_page(url):
  resp = requests.get(url)
  print('=================')
  print(resp)
  print('=================')
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text

# def get_web_page2(url):
  # ua = UserAgent()
  # print(ua.chrome)
  # header = {'User-Agent':str(ua.chrome)}
  # print(header)
  # # url = "https://www.hybrid-analysis.com/recent-submissions?filter=file&sort=^timestamp"
  # htmlContent = requests.get(url, headers=header)

  # ua = UserAgent()
  # user_agent = ua.random
  # # 產生 headers
  # headers = {'user-agent': user_agent}
  # htmlContent = requests.get(url, headers=headers)

  # driver = webdriver.Chrome()
  # driver.get(url)
  # sleep(2)
  # eles = driver.find_elements_by_class_name('tgn9uw-0')
  # eles = driver.find_element(By.CLASS_NAME, "kpbNHU")
  # for ele in eles:
  #     print(ele)
  # driver.quit()
  # print('===============')
  # print(eles)
  # for ele in eles:
  #   print('===============')
  #   print(ele)


  # print(htmlContent)

# def find_top10_hot_title(soup, topic_entry_pattern, topic_title_pattern):
#   top_ten_topic = soup.find_all('div', {'class': re.compile(topic_entry_pattern)})
#   i = 1
#   for topic in top_ten_topic[:10]:
#     print(str(i) + ': ' + topic.find(topic_title_pattern).text)
#     i += 1

  # pass
  # top_ten_topic = soup.find_all('div', {})

if __name__ == '__main__':
  main()