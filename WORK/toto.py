
# 배트맨 토토 승부식 웹 크롤링

import csv
import requests
from bs4 import BeautifulSoup

def get_batman_data():
    url = "https://www.betman.co.kr/main/mainPage/gamebuy/gameSlip.do?gmId=G101&gmTs=240039"  # 배트맨 사이트의 URL을 여기에 입력하세요
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }  # 필요에 따라 헤더 정보를 수정하세요

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        matches = soup.find_all('div', class_='match')  # 승부식 게임 데이터가 있는 태그를 찾습니다
        data = []
        for match in matches:
            teams = match.find_all('div', class_='team')  # 팀 정보를 추출합니다
            team1 = teams[0].text.strip()
            team2 = teams[1].text.strip()
            odds = match.find('span', class_='odds').text.strip()  # 배당률을 추출합니다
            data.append([team1, team2, odds])
        return data
    else:
        print("Failed to retrieve data")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Team 1', 'Team 2', 'Odds'])  # 헤더를 쓰기
        writer.writerows(data)

if __name__ == "__main__":
    batman_data = get_batman_data()
    if batman_data:
        save_to_csv(batman_data, 'batman_data.csv')
        print("Data saved successfully.")
