# dp = [[-1 for i in range(10010)] for j in range(310)]
# def recur(cur, c):
#     ret = 0

#     if cur > n:
#         return -1000000
    
#     if cur == n:
#         return ret
    
#     if dp[cur][c] != -1:
#         return dp[cur][c]
    
#     if c == 0:
#         print(f'num1 : {cur}')
#         ret = max(recur(cur + 1, 1) + arr[cur], recur(cur + 2, 0) + arr[cur])
#     else:
#         print(f'num2 : {cur}')
#         ret = max(recur(cur + 1, 0) + arr[cur], recur(cur + 2, 1) + arr[cur])
        
#     dp[cur][c] = ret
#     return ret

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# ans = 0
# print(recur(0, 0))


# def recur(cur, total, c1):
#     global ans
    
#     if cur > n:
#         return
    
#     if cur == n:
#         ans = max(ans, total)
#         return
    
#     if c1 == 0:
#         recur(cur + 1, total + arr[cur], 1)
#     recur(cur + 2, total + arr[cur], 0)
    

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# ans = 0
# recur(0, 0, 0)
# print(ans)


# dp = [[-1 for i in range(10010)] for j in range(310)]
# def recur(cur, c):
#     global ans
    
#     ret = 0
    
#     if cur > n:
#         return -100000000
    
#     if cur == n:
#         ans = max(ans, ret)
#         return
#     if dp[cur][c] != -1 :
#         return dp[cur][c]
    
#     if c == 0:
#         ret = recur(cur + 1, 1) + arr[cur]
    
#     ret = recur(cur + 2, 0) + arr[cur]
#     dp[cur][c] = ret
#     return ret

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# ans = 0
# recur(0, 0, 0)
# print(ans)



dp = [[-1 for i in range(10010)] for j in range(310)]
def recur(cur, c):    
    if c >= 2:
        return -1000000
    
    if cur >= n:
        return -1000000
    
    if cur == n - 1:
        return ret
    
    if dp[cur][c] != -1:
        return dp[cur][c]
    
    ret = max(recur(cur + 1, c + 1) + arr[cur], recur(cur + 2, c) + arr[cur])
    dp[cur][c] = ret
    return ret

n = int(input())
arr = [int(input()) for _ in range(n)]

print(max(recur(0, 0), recur(1, 0)))


dp = [[-1, -1] for i in range(310)]

def recur(cur, c1):
    if c1 >= 2:
        return -1000000000

    if cur >= n:
        return -1000000000

    if cur == n - 1:
        return arr[cur]

    if dp[cur][c1] != -1:
        return dp[cur][c1]

    ret = max(recur(cur + 1, c1 + 1), recur(cur + 2, 0))

    dp[cur][c1] = ret + arr[cur]

    return ret + arr[cur]


n = int(input())
arr = [int(input()) for _ in range(n)]
print(max(recur(0, 0), recur(1, 0)))