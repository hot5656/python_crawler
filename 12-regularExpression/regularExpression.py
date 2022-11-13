
import requests
from bs4 import BeautifulSoup
import re

url = 'http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html'

def main():
  current_page = get_web_page(url)
  soup = BeautifulSoup(current_page, 'html.parser')
  # get h1~6
  print("\nprint h1~6 -->")
  find_text_content_by_reg(soup, 'h[1-6]')
  # get.png
  # $ means the tail, the end of the string.
  # \. means "."
  print("\nprint image source -->")
  find_img_source_by_reg(soup, '\.png$')
  # .* means any 0~n character
  print("\nprint image source(include beginner) -->")
  find_img_source_by_reg(soup, 'beginner.*'+'\.png$')
  print("\nprint image source(include beginner) -->")
  count_blog_number(soup, 'card\-blog')
  print("\nprint image source(include crawler) -->")
  find_img_source_by_reg(soup, 'crawler.*')

def get_web_page(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text

def find_text_content_by_reg(soup, reg_pattern):
  for element in soup.find_all(re.compile(reg_pattern)):
    print(element.name, element.text.strip())

def find_img_source_by_reg(soup, reg_pattern):
  for img in soup.find_all('img', {'src': re.compile(reg_pattern)}):
    # print(img['class'])
    print(img['src'])

def count_blog_number(soup, pattern):
  count = len(soup.find_all('div', {'class' : re.compile(pattern)}))
  print("Blog count: " + str(count))

if __name__ == '__main__':
  main()