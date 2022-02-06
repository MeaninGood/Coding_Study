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

import datetime

d, m = map(int, input().split())

date = datetime.datetime(2009, m, d)

print(date.strftime("%A"))