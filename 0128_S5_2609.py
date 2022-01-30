# 2609번_최대공약수와 최소공배수

## 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성

'''
# 첫째 줄에는 두 개의 자연수
# 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백
## 첫째 줄에는 입력으로 주어진 두 수의 최대공약수
## 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력

(입력)
24 18

(출력)
6
72

'''

n, m = map(int, input().split())

max_num = max(n, m)
min_num = min(n, m)
gcm_li = [] # 최대 공약수
lcm_li = [] # 최소 공배수
gcm = 0
lcm = 999999999
# def solve(n, m):
   
for i in range(1, min_num+1) :
    if min_num % i == 0 :
        gcm_li.append(i)
            
for gnum in gcm_li :
    if (max_num % gnum == 0) and (gnum > gcm) :
        gcm = gnum
            
            
for j in range(1, max_num+1) :
    k = j * max_num
    lcm_li.append(k)
        
for lnum in lcm_li :
    if (lnum % min_num == 0) and lcm > lnum :
        lcm = lnum
        break

print(gcm, lnum, sep = '\n')

            

