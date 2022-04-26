# 15666번_N과 M(12)

## N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
## N개의 자연수 중에서 M개를 고른 수열
## 같은 수를 여러 번 골라도 된다.
## 고른 수열은 비내림차순

'''
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 둘째 줄에 N개의 수가 주어짐
# 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수
## 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력
## 중복되는 수열을 여러 번 출력하면 안되며
## 각 수열은 공백으로 구분해서 출력
## 수열은 사전 순으로 증가하는 순서로 출력

(입력)
4 2
9 7 9 1

(출력)
1 1
1 7
1 9
7 7
7 9
9 9

'''

# m, n = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()

# v = [0 for i in range(n)]
# visited = [False for i in range(m)]
# def recur(cur, start):
#     if cur == n:
#         print(*v)
#         return
    
#     for i in range(start, m):
#         if visited[i]:
#             continue
        
#         visited[cur] = True
#         v[cur] = arr[i]
#         recur(cur + 1, i + 1)
#         visited[cur] = False
        
# recur(0, 0)




m, n = map(int, input().split())
arr = set(map(int, input().split())) # 미리 중복 제거해서 받기
arr = list(arr)                     # 정렬할 거니까 list로 만들기
arr.sort()


e = len(arr)                        # 중복 제거한 arr의 길이 구해줌
v = [0 for i in range(n)]

def recur(cur, start):
    if cur == n:                    # n만큼의 자리가 다 차면
        print(*v)                   # v에 채워진 값 print
        return
    
    for i in range(start, e):       # 중복 제거한 arr를 돌면서
        v[cur] = arr[i]             # v 채워주기
        recur(cur + 1, i)           # v[cur] = arr[i]이므로 v자리 채워주기
                                    # 같은 수를 배열에 담을 수 있으므로
                                    # (cur + 1, i)로 재귀 호출
        
recur(0, 0)