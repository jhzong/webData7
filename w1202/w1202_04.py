import requests

url="https://www.melon.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

res=requests.get(url,headers=headers)
res.raise_for_status()

with open("agent3.html","w",encoding="utf8") as f:
    f.write(res.text)

print('[saved]')