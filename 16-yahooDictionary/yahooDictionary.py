import requests
from bs4 import BeautifulSoup

dict_url = 'https://tw.dictionary.search.yahoo.com/'
search_head = 'search?p='
search_tail = '&fr=sfp&iscqry=&fr2=sb-top-search'

def main():
  while True:
    word = input("\nPlease enter a word : ")
    if len(word.strip()) == 0:
      print('search quit!')
      break
    search_dictionary(word)

# java - correct input
# swd  - no word
# swf  - english disctript
# dwf  - =...
# pm   - =...
def search_dictionary(word):
  # word = 'java'
  search_url = dict_url + search_head + word + search_tail
  page = get_web_page(search_url)
  i = 1
  mean = None
  if(page):
    soup = BeautifulSoup(page, 'html5lib')
    if soup.find('h3').text.strip()  == '很抱歉，字典找不到您要的資料喔！':
      print(f' "{word}" isn\'t found')
      means = word
    else:
      try:
        means = soup.find_all('div', {'class' : 'dictionaryExplanation'})
        if means:
          for item in means:
            print(f' {item.text}')
        else:
            print(f' "{word}" isn\'t found')
      except:
        pass

    if means == None:
      print(f' "{word}" isn\'t found')

  return

def get_web_page(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text

if __name__ == '__main__':
  main()