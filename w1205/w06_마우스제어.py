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
# 마우스제어
import pyautogui

# 2.selenium으로 정보가져오기
browser=webdriver.Chrome()
browser.get("http://www.naver.com")
browser.maximize_window()# 창화면 확대


# pyautogui.sleep(1)# 대기
# pyautogui.scroll(-700)# 스크롤
# pyautogui.sleep(2)
# pyautogui.scroll(700)
pyautogui.moveTo(890,280)# 이동
pyautogui.sleep(1)
pyautogui.click()

input('hold')