from bs4 import BeautifulSoup as beauty
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
url = "https://web.archive.org/web/20190101085451/https://coinmarketcap.com/"

info = scraper.get(url).text
soup = beauty(info, "html.parser")
soup = soup.find_all('a', 'currency-name-container link-secondary')

for data in soup:
    sub_url = f"https://web.archive.org{data['href']}"
    print("===============")
    # print(data.get_text())
    print(sub_url)

    info2 = scraper.get(sub_url).text
    soup2 = beauty(info2, "html.parser")
    if soup2.find('span', 'label label-success'):
        h1_str = soup2.find('h1').text.strip().split('\x0a')
        print(f"name: {h1_str[0]}")
        print(f"rank: {soup2.find('span', 'label label-success').text}")
        print(f"price(USD): {soup2.find('span', 'h2 text-semi-bold details-panel-item--price__value').text}")
    else:
        print(f"error link: {data.get_text()}")

