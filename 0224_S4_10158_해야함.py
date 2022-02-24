
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
arr = [[0]*(w+1) for i in range(h+1)]

dx = [1, 1, -1, 1]
dy = [1, -1, -1, -1]

x = q
y = p
d = 0
for i in range(t+1):
    arr[x][y] = i
    
    nx = x + dx[d]
    ny = y + dy[d]
    
    if not (0 <= nx < h+1 and 0 <= ny < w+1):
        d = (d + 1) % 4
        
    x += dx[d]
    y += dy[d]

pprint.pprint(arr)
for i in range(h+1):
    for j in range(w+1):
        if arr[i][j] == t:
            print(j, i)
            exit()