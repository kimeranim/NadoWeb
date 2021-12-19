### 목차: requests ###
# 1. WebScraping 가능여부 확인
# 2. WebScraping > html 파일로 만들기


import requests
res = requests.get("http://google.com")


### 1. WebScraping 가능여부 확인: status_code

# 1) status_code
print("응답코드", res.status_code)        # 200이면 정상


# 2) (방법1) status_code + if문 >
# if res.status_code == requests.codes.ok:  # status_code == 200
#     print("정상입니다")
# else:
#     print("Error Code 발생 >>>", res.status_code)


# 3) (방법2) raise_for_status() > Best Solution
# (설명) 에러가 있으면 실행되지 않고 중지
res.raise_for_status()


### 2. WebScraping > html 파일로 만들기
with open("mygoogle.html", 'w', encoding="utf8") as f:
    f.write(res.text)