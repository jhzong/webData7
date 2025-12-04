## step1)
# requests 라이브러리 설치 : pip install requests
# beautifulsoup4 라이브러리 설치 : pip install beautifulsoup4
# lxml 라이브러리 설치 : pip install lxml

## step2)
import requests

# requests: url링크에 가서 html소스를 text형태로 가져옴.
# res=requests.get("http://www.naver.com")

# url="http://www.naver.com"
url="http://www.google.com"

res=requests.get(url)
# status_code : 실행코드 출력
# (2XX: Success(성공),4XX: Client Error(클라이언트 에러),5XX: Server Error(서버 에러))
res.raise_for_status() # error시 프로그램 종료
print('응답코드 :',res.status_code) # 200:성공,400/500:실패
print(requests.codes.ok)
# print(res.status_code)# 성공:200,실패:400/500
# print(requests.codes.ok)#ok,not_found,notmodified



print(res.text)
