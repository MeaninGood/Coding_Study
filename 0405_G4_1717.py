# 1717번_집합의 표현

## 초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다
##  여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행

'''
# 첫째 줄에 n(1 ≤ n ≤ 1,000,000), m(1 ≤ m ≤ 100,000)
# m은 입력으로 주어지는 연산의 개수
# 다음 m개의 줄에는 각각의 연산이 주어짐
# 합집합은 0 a b의 형태로 입력이 주어짐
# 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미
# 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력
# 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산
# a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있음
## 1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과를 출력

(입력)
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

(출력)
NO
NO
YES

'''
def find_(x):
    if par[x] == x:
        return x
    
    return find_(par[x])

def union_(a, b):
    a = find_(a)
    b = find_(b)
    
    if a == b:
        return
    
    if rnk[a] < rnk[b]:
        par[a] = b
        sz[b] += sz[a]
    
    elif rnk[a] > rnk[b]:
        par[b] = a
        sz[a] += sz[b]
    else:
        par[a] = b
        sz[b] += sz[a]
        rnk[b] += 1
        

n, m = map(int, input().split())

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]
sz = [1 for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    
    if a == 0:
        union_(b, c)
    
    else:
        if find_(b) == find_(c):
            print('YES')
        else:
            print('NO')
    
   
    