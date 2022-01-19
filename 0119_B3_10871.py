# 10871번_X보다 작은 수

## 정수 N개로 이루어진 수열 A와 정수 X
## A에서 X보다 작은 수를 모두 출력하는 프로그램 작성

'''
# 첫째 줄에 N과 X 주어짐
# 둘째 줄에 수열 A를 이루는 정수 N개
## X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력

(입력)
10 5
1 10 4 9 2 3 8 5 7 6

(출력)
1 4 2 3

'''

# 1. 기본 코드

N, X = map(int, input().split()) # 각 변수에 Input 생성
A = map(int, input().split()) # A를 map으로 받아주기

for i in A : # i 가 수열 A 탐색
    if i < X : # A에서 i가 X보다 작으면
        print(i, end = ' ') # 출력, end = ' '으로 공백 만들어주기



# 2. 다른 코드

N, X = map(int, input().split())
A = map(int, input().split())

B = [ i for i in A if i < X ] # 리스트에서 바로 한 줄로 작성

print(*B) # 리스트 언패킹 * => 숫자만 뜸