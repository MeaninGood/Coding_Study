import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

lis = [0]

for i in arr:
    if lis[-1] < i:
        lis.append(i)
        
    else:
        s = 0
        e = len(lis)
        
        while s < e:
            mid = (s + e) // 2
            
            if i > lis[mid]:
                s = mid + 1
            
            else:
                e = mid
        lis[e] = i
        
print(len(lis) - 1)