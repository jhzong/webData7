import requests
from bs4 import BeautifulSoup
import os
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# url="https://search.daum.net/search?w=tot&m=&q=%EC%98%81%ED%99%94%20%EC%98%88%EB%A7%A4%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=NSJ"
# res=requests.get(url,headers=headers)

# 파일 불러오기
with open("daum_movie.html","r",encoding="utf8") as f:
    soup= BeautifulSoup(f,"lxml")

print(soup.prettify())

# 셀레니움으로 파일 저장
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time

# # 크롬 드라이버를 활용해 크롬 브라우저를 제어할 수 있다.
# browser = webdriver.Chrome()
# # 크롬 브라우저 열림
# browser.get("https://search.daum.net/search?w=tot&m=&q=%EC%98%81%ED%99%94%20%EC%98%88%EB%A7%A4%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=NSJ")

# time.sleep(8) # 8초 대기후 실행
# soup=BeautifulSoup(browser.page_source,"lxml")
# print(soup.prettify())

# with open ('daum_movie.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())



# ## 파일저장
# with open ("daum_movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print('saved')




# ## 실시간 예매율,일일 관객수
# section=soup.find('div',{'id':'morColl'}).find('div',{'class':'c-section-subtab'})
# atxts=section.find_all('a')
# for a in atxts:
#     print(a.contents[0]) #text->contents
    
    