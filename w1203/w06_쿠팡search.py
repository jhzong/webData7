import requests # url정보
from bs4 import BeautifulSoup # html정보-lxml,html-parser
from selenium import webdriver
import time
import os
import undetected_chromedriver as uc


# REQUEST
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
   "Accept-Language": "ko-KR,ko;q=0.9",
   "Referer": "https://www.coupang.com/",
}
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36")

# SELENIUM
url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=mipmzjse&channel=user&page=1"
browser=uc.Chrome(options=options)
browser.get(url)
time.sleep(5)
soup=BeautifulSoup(browser.page_source,"lxml")
input('enter')

print(soup.prettify())

# 파일저장
with open("coupang1.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
print('saved')