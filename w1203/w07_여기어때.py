import requests # url정보
from bs4 import BeautifulSoup # html정보-lxml,html-parser
from selenium import webdriver
import time
import os

# # 1)selenium으로 정보가져오기
# browser=webdriver.Chrome()
# browser.get("https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&personal=2&checkIn=2025-12-26&checkOut=2025-12-28&typoCorrect=true&nonAffiliated=true&sortType=RECOMMEND&category=2")
# time.sleep(5)# 정보 불러오는 시간 딜레이
# soup=BeautifulSoup(browser.page_source,"lxml")
# print(soup.prettify())

# # (1).파일저장
# with open("yeogi1.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())
# print("[file saved]")

# (2).파일불러오기
with open("yeogi1.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")

# 참고구문
# 세인트존스 호텔
divs=soup.find('div',{'class':'css-1jiha5s'}).find_all('div',{'class':'gc-thumbnail-type-seller-card-wrapper css-1u8qly9'})

# print(img)
# print(hotel)
# print(starRating)
# print(rateCount)
# print(price)

# 이미지링크,제목,평점,평가수,금액
for div in divs:
    try:
        img=div.find('img')['src']
        hotel=div.find('h3').text.strip()
        starRating=float(div.find('span',{'class':'css-9ml4lz'}).text.strip())
        rateCount=int(div.find('span',{'class':'css-oj6onp'}).text.strip().split(" ")[0].strip().replace(",",""))
        price=int(div.find('span',{'class':'css-5r5920'}).text.strip().replace(",",""))
        hotelData=[img,hotel,starRating,rateCount,price]
        print(img,hotel,starRating,rateCount,price)
    except:print('[오류]')
# 평점 9.0이상 and 평가수 3000이상 and 금액 200000원 미만