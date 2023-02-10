from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/news")
cwebpage = response.text

soup = BeautifulSoup(cwebpage, "lxml")
print(soup.title)

article_texts = []
article_links = []
atticle_upvotes = []

# show article
links = soup.select(".titleline > a")
index = 1
for link in links:
    url = link.get("href")
    article_name = link.text
    # print(f"({index}) {article_name} {url}")
    index += 1
    article_texts.append(article_name)
    article_links.append(url)

# upvotes = soup.find_all("span", class_='score')
article_upvotes =[int(score.text.split()[0]) for score in soup.find_all("span", class_='score')]
# print(len(article_upvotes))
# print(article_texts)
# print("===============")
# print(article_links)

# sort by other list
# article_texts2 = [text for _,text in sorted(zip(article_upvotes,article_texts))]
# article_links2 = [link for _,link in sorted(zip(article_upvotes,article_links))]
# print(article_texts2)
# print(article_links2)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])