# 10158번_개미

## w×h인 격자 공간
## 처음에 (p,q)에서 출발하는 개미의 t시간 후의 위치 (x,y)를 계산하여 출력
## w와 h는 자연수이며 범위는 2 ≤ w,h ≤ 40,000
## 미의 초기 위치 p와 q도 자연수이며 범위는 각각 0 < p < w과 0 < q < h
## 시간 t의 범위는 1 ≤ t ≤ 200,000,000

'''
# 첫줄에는 w와 h가 공백을 사이에 두고 주어짐
# 그 다음 줄에는 초기 위치의 좌표값 p와 q가 공백을 사이에 두고 주어짐
# 3번째 줄에는 개미가 움직일 시간 t
## t 시간 후에 개미의 위치 좌표 (x,y)의 값 x와 y를 공백을 사이에 두고 출력

(입력)
6 4
4 1
8

(출력) 
0 1

'''

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x1 = 0
y1 = 0
if t >=( w - x ):
    print(abs(t - (w - x)*2 - x), end = ' ')
elif t < (w - x):
    print(x - t, end = ' ')
    
if t >= (h - y):
    print(abs(t - (h - y)*2 - y), end = ' ')
elif t < ( h - y):
    print(y - t, end = ' ')