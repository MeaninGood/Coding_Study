# 11725번_트리의 부모 찾기

## 루트 없는 트리가 주어짐
## 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성

'''
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어짐
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어짐
## 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력

(입력)
7
1 6
6 3
3 5
4 1
2 4
4 7

(출력)
4
6
1
3
1
4

'''


import sys
sys.setrecursionlimit(150000)

n = int(input())
v = [[] for i in range(n + 1)]
par = [0 for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

def dfs(cur, prv):
    par[cur] = prv

    for nxt in v[cur]:
        if nxt == prv:
            continue

        dfs(nxt, cur)

dfs(1, -1)

for i in range(2, n + 1):
    print(par[i])