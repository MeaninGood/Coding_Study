import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

dk = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 0, 1, 0, -1]
dy = [0, 0, 1, 0, -1, 0] 

def in_range(k, x, y):
    return 0 <= k < c and 0 <= x < n and 0 <= y < m

def bfs(k, x, y):
    que = deque()
    visited = [[[False for i in range(m)] for j in range(n)] for _ in range(c)]
    
    que.append([k, x, y])
    visited[k][x][y] = True
    
    ret = 0
    while que:
        size = len(que)
        
        for _ in range(size):
            k, x, y = que.popleft()
            
            if k == ek and x == ex and y == ey:
                return f'Escaped in {ret} minute(s).'
            
            for d in range(6):
                nk = k + dk[d]
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nk, nx, ny) or visited[nk][nx][ny] or arr[nk][nx][ny] == '#':
                    continue
                
                que.append([nk, nx, ny])
                visited[nk][nx][ny] = True
                
        ret += 1
    
    return 'Trapped!'
                
                
    
while 1:
    c, n, m = map(int, input().split())
    
    if c == 0 and n == 0 and m == 0:
        exit()
         
    arr = []

    for i in range(c):
        arr.append([list(input().rstrip()) for _ in range(n)])
        input()
        
    sk, sx, sy = 0, 0, 0
    ek, ex, ey = 0, 0, 0

    for k in range(c):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 'S':
                    sk, sx, sy = k, i, j
                
                if arr[k][i][j] == 'E':
                    ek, ex, ey = k, i, j
                    
    print(bfs(sk, sx, sy))
