# 17413번_단어 뒤집기 2

## 문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집기
## 1. 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
## 2. 문자열의 시작과 끝은 공백이 아니다.
## 3. '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장
## 3. 두 문자의 개수는 같다.
## 태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열
##  '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다
## 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분
##  태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

'''
# 첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하
## 첫째 줄에 문자열 S의 단어를 뒤집어서 출력

(입력)
baekjoon online judge

<ab cd>ef gh<ij kl>

(출력)
noojkeab enilno egduj

<ab cd>fe hg<ij kl>

''' 


'''
단어만 뒤집기 - 소문자, 숫자, 공백, 특수문자 <>
1. <>는 세트로 뒤집지 않음
2. < 길이 3 이상 문자열, 알파벳 소문자 & 공백 > : 태그
3. 단어 : 알파벳 소문자, 숫자
4. 연속하는 두 단어는 공백 하나로 구분
5. 태그는 단어 x, 태그와 단어 사이에는 공백 없음

baekjoon online judge -> 다 뒤집어짐 / 공백 기준
<open>tag<close> ->  <>안에 있는 건 태그라서 그대로, tag 단어만 바뀜
>>> <open>gat<close>

<ab cd>ef gh<ij kl> -> <> 그대로, df gh만 바뀜
>>> <ab cd>fe hg<ij kl>

<int><max>2147483647<long long><max>9223372036854775807
>>> <int><max>7463847412<long long><max>7085774586302733229



공백,  <> 기준으로

다 뒤집어서 출력하다가
>< 얘 만나면 얘네만 그대로 출력하는 법


'''

word = input()

n = len(word)

istag = False
p = ''
for i in range(n-1, -1, -1):
    if word[i] == '>':
        istag = True
        
    elif word[i] == '<':
        p += word[i]
        istag = False
        print(p[::-1], end='')
        
    if istag:
        p += word[i]
    
    else:
        # p += word[i]
        print(word[i], end='')

    
 
 

# s = input() + ' '

# istag = False

# p = ''
# for i in range(len(s)):
#     if s[i] == '<':
#         print(p[::-1], end=' ')
        
#         p = ''
#         istag = True
#     elif s[i] == '>':
#         istag = False

#     if istag:
#         continue

#     if s[i] == ' ':
#         print(p[::-1], end=' ')
#         p = ''
#     else:
#         p += s[i]
        
