# 17352번_여러분의 다리가 되어 드리겠습니다!

## N개의 섬
## 섬에는 1, 2, ..., N의 번호가 하나씩 붙어 있다
## 그 섬들을 N - 1개의 다리가 잇고 있으며, 어떤 두 섬 사이든 다리로 왕복할 수 있다
## 다리 하나가 무너져서 서로 다른 두 섬을 다리로 이어서 다시 어떤 두 섬 사이든 왕복할 수 있게 해야 한다

'''
# 첫 줄에 정수 N이 주어진다. (2 ≤ N ≤ 300,000)
# 그 다음 N - 2개의 줄에는 욱제가 무너뜨리지 않은 다리들이 잇는 두 섬의 번호가 주어짐
## 다리로 이을 두 섬의 번호를 출력
## 여러 가지 방법이 있을 경우 그 중 아무거나 한 방법만 출력

(입력)
4
1 2
1 3

(출력)
1 4

'''

import sys
input = sys.stdin.readline

def find_(x):
    if par[x] == x:
        return x
    
    return find_(par[x])

def union_(a, b):
    a, b = find_(a), find_(b)
    
    if a == b:
        return
    
    if rnk[a] > rnk[b]:
        par[b] = a
    
    elif rnk[a] < rnk[b]:
        par[a] = b
    
    else:
        par[a] = b
        rnk[b] += 1


n = int(input())

v = [list(map(int, input().split())) for _ in range(n - 2)]
par = [i for i in range(n + 1)]
rnk = [0 for _ in range(n + 1)]

for i in range(n - 2):
    a, b = v[i]

    union_(a, b)

print(par)

for i in range(1, n + 1):
    par[i] = find_(par[i])

print(par)
tmp = par[1]
idx = 1
for i in range(2, n + 1):
    if par[i] != tmp:
        print(idx, i)
        break

    
    
