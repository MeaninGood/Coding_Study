arr = [[0]*1010 for _ in range(1010)]

t = int(input())

for n in range(1, t+1):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x1+x2):
        for j in range(y1, y1+y2):
            arr[i][j] = n
    
## 시간초과 - 53점
# idx = 1
# while idx <= t:
#     cnt = 0
#     for i in range(1010):
#         for j in range(1010):
#             if arr[i][j] == idx :
#                 cnt += 1
#     idx += 1
        
#     print(cnt)


# 카운팅 소트
cnt = [0]*110 # 색종이 100장까지 까니까 넉넉하게 110칸
for i in range(1010):
    for j in range(1010):
        cnt[arr[i][j]] += 1 # cnt 인덱스로 접근해서 += 1
        
for i in range(1, t+1):
    print(cnt[i])