
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
import json

def main() :
  page = get_web_page('https://movies.yahoo.com.tw/movie_thisweek.html')
  if page:
    movies = get_movies(page)
    for movie in movies:
      print(movie)
    with open('movie.json', 'w', encoding='utf-8') as file:
      json.dump(movies, file, indent=2, sort_keys=True, ensure_ascii=False)

    # show_movies(page)

def get_web_page(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text

def show_movies(page):
  page_num = 1
  soup = BeautifulSoup(page, 'html5lib')
  show_movies_info(soup, page_num)
  next = soup.find('li', {'class': 'nexttxt'}).find('a')
  while next:
    page_num += 1
    # print('next url = ' + next['href'])
    page = get_web_page(next['href'])
    soup = BeautifulSoup(page, 'html5lib')
    show_movies_info(soup, page_num)
    next = soup.find('li', {'class': 'nexttxt'}).find('a')


def show_movies_info(soup, page_num):
  movies = soup.find_all('li')
  i = 1
  for movie in movies:
    movie_info = movie.find('div', {'class': 'release_info'})
    if movie_info:
      print(f'\n\r========= {page_num}-{i} =========')
      print(movie_info.find('div', {'class': 'release_movie_name'}).find('a').text.strip())
      print(movie_info.find('div', {'class': 'en'}).find('a').text.strip())
      # some movie no exceptation
      # print(movie_info.find('div', {'class': 'leveltext'}).find('span').text.strip())
      exceptation = movie_info.find('div', {'class': 'leveltext'})
      if exceptation:
        print(exceptation.text.strip().split('\n')[0])
      print(movie_info.find('div', {'class': 'release_text'}).find('span').text.strip())
      print(movie_info.find('div', {'class': 'release_movie_time'}).text.strip().split(' ')[-1])
      # 修正中文 show 亂碼
      trailer_url = unquote(movie_info.find('div', {'class': 'release_movie_name'}).find('a')['href'], 'utf-8')
      print(trailer_url)
      print(movie.find('div', {'class': 'release_foto'}).find('img')['data-src'])
      i += 1

def get_movies(page):
  movies_return = []
  soup = BeautifulSoup(page, 'html5lib')
  movies = soup.find_all('li')
  for movie in movies:
      item = get_movie_info(movie)
      if item:
        movies_return.append(item)

  next = soup.find('li', {'class': 'nexttxt'}).find('a')
  while next:
    # print('next url = ' + next['href'])
    page = get_web_page(next['href'])
    soup = BeautifulSoup(page, 'html5lib')
    movies = soup.find_all('li')
    for movie in movies:
        item = get_movie_info(movie)
        if item:
          movies_return.append(item)
    next = soup.find('li', {'class': 'nexttxt'}).find('a')

  return movies_return

def get_movie_info(movie):
  item = None
  movie_info = movie.find('div', {'class': 'release_info'})
  if movie_info:
    # 修正中文 show 亂碼
    trailer_url = unquote(movie_info.find('div', {'class': 'release_movie_name'}).find('a')['href'], 'utf-8')
    # some movie no exceptation
    exceptation = movie_info.find('div', {'class': 'leveltext'})
    if exceptation:
      pexceptation = exceptation.text.strip().split('\n')[0]
    else:
      pexceptation = ""

    # some movie no exceptation
    item = {
      'ch_name': movie_info.find('div', {'class': 'release_movie_name'}).find('a').text.strip(),
      'en_name': movie_info.find('div', {'class': 'en'}).find('a').text.strip(),
      'expectation': pexceptation,
      'intro': movie_info.find('div', {'class': 'release_text'}).find('span').text.strip(),
      'poster_url': movie.find('div', {'class': 'release_foto'}).find('img')['data-src'],
      'release_date': movie_info.find('div', {'class': 'release_movie_time'}).text.strip().split(' ')[-1],
      'trailer_url': trailer_url
    }
  return item

if __name__ == '__main__':
  main()