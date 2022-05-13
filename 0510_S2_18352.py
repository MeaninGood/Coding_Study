# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(s):
#     que = deque()
#     visited = [False for _ in range(n + 1)]
    
#     que.append(s)
#     visited[s] = True
    
#     ret = 0 
#     ans = []
#     while que:
#         size = len(que)
        
#         for _ in range(size):
#             cur = que.popleft()
            
#             if ret == k:
#                 ans.append(cur)
                
#             for nxt in v[cur]:
#                 if visited[nxt]:
#                     continue
                
#                 que.append(nxt)
#                 visited[nxt] = True
                
#         ret += 1
#     return ans

# n, m, k, x = map(int, input().split())

# v = [[] for _ in range(n + 1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     v[a].append(b)

# res = bfs(x)

# if len(res) == 0:
#     print(-1)

# else:
#     res.sort()
#     for i in res:
#         print(i)
