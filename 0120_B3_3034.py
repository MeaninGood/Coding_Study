# 3034번_앵그리 창영

## 박스의 크기와 성냥의 길이가 주어졌을 때,
## 성냥이 박스에 들어갈 수 있는지 없는지 구하는 프로그램 작성

'''
# 첫째 줄에 던진 성냥의 개수 N과 박스의 가로 크기 W와 세로 크기 H가 주어짐
# 다음 N개 줄에는 성냥의 길이가 주어짐
## 입력으로 주어지는 각각의 성냥에 대해, 박스 안에 들어갈 수 있으면 DA, 없으면 NE 출력

(입력)
5 3 4
3
4
5
6
7

(출력)
DA
DA
DA
NE
NE

'''

N, W, H = map(int, input().split())

for i in range(N) :
    matches = int(input())
    
    if (W**2 + H**2)**(1/2) >= matches :
        print('DA')
        
    else :
        print('NE')
