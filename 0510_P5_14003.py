import sys
input = sys.stdin.readline

n = int(input())
arr = [-1000000010] + list(map(int, input().split()))
dp = [-1 for i in range(n + 1)]
lis = [-1000000010]

mx = -1
for i in range(n + 1):
    if lis[-1] < arr[i]: 
        lis.append(arr[i])
        dp[i] = len(lis) - 1
        
        if dp[i] > mx:
            mx = dp[i]
        
    else:
        s = 0
        e = len(lis)
        
        while s < e:
            mid = (s + e) // 2
            
            if arr[i] > lis[mid]:
                s = mid + 1
                
            else:
                e = mid
                
        lis[e] = arr[i]
        dp[i] = e
        if dp[i] > mx:
            mx = dp[i]

print(mx)

ans = []
for i in range(n + 1)[::-1]:
    if mx == 0:
        break
    
    if mx == dp[i]:
        ans.append(arr[i])
        mx -= 1

for i in ans[::-1]:
    print(i, end = ' ')