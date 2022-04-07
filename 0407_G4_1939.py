# 1939번_중량제한

## N(2 ≤ N ≤ 10,000)개의 섬으로 이루어진 나라가 있다
## 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다
## 그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없음
## 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 됨
## 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성

'''
# 첫째 줄에 N, M(1 ≤ M ≤ 100,000)
# 다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)
# 이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미
# 서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향
# 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어짐
# 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어짐
## 첫째 줄에 답을 출력

(입력)
3 3
1 2 2
3 1 3
2 3 2
1 3

(출력)
3

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
v = [list(map(int, input().split())) for _ in range(m)]
s, e = map(int, input().split())

par = [i for i in range(n + 1)]
rnk = [0 for i in range(n + 1)]
sz = [1 for i in range(n + 1)]

v.sort(key=lambda x: -x[2])

for i in range(m):
    union_(v[i][0], v[i][1])
    
    if find_(s) == find_(e):
        print(v[i][2])
        break