# omulee@naver.com
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
# browser.get("http://www.naver.com")
# time.sleep(1)
# soup=BeautifulSoup(browser.page_source,"lxml")
# with open("naver_w.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())

with open("naver_w.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")
    
# 날씨정보(기온,날씨,최고/저기온,미세먼지)
weather=soup.find('div',{'class':'DailyBoardView-module__weather_temperature___pOAGy'}).text.strip().replace(' ','').split('\n')
# print(weather[0],weather[2])
temp_H=soup.find('span',{'class':'DailyBoardView-module__temperature_low___aC6Fe'}).text.strip().replace(' ','').split('\n')
temp_L=soup.find('span',{'class':'DailyBoardView-module__temperature_high___QLp_M'}).text.strip().replace(' ','').split('\n')
# print(temp_H[2],temp_L[2])

today_weather=f'''기온:{weather[0]}, 날씨:{weather[2]}
최고:{temp_H[2]} / 최저:{temp_L[2]}'''
print(today_weather)

content=f'''
{today_weather}
'''
print(content)


# 메일내용부분
msg=MIMEText(content)
msg['From']='jhzong@naver.com'# 보내는메일
msg['To']='omulee@naver.com'# 받는주소
msg['Subject']='오늘날씨를 발송합니다.'
# 메일서버정보
s=smtplib.SMTP('smtp.naver.com',587)#
# 메일서버접근
s.starttls()
# 서버로그인
s.login('jhzong@naver.com','WXEPSFSR82KX')
# 서버발송
# 보내는주소,받는주소,내용
s.sendmail('jhzong@naver.com','omulee@naver.com',msg.as_string())
print(msg.as_string())
# 메일서버 닫기
s.close()

print('이메일 발송')