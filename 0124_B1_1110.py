# 1110번_더하기 사이클

## 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들기
## 각 자리의 숫자를 더함
## 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어붙임
## 26 -> 2 + 6 = 8 // 68 -> 6 + 8 = 14 // 84 -> 8 + 4 = 12 // 42 -> 4 + 2 = 6 // 26
## 사이클 4번만 돌면 원래의 수로 돌아옴
## N이 주어졌을 떄, N의 사이클의 길이를 구하는 프로그램

'''
# 첫째 줄에 N
## 첫쨰 줄에 N의 사이클 길이 출력

(입력)
26

(출력)
4

'''

    
n = int(input())

cnt = 0 # 싸이클 길이 카운트하는 변수
new = n # n 값 고정하려고 둔 변수 new // 왜냐면 while문 돌면서 값이 계속 바뀔 것임

while 1 :
    
    temp = n//10 + n%10 # 임시변수 : 26 -> 2 + 6
    result = (n%10)*10 + temp%10  # 계산 값 2 + 6 = 8 // 68
    cnt += 1 # 카운트 +1 해줌
    n = result # n을 result로 
        
    if new == result : # 고정해둔 첫 n과 싸이클을 돌고 난 후 result가 같으면
        break # break
    
print(cnt)
    
    
    