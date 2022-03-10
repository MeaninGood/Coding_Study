# 2468번_안전 영역

## 어떤 지역의 높이 정보를 파악
## 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다
## 행과 열의 크기가 각각 N인 2차원 배열에서 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수
## 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산

'''
# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력
# N은 2 이상 100 이하의 정수
# 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력
# 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력
# 높이는 1이상 100 이하의 정수
## 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력


(입력)
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

(출력) 
5

'''

import sys
sys.setrecursionlimit(100000) 
     
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

num = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > num:
            num = arr[i][j]
        
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = True

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        
        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or arr[nx][ny] <= i:
            continue

        dfs(nx, ny)

ans = 0
for i in range(num+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and not visited[j][k] :
                cnt += 1
                dfs(j, k)
            
    ans = max(ans, cnt)
            
print(ans)
