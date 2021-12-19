### bs4_daum.movies: 목차 ###
# 1. 예제: 다음 영화 인기 영화(역대 관객순위) 목록 가져오기


# 1. 예제: 다음 영화 인기 영화(역대 관객순위) 목록 가져오기

# 1) 기본설정: url변수, headers변수, requests.get(), raise_for_status(), BeautifulSoup()
import requests
from bs4 import BeautifulSoup

for year in range(2016, 2021):  # 상위 5개년도
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
                                                # {}: .format(year)
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

# 2) 영화 이미지 파일 크롤링 / 저장
# (이미지 크롤링) img element, class: thumb_img, src 값
    images = soup.find_all("img", {"class":("thumb_img")})

# (1) 이미지 파일 크롤링 및 링크 완성
    for idx, image in enumerate(images):     # enumerate: 인덱스/전달값 반환
        image_url = image["src"]

        if image_url.startswith("//"):       # startswith: 시작문자 검색
            image_url = "https" + image_url

    # (2) 이미지 저장 - 년도별 5위까지 추출
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open("movie{}_{}.jpg".format(year, idx+1), "wb") as f:  # Wb: 사진 파일
            f.write(image_res.content)                      # content: 사진 파일

        if idx >= 4:  # 상위 5개 이미지 저장
            break