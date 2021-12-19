### bs4_webtoons: 목차 ###
# 1. 예제: 웹툰 전체 리스트 가져오기


### 1. 예제: 웹툰 전체 리스트 가져오기

# 1) 기본설정: url변수, headers변수, requests.get(), raise_for_status(), BeautifulSoup()
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# # 2) 웹툰 전체 리스트 가져오기: find_all 메소드 사용 > 조건에 맞는 값 리스트로 반환
# cartoons = soup.find_all("a", attrs={"class":"title"})  # find_all: 모두 찾기 // cf) find: 첫번째거 찾기
# for cartoon in cartoons:
#     print(cartoon)
#     print(cartoon.get_text())  # a elemnet > class: title






