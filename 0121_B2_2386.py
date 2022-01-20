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

while 1 :
    word = input().lower()
    
    if word == '#' :
        break

    idx = word[0]
    cnt = 0
    for i in word :
        if idx == i :
            cnt += 1
            
    print(idx, cnt-1)