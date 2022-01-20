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

def factorial(n) :
    while 1 :
        if n == 0 or n == 1 :
            return 1
    
        else :
            return n * factorial(n-1)
    
n = int(input())    
print(factorial(n))