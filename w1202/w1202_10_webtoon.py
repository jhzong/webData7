import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/index"
# selenium 함수호출

# 파일 불러오기
with open("webtoon_browser.html","r",encoding="utf8") as f:
    soup= BeautifulSoup(f,"lxml")
    
# print(soup.find("span",{"class":"ComponentHead__text--dhKW7"}).text.strip())
# print(soup.find("div",{"class":"Aside__aside_wrap--iF5ju"}))
# asideDiv=soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# print(asideDiv.find("span",{"class":"ComponentHead__text--dhKW7"}).text.strip())
# print(soup.prettify())

# print(soup.find('div',{'class':'Aside__type_home_logout--R6qSd'}))
# asideDiv2=soup.find('div',{'class':'Aside__type_home_logout--R6qSd'})
# print(asideDiv2.find_all('h2',{'class':'ComponentHead__title--TjYVo'})[2].text.strip())

# print(asideDiv.find_all('div',{'class':'component_wrap'})[3])

# # ex1)print 공지사항 ----------------------------------------------------------------------------
# asideDiv3=asideDiv.find_all('div',{'class':'component_wrap'})[3]
# print(asideDiv3.find('h2',{'class':'ComponentHead__title--TjYVo'}).text.strip())

# # ex2)print 베스트도전 ----------------------------------------------------------------------------
# ul=soup.find('ul',{'id':'menu'})
# print(ul.find_all('li')[3].text.strip())



# lis=ul.find_all('li')
# print(lis)
# for li in lis:
#     print(lis[li].a.text.strip())





# ## ex3)실시간 인기웹툰 + 하위메뉴 ----------------------------------------------------------------------------
# aside=soup.find('div',{'class':'Aside__aside_wrap--iF5ju'})
# # 실시간 인기 웹툰-wraps[0]
# wraps=aside.find_all('div',{'class':'component_wrap'})
# # 5개의 인기웹툰 내용
# lis=wraps[0].find_all('li')
# # 1위 등수,제목,작가
# print(lis[0].find('strong',{'class':'AsideList__ranking--sNPZy'}).text.strip())
# print(lis[0].find('span',{'class':'text'}).text.strip())
# print(lis[0].find('a',{'class':'ContentAuthor__author--CTAAP'}).text.strip())


# print('[실시간 인기 웹툰 리스트]')
# for li in lis:
#     print(li.find('strong',{'class':'AsideList__ranking--sNPZy'}).text.strip())
#     print(li.find('span',{'class':'text'}).text.strip())
#     print(li.find('a',{'class':'ContentAuthor__author--CTAAP'}).text.strip())
#     print('-'*50)

## ex4)실시간 신작랭킹 + 하위메뉴----------------------------------------------------------------------------
aside=soup.find('div',{'class':'Aside__aside_wrap--iF5ju'})
# 실시간 신작랭킹-wraps[1]
wraps=aside.find_all('div',{'class':'component_wrap'})
# 5개의 신작웹툰 내용
# print(wraps[1].find_all('li'))
lis=wraps[1].find_all('li')
# 1위 신인
# print(lis[0].find('strong',{'class':'AsideList__ranking--sNPZy'}).text.strip())
# print(lis[0].find('span',{'class':'text'}).text.strip())
# print(lis[0].find('a',{'class':'ContentAuthor__author--CTAAP'}).text.strip())
# 1~5위 리스트
for li in lis:
    print(li.find('strong',{'class':'AsideList__ranking--sNPZy'}).text.strip())
    print(li.find('span',{'class':'text'}).text.strip())
    print(li.find('a',{'class':'ContentAuthor__author--CTAAP'}).text.strip())
