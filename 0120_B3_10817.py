# 10817번_세 수

## 세 정수 A, B, C가 주어짐.
## 이때, 두 번째로 큰 정수를 출력하는 프로그램 작성

'''
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어짐
## 두 번째로 큰 정수 출력

(입력)
20 30 10

(출력)
20

'''

numbers = list(map(int, input().split()))

numbers.sort()

print(numbers[1])