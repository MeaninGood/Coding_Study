n = int(input())
arr = [[0 for i in range(3)]] + [list(map(int, input().split())) for i in range(n)]
ans = 1000000000

for k in range(3):
    dp = [[0 for i in range(3)] for j in range(n + 1)]
    for i in range(3):
        if i == k:
            dp[1][i] = arr[1][i]
        else:
            dp[1][i] = 100000000
                    
    for i in range(2, n + 1):
        mn = 100000000
        midx = 0
        for j in range(3):
            if mn > dp[i - 1][j]:
                mn = dp[i - 1][j]
                midx = j

        for j in range(3):
            if j == midx:
                continue

            dp[i][j] = mn + arr[i][j]

        mn = 1000000
        for j in range(3):
            if j == midx:
                continue

            mn = min(mn, dp[i - 1][j])

        dp[i][midx] = mn + arr[i][midx]

    
    
    for i in range(3):
        if i == k:
            continue
        ans = min(ans, dp[n][i])


print(ans)
