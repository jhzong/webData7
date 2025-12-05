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
from selenium.webdriver.support.ui import WebDriverWait # 대기툴
from selenium.webdriver.support import expected_conditions as EC # 대기툴
from selenium.webdriver.chrome.options import Options
# 이메일발송 라이브러리
import smtplib
from email.mime.text import MIMEText
# 날짜함수
from datetime import datetime

# ### 임시비밀번호 함수
# def random_pw():
#     arr=[i for i in range(10)]
#     # arr2=random.sample(arr,8)
#     # print(arr)
#     ranNum="".join(map(str,random.sample(arr,8)))
#     print(ranNum)
#     return ranNum

### 웹스크랩핑(오늘의 날씨)
# # .selenium으로 정보가져오기
# browser=webdriver.Chrome()
# browser.get("http://www.naver.com")
# time.sleep(1)# 버퍼링 딜레이(C=정보량/시간)
# soup=BeautifulSoup(browser.page_source,"lxml")
# with open("naver1.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())

# 온도/날씨, 
with open("naver1.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")
weather=soup.find('div',{'class':'DailyBoardView-module__weather_temperature___pOAGy'}).text.strip().replace(' ','').split('\n')
print(weather[0],weather[2])

today_weather=f"기온:{weather[0]} / 날씨:{weather[2]}"

# 최고/최저
temp_HL=soup.find('div',{'class':'DailyBoardView-module__weather_temperature___pOAGy'}).text.strip().replace(' ','').split('\n')

# 날짜
today=datetime.today()
now=today.strftime('%Y-%m-%d %H:%M:%S')
print(now)


# 임시비번
# content=f'''
# 임시비밀번호:{random_pw()}
# '''

# # 날씨
# content=f'''
# {now}
# {today_weather}
# {}
# '''
# print(content)


# # 메일내용부분
# msg=MIMEText(content)
# msg['From']='jhzong@naver.com'# 보내는메일
# msg['To']='jhzong05@gmail.com'# 받는주소
# msg['Subject']='임시비밀번호를 발송합니다.'# 제목
# # 메일서버정보
# s=smtplib.SMTP('smtp.naver.com',587)#
# # 메일서버접근
# s.starttls()
# # 서버로그인
# s.login('jhzong@naver.com','WXEPSFSR82KX')
# # 서버발송
# # 보내는주소,받는주소,내용
# s.sendmail('jhzong@naver.com','jhzong05@gmail.com',msg.as_string())
# print(msg.as_string())
# # 메일서버 닫기
# s.close()

# print('이메일 발송')