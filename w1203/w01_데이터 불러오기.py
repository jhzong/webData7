import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
import csv

# # 1.requests로 정보가져오기
# url="http://www.naver.com"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
# res=requests.get(url,headers=headers)
# soup=BeautifulSoup(res.text,"lxml")
# res.raise_for_status()
# print(soup.prettify())

# 2.selenium으로 정보가져오기
browser=webdriver.Chrome()
browser.get("http://www.naver.com")
time.sleep(5)# 버퍼링 딜레이(C=정보량/시간)
soup=BeautifulSoup(browser.page_source,"lxml")
print(soup.prettify())

# 2-1).파일저장
with open("test.html","w",encoding="utf8")as f:
    f.write(soup.prettify())
print("[file saved]")
# 2-2).파일불러오기
with open("test.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")