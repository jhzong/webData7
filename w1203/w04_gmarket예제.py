import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
import time
import os
import csv

# browser=webdriver.Chrome()
# browser.get("https://www.gmarket.co.kr/n/best?spm=gmktpc.home.0.0.d9c5486a2uTZ2i")
# time.sleep(5)# 정보 불러오는 시간 딜레이
# soup=BeautifulSoup(browser.page_source,"lxml")


# # 2-1).파일저장
# with open("gmarket1.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())
# 2-2).파일불러오기
with open("gmarket1.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")
#--------------------------------------------------------
div=soup.find('div',{'id':'container'})
ul=div.find('ul',{'class':'list__best'})
lis=ul.find_all('li')
#--------------------------------------------------------
# # prob1).gmarket-best 1위 신라면 이미지,상품,가격(http://)
# print("http:"+lis[0].find('img')['src'])
# print(lis[0].find('p',{'class':'box__item-title'}).text.strip())
# print(lis[0].find('span',{'class':'for-a11y'}).text.strip(),end='')
# print(lis[0].find('span',{'class':'text text__value'}).text.strip().replace(',',''),end='')
# print(lis[0].find('span',{'class':'text text__unit'}).text.strip())

# # prob2).top10 상품 출력
# for i in range(10):
#     print("http:"+lis[i+1].find('img')['src'])
#     print(lis[i+1].find('p',{'class':'box__item-title'}).text.strip())
#     print(lis[i+1].find('span',{'class':'for-a11y'}).text.strip(),end='')
#     print(lis[i+1].find('span',{'class':'text text__value'}).text.strip().replace(',',''),end='')
#     print(lis[i+1].find('span',{'class':'text text__unit'}).text.strip())
#     print('-'*50)

# # prob3).top10 최고가(17950원)
# max_price=0
# for i in range(10):
#     print("http:"+lis[i+1].find('img')['src'])
#     print(lis[i+1].find('p',{'class':'box__item-title'}).text.strip())
#     print(lis[i+1].find('span',{'class':'for-a11y'}).text.strip(),end='')
#     print(lis[i+1].find('span',{'class':'text text__value'}).text.strip().replace(',',''),end='')
#     price=int(lis[i+1].find('span',{'class':'text text__value'}).text.strip().replace(',',''))
#     print(lis[i+1].find('span',{'class':'text text__unit'}).text.strip())
#     print('-'*50)
#     if max_price<price:
#         max_price=price
# print("최고가 :",max_price)


# # prob4)전체 최고가(스크립트 에러시 스킵)
# max_price=0
# for i,li in enumerate(lis):
#     print(f"<{i+1}>")
#     try:
#         print("http:"+li.find('img')['src'])
#         print(li.find('p',{'class':'box__item-title'}).text.strip())
#         print(li.find('span',{'class':'for-a11y'}).text.strip(),end='')
#         print(li.find('span',{'class':'text text__value'}).text.strip().replace(',',''),end='')
#         price=int(li.find('span',{'class':'text text__value'}).text.strip().replace(',',''))
#         print(li.find('span',{'class':'text text__unit'}).text.strip())
#         print('-'*50)
#         if max_price<price:
#             max_price=price
#     except:print('[[error...skipping]]')
# print("최고가 :",max_price)

# prob5) top10 정보저장
fileName="gmarket_top10.csv"
title=['썸네일','상품명','가격']

# csv 파일 저장
f= open(fileName,"w",encoding="utf-8-sig",newline="")
writer=csv.writer(f)

# writerow는 리스트 타입으로 저장해야함.
writer.writerow(title)
for i in range(10):
    thumbnail="http:"+lis[i+1].find('img')['src']
    item=lis[i+1].find('p',{'class':'box__item-title'}).text.strip()
    price=int(lis[i+1].find('span',{'class':'text text__value'}).text.strip().replace(',',''))
    data=[thumbnail,item,price]
    writer.writerow(data)

f.close()
print('파일저장')

# prob6) 전체 베스트 정보저장['순위','썸네일','상품명','가격']




