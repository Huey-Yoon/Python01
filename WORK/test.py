from pyautogui import click
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyscreeze
import PIL
import time


URL = "http://davichi.koreasarang.co.kr/bbs/login.php?url=http%3A%2F%2Fdavichi.koreasarang.co.kr%2Fadm%2F"

driver = webdriver.Chrome()
driver.get(url=URL)
time.sleep(1)

click('mb_id')
print('admin')
time.sleep(1)

click('login_pw')
print('davi1234')
time.sleep(1)

click('btn_submit')
time.sleep(1)

