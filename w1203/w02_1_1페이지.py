import requests # url정보
from bs4 import BeautifulSoup # html정보-lxml,html-parser
from selenium import webdriver
import time
import os

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

# # SELENIUM
# browser=webdriver.Chrome() #chromedriver.exe 필수
# browser.get("https://comic.naver.com/webtoon/list?titleId=811721&page=1&sort=DESC")
# time.sleep(5)# 불러오는 시간
# soup=BeautifulSoup(browser.page_source,"lxml")
# print(soup.prettify())

# # REQUEST
# url="https://comic.naver.com/webtoon/list?titleId=811721&page=1&sort=DESC"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res=requests.get(url,headers=headers)
# soup=BeautifulSoup(res.text,"lxml")
# res.raise_for_status()
# print(soup.prettify())

# # 파일저장
# with open("webtoon2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print('saved')

# 파일불러오기
with open("naver_webtoon2.html","r",encoding="utf8") as f:
    soup=BeautifulSoup(f,"lxml")

# ex1)웹툰 리스트 제목,별점,날짜 + 평균별점
ul=soup.find("ul",{"class":"EpisodeListList__episode_list--_N3ks"})
lis=ul.find_all("li")
rating=0

for i,li in enumerate(lis):
    print(li.find('img')['src'])
    # 파일저장----------------------------------
    img_url=requests.get(li.find('img')['src'],headers=headers)# image파일을 불러오기

    os.makedirs("naver_webtoon",exist_ok=True)# 폴더 생성(확인해 없으면 생성후 저장)
    
    with open(f"naver_webtoon/webtoon_{i+1}.jpg","wb") as f:
        f.write(img_url.content)# content:파일내용을 모두 가져오기
        
    # //파일저장--------------------------------
    print(li.find('span',{'class':'EpisodeListList__title--lfIzU'}).text.strip())
    rating+=float(li.find('span',{'class':'text'}).text.strip())
    print(li.find('span',{'class':'text'}).text.strip())
    print(li.find('span',{'class':'date'}).text.strip())
    print('-'*50)

print("20개(페이지) 평균평점 :",f"{rating/len(lis):.2f}")    # 페이지평균평점 출력

# ex2)평균 별점
# print(len(lis))
# print(li.find('span',{'class':'text'}).text.strip())


