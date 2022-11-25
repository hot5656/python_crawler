import requests
from bs4 import BeautifulSoup

dict_url = 'https://tw.dictionary.search.yahoo.com/'
search_head = 'search?p='
search_tail = '&fr=sfp&iscqry=&fr2=sb-top-search'

def main():
  word = 'java'
  search_url = dict_url + search_head + word + search_tail
  # search_url = 'https://tw.dictionary.search.yahoo.com/search?p=java&fr=sfp&iscqry=&fr2=sb-top-search'

  # print(f'=={search_url}==')
  # print(f'=={search_url2}==')
  # return
  page = get_web_page(search_url)
  if (page):
    soup = BeautifulSoup(page, 'html5lib')
    print(soup)

def get_web_page(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text

if __name__ == '__main__':
  main()