# 2547번_사탕 선생 고창영

## N명의 학생이 각자 사탕을 들고 왔을 때
## 모두에게 같은 개수의 사탕 나눠줄 수 있나?

'''
# 첫째 줄에 테스트 케이스 T, 각 테스트 케이스는 빈 줄로 구분
# 테스트 케이스 첫 줄에 학생 수 N, 다음 N개의 줄에 각 학생들이 가져온 사탕 수
## 모두에게 같은 사탕을 나눠줄 수 있으면 YES, NO

(입력)
2

5
5
2
7
3
8

6
7
11
2
7
3
4

(출력)
YES
NO

'''

T = int(input()) # 테스트케이스 개수

for i in range(T) : # 테스트케이스만큼 반복문 생성
    if input() == '' : # T를 공백으로 구분, 공백을 넣을 때만 다음 input() 생기게 함
        N = int(input()) # 첫 줄 학생 수 N창만 먼저 생성
        candy = 0 # 사탕 개수 저장한 변수
        for j in range(N) : # 학생 수 N을 돌면서
            candy += int(input()) # 인풋창 N개를 만들어 사탕 개수로 바로 합쳐줌
        
        if candy % N == 0 : # 사탕 수 % 학생 수 == 0 이면 (딱 맞게 나눠줄 수 있으면)
            print('YES') 
    
        else :
            print('NO')
            
'''
## 테스트 케이스 사이에 공백 주기

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break
        
'''