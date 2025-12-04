from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

browser=webdriver.Chrome()
url="http://www.naver.com"
# 1.url 페이지 열기(네이버)
browser.get(url)

# 2.뉴스클릭
element=browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[5]/a/span[2]')
element.click()
time.sleep(2)


# 상단탭 
tabs=browser.window_handles# 리스트 가져오기(tabs)
browser.switch_to.window(tabs[1])# 2번째 탭 선택-tabs[0],tabs[1]

# 3.IT/과학 클릭
element=browser.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div/div/div/ul/li[6]/a/span')
element.click()

# 4. 첫번째 뉴스 클릭
element=browser.find_element(By.CLASS_NAME,'sa_text_title')
element.click()
time.sleep(2)
input("대기")


# # 선생님꺼
# # 1. naver 페이지 열기
# browser.get(url)
# # 2. 뉴스 선택 클릭
# browser.find_element(By.CLASS_NAME,"type_news").click()
# # 상단 탭 리스트 가져오기
# tabs = browser.window_handles
# # 2번째 탭 선택 - tabs[0] : 원본, tabs[1]: 새창
# browser.switch_to.window(tabs[1])
# # it/과학 선택 클릭
# browser.find_element(By.XPATH,"/html/body/section/header/div[2]/div/div/div/div/div/ul/li[6]/a/span").click()
# # 첫번째 뉴스 선택 클릭
# browser.find_element(By.CLASS_NAME,'sa_text_title').click()

