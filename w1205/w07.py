import time
import os
import random
import csv
# 웹스크랩핑
import requests
from bs4 import BeautifulSoup
# 셀레니움
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 이메일발송 라이브러리
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
# 날짜함수
from datetime import datetime
#마우스제어
import pyautogui

url="https://www.daum.net/"
browser=webdriver.Chrome()# 새창열기
browser.maximize_window()# 창화면 확대
browser.get(url)

# 검색
element=browser.find_element(By.ID,"q")
element.click()
element.send_keys('서울특별시 용산구 이태원동 아파트')
element.send_keys(Keys.ENTER)

print('대기')