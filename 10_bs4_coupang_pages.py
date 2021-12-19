### bs4_coupang_pages: 목차 ###
# 1. 예제: 쿠팡 쇼핑 목록 가져오기 (여러 페이지)


### 1. 예제: 쿠팡 쇼핑 목록 가져오기: 1 ~ 5페이지

# 1) 기본설정: url변수, headers변수, requests.get(), raise_for_status(), BeautifulSoup()
import requests
import re
from bs4 import BeautifulSoup
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}

# 2) 1 ~5페이지 반복 크롤링: url 페이지 정보 변경
for i in range(1, 6):
    print("페이지:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})  # 광고 제외
        if ad_badge:
            print("------<광고상품제외>------")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()  # 목록
        price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격정보


        rate = item.find("em", attrs={"class":"rating"})   # 평점이 없는 항목 존재하여 예외처리 필요
        if rate:
            rate = rate.get_text()
        else:
            "평점없음"

        review = item.find("span", attrs={"class":"rating-total-count"})  # 리뷰수가 없는 항목 존재하여 예외처리 필요
        if review:
            review = review.get_text()
        else:
            "리뷰없음"

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        print("제품명: {}".format(name))
        print("가격: {}".format(price))
        print("별점: {}".format(rate))
        print("리뷰수: {}".format(review))
        print("링크: {}".format("https://www.coupang.com" + link))
        print("-"*100)