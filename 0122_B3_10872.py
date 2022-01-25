# 10872번_팩토리얼

## 정수 N이 주어질 때 N! 출력

'''
# 첫째 줄에 정수 N 주어짐
## 첫째 줄에 N! 출력

(입력)
10

(출력)
3628800

'''

def factorial(n) : # 팩토리얼 재귀 함수 생성
    while 1 : 
        if n == 0 or n == 1 : # n이 0이거나 1일 때 종료
            return 1 # 1 반환
    
        else :
            return n * factorial(n-1) # n * f(n-1)을 계속해서 리턴하는 구조
    
n = int(input())    
print(factorial(n))