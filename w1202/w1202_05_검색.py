import requests
from bs4 import BeautifulSoup

url="http://www.naver.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

### html 태그,css문법으로 검색가능
# # find():1개,find_all():여러개
# # 태그 입력시 검색됨(.text:tag글자 .attrs:tag속성)
# print(soup.find('title'))
# print(soup.title.text)
# print(soup.a.attrs)
# print(soup.a['href'])

# print(soup.find('div')) # 첫번째 div
# print(soup.find_all('div')[0]) # 전체 중 [0]번째
# print(len(soup.find_all('div'))) # 검색 개수

# print(soup.find_all('div')[1].find('div').attrs) # div tag 여러개 가져오기

# print(soup.find('div',{'id':'header'}))
# idHeader=soup.find('div',{'id':'header'})
# print(idHeader.find('h1',{'class':'search_logo'}))

# print(soup.find('legend',{'class':'blind'}))
print(soup.find('legend',class_='blind')) # class검색 최신
print(soup.find('div',id='header')) # id검색 최신

# 파일저장
# with open("naver1.html","w",encoding="utf8") as f:
#     f.write(res.text)

# with open("naver2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
# print('saved complete')