# 2386번_도비의 영어 공부

## 영어 문장과 알파벳 하나가 주어짐
## 그 알파벳이 문장에서 몇 번 나타내는지 세기

'''
# 입력은 몇 개의 줄들로 이루어짐
# 각 줄에는 하나의 소문자와 영어 문장이 공백으로 주어짐
# 입력의 마지막은 #
## 주어진 소문자와 그 소문자 알파벳이 나타난 횟수
## 해당 알파벳이 소문자던 대문자던 모두 세기

(입력)
g Programming Contest
n New Zealand
x This is quite a simple problem.
#

(출력)
g 2
n 2
x 0

'''

while 1 : # '#'을 input으로 받기 전까지 계속 반복
    words = input().lower() # 인풋을 소문자로 받아줌, 비교 편하게 하기 위해
    
    if words == '#' : # break 조건 = input에 '#' 들어올 때
        break

    idx = words[0] # 배열의 맨 앞에 비교할 소문자를 idx로 설정
    cnt = 0 # 몇 번 나타내는지 카운트해줄 변수
    for i in words : # 배열을 돌면서
        if idx == i : # idx가 각 문자와 같다면
            cnt += 1 # 카운트
            
    print(idx, cnt-1) # 배열의 맨 앞부터 돌기 때문에
                    # 즉, 본인도 카운트하기 때문에 cnt-1로 출력