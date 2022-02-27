# 2477번_참외밭

##  참외밭은 ㄱ자 모양이거나 ┏, ┗, ┛ 모양의 육각형
## 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성

'''
# 첫 번째 줄에 1m2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1 ≤ K ≤ 20)
# 참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발
# 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이 (1 이상 500 이하의 정수)가
# 둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어짐
# 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
## 입력으로 주어진 밭에서 자라는 참외의 수를 출력


(입력)
7
4 50
2 160
3 30
1 60
3 20
1 100

(출력) 
47600

'''

# k = int(input())

# d = {}
# temp = 0
# for i in range(6):
#     idx, n = map(int, input().split())
#     if d.get(idx):
#         d[idx].append(n)
#         temp = n
#     else:
#         d[idx] = [n]

# print(d)
# print(f'^{temp}')

# {4: [50], 2: [160], 3: [30, 20], 1: [60, 100]}

# temp1 = 1
# temp2 = 1
# for i in range(1, 5):
#     if len(d[i]) == 2 and d[i][1] != temp:
#         temp2 = d[i][0]
#         print(f'#{d[i][0]}')
#     else:
#         temp1 *= d[i][0]
#         print(d[i])
        
# print((temp1 - temp2*temp)*k)



k = int(input())

d = {}
for _ in range(6):
    idx, n = (map(int, input().split()))

    if d.get(idx):
        d[idx].append(n)
        
    else:
        d[idx] = [n]
print(d)

temp1 = 1
for i in range(1, 5):
    if len(d[i]) == 1:
        temp1 *= d[i][0]
        
print(temp1)