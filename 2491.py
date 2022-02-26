n = int(input())
arr = list(map(int, input().split()))


dp = [-1 for i in range(n)]
def recur(cur, prv):
    if cur == n:
        return -1000000
    
    if arr[cur] >= arr[prv]:
        pass
    
    

# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# dp = [-1 for i in range(1500010)]

# def recur(cur):
#     if cur > n:
#         return -1000000000
#
#     if cur == n:
#         return 0
#
#     if dp[cur] != -1:
#         return dp[cur]
#
#     dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
#
#     return dp[cur]
#
#
# print(recur(0))