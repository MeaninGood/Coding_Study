# 2644번_촌수계산

## 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때
## 주어진 두 사람의 촌수를 계산하는 프로그램을 작성

'''
# 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시
# 입력 파일의 첫째 줄에는 전체 사람의 수 n
# 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어짐
# 셋째 줄에는 부모 자식들 간의 관계의 개수 m
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호
# 각 사람의 부모는 최대 한 명
## 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력
## 두 사람의 친척 관계가 전혀 없어 촌수는 -1로 출력


(입력)
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

(출력) 
3

'''

def dfs(cur):
    ret = 1
    visited[cur] = True
    
    for nxt in arr[cur]:
        if visited[k2]:
            break
        if visited[nxt]:
            continue
        ret += dfs(nxt)
        
    if not visited[k2]:
        return 0   
    return ret
        
    
    
n = int(input())
k1, k2 = map(int, input().split())
m = int(input())
arr = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False for _ in range(n+1)]

ans = dfs(k1)

print(ans -1)