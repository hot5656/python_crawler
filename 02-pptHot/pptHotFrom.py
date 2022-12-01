import requests
import time
import json
from bs4 import BeautifulSoup
import re

PTT_URL = 'https://www.ptt.cc'

def get_web_page(url):
    resp = requests.get(url=url, cookies={'over18': '1'})
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

def get_local_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
def get_location(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/', headers=headers).json()
    location_data = {
        "ip": ip,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

def get_ip(url):
    print('+', end="",flush=True)
    ip = None
    page = get_web_page(url)
    if page:
      soup_item = BeautifulSoup(page, 'html5lib')
      # dom = soup_item.find('span', {'class': 'f2'}).text
      dom = soup_item.find('div', {'id': 'main-container'}).text
      pattern = '來自: \d+\.\d+\.\d+\.\d+'
      match = re.search(pattern, dom)
      if match:
        return match.group(0).replace('來自: ', '')
      else:
        return None

def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html5lib')
    # Retrieve the link of previous page
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        # If post date matched:
        if d.find('div', 'date').text.strip() == date:
            # To retrieve the push count:
            push_count = 0
            push_str = d.find('div', 'nrec').text
            if push_str:
                try:
                    push_count = int(push_str)
                except ValueError:
                    # If transform failed, it might be '爆', 'X1', 'X2', etc.
                    if push_str == '爆':
                        push_count = 99
                    elif push_str.startswith('X'):
                        push_count = -10

            # To retrieve title and href of the article:
            if d.find('a'):
                href = d.find('a')['href']
                title = d.find('a').text
                author = d.find('div', 'author').text if d.find('div', 'author') else ''
                ip = get_ip(PTT_URL+href)
                if ip:
                  location_data = get_location(ip)
                else:
                  location_data = None
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count,
                    'author': author,
                    'ip': ip,
                    'location_data': location_data,
                })

    return articles, prev_url


def main():
    current_page = get_web_page(PTT_URL + '/bbs/Gossiping/index.html')
    if current_page:
        # To keep all of today's articles.
        articles = []
        # Today's date, here we remove the 0 at the head to match the format of PTT date.
        # API doc for strftime: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        # API doc for lstrip: https://www.tutorialspoint.com/python/string_lstrip.htm
        today = time.strftime("%m/%d").lstrip('0')
        current_articles, prev_url = get_articles(current_page, today)

        while current_articles:
            print('.', end="",flush=True)
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)
            if len(articles) >= 20:
              break

        i = 1
        print(" ")
        # for article in articles[:10]:
        for article in articles:
          if article["location_data"] == None:
            print(f'({i:02d})                {article["title"]}')
          else:
            print(f'({i:02d}) {article["ip"]:15s}-{article["location_data"]["country"]:15s} {article["title"]}')
          i += 1

        print('\nThere are ', len(articles), ' posts today.')


if __name__ == '__main__':
    # ip = get_local_ip()
    # if (ip != None):
    #   print(get_location(ip))
    main()
