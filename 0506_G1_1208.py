import sys
input = sys.stdin.readline

def recur(cur, total, idx, e):
    if cur == e:
        v[idx].append(total)
        return
    
    recur(cur + 1, total + arr[cur], idx, e)
    recur(cur + 1, total, idx, e)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
v = [[] for _ in range(2)]

recur(0, 0, 0, n // 2)
recur(n // 2, 0, 1, n)

v[0].sort()
v[1].sort()

s = 0
e = len(v[1]) - 1
cnt = 0
while s < len(v[0]) and e >= 0:
    if v[0][s] + v[1][e] == m:
    
        tmp = v[0][s]
        x = 0
        while s < len(v[0]) and v[0][s] == tmp:
            x += 1
            s += 1
        
        tmp = v[1][e]
        y = 0
        while e >= 0 and v[1][e] == tmp:
            y += 1
            e -= 1
            
        cnt += x * y
    
    elif v[0][s] + v[1][e] < m:
        s += 1
    
    else:
        e -= 1
        
print(cnt - (m == 0))