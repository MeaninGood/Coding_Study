# 11724번_연결 요소의 개수

## 방향 없는 그래프가 주어졌을 때, 연결 요소의 개수 구하기

'''
# 첫째 줄에 정점의 개수 N과 간선의 개수 M
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ Nx(N-1)/2) 
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v
# (1 ≤ u, v ≤ N, u ≠ v)
# 같은 간선은 한 번만 주어짐
## 첫째 줄에 연결 요소의 개수를 출력


(입력)
6 5
1 2
2 5
5 1
3 4
4 6

(출력) 
2

'''

def dfs(cur):
    visited[cur] = True
    
    for nxt in v[cur]: # 연결된 애들을 돌면서
        if visited[nxt]: # True면 continue
            continue
        
        dfs(nxt) # 아니면 다 True로 바꿔줌


n, m = map(int, input().split())

v = [[] for i in range(n+1)] # 인덱스 맞추려고 그냥 n+1해줌
for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b) # 무향이니까 둘 다 추가
    v[b].append(a)
    
visited = [False for i in range(n+1)]

cnt = 0
for i in range(1, n+1):
    if not visited[i]: # False인 1번 인덱스부터 시작해서
        dfs(i) # dfs(i)를 한 번 다 돌고 나면
        cnt += 1 # cnt += 1씩 함, 다 True가 될 때까지

print(cnt)
