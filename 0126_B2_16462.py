# 16462번_'나교수' 교수님의 악필

## 숫자 '0', '6', '9'를 모두 9로 바꿔서 평균 내기
## 점수가 100점이 넘는 경우 100점으로 처리

'''
# 첫째 줄에 학생의 수 N
# 다음 N개의 줄에 학생들의 성적 정수가 차례대로 주어짐
## 학생들의 평균 성적과 가장 가까운 정수 출력.

(입력)
5
96
60
100
88
6

(출력)
79

'''

import math # 이걸로 ceil, floor 써줘야 함

n = int(input())

score = [] # 점수 저장할 리스트
for i in range(n) :
    num = input() # int가 아닌 str 그대로 받아 줌, 이후 숫자 바꿔야 하기 때문
    
    if num == '100' : # 100은 바로 score 리스트에 추가됨
        score.append(num)
        
    else : # 100이 아닌 경우
        tmp = '' # 빈 문자열 생성해서 바꾼 값 넣어줄 것
        for j in range(len(num)) : # 입력 받은 숫자 num을 돌며
            if (num[j] == '0') or (num[j] == '6') : # 0과 6을 찾으면
                tmp += '9' # 9로 바꿔서 tmp 문자열에 추가
            else :
                tmp += num[j] # 0, 9 가 아닌 경우 바로 문자열에 추가
            
        score.append(tmp) # 위에서 만들 문자열을 score 리스트에 넣어줌
        
total = sum(map(int, score)) # 몽땅 int로 바꿔주고
result = total / n # 그걸 나눠줌, 소수점 자리 있을 시 result는 float가 됨

if result - int(result) >= 0.5 : # 평균 소수점이 0.5 이상이면 반올림
    print(math.ceil(result))
else : # 아니면 내림
    print(math.floor(result))
