# 13910번_개업

## 동시에 두 개의 웍(중국 냄비)을 사용하여 요리할 수 있다
## 주문 받은 짜장면의 그릇 수에 딱 맞게 요리
## 해빈이가 주문 받은 짜장면의 수와 가지고 있는 웍의 크기가 주어질 때,
## 최소 몇 번의 요리로 모든 주문을 처리할 수 있는지 출력하는 프로그램을 작성

'''
# 첫 번째 줄에는 해빈이가 주문 받은 짜장면의 수N(1≤N≤10,000)과
# 가지고 있는 웍의 개수 M(1≤M≤100)이 주어짐
# 두 번째 줄에는 웍의 크기 Si(1≤Si≤N)이 M개가 주어짐
# 같은 크기의 웍을 여러 개 가지고 있을 수 있다
## 해빈이가 모든 주문을 처리하기 위해 해야 하는 최소 요리 횟수를 출력
## 만약 모든 주문을 처리 할 수 없는 경우 -1을 출력

(입력)
5 2
1 3

(출력)
2

'''


import sys, heapq
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))             # 한그릇도 배열 만드려고 0으로 패딩

def get_dist(s):
    pq = []

    dist[s] = 0
    heapq.heappush(pq, (0, s))                          # 처음 거리 0
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if cur == n:                                    # 현재의 위치가 n과 같으면 return
            return d
        
        if dist[cur] != d:
            continue
        
        for nxt in v:
            nd = d + 1                                  # 거리를 요리 횟수로 써서, + 1씩 해줌
            
            if cur + nxt > 10000:                       # n제한 넘으면 못 만드는 경우니까 continue
                continue
            
            if dist[cur + nxt] > nd:                    # 다음 노드는 현재까지 만든 짜장면 수 + 다음에 만들 짜장면 수
                dist[cur + nxt] = nd
                heapq.heappush(pq, (nd, cur + nxt))
                
    return -1

v = []

for i in range(m):
    for j in range(i + 1, m + 1):
        v.append(arr[i] + arr[j])

dist = [1000000000 for _ in range(10010)]


print(get_dist(0))