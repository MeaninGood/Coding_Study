# 2711번_오타맨 고창영

## 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 오타를 지운 문자열 출력


'''
# 첫째 줄에 테스트 케이스 T, 각 테스트 케이스는 한 줄로 구성
# 첫 숫자는 오타를 낸 위치, 두 번째 문자열의 첫 문자는 1번째 문자
# 문자는 대문자로만 이루어져 있음
## 각 테스트 케이스에 대해 오타를 지운 문자열을 출력한다.

(입력)
4
4 MISSPELL
1 PROGRAMMING
7 CONTEST
3 BALLOON


(출력)
MISPELL
ROGRAMMING
CONTES
BALOON

'''


T = int(input())

for i in range(T) :
    idx, word = input().split()
    
    # 인덱스 맞춰서 지우기 4 -> 3으로 바꿔줌 (인덱스 0부터 시작) // 편하게 하려고
    idx = int(idx) - 1
    
    result = '' # 값을 담을 문자열
    
    for i in word[:idx] : # 처음~값을 뺄 문자 앞까지 result에 더해줌
        result += i
        
    for j in word[idx+1:] : # 값을 뺀 문자 다음부터~끝까지 result에 더해줌
        result += j
    print(result) 