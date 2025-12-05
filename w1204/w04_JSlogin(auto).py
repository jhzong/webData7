from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os
import random

url="https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
browser=webdriver.Chrome()
browser.get(url)

# JavaScript로 자동로그인
input_js='''
document.getElementById("id").value="{id}";
document.getElementById("pw").value="{pw}";
'''.format(id='*********',pw='*********')# 아이디/비번 입력하는 script

time.sleep(3)
# time.sleep(random.uniform(1,5))# 1,5사이 랜덤

# 네이버에서 elem요소로 찾아, 입력시 차단
# JS를 이용해 데이터 입력
browser.execute_script(input_js)# script실행
time.sleep(3)
browser.find_element(By.ID,"log.login").click()#로그인버튼 클릭
# -----------------------------------------------------------------------------
input('hold')

# 메일 클릭
time.sleep(3)
browser.find_element(By.CLASS_NAME,"MyView-module__menu_item___zAxPt").click()

input('hold2')
# 메일쓰기(좋은 하루 되세요.)