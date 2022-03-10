# 2667번_단지번호붙이기

## 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때
## 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력

'''
# 첫째 줄에는 컴퓨터의 수
# 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨짐
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어짐
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어짐
## 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력


(입력)
7
6
1 2
2 3
1 5
5 2
5 6
4 7

(출력) 
4

'''

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y):
    ret = 1
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] != 1 or visited[nx][ny]:
            continue
        
        ret += dfs(nx, ny)
    return ret

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

cnt = 0
li = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt += 1
            li.append(dfs(i, j))
            
li.sort()
print(cnt)
print(*li, sep='\n')