# 12866번_피노키오

## 'A','C','G','T' 빼내서 합성해서 조합 가지수 구하기


'''
# 첫 줄에 문자열의 길이 L이 주어짐.
# 둘쨰 줄에 길이 L의 문자열 S가 주어짐, 모든 문자는 ACGT중 하나
## 한 줄에 가능한 피노키오의 종류를 출력

(입력)
5
AACGT

(출력)
2

'''



n = int(input())

s = input()

acgt = list(set(s)) # 중복 제거한 s 문자열 리스트

if n > 3 : # n이 4이상일 때만 곱한 값 출력

    result = [] # 개수 카운트한 거 추가해줄 리스트
    for i in acgt : # 중복 제거한 ACGT 그 자체를 돌면서
        result.append(s.count(i)) # 문자열 s에서 각 문자의 개수를 세어줌
    
    total = 1 # result를 돌면서 값을 다 곱해줄 거임
    for k in result :
        total *= k # total에 result의 각 값을 곱해서 저장
    
    print(total%1000000007)
    
else : # n이 3이하일 때는 0 출력
    print(0)


''' 다른 코드 1

n = int(input())

s = input()

acgt = list(set(s)) # 중복 제거한 s 문자열 리스트

result = [] # 개수 카운트한 거 추가해줄 리스트
for i in acgt : # 중복 제거한 ACGT 그 자체를 돌면서
    cnt = 0 # cnt 0으로 초기화
    for j in s : # 입력받은 문자열을 돌면서 하나씩 문자 비교
        if i == j : # 같은 문자가 있으면
            cnt += 1 # 카운트를 1추가해 줌

    result.append(cnt) # 4개 카운트 다 하면 값을 result 리스트에 추가해 줌
    
total = 1 # result를 돌면서 값을 다 곱해줄 거임
for k in result :
    total *= k # total에 result의 각 값을 곱해서 저장
    
print(total%1000000007) # 그 값을 1,000,000,007로 나눈 나머지 출력


'''


''' 다른 코드 2

l = int(input())
s = str(input())

a = s.count('A')
c = s.count('C')
g = s.count('G')
t = s.count('T')

qq = a*c*g*t
print(qq%1000000007)

'''



n = int(input())
s = input()
pinokio = ['A', 'C', 'G', 'T']

cnt = 1
for i in pinokio:
    cnt *= s.count(i)

print(cnt % 1000000007)



