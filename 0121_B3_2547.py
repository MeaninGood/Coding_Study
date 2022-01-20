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

T = int(input())

for i in range(T) :
    if input() == '' : 
        N = int(input())
        candy = 0
        for j in range(N) :
            candy += int(input())
        
        if candy % N == 0 :
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