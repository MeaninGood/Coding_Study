# 7568번_덩치

## N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수
## 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
## 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력

'''
# 첫 줄에는 전체 사람의 수 N
# N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 주어짐
## 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력
## 각 덩치 등수는 공백문자로 분리


(입력)
5
55 185
58 183
88 186
60 175
46 155

(출력)
2 2 1 2 5

'''

n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))
    
# b = sorted(arr, key = lambda x : (-x[0], -x[1]))

ans = []
for i in arr :    
    rank = 1
    for j in arr :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    ans.append(rank)
        
print(ans)
