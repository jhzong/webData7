# 비동기식:동시에 실행
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 크롬 드라이버를 활용해 크롬 브라우저를 제어할 수 있다.
browser = webdriver.Chrome()
# 크롬 브라우저 열림
browser.get("https://comic.naver.com/index")

time.sleep(8) # 8초 대기후 실행
soup=BeautifulSoup(browser.page_source,"lxml")
print(soup.prettify())

with open ('webtoon_browser.html','w',encoding='utf8') as f:
    f.write(soup.prettify())

# url="https://www.daum.net/"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res=requests.get(url,headers=headers)
# res.raise_for_status()
# soup= BeautifulSoup(res.text,"lxml")

# print(res.text)
