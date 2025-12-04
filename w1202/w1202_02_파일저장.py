import requests
from bs4 import BeautifulSoup

url="http://www.google.com"
res=requests.get(url)
res.raise_for_status()


## 1.파일저장방법 w:write,r:read,a:append(추가)
# f=open("aaa.html","w",encoding="utf8")
# f.write(res.text)
# f.close()

## 2.파일저장방법(이쁘게)
## soup.prettify():문서가 정리되어 출력
soup=BeautifulSoup(res.text,"lxml")
with open ('aaa2.html','w',encoding='utf8') as f:
    f.write(soup.prettify()) # html태그 정리해서 출력

print('파일저장')