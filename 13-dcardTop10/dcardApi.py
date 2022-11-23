from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import json

def main():
  # show_dcard_json_file('posts.json')
  call_dcard_api()


def call_dcard_api():
  browser = webdriver.Chrome()
  browser.get('https://www.dcard.tw/service/api/v2/posts')
  sleep(2)

  # print(browser.page_source)
  soup = BeautifulSoup(browser.page_source, 'html.parser')
  api_resp = soup.find('pre')

  if api_resp:
    # show respone json
    if is_json(api_resp.string):
      # print(api_resp.string)
      dcard_shwo_api_title(api_resp.string)
      print("get from dcard api....")
    else:
      print('===== query api falure =====')
      print(api_resp.string)
  else:
    print('response Invalid')

  # json_resp = json.loads(api_resp.text)
  # print('----------------------')
  # print(json_resp)

  # exit browser
  browser.quit()

def show_dcard_json_file(file_name):
  # encoding='utf-8', load 中文正常
  f = open(file_name, 'r', encoding='utf-8')
  content = f.read()
  # print(content)
  dcard_shwo_api_title(content)
  print("get from file....")

  f.close()


def dcard_shwo_api_title(content):
  # load json to variable
  parsed = json.loads(content)

  # show json
  # ensure_ascii=False, show 中文
  # print(json.dumps(parsed, indent=4, ensure_ascii=False))

  i = 1
  for item in parsed:
    print('('+str(i)+') '+item['title'])
    i += 1


# check json format
def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

if __name__ == '__main__':
  main()
