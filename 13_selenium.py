### selenium: 목차 ###
# 1. 기본설정
# 2. 네이버 접속
# 3. 네이버 로그인 버튼 클릭 및 앞뒤 페이지 이동
# 4. 네이버 검색창 클릭 및 입력: send_keys()
# 5. 브라우저 닫기
# 6. 예제: 네이버 로그인



# 1. 기본설정: selenium, webdriver, common.keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 키 입력 위해 필요
browser = webdriver.Chrome()                     # = Chrome(./chromedriver.exe)


# # 2. 네이버 접속
# browser.get("http://naver.com")
#
#
# # 3. 네이버 로그인 버튼 클릭 / 앞뒤 이동: click()
# # (로그인 버튼) a element, class:link-login
# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# # browser.back()    # 이전 페이지
# # browser.forward   # 다음 페이지
#
#
# # 4. 네이버 검색창 클릭 및 입력: send_keys()
# # (검색창) input elemnet, id:query
# elem = browser.find_element_by_id("query")
# elem.send_keys("키메라님")  # 입력값 전송
# elem.send_keys(Keys.ENTER)  # 입력값 > 엔터
#
#
# # 5. 브라우저 닫기
# browser.close()  # 하나의 탭만 닫기
# browser.quit()   # 모든 탭 닫기
#

# 6. 예제: 네이버 로그인

# 1) 네이버 이동
browser.get("http://naver.com")

# 2) 로그인 버튼 클릭
# (로그인 버튼) a element, class:link-login
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3) ID / PW 입력
# (ID 버튼) input element, id:id
# (PW 버튼) input element, id:pw
browser.find_element_by_id("id").send_keys("kimeranim")
browser.find_element_by_id("pw").send_keys("pp11")
browser.find_element_by_id("pw").clear()                 # 입력되어 있는 칸을 삭제하고 재입력
browser.find_element_by_id("pw").send_keys("pp222222")

# 4) 로그인 버튼 클릭
# (로그인 버튼) button element, id:log.login
browser.find_element_by_id("log.login").click()


