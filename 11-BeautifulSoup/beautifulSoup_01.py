import requests
from bs4 import BeautifulSoup

def get_web_page(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text


url = 'http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html'

def main():
  current_page = get_web_page(url)
  if current_page:
    # print(current_page)
    # print('===============================')
    soup = BeautifulSoup(current_page, 'html.parser')
    # print(soup)
    # print('===============================')
    # soup2 = BeautifulSoup(current_page, 'html5lib')
    # print(soup2)

    print('===============================')
    print('First soup.h4 : ')
    print(soup.h4)
    # print('===============================')
    # print('First soup.find("h4")')
    # print(soup.find("h4"))
    # print('===============================') .....
    # print('First soup.find("h4").text')
    # print(soup.find("h4").text)
    print('===============================')
    print('First soup.h4.a.text : ')
    print(soup.h4.a.text)

    print('===============================')
    print('ALL soup.h4.a.text : ')
    h4_tags = soup.find_all('h4')
    # print('===============================')
    # print(h4_tags)
    for h4 in h4_tags:
      # h4.text 會有很多空白
      print(h4.a.text)
    print('===============================')
    print('ALL soup.h4.a.text for class="card-title" : ')
    # 以下代表相同
    # h4_tags = soup.find_all('h4', class_='card-title')
    # h4_tags = soup.find_all('h4', 'card-title')
    # h4_tags = soup.find_all('h4', {'class' : 'card-title'})
    h4_tags = soup.find_all('h4', 'card-title')
    for h4 in h4_tags:
      print(h4.a.text)
    print('===============================')
    print('soup.find(id="mac-p").text.strip() : ')
    print('-'+soup.find(id='mac-p').text.strip()+'-')

    # print('===============================')
    # 若屬行含非標準會有錯誤
    # print(soup.find(data-foo='mac-p').text.strip())
    print('===============================')
    # 改用以下方式
    print(soup.find_all('', {'data-foo': 'mac-foo'}))

    print('===============================')
    print('<< blog list >>')
    divs = soup.find_all('div', 'content')
    for div in divs:
        print(div.h6.text.strip(), div.h4.text.strip(), div.p.text.strip())
    print('===============================')
    print('<< blog list 2nd way>>')
    for div in divs:
      print([s for s in div.stripped_strings])


if __name__ == '__main__':
  main()