from bs4 import BeautifulSoup as beauty
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
url = "https://www.fiverr.com/categories/online-marketing"

info = scraper.get(url).text
soup = beauty(info, "html.parser")
soup = soup.find_all('a', 'item-name')

for data in soup:
    print("===============")
    print(data.get_text())