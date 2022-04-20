# 10815번_숫자 카드

## 숫자 카드는 정수 하나가 적혀져 있는 카드
## 숫자 카드 N개
## 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 구하기

'''
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)
# 둘째 줄에는 숫자 카드에 적혀있는 정수
# 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같
# 두 숫자 카드에 같은 수가 적혀있는 경우는 없다
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어짐
# 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어짐
# 이 수는 공백으로 구분되어져 있음
# 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다
## 첫째 줄에 입력으로 주어진 M개의 수에 대해 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1
## 아니면 0을 공백으로 구분해 출력

(입력)
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10

(출력) 
1 0 0 1 1 0 0 1

'''

import sys
input = sys.stdin.readline

n = int(input())
v = sorted(list(map(int, input().split())))
m = int(input())
ans = list(map(int, input().split()))

d = {}
for i in range(m):
    d[ans[i]] = d.get(i, 0)
    
print(d)
arr = sorted(ans)

# print(v)
# print(ans)
# print(arr)

s = 0
e = 0

# print(ans.index(arr[1]))

tmp = []

while s < n and e < m:
    if v[s] > arr[e]:
        e += 1
        
    elif v[s] < arr[e]:
        s += 1
    
    elif v[s] == arr[e]:
        d[arr[e]] = 1
        s += 1
        e += 1

print(d)

for i in d:
    print(d[i], end = ' ')
# print(*ans)
