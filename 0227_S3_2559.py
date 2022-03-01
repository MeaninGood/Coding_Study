# 2559번_수열

## 정수의 수열에서 연속적인 몇 개의 합이 가장 큰 값을 계산하는 프로그램


'''
# 첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어짐
# 첫 번째 정수 N은 온도를 측정한 전체 날짜의 수, N은 2 이상 100,000 이하
# 두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수
# 둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어짐
# 이 수들은 모두 -100 이상 100 이하
## 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력


(입력)
10 2
3 -2 -4 -9 0 3 7 13 8 -3

(출력) 
21

'''


# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# dp = [0] * n
# temp = 0
# i = 0
# idx = 0
# while idx <= n - k:
#     temp += arr[i]
#     i += 1
#     if i == k + idx :
#         dp[idx] = temp
#         temp = 0
#         idx += 1
#         i = idx
    
# print(max(dp))

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# li = [0] * (n - k + 1)

# s = 0
# e = 0
# total = arr[0]
# while e < n:
#     if s > n - k:
#         li[s-1] == total
#         break

#     if e < s + k - 1:
#         e += 1
#         total += arr[e]
        
#     else:
#         li[s] = total
#         total -= arr[s]
#         s += 1

# print(max(li))

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# res = 0
# total = sum(arr[0:k])
# for i in range(1, n - k + 1):
#     total += arr[i+k-1]
#     total -= arr[i]
    
#     if total > res:
#         res = total
    
# print(res)