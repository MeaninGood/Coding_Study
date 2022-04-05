# 15652번_N과 M(4)

## 1부터 N까지 자연수 중에서 M개를 고른 수열
## 같은 수를 여러 번 골라도 된다.
## 고른 수열은 비내림차순

'''
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
## 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력
## 각 수열은 공백으로 구분해서 출력

(입력)
4 2

(출력) 
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4

'''

m, n = map(int, input().split())
arr = [0 for i in range(n)]

def recur(cur, start):
    if cur == n:
        print(*arr)
        return
    
    for i in range(start - 1, m):
        arr[cur] = i + 1
        recur(cur + 1, i + 1)
        
recur(0, 1)