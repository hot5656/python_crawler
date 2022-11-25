import requests
from bs4 import BeautifulSoup

apple_url = "https://www.appledaily.com.tw/realtime/recommend/"
ltn_url = "https://news.ltn.com.tw/list/breakingnews/popular"

def main():
  page = get_web_page(apple_url)
  if (page):
    print('蘋果今日焦點')
    show_apple_list(page)
  page = get_web_page(ltn_url)
  if (page):
    print('自由今日焦點')
    show_ltn_list(page)

def show_apple_list(page):
    soup = BeautifulSoup(page, 'html5lib')
    items = soup.find_all('div', {'class' : 'text-container'})
    i = 1
    for item in items:
      time_tag = item.find('div', {'class' : 'timestamp'}).text.strip().split('：')[1]
      title = item.find('div', {'class' : 'storycard-headline'}).span.text.strip()
      print(f'{i:02d} {time_tag} {title}')
      i += 1

def show_ltn_list(page):
    soup = BeautifulSoup(page, 'html5lib')
    items = soup.find('ul', {'class' : 'list'}).find_all('li')
    i = 1
    for item in items:
      time_tag = item.find('span', {'class' : 'time'}).text
      title = item.a['title']
      print(f'{i:02d} {time_tag:16s} {title}')
      i += 1

def get_web_page(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text


if __name__ == '__main__':
  main()