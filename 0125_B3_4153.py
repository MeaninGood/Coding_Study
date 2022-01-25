# 4153번_직각삼각형

## 주어진 세 변의 길이로 삼각형이 직각인지 아닌지 구분


'''
# 입력은 여러 개의 테스트 케이스로 주어지며 마지막 줄에는 0 0 0 이 입력된다
# 각 입력은 변의 길이를 의미한다
## 직각 삼각형이 맞다면 right, 아니라면 wrong 출력

(입력)
6 8 10
25 52 60
5 12 13
0 0 0


(출력)
right
wrong
right

'''

while 1 :
    a, b, c = map(int, input().split())
    
    if not a and not b and not c :
        break
    
    if (a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2 :
        print('right')
    
    else :
        print('wrong')