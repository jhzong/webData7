import requests
from bs4 import BeautifulSoup
import os
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

url="https://comic.naver.com/index"
# selenium 함수호출

# 파일 불러오기
with open("webtoon_browser.html","r",encoding="utf8") as f:
    soup= BeautifulSoup(f,"lxml")

# # 실시간 신작
# aside=soup.find('div',{'class':'Aside__aside_wrap--iF5ju'})
# wraps=aside.find_all('div',{'class':'component_wrap'})
# lis=wraps[1].find_all('li')
# for i,li in enumerate(lis):
#     print(li.find('img')['src'])
#     # request url 정보를 가져옴. jpg->jpg정보를 가져옴.
#     img_req=requests.get(li.find('img')['src'],headers=headers)
#     os.makedirs('webtoon',exist_ok=True)# 폴더가 없으면 생성함
#     # if not 'webtoon'.exist():
#     #     os.makedirs('webtoon')# 폴더가 있는지 확인 후 파일 저장
    
#     with open(f'webtoon/webtoon_{i+1}.jpg','wb') as f:
#         f.write(img_req.content)# 파일로 저장
#     print(li.find('strong',{'class':'AsideList__ranking--sNPZy'}).text.strip())
#     print(li.find('span',{'class':'text'}).text.strip())
#     print(li.find('a',{'class':'ContentAuthor__author--CTAAP'}).text.strip())

# # prac1)공지사항+하위항목
# print()
# aside=soup.find('div',{'class':'Aside__aside_wrap--iF5ju'})
# wraps=aside.find_all('div',{'class':'component_wrap'})
# lis=wraps[3].find_all('li')

# print(wraps[3].find('h2').text.strip(),end='\t')
# print(wraps[3].find('a').text.strip())
# for li in lis:
#     print(li.text.strip())

# prac2)가장 핫한 스릴러 웹툰만 모아봤어요!
# content=soup.find('div',{'id':'content'})
# headTitle=content.find('div',{'class':'ComponentHead__title_area--IEQEG'})
# print(headTitle.find('h2').find_all('span')[0].text.strip(),end=' ')
# print(headTitle.find('strong').text.strip(),end=' ')
# print(headTitle.find('h2').find_all('span')[0].text.strip(),end='')

ol=soup.find('ol',{'class':'FlickingList__content_list--vG5lo'})
print(ol.find_all('li')[0])
