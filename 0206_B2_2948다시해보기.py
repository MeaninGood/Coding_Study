# 2948번_2009년

## 2009년 날짜가 주어졌을 때, 무슨 요일인지 출력하는 프로그램을 작성

'''
# 첫째 줄에 D와 M, M월 D일
## 2009년 M월 D일의 요일을 영어로 출력

(입력)
17 1

(출력)
Saturday

'''

# 코드 1, 모듈 이용

# import datetime 이용하기
import datetime

d, m = map(int, input().split())

date = datetime.datetime(2009, m, d) # 2009년, m월, d일

print(date.strftime("%A")) # 요일 대문자로 출력


# 코드 2, 구현

# 2009년 월 입력, 9월이면 8월까지 더해야 하기 때문에 앞에 0 써줌
date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 2009년 1월 1일은 목요일, 인덱스는 0부터 시작하기 때문에 수요일을 맨 앞에 써줌
arr = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']

d, m = map(int, input().split())

# 입력받은 날짜 d에 각 월별 일수 더해주기
for i in range(m) :
    d += date[i]

# 요일에 해당하는 날짜 출력
print(arr[d%7])
    