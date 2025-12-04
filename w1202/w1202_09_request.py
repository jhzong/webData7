# 동기식:순서대로 실행
import requests
from bs4 import BeautifulSoup

url="https://www.naver.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup= BeautifulSoup(res.text,"lxml")
print(soup.prettify())

with open ('naver_req.html','w',encoding='utf8') as f:
    f.write(soup.prettify())