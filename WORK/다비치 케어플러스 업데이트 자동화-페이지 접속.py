
# 다비치 페이지 직접 접속해서 데이터 자동 업데이트하기
import pyautogui as pa
import schedule
import time
import requests
from bs4 import BeautifulSoup

# 다비치 웹 페이지 가져오기
url = 'http://davichi.koreasarang.co.kr/'
html = requests.get(url)

# HTML 피싱
soup = BeautifulSoup(html.text, 'lxml')

# 로그인 폼 찾기
div = soup.find('input', class_='login')
print(div)







login_form = soup.find('form', {'id': 'mb_login'})

# 폼 데이터 추출
print(login_form)
