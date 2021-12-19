### bs4_gauss: 목차 ###
# 1. 예제: 회차 제목 가져오기(가우스전자)


### 1. 예제: 회차 제목 가져오기(가우스전자)

# 1) 기본설정: url변수, headers변수, requests.get(), raise_for_status(), BeautifulSoup()
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list?titleId=675554"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# # 2) 회차제목/링크 가져오기
# # (회차제목) td element, class: title > a element, 텍스트 값
# # (회차링크) td element, class: tilte > a element, href 속성
# cartoons = soup.find_all("td", attrs={"class":"title"})
#
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     # link = cartoon.a["href"]                            # /webtoon/detail?titleId=675554&no=902&weekday=mon
#     link = "https://comic.naver.com" + cartoon.a["href"]  # https://comic.naver.com/webtoon/detail?titleId=675554&no=902&weekday=mon
#     print(title, link)


# # 3) 평균평점(1페이지) 가져오기
# # (정보) div element, class:rating_type > strong element, 숫자값
# total_scores = 0
# cartoons = soup.find_all("div", attrs={"class":"rating_type"})
# for cartoon in cartoons:
#     rate = cartoon.find("strong").get_text()   # find메소드: div > strong element 검색
#     total_scores = total_scores + float(rate)  # float 혀앹로 반환
# print(total_scores / len(cartoons))            # 9.972999: 1페이지 10개 회차의 평균평점








