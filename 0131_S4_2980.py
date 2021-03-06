# 2980번_도로와 신호등

## 
## 점수가 100점이 넘는 경우 100점으로 처리

'''
# 첫째 줄에 학생의 수 N
# 다음 N개의 줄에 학생들의 성적 정수가 차례대로 주어짐
## 학생들의 평균 성적과 가장 가까운 정수 출력.

(입력)
5
96
60
100
88
6

(출력)
79

'''

# import sys
# n, l = map(int, sys.stdin.readline().split())

# li = []
# for _ in range(n) :
#     d, r, g = map(int, sys.stdin.readline().split())
#     li.append([d, r, g])

# t = 0    
# for i in range(len(li)-1) :
#     t += li[i+1][0] % li[i][1]
    
# total = l + t + li[-1][-2]

# print(total)




# import sys
# n, l = map(int, sys.stdin.readline().split())

# li = []
# for _ in range(n) :
#     d, r, g = map(int, sys.stdin.readline().split())
#     li.append([d, r, g])

# t = 1
# tr = [li[0][0]]
# for i in range(len(li)-1) :
#     tr.append(li[i+1][0] - li[i][0])

# for i in range(len(li)) :
#     if tr[i] > li[i][1] + li[i][2] :
#         t += tr[i] % (li[i][1] + li[i][2])
        
#     else :
#         t += (li[i][1] + li[i][2]) % tr[i]
        
# total = l + t

# print(total)



# import sys
# n, l = map(int, sys.stdin.readline().split())

# li = [[0,0,0]]
# for _ in range(n) :
#     d, r, g = map(int, sys.stdin.readline().split())
#     li.append([d, r, g])
    
# t = li[1][0] - li[0][0]  
# for i in range(len(li)-1) :
#     dis = li[i+1][0] - li[i][0]
#     dr = li[i+1][1] + li[i+1][2]
#     print(dis)
#     print(dr)
#     print(li[i+1][1])
#     print(li[i+1][1] - dis)
#     if t % dr == 0 :
#         t += li[i+1][1]
        
#     elif t % dr < li[i+1][1] :
#         t += li[i+1][1] - dis
        
#     # elif dis % dr >= li[i+1][1] :
#         # t += 0
    
#     else :
#         t += 0
    
# print(t)



import sys
n, l = map(int, sys.stdin.readline().split())

li = [[0,0,0]]
for _ in range(n) :
    d, r, g = map(int, sys.stdin.readline().split())
    li.append([d, r, g])
    
t = 0 # 시간
dis = 0 # 거리

for i in range(len(li)-1) :
    dis += li[i+1][0] - li[i][0] # for문 돌 때마다 거리 추가해줌
    rg = li[i+1][1] + li[i+1][2] # 매 신호등마다 빨간불 + 초록불 시간 합

    if (t+dis) % rg == 0 : # 거리 + 시간 을 신호등 사이클로 나눈 몫이 0이면
        t += li[i+1][1] # 빨간불만큼 멈춰있어야 하니까 빨간불 초 추가해줌
        
    elif (t+dis) % rg < li[i+1][1] :# 거리 + 시간을 신호등 사이클로 나눈 몫이 빨간불일 때보다 작으면
        t += li[i+1][1] - ((t+dis)%rg) # 빨간불일 때의 시간 - 거리

    else :
        t += 0
dis += l - li[-1][0] # 마지막 거리 추가해줌

print(t + dis)