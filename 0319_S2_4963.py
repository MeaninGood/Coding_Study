# 4963번_섬의 개수

## 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램 작성
## 한 정사각형과 가로, 세로 또는 대각선으로 연결

'''
# 입력은 여러 개의 테스트 케이스
# 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h
# w와 h는 50보다 작거나 같은 양의 정수
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다
# 입력의 마지막 줄에는 0이 두 개
## 각 테스트 케이스에 대해서, 섬의 개수를 출력

(입력)
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

(출력)
0
1
1
3
1
9

'''

from collections import deque


dx = [1, 0, -1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    que = deque()
    
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que[0][0], que[0][1]
            que.popleft()
            
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited[nx][ny] or v[nx][ny] != 1:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
    
while 1:
    m, n = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    v = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [[False for i in range(m)] for j in range(n)]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if v[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j)
                
    print(cnt)
    
    
