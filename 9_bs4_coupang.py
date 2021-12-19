### bs4_coupang: 목차 ###
# 1. 예제: 쿠팡 쇼핑 목록 가져오기 (한 페이지)


### 1. 예제: 쿠팡 쇼핑 목록 가져오기

# 1) 기본설정: url변수, headers변수, requests.get(), raise_for_status(), BeautifulSoup()
import requests
import re
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# # 2) 노트북 정보 목록 하나 가져오기
# # (위치) li element, i) class:search-product > a > dl > dd > div > div element, class:name
# #                   ii) class search-product__ad-badge
#
# items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())


# 3) 노트북 정보 가져오기: find_all > for문 + find
# (목록) li element, i) class:search-product > a > dl > dd > div > div element, class:name
#                   ii) class search-product__ad-badge
# (가격) strong element, class: price-value
# (별점) em element, class: rating                  // 평점이 없는 항목 존재하여 예외처리 필요
# (리뷰수) span element, class: rating-total-count  // 리뷰수 없는 항목 존재하여 예외처리 필요
# (링크) a element, class: serch-product-link       // a elemnet의 href값

# (광고제품 - 제외) span element, class: ad-badge-text
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

    link = item.find("a", attrs={"class":"search-product-link"})["href"]

    print(name, price, rate, review, link)



