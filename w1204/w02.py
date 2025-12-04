from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

browser=webdriver.Chrome()
url="http://www.naver.com"
# selenium 4.3버전에서 찾기 변경됨.
# 1.url 페이지 열기(네이버)
browser.get(url)
# 2.검색창에 검색(시가총액순위)
element=browser.find_element(By.ID,"query")
element.click()# click():클릭명령어
element.send_keys("시가총액 순위")# input 명령어
# 3.ENTER키 입력
element.send_keys(Keys.ENTER)
time.sleep(1)
element=browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[2]/div/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a')#Xpath이용해 태그주소 찾기
element.click()


input("대기")

# # input(글자 입력) 명령어
# element.send_keys("시가총액")
# # input후 enter입력
# element.send_keys(Keys.ENTER)





