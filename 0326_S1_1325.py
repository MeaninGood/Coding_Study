# 1325번_효율적인 해킹

## A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다
## 컴퓨터의 신뢰하는 관계가 주어졌을 때,
## 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력

'''
# 첫째 줄에, N과 M(N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수)
# 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어옴
# 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있음
## 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력

(입력)
5 4
3 1
3 2
4 3
5 3

(출력) 
1 2

'''

import sys
from collections import deque


def bfs(s):
    que = deque()
    visited = [False for _ in range(n + 1)]
    ret = 0
    
    que.append(s)
    visited[s] = True
    ret += 1
    while len(que) > 0 :
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()
            
            for nxt in v[cur]:
                if visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
                ret += 1
    return ret

si = sys.stdin.readline

n, m = map(int, si().split())
v = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, si().split())
    
    v[b].append(a)
    
ans = []
mx = -1000000
for i in range(n + 1):
    ans.append(bfs(i))
    mx = max(mx, ans[i])
    
for r in range(len(ans)):
    if mx == ans[r]:
        print(r, end = ' ')