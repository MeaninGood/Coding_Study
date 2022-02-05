# 3076번_상근이의 체스판

## 검정색은 'X', 흰 색은 '.'으로 표시함
## R행 * C열, 행의 높이는 문자 A개 만큼, 각각의 열 너비는 문자 B개 만큼
## R,C,A,B가 주어졌을 때, 상근이의 체스판 출력

'''
# 첫째 줄에 두 양의 정수 R, C
# 둘째 줄에 두 양의 정수 A, B
## 출력은 R*A행, C*B열로 이루어져 있어야 함


(입력)
2 4
2 2

(출력)
XX..XX..
XX..XX..
..XX..XX
..XX..XX

'''


'''
1. 각 문자열 한 줄씩 생성

빈 문자열 ''
for i in range(4) -> 0 1 2 3
i의 나머지가 0이면 문자열에 X가 3개 추가 됨
'XXX'
그 다음 나머지가 1이면 문자열에 . 3개가 추가됨
'XXX...'
위와 같은 과정을 거쳐서

i = 0이면 res1 = 'XXX'
i = 1이면 res1 = 'XXX...'
i = 2이면 res1 = 'XXX...XXX'
i = 3이면 res1 = 'XXX...XXX...' 순서로 res1이 생성됨.
최종적으로 문자열 res1이 됨

## res2는 위의 과정을 반대로 함





2. 합쳐서 최종 문자열 생성

빈 문자열 ''

for i in range(2) -> 0 1
i의 나머지가 0이면 문자열에 'res1+공백' 2개 추가 됨
'XX..XX..'+'\n'+'XX..XX..'+'\n'
그 다음 나머지가 1이면 문자열에 'res2+공백' 2개 추가 됨
'..XX..XX'+'\n'+'..XX..XX'+'\n'

위와 같은 과정을 거쳐서

i = 0이면 res1 * 2
'XX..XX..
XX..XX..
' (공백 때문에 따옴표가 여기서 끝이 납니다)

i = 1이면 res2 * 2
'XX..XX..
XX..XX..
..XX..XX
..XX..XX
'(공백 때문에 따옴표가 여기서 끝이 납니다)

## 따옴표가 밑에 있어도 \n = False이므로 제출 시 문제 없는 듯?

'''

r, c = map(int, input().split()) ## 2 4 라고 가정
a, b = map(int, input().split()) ## 2 2 라고 가정

res1 = '' # 빈 문자열 생성 / 한 줄을 만들어주는 과정
for column in range(c) : # 4까지 돌면서
    if column % 2 : # 나머지가 1이면 .이 b번 곱해져 입력되고
        res1 += '.' * b
    else : # 나머지가 0이면 X가 b번 곱해져 입력됨
        res1 += 'X' * b

res2 = '' 
for column in range(c) : 
    if column % 2 :
        res2 += 'X' * b 
    else :
        res2 += '.' * b
        
tt = '' # 최종적으로 출력할 빈 문자열 생성
for row in range(r) : # 2까지 돌면서
    if row % 2 :  # 나머지가 1이면 
        tt += (res2+'\n') * a # res2 + 공백이 a번 곱해져 입력
         
    else : # 나머지가 0이면
        tt += (res1+'\n') * a # res1 + 공백이 a번 곱해져 입력
         
print(tt)