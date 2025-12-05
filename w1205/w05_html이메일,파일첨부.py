import time
import os
import random
import csv
# 웹스크랩핑
import requests
from bs4 import BeautifulSoup
# 셀레니움
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 이메일발송 라이브러리
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
# 날짜함수
from datetime import datetime

### 임시비밀번호 함수
def random_pw():
    arr=[i for i in range(10)]
    # arr2=random.sample(arr,8)
    # print(arr)
    ranNum="".join(map(str,random.sample(arr,8)))
    print(ranNum)
    return ranNum


# html소스
content='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>임시비번 안내</title>
    <style>
        *{margin: 0; padding: 0;}
        table{width: 760px; margin: 0 auto;}
        td{height: 45px;}
        #txt{text-align: center; font-size: 20px; color: rgb(91, 91, 91);
        font-weight: 600;}
        #top{height: 105px; width: 100%;}
        #bottom{height: 200px; background: #eee;}
    </style>
</head>
<body>
    <table>
        <colgroup>
            <col width="182px">
            <col width="*">
            <col width="135px">
        </colgroup>
        <tr id="top">
            <td><img src="https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_01.png"></td>
            <td></td>
            <td><img src="https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_02.png"></td>
        </tr>
        <tr id="bottom">
            <td id="txt" colspan="3">임시비밀번호:
            '''
content2=f'''{random_pw()}</td>
        </tr>
    </table>
</body>
</html>
'''
all_con=content+content2
print(all_con)

# 멀티미디어_메일내용
msg=MIMEMultipart()#
html_part=MIMEText(all_con,"html","utf-8")#
msg.attach(html_part)#
msg['From']='jhzong@naver.com'# 보내는메일
msg['To']='jhzong@naver.com'# 받는주소
msg['Subject']='(html멀티)임시비밀번호를 발송합니다.'

# # 파일첨부(option1)
# file_part=MIMEBase('application','octet-stream')
# # 파일읽어오기
# with open('flightData.csv','rb') as f:
#     file_part.set_payload(f.read())
# encoders.encode_base64(file_part) # 파일을 첨부가능하게 인코딩
# file_part.add_header('Content_Disposition','attachment',filename='flightData.csv')
# msg.attach(file_part)

# 파일첨부(option2)
with open('flightData.csv','rb') as f:
    attachment=MIMEApplication(f.read())
attachment.add_header('Content_Disposition','attachment',filename='flightData.csv')
msg.attach(attachment)

# 메일서버정보
s=smtplib.SMTP('smtp.naver.com',587)#
# 메일서버접근
s.starttls()
# 서버로그인
s.login('jhzong@naver.com','WXEPSFSR82KX')
# 서버발송
# 보내는주소,받는주소,내용
s.sendmail('jhzong@naver.com','jhzong@naver.com',msg.as_string())
print(msg.as_string())
# 메일서버 닫기
s.close()

print('이메일 발송')