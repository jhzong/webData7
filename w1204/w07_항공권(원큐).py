from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import os
import random

url="https://flight.naver.com/"
browser=webdriver.Chrome()# 새창열기
browser.maximize_window()# 창화면 확대
browser.get(url)
time.sleep(1)

# 광고팝업 닫기
browser.find_element(By.XPATH,'//*[@id="layer"]/button[2]').click()

# 1-1.김포
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()
time.sleep(1)
# 1-2.제주
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button').click()
time.sleep(1)

# 2-1.달력열기
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
# 2-2.가는날
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[4]/td[3]/button').click()
time.sleep(1)
# 2-3.오는날
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[4]/td[7]/button').click()
time.sleep(1)
# 3.검색 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)

input('hold')