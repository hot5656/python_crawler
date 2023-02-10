from bs4 import BeautifulSoup
import lxml


# f = open("website.html", "r", encoding='utf-8')
# content = f.read()
# print(content)

with open('website.html', 'r', encoding='utf-8') as file:
    content = file.read()

# soup = BeautifulSoup(content, "html.parse")
# 較快速
soup = BeautifulSoup(content, "lxml")

# print(soup.title)       # <title>Angela's Personal Site</title>
# print(soup.title.name)  # show tag: title
# print(soup.title.string)    # Angela's Personal Site
# print("==================")
# print(soup)
# print("==================")
# print(soup.prettify()) # 美化排列

# find 1st tag
# print(soup.a)   # 1st tag a
# print(soup.p)   # 1st tag p
# print(soup.li)  # 1st tag li

# find all tag
# links = soup.find_all('a')
# print(links)
# for link in links:
#     # all accept
#     # print(link.get_text())
#     # print(link.getText())
#     # print(link.text)
#     # get link
#     print(link.get('href'))

# find tag add condition
# print(soup.find("h1", id='name'))
# class is keyword, change to class_
# print(soup.find("h3", class_='heading'))

print(soup.select_one("p a"))
print(soup.select_one("#name"))
print(soup.select(".heading"))

