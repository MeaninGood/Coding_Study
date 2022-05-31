import sys
input = sys.stdin.readline
sys.setrecursionlimit(100010)


def dfs(cur):
    # 사이클 판별이 되어 있으면 -1 리턴
    if cycle[cur] != -1:
        return -1
    
    # 방문처리 되어 있으면 cur 계속 리턴
    if visited[cur]:
        return cur
    
    # 그렇지 않다면 방문처리 해주고
    visited[cur] = True
    # 다음 걸로 넘어가기
    ret = dfs(arr[cur])
    
    # 리턴 값이 -1이면 사이클이 아니라는 뜻이므로
    if ret == -1:
        # 사이클이 아니다 : 0
        cycle[cur] = 0
        # -1 리턴해줌
        return -1
    
    # 그게 아니면 다 사이클이라는 뜻이므로 사이클이다 : 1
    cycle[cur] = 1

    # 방문처리 된 후 ret == cur(자기 자신을 다시 만난다)면 사이클이라는 뜻
    if ret == cur:
        # 그때부터 사이클이 아닌 나머지는 다 -1리턴해 줌
        return -1
    
    # 그렇지 않다면 자기 자신을 만날 때까지 계속 ret 리턴
    return ret

T = int(input())

for tc in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    
    # 방문처리
    visited = [False for _ in range(n + 1)]
    # 사이클 판별 안 했다: -1, 사이클이 아니다: 0, 사이클이다: 1
    cycle = [-1 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
        
    ans = 0    
    for i in range(1, n + 1):
        # 사이클이 아닌 것의 개수
        if cycle[i] == 0:
            ans += 1
            
    print(ans)