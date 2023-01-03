from bs4 import BeautifulSoup as beauty
import cloudscraper

# scraper = cloudscraper.create_scraper(delay=10, browser='chrome',debug=True)
scraper = cloudscraper.create_scraper(delay=10, browser='chrome')
url = "https://www.fiverr.com/categories/online-marketing"


info = scraper.get(url).text
# print("0 ===============")
# print(info)
soup = beauty(info, "html.parser")
# print("1 ===============")
# print(soup)
soup = soup.find_all('a', 'item-name')
print("2 ===============")
print(soup)

for data in soup:
    sub_url = 'https://www.fiverr.com'+data['href']
    print("===============")
    print(data.get_text())
    # print(sub_url)

    # info2 = scraper.get(sub_url).text
    # soup2 = beauty(info2, "html.parser")
    # if soup2.find('p', 'sc-subtitle'):
    #     print(f"title: {soup2.find('h1').text}")
    #     print(f"description: {soup2.find('p', 'sc-subtitle').text}")
    # else :
    #     print("error")
    #     print(f"title: {soup2.find('h1')}")
    #     print(f"description: {soup2.find('p', 'sc-subtitle')}")

