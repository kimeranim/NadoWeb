### 목차: regular_expressions ###
### 1. 정규 표현식의 기초, 메타 문자
### 2. 파이썬에서 정규 표현식을 지원하는 re모듈
### 3. 정규식을 이용한 문자열 검색
### 4. match 객체의 메서드
### 5. 컴파일 옵션
### 6. 백슬래시 문제


### 1. 정규 표현식의 기초, 메타 문자

# 1) 문자 클래스(character class): []
# - 대괄호 안에 문자 매치 / 하이픈은 From~To
# - [a-zA-z]: 알파벳 모두
# - [0-9]: 숫자
# - [^] : not

# 2) Dot(.)
#  - \n을 제외한 모든 문자와 매치

# 3) 반복(*)
# - * 바로 앞 문자가 반복될 수 있음을 의미 (0회 포함)

# 4) 반복(+)
# - + 바로 앞 문자가 반복될 수 있음을 의미 (0회 미포함)

# 5) 반복({m, n})
# - {} 앞 문자가 m부터 n까지 반복 / m의 기본 값은 0

# 6) 반복(?)
# - ? 앞 문자가 0 또는 1회 반복


### 2. 파이썬에서 정규 표현식을 지원하는 re모듈
# import re
# p = re.compile("ab*")


### 3. 정규식을 이용한 문자열 검색
# 1) match > 문자열의 처음부터 정규식과 매치되는지 조사
import re

p = re.compile("[a-z]+")
m = p.match("python")  # <re.Match object; span=(0, 6), match='python'>
print(m)
m = p.match("3 Python")
print(m)  # None
print()
print()

# 2) serch > 문자열 전체를 검색하여 정규식과 매치되는지 조사
import re

p = re.compile("[a-z]+")
m = p.search("python")
print(m)  # <re.Match object; span=(0, 6), match='python'>
m = p.search("3 python")
print(m)  # <re.Match object; span=(2, 8), match='python'>
print()
print()

# 3) findall > 정규식과 매치되는 모든 문자열을 리스트로 반환
import re

p = re.compile("[a-z]+")
result = p.findall("life is too short")
print(result)  # ['life', 'is', 'too', 'short'] > 리스트로 반환
print()
print()

# 4) finditer > 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 반환
import re

p = re.compile("[a-z]+")
result = p.finditer("life is too short")
print(result)
for r in result: print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>


### 4. match 객체의 메서드: match / search
# 1) group() > 매치된 문자열 반환
# 2) start() > 매치된 문자열의 시작 위치
# 3) end() > 문자열의 끝 위치
# 4) span() > 문자열의 (시작, 끝) 튜플로 반환
# 5) string > 입력받은 문자열


### 5. 컴파일 옵션
# 1) DOTALL, S     > 모든 문자와 매치할 수 있도록 함
# 2) IGNORECASE, I > 대소문자 무시
# 3) MULTILINE, M  > 여러줄과 매치
# 4) VERBOSE, X    > verbose 모드 (주석 사용 등)

### 6. 백슬래시 문제
