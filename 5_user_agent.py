### user_agent ###
# 1. (정의) 사용자를 대신하여 일을 수행하는 소프트웨어의 식별 정보
#           사용자 에이전트가 뭔지 표시하는 문자열이고, 영어로 정확히 표현하면 User-Agent string in HTTP
# 2. (확인) https://www.whatismybrowser.com/detect/what-is-my-user-agent 접속


import requests
url = "https://nadocoding.tistory.com/"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html", 'w', encoding="utf8") as f:
    f.write(res.text)