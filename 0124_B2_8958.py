# 8958번_OX퀴즈

## 'OOXXOXXOOO'와 같은 퀴즈 결과가 있을 때, 문제의 점수는 연속된 O의 개수
## 위는 1+2+0+0+1+0+0+1+2+3 = 10점
## 점수 구하는 프로그램 작성

'''
# 첫째 줄에 테스트케이스 T
# 다음 N개의 줄에 문자열 주어짐
## 각 테스트케이스마다 점수 출력

(입력)
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

(출력)
10
9
7
55
30

'''

t = int(input())

for i in range(t) :
    result = input()
    
    cnt = 0 # 연속된 개수 카운트해줄 변수
    score = 0 # 최종 점수
    
    for i in result : # 입력 받은 문자열을 돌며
        if i == 'O' : # O가 있으면
            cnt += 1 # cnt를 1씩 증가시킴
                    # 2연속이면 cnt는 2가 됨 
            score += cnt # 증가시킨 cnt를 그대로 score에 더해줌
                        # 1연속 = 1, 2연속 = 2, 3연속 = 3점 추가 됨
            
        else :
            cnt = 0 # i가 'O'가 아니면 cnt 0으로 초기화
                    # 다음 번에 다시 1 -> 2 -> 3으로 가야 하기 때문
            
    print(score)