# 엔비디아 and 삼성전자 주식가격
import time
import os
import random
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # 대기툴
from selenium.webdriver.support import expected_conditions as EC # 대기툴
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# browser=webdriver.Chrome()
# browser.get("https://finance.naver.com/")
# time.sleep(1)
# soup=BeautifulSoup(browser.page_source,"lxml")
# with open("naver_f.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())

with open("naver_f.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")
    
# 삼성전자
soup.find()