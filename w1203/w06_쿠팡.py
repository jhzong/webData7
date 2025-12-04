import requests  # url정보
from bs4 import BeautifulSoup # html정보 - lxml,html-parser
from selenium import webdriver
import time
import os
import csv
import undetected_chromedriver as uc
# 1. requests 정보가져오기
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
#     "Accept-Language": "ko-KR,ko;q=0.9",
#     "Referer": "https://www.coupang.com/",
# }
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
# # 2. selenium 정보가져오기
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=mipmz9on&channel=user&page=1"
# browser = uc.Chrome(options=options)
# browser.get(url)
# time.sleep(5)
# soup = BeautifulSoup(browser.page_source,"lxml")
# # 파일저장
# with open("coupang1.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
# 파일불러오기
with open("coupang1.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")

# 참고문구--------------------------------------------------------------------------------------------------    
ul=soup.find('ul',{"id":"product-list"})
lis=ul.find_all('li')

# img=lis[0].find('img')['src']
# print(img)
# name=lis[0].find('div',{'class':'ProductUnit_productNameV2__cV9cw'}).text.strip()
# print(name)
# price=lis[0].find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700'}).text.strip()[:-1].replace(',','')
# print(price)
# starRating=lis[0].find('div',{'class':'ProductRating_star__RGSlV'}).text.strip()
# print(starRating)
# comCount=lis[0].find('span',{'class':'ProductRating_ratingCount__R0Vhz'}).text.strip()
# print(comCount[1:-1])

# num=1
# for li in lis:
#     img=li.find('img')['src']
#     name=li.find('div',{'class':'ProductUnit_productNameV2__cV9cw'}).text.strip()
#     price1=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700'})# .text.strip()[:-1].replace(',','')
#     price2=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-900'})# .text.strip()[:-1].replace(',','')
#     price3=li.find('strong',{'class':'Price_priceValue__A4KOr'})# .text.strip()[:-1].replace(',','')
#     price4=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-400'})# .text.strip()[:-1].replace(',','')
#     if price1:#none인지 확인
#         price=int(price1.text.strip()[:-1].replace(',',''))
#     elif price2:
#         price=int(price2.text.strip()[:-1].replace(',',''))
#     elif price3:
#         price=int(price3.text.strip()[:-1].replace(',',''))
#     else:
#         price=int(price4.text.strip()[:-1].replace(',',''))
    
#     starRating=li.find('div',{'class':'ProductRating_star__RGSlV'}).text.strip()
#     comCount=li.find('span',{'class':'ProductRating_ratingCount__R0Vhz'}).text.strip()[1:-1]
#     print(f'<{num}>')
#     print(img)
#     print(name)
#     print(price)
#     print(starRating)
#     print(comCount)
#     num+=1

# //참조--------------------------------------------------------------------------------------------------
    
# # ex1)가격 1100000이하
# count=1
# for li in lis:
#     try:
#         img=li.find('img')['src']
#         name=li.find('div',{'class':'ProductUnit_productNameV2__cV9cw'}).text.strip()
#         price=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700'}).text.strip()[:-1].replace(',','')
#         starRating=li.find('div',{'class':'ProductRating_star__RGSlV'}).text.strip()
#         comCount=li.find('span',{'class':'ProductRating_ratingCount__R0Vhz'}).text.strip()[1:-1]
#         if int(price)<=1100000:
#             print(f'{count}번 상품')
#             print(name)
#             print(price)
#     except: pass # print('[[error...skipping]]')
#     count+=1

# # ex2)평점 4.5 이상 검색
# count=1
# for li in lis:
#     try:
#         img=li.find('img')['src']
#         name=li.find('div',{'class':'ProductUnit_productNameV2__cV9cw'}).text.strip()
#         price=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700'}).text.strip()[:-1].replace(',','')
#         starRating=li.find('div',{'class':'ProductRating_star__RGSlV'}).text.strip()
#         comCount=li.find('span',{'class':'ProductRating_ratingCount__R0Vhz'}).text.strip()[1:-1]
#         if float(starRating)>=4.5:
#             print(f'{count}번 상품')
#             print(name)
#             print(f'{price}원')
#             print(f'{starRating}')
#     except: pass # print('[[error...skipping]]')
#     count+=1

# # ex3)후기 500 이상
# count=1
# for li in lis:
#     try:
#         img=li.find('img')['src']
#         name=li.find('div',{'class':'ProductUnit_productNameV2__cV9cw'}).text.strip()
#         price=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700'}).text.strip()[:-1].replace(',','')
#         starRating=li.find('div',{'class':'ProductRating_star__RGSlV'}).text.strip()
#         comCount=li.find('span',{'class':'ProductRating_ratingCount__R0Vhz'}).text.strip()[1:-1]
#         if int(comCount)>=500:
#             print(f'{count}번 상품')
#             print(name)
#             print(f'{price}원')
#             print(f'댓글개수 : {comCount}')
#     except: pass # print('[[error...skipping]]')
#     count+=1

# ex4)가격 1100000이하 and 평점 4.5 이상 and 후기 500 이상
num=1
for li in lis:
    img=li.find('img')['src']
    name=li.find('div',{'class':'ProductUnit_productNameV2__cV9cw'}).text.strip()
    price1=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-red-700'})# .text.strip()[:-1].replace(',','')
    price2=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-900'})# .text.strip()[:-1].replace(',','')
    price3=li.find('strong',{'class':'Price_priceValue__A4KOr'})# .text.strip()[:-1].replace(',','')
    price4=li.find('div',{'class':'custom-oos fw-text-[20px]/[24px] fw-font-bold fw-mr-[4px] fw-text-bluegray-400'})# .text.strip()[:-1].replace(',','')
    if price1:#none인지 확인
        price=int(price1.text.strip()[:-1].replace(',',''))
    elif price2:
        price=int(price2.text.strip()[:-1].replace(',',''))
    elif price3:
        price=int(price3.text.strip()[:-1].replace(',',''))
    else:
        price=int(price4.text.strip()[:-1].replace(',',''))
    starRating=float(li.find('div',{'class':'ProductRating_star__RGSlV'}).text.strip())
    comCount=int(li.find('span',{'class':'ProductRating_ratingCount__R0Vhz'}).text.strip()[1:-1])
    if price<=1100000 and starRating>=4.5 and comCount>=500:
        print(f'<{num}>')
        print(img)
        print(name)
        print(price)
        print(starRating)
        print(comCount)
    num+=1
