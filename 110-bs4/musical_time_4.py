
import requests
from bs4 import BeautifulSoup
import lxml

URL_BASE = 'https://www.billboard.com/charts/hot-100/'


# input date
prompt_str = "Which year do you want to trave to? Type the date in this format YYYY-MM-DD:"
while True:
    switch_date_str = input(prompt_str)
    year, month, day = [int(item) for item in switch_date_str.split('-')]
    if year!=0 and month!=0 and day!=0:
        break

reponse = requests.get(f"{URL_BASE}{switch_date_str}/")
web_html = reponse.text

soup = BeautifulSoup(web_html, 'lxml')
print(soup.title)