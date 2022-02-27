# 2491번_수열

## 0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열
## 그 수열 안에서 연속해서 커지거나(같은 것 포함),
## 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력

'''
# 첫째 줄에는 수열의 길이 N
# 둘째 줄에는 N개의 숫자가 빈칸을 사이에 두고 주어짐
# N은 1 이상 100,000 이하의 정수
## 첫째 줄에 가장 긴 길이를 출력


(입력)
9
1 2 2 4 4 5 7 7 2

(출력) 
8

'''


# n = int(input())
# arr = list(map(int, input().split())) + [-1]

# cnt = 1
# res = 1
# for i in range(1, n):
#     if arr[i - 1] >= arr[i]:
#         cnt += 1
        
#     else:
#         cnt = 1
    
#     if res < cnt:
#         res = cnt
        
# cnt = 1
# for i in range(1, n):
#     if arr[i - 1] <= arr[i]:
#         cnt += 1
#     else:
#         cnt = 1
        
#     if res < cnt:
#         res = cnt
        
# print(res)


n = int(input())
arr = list(map(int, input().split()))

dp1 = [1] * (n)

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        dp1[i] = dp1[i - 1] + 1
    else:
        dp1[i] = 1

a = max(dp1)   
        

dp2 = [1] * (n)

for i in range(1, n):
    if arr[i] <= arr[i - 1]:
        dp2[i] = dp2[i - 1] + 1
    
    else:
        dp2[i] = 1   
b = max(dp2)

print(max(a, b))
