### bs4: 목차 ###
# 1. 예제: 네이버웹툰 가져오기


### 1. 예제: 네이버웹툰 가져오기

# 1) 기본설정: url변수, headers변수, requests.get(), raise_for_status(), BeautifulSoup()
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


# 2) bs4 객체를 정보 받아오기
print(soup.title)               # title 출력
print(soup.title.get_text())      # title 중 글자만 출력
print(soup.a)                   # 처음 발견한 a 엘리먼트 출력
print(soup.a.attrs)             # a element 모든 속성 보기
print(soup.a["href"])           # a element href 속성 가져오기


# # 2) bs4 객체를 정보 받아오기: find 메소드 사용 (웹툰올리기 버튼 찾기)
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))  # element 포함
# print(soup.find(attrs={"class":"Nbtn_upload"}))       # element 미포함


# # 3) bs4 객체를 정보 받아오기: find 메소드 사용 (인기급상승 -> 랭크1 만화)
# rank1 = soup.find("li", attrs={"class":"rank01"})  # li element의 class 속성
# print(rank1.a)                                     # li > a element의 class 속성 출력
# print(rank1.a.get_text())                          # li > a element의 텍스트 출력


# 4) bs4 객체를 정보 받아오기: 형제/부모 항목 추출 (인기급상승 -> 랭크2~10 만화)

# # (1) 형제1(다음/이전): next_sibling / previous_sibling
# rank1 = soup.find("li", attrs={"class":"rank01"})
# rank2 = rank1.next_sibling.next_sibling              # 개행이 섞여 있어 next_sibling 두번 사용
# print(rank2.get_text())

# # (2) 형제2(다음/이전): find_next_sibling(element) / find_previous_sibling(element) > BEST SOLUTION
# rank1 = soup.find("li", attrs={"class":"rank01"})
# rank2 = rank1.find_next_sibling("li")
# rank3 = rank2.find_next_sibling("li")
#
# print(rank2.get_text())
# print(rank3.get_text())

# # (3) 형제들(모두): find_next_siblings(element) > 모든 형제 element 가져오기
# rank1 = soup.find("li", attrs={"class":"rank01"})
# ranks = rank1.find_next_siblings("li")
# print(ranks)

# # (4) 부모(위/아래): parent
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.parent)


