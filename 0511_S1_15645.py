import sys
input = sys.stdin.readline

n = int(input())
dp1 = [[0, 0, 0], [0, 0, 0]]
dp2 = [[0, 0, 0], [0, 0, 0]]
idx1 = 0
idx2 = 0
for i in range(n):
    arr = list(map(int, input().split()))
    
    for j in range(3):
        dp1[idx1][j] = 0
        dp2[idx2][j] = 1 << 30 
        
        for k in range(3):
            if abs(j - k) >= 2:
                continue
            
            dp1[idx1][j] = max(dp1[idx1][j], dp1[idx1 ^ 1][k] + arr[j])
            dp2[idx2][j] = min(dp2[idx2][j], dp2[idx2 ^ 1][k] + arr[j])

    idx1 ^= 1
    idx2 ^= 1 

print(max(dp1[idx1 ^ 1]), min(dp2[idx2 ^ 1]))
