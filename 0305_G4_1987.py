# 1987번_알파벳

## 세로 R칸, 가로 C칸으로 된 표 모양의 보드
## 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고,
## 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
## 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동
## 같은 알파벳이 적힌 칸을 두 번 지날 수 없다
## 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성
## 말이 지나는 칸은 좌측 상단의 칸도 포함

'''
# 첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20)
# 둘째 줄부터 R개의 줄에 걸쳐서 C개의 대문자 알파벳들이 빈칸 없이 주어짐
## 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력


(입력)
3 6
HFDFFB
AJHGDH
DGAGEH

(출력) 
6

'''
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# visited = [] 1. 리스트로 해보기 (시간초과)
# visited = {} 2. 딕셔너리로 해보기 (시간초과)
visited = set() # set으로 만드니까 통과!!
def dfs(x, y):
    ret = 1
    # visited.append(arr[x][y]) ## 방문처리, list 기준
    # visited[arr[x][y]] = True ## 방문처리, dict 기준
    visited.add(arr[x][y]) # set
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # arr[nx][ny] in visited: list 기준
        # visited.get(arr[nx][ny], False): dict 기준
        if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] in visited:
            continue
        ret = max(ret, dfs(nx, ny) + 1)
    # visited.pop() ## list 기준
    # visited[arr[x][y]] = False ## dict 기준
    visited.remove(arr[x][y])
    return ret

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(n)]

print(dfs(0, 0))           