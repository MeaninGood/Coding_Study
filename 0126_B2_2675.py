# 2675번_문자열 반복

## 문자열 S를 입력받은 후, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램 작성
## 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P 만들기


'''
# 첫째 줄에 테스트 케이스 개수 T가 주어짐.
# 각 테스트 케이스는 반복 횟수 R, 문자열 S가 공백으로 구분되어 주어짐.
## 각 테스트 케이스에 대해 P를 출력.

(입력)
2
3 ABC
5 /HTP

(출력)
AAABBBCCC
/////HHHHHTTTTTPPPPP

'''

t = int(input())

for i in range(t) :
    r, s = input().split() # 공백으로 나눠서 변수에 넣음, str로 받기
    r = int(r) # 맨 앞에 str로 들어온 숫자 int로 바꿔줌
    
    for i in range(len(s)) : # 입력 받은 문자열 s를 돌면서
        print(s[i]*r, end='') # 각 문자를 r번 곱해줌, 공백 없음
        
    print() # 줄바꿈