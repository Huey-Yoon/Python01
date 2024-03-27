
# 네이버 뉴스 헤드라인 크롤링

import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'lxml')

div = soup.find('div', class_='cjs_news_tw')
print(div)

headline = div.get_text()  # find('div', class_='cjs_t')
print(headline)

