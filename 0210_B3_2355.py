# 2355번_시그마

## 두 정수 A와 B
## 두 정수 사이에 있는 수의 합을 구하는 프로그램
## 사이에 있는 수들은 A와 B도 포함

'''
# 첫째 줄에 두 정수 A, B (-2,147,483,648 ≤ A, B ≤ 2,147,483,647)
## 첫째 줄에 답을 출력 (-2,147,483,648 ≤ 답 ≤ 2,147,483,647)

(입력)
1 2

(출력)
3

'''

''' 시간초과 
a, b = map(int, input().split())

ans = 0
for i in range(a, b+1):
    ans += i
    
print(ans)
'''


''' 메모리초과
a, b = map(int, input().split())
arr = [i for i in range(a, b+1)]

print(sum(arr))
'''

a, b = map(int, input().split())

if a > b :
    print(int((a+b) * (a - b + 1) / 2))
    
else :
    print(int((a+b) * (b - a + 1) / 2))
