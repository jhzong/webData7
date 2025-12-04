import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
import time
import os
import csv

# 1.requests로 정보가져오기
url="https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,"lxml")
res.raise_for_status()

# ex)시가총액
# title
box_type=soup.find('div',{'class':'box_type_l'})
trs=box_type.find_all('tr')
ths=trs[0].find_all('th')

title=[th.text.strip() for th in ths]
print(title)


# # ex)증권 1위
# # 삼성전자
# tds=trs[2].find_all('td')
# rank=tds[0].text.strip()
# item=tds[1].text.strip()
# search=tds[2].text.strip()
# cur=tds[3].text.strip()
# updown=tds[4].find('span',{'class':'blind'}).text.strip()
# prev=tds[4].find('span',{'class':'tah'}).text.strip()
# fluc=tds[5].text.strip()
# vol=tds[6].text.strip()
# marketPrice=tds[7].text.strip()
# highEnd=tds[8].text.strip()
# lowEnd=tds[9].text.strip()
# per=tds[10].text.strip()
# roe=tds[11].text.strip()
# data=[rank,item,search,cur,updown+prev,fluc,vol,marketPrice,highEnd,lowEnd,per,roe]
# print(data)


# 전체차트
for tr in trs:
    tds=tr.find_all('td')
    rank=tds[0].text.strip()
    item=tds[1].text.strip()
    search=tds[2].text.strip()
    cur=tds[3].text.strip()
    updown=tds[4].find('span',{'class':'blind'}).text.strip()
    prev=tds[4].find('span',{'class':'tah'}).text.strip()
    fluc=tds[5].text.strip()
    vol=tds[6].text.strip()
    marketPrice=tds[7].text.strip()
    highEnd=tds[8].text.strip()
    lowEnd=tds[9].text.strip()
    per=tds[10].text.strip()
    roe=tds[11].text.strip()
    print(rank,item,search,cur,updown+prev,fluc,vol,marketPrice,highEnd,lowEnd,per,roe)

# 1) stock.csv(1~30)


