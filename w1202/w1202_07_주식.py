import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup= BeautifulSoup(res.text,"lxml")
trs=soup.find("div",{"class":"box_type_l"}).table.find_all("tr")

## 예제)네이버증권(증권홈 > 국내증시 > 검색상위 종목)에서 항목 찾아서 출력(1~3위)
## 표에서
# for th in trs[0].find_all("th"):
#     print(th.text.strip(),end='\t')

for tr in trs:
    for td in tr:
        print(td.text.strip(),end='\t')

