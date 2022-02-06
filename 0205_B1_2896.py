# 2896번_무알콜 칵테일

## 오렌지 주스, 사과 주스, 파인애플 주스를 구매
## 무알콜 칵테일을 만드는데 필요한 오렌지, 사과, 파인애플 주스의 비율
## 구매한 주스의 양이 주어짐
## 칵테일을 최대한 많이 만들었을 때, 각 주스가 얼만큼 남는지 구하기

'''
# 첫째 줄에 구매한 오렌지, 사과, 파인애플 주스의 양 A, B, C
# 둘째 줄에 칵테일을 만드는데 필요한 각 주스의 비율 I, J, K
## 칵테일을 최대한 많이 만들었을 때,
## 각 주스가 얼만큼 남는지를 공백으로 구분하여 출력

(입력)
10 15 18
3 4 1
---------
9 9 9
3 2 1

(출력)
0 1.666667 14.666667
---------
0 3 6

'''

a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

res = min(a/i, b/j, c/k)

x = a - i*res
y = b - j*res
z = c - k*res

print(f'{x:.6f} {y:.6f} {z:.6f}')



'''
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mn = 1000000000
for i in range(3):
    mn = min(mn, a[i] / b[i])

for i in range(3):
    a[i] -= mn * b[i]

print(*a)

'''
