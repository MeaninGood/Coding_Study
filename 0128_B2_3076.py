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
..XX..X
..XX..XX

'''

r, c = map(int, input().split())
a, b = map(int, input().split())

for row in range(r):
    res = ''
    for column in range(c):
        val1 = 'X' * b
        val2 = '.' * b
        res += val1 + val2
    for i in range(a):
        if i % 2:
            

