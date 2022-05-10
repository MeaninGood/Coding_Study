import sys
input = sys.stdin.readline

n = int(input())
arr = [-1000000010] + list(map(int, input().split()))
prv = [-1 for i in range(n + 1)]
lis = [-1000000010]

for i in range(n + 1):
    if lis[-1] < arr[i]: 
        lis.append(arr[i])
        # prv[i] = len(lis) - 1
        prv[i] = i
        
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
        prv[i] = e
        
            
print(len(lis) - 1)
print(*lis[1:])
print(lis)
print(prv)
print(arr)

ans = []
idx = prv[-1]
for i in range(len(prv)):
    if idx == 0:
        break
    ans.append(arr[idx])
    idx = prv[idx]
    
print(*ans)