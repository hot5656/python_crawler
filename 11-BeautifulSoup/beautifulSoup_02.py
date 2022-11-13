import requests
from bs4 import BeautifulSoup

url = 'http://blog.castman.net/web-crawler-tutorial/ch2/table/table.html'
def main():
  current_page = get_web_page(url)
  if current_page:
    # print(current_page)
    soup= BeautifulSoup(current_page, 'html.parser')
    count_course_number(soup)
    clalculate_course_average_price(soup)
    clalculate_course_average_price2(soup)
    retrieve_all_tr_content(soup)
    print("=============")

def get_web_page(url):
  resp = requests.get(url)
  if resp.status_code != 200:
    print('Invalid url:', resp.url)
    return None
  else:
    return resp.text

def count_course_number(soup):
  print('Total clouse count: ' + str(len(soup.find('table', 'table').tbody.find_all('tr'))))

def clalculate_course_average_price(soup):
  prices = []
  rows = soup.find('table', 'table').tbody.find_all('tr')
  for row in rows:
    price = row.find_all('td')[2].text
    print(price)
    prices.append(int(price))
  print('Average courage price: ' + str(sum(prices)/len(prices))+'\n')

def clalculate_course_average_price2(soup):
  prices = []
  links = soup.find_all('a')
  for link in links:
    price = link.parent.previous_sibling.text
    print(price)
    prices.append(int(price))
  print('Average courage price: ' + str(sum(prices)/len(prices))+'\n')

def retrieve_all_tr_content(soup):
  rows = soup.find('table', 'table').tbody.find_all('tr')
  for row in rows:
    # all_tds = row.find_all('td') - same as below
    all_tds = [td for td in row.children]
    # print(all_tds)
    if 'href' in all_tds[3].a.attrs :
      href = all_tds[3].a['href']
    else:
      href = None;
    print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])


if __name__ == '__main__':
  main()