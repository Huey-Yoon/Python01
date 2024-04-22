# pyautogui 모듈 불러오기
import pyautogui as pa
import schedule
import time

# 좌표 객체 얻기
# print(pa.position())

def job():
    # 업데이트 버튼 좌표
    pa.moveTo(1784,181)
    pa.click(clicks=1)

    time.sleep(10)

    # 팝업창 닫기 버튼 좌표
    pa.moveTo(600,29)
    pa.click(clicks=1)

    # 보상완료관리 페이지 좌표
    pa.moveTo(103,325)
    pa.click(clicks=1)

    # 업데이트 버튼 좌표
    pa.moveTo(1784,181)
    pa.click(clicks=1)

    time.sleep(10)

    # 팝업창 닫기 버튼 좌표
    pa.moveTo(600,29)
    pa.click(clicks=1)

    # 보험료관리 페이지 좌표
    pa.moveTo(114,349)
    pa.click(clicks=1)

    # 업데이트 버튼 좌표
    pa.moveTo(1784,181)
    pa.click(clicks=1)

    time.sleep(10)

    # 팝업창 닫기 버튼 좌표
    pa.moveTo(600,29)
    pa.click(clicks=1)

    # 보상접수 페이지 좌표
    pa.moveTo(102,239)
    pa.click(clicks=1)

    print("다비치 자료 업데이트 완료!")
    while True:
        schedule.run_pending()
        time.sleep(1)

# schedule.every(10).minutes.do(job())

schedule.every().day.at("09:00").do(job())